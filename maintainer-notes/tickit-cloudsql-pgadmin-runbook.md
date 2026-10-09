# IA342 — AWS TICKIT on Cloud SQL / pgAdmin: Rebuild Runbook

> **Maintainer reference, recorded October 9, 2026.** This is a public, reusable setup and troubleshooting guide, **not student-facing instructions or a private infrastructure inventory**. Never commit real server IPs, instance IDs, passwords, credentials, personal file paths, or student data. Verify the current sample version and console UI before future use.

## 1. Scope and source materials

The 2026 class setup imported the public AWS **TICKIT** sample into Google Cloud SQL for **PostgreSQL 17**, using Windows **pgAdmin 4** for administration and the bundled **psql** client to import text files. The database contains **seven original tables**; the IA342 Tableau Flow assignment can use a **six-table subset**, because the seventh (`date`) is useful for a complete database ER diagram but not mandatory for that lab's joins.

References:
- [AWS dataset download (`tickitdb.zip`)](https://docs.aws.amazon.com/redshift/latest/gsg/samples/tickitdb.zip)
- [AWS TICKIT table definitions](https://docs.aws.amazon.com/redshift/latest/dg/c_sampledb.html)
- [Dataedo TICKIT ER diagram and data dictionary](https://dataedo.com/samples/html/Tickit/doc/Tickit_16/home.html)
- [Cloud SQL built-in authentication and database roles](https://cloud.google.com/sql/docs/postgres/create-manage-users)
- [PostgreSQL `COPY` reference](https://www.postgresql.org/docs/17/sql-copy.html)

## 2. Cloud SQL and pgAdmin setup

1. Create a short-term **Cloud SQL for PostgreSQL** instance. The 2026 example was Enterprise, PostgreSQL 17, single-zone, approximately **2 vCPU / 8 GiB RAM / 10 GiB SSD**; this was a starting configuration, **not a tested classroom concurrency guarantee**. Do not automatically choose production HA/PITR for disposable public demo data; decide backup policy based on actual usage.
2. Create/use the desired database. **The actual 2026 seven-table setup used the default database `postgres`, schema `public`**, not a new `tickit` database. Adapt later commands if you choose another DB in a future semester.
3. On the instance, allowlist the instructor workstation's public IP and, later, the appropriate **Tableau Cloud egress** IP range. Use encrypted connections according to Cloud SQL's TLS configuration; do not open `0.0.0.0/0`.
4. In pgAdmin Desktop, **Servers → Register → Server**. Host is the Cloud SQL public address, port `5432`, maintenance database `postgres`, administrator account `postgres`. Use a private admin password; never reuse the student/demo password.
5. Database shutdown is an **independent operator action** after the lab. Stopping a dedicated instance can reduce compute charges, but storage and some networking costs can remain; do not shut down any instance used by other courses.

### Create the seven empty tables once

Open **pgAdmin Query Tool** or Cloud SQL Studio as the administrator, connected to the target empty database. Create the tables **before** loading data; do **not** apply FK constraints yet. The schema below matches the field definitions used in the October 2026 import.

~~~sql
CREATE TABLE public.users (
  userid integer PRIMARY KEY, username char(8), firstname varchar(30),
  lastname varchar(30), city varchar(30), state char(2),
  email varchar(100), phone char(14),
  likesports boolean, liketheatre boolean, likeconcerts boolean,
  likejazz boolean, likeclassical boolean, likeopera boolean,
  likerock boolean, likevegas boolean, likebroadway boolean,
  likemusicals boolean
);

CREATE TABLE public.venue (
  venueid smallint PRIMARY KEY, venuename varchar(100),
  venuecity varchar(30), venuestate char(2), venueseats integer
);

CREATE TABLE public.category (
  catid smallint PRIMARY KEY, catgroup varchar(10),
  catname varchar(10), catdesc varchar(50)
);

CREATE TABLE public."date" (
  dateid smallint PRIMARY KEY, caldate date NOT NULL,
  day char(3), week smallint, month char(5), qtr char(5),
  year smallint, holiday boolean DEFAULT FALSE
);

CREATE TABLE public.event (
  eventid integer PRIMARY KEY, venueid smallint, catid smallint,
  dateid smallint, eventname varchar(200), starttime timestamp
);

CREATE TABLE public.listing (
  listid integer PRIMARY KEY, sellerid integer, eventid integer,
  dateid smallint, numtickets smallint,
  priceperticket numeric(8,2), totalprice numeric(8,2),
  listtime timestamp
);

CREATE TABLE public.sales (
  salesid integer PRIMARY KEY, listid integer, sellerid integer,
  buyerid integer, eventid integer, dateid smallint,
  qtysold smallint, pricepaid numeric(8,2),
  commission numeric(8,2), saletime timestamp
);
~~~

**2026 lesson:** The initial script contained six tables. The additional `date` table was created manually after inspecting the original seven-table ER diagram. Do not create these tables again in an already populated DB.

## 3. Import the AWS text files from Windows

Download the AWS ZIP above and extract it to a local folder. It contains **no header rows**; the files have different delimiters.

| Destination table | ZIP filename | Delimiter | Rows observed |
|---|---|---|---:|
| `category` | `category_pipe.txt` | `|` | 11 |
| `date` | `date2008_pipe.txt` | `|` | 365 |
| `event` | `allevents_pipe.txt` | `|` | 8,798 |
| `listing` | `listings_pipe.txt` | `|` | 192,497 |
| `sales` | `sales_tab.txt` | Tab | 172,456 |
| `users` | `allusers_pipe.txt` | `|` | 49,990 |
| `venue` | `venue_pipe.txt` | `|` | 202 |

### Why pgAdmin Import/Export and the PSQL Tool failed

- The pgAdmin **Import/Export Data** UI did not successfully import these local files into the remote database in this session. Do not interpret this as Google Cloud SQL lacking text-import support.
- SQL `COPY FROM '/local/Windows/path'` can be server-side, and the remote server cannot read a Windows desktop path. **Use the psql client command `\copy`**, which reads from the client machine.
- The pgAdmin **PSQL Tool** launched a **Windows CMD** prompt (starting with `C:\...>`), not a live `postgres=>` prompt, because `psql.exe` exited immediately. The result was `'\copy' is not recognized...`.
- A later attempt to run CMD's `set "PATH=..."` in **PowerShell** did not update PowerShell's environment. Use `$env:Path` and PowerShell's `&` invocation operator instead.

Start a separate **Windows PowerShell** session (sample folder path is generic):

~~~powershell
$pgRoot = Join-Path $env:LOCALAPPDATA 'Programs\pgAdmin 4'
$env:Path = "$pgRoot\python;$pgRoot\runtime;$env:Path"
& "$pgRoot\runtime\psql.exe" --version
Set-Location (Join-Path $env:USERPROFILE 'Downloads\tickitdb')
& "$pgRoot\runtime\psql.exe" -h <CLOUD_SQL_HOST> -p 5432 -U postgres -d postgres -W
~~~

Enter the private admin password at the prompt. Once the terminal says `postgres=>` or `postgres=#`, the following commands will work. **Do not run `\copy` in pgAdmin Query Tool, Windows CMD, or PowerShell itself.**

### Correct psql import commands

The AWS text files use PostgreSQL's default **`\N` NULL marker**. **Do not add `NULL ''`**. In 2026 that incorrect option caused `invalid input syntax for type integer: "N"` in `venue.venueseats`. PostgreSQL text format with the default NULL value imported `venue` successfully.

Run these one line at a time from inside `psql` (current working directory = extracted AWS folder):

~~~text
\copy public.users FROM 'allusers_pipe.txt' WITH (FORMAT text, DELIMITER '|')
\copy public.venue FROM 'venue_pipe.txt' WITH (FORMAT text, DELIMITER '|')
\copy public.category FROM 'category_pipe.txt' WITH (FORMAT text, DELIMITER '|')
\copy public."date" FROM 'date2008_pipe.txt' WITH (FORMAT text, DELIMITER '|')
\copy public.event FROM 'allevents_pipe.txt' WITH (FORMAT text, DELIMITER '|')
\copy public.listing FROM 'listings_fixed.txt' WITH (FORMAT text, DELIMITER '|')
\copy public.sales FROM 'sales_fixed.txt' WITH (FORMAT text, DELIMITER E'\t')
~~~

The final two `_fixed.txt` files must be generated only after the checks below pass; use the original filenames if they import without line-ending issues. Do not repeat successful imports: PK conflicts are expected on duplicate input.

### Fix: `literal carriage return found in data`

In the 2026 dataset, `listings_pipe.txt` failed at **line 54,736** and `sales_tab.txt` at **line 41,107** because of irregular carriage returns. PowerShell `ReadAllLines` counted **192,500** apparent listing lines, not the 192,497 actual records; a naive rewrite would have preserved the wrong split.

The following creates **new** files while preserving the originals. It removes carriage-return characters and only writes results when both expected row count and delimiter field count match the known sample. If it prints STOP or throws, investigate instead of importing.

~~~powershell
$folder = Join-Path $env:USERPROFILE 'Downloads\tickitdb'

function Repair-TickitFile {
  param([string]$Source, [string]$Target,
        [char]$Separator, [int]$Columns, [int]$ExpectedRows)
  $raw = [System.IO.File]::ReadAllText($Source)
  $rows = @($raw.Replace([char]13, '').Split([char]10) |
            Where-Object { $_ -ne '' })
  $bad = @($rows | Where-Object {
    $_.Split([char]$Separator).Count -ne $Columns
  }).Count
  if ($rows.Count -ne $ExpectedRows -or $bad -ne 0) {
    throw "STOP: $($rows.Count) rows, $bad invalid rows"
  }
  [System.IO.File]::WriteAllLines(
    $Target, $rows, [System.Text.UTF8Encoding]::new($false))
  "READY: $($rows.Count) rows"
}

Repair-TickitFile -Source (Join-Path $folder 'listings_pipe.txt') -Target (Join-Path $folder 'listings_fixed.txt') -Separator '|' -Columns 8 -ExpectedRows 192497
Repair-TickitFile -Source (Join-Path $folder 'sales_tab.txt') -Target (Join-Path $folder 'sales_fixed.txt') -Separator ([char]9) -Columns 10 -ExpectedRows 172456
~~~

**This fix was used for the observed TICKIT sample, not arbitrary user data.** It makes no claim that every carriage return in every dataset is safe to strip.

### Verify counts after import

Run in pgAdmin Query Tool (connected to the same database):

~~~sql
SELECT 'category' AS table_name, count(*) AS rows FROM public.category
UNION ALL SELECT 'date', count(*) FROM public."date"
UNION ALL SELECT 'event', count(*) FROM public.event
UNION ALL SELECT 'listing', count(*) FROM public.listing
UNION ALL SELECT 'sales', count(*) FROM public.sales
UNION ALL SELECT 'users', count(*) FROM public.users
UNION ALL SELECT 'venue', count(*) FROM public.venue;
~~~

The above counts are sample-version-specific, **not** guarantees for future AWS revisions.

## 4. Foreign keys and ER diagram corrections

**Create FKs after data import**, so PostgreSQL can test historic references. AWS Redshift treats PK/FK differently from PostgreSQL: Redshift does not enforce them, whereas PostgreSQL does. Students still build their own Tableau Flow joins.

The Dataedo ER diagram misleadingly reverses the `listing`–`sales` direction: **`listing.listid` is the one-side primary key; `sales.listid` is the many-side foreign key**. In the full seven-table schema there are **11 FK relationships**:

| Child foreign key | Parent primary key |
|---|---|
| `event.venueid` | `venue.venueid` |
| `event.catid` | `category.catid` |
| `event.dateid` | `date.dateid` |
| `listing.sellerid` | `users.userid` |
| `listing.eventid` | `event.eventid` |
| `listing.dateid` | `date.dateid` |
| `sales.listid` | `listing.listid` |
| `sales.sellerid` | `users.userid` |
| `sales.buyerid` | `users.userid` |
| `sales.eventid` | `event.eventid` |
| `sales.dateid` | `date.dateid` |

#### Important historical-data exception: `event.venueid`

A normal `fk_event_venue` creation **failed** with `venueid=64 not present in venue`. The following read-only query found **three missing venue IDs** in the original AWS sample: `64` (56 events), `12` (47 events), `51` (36 events), affecting **139 events**. Checking the raw `venue_pipe.txt` found none of those IDs.

~~~sql
SELECT e.venueid, count(*) AS affected_events
FROM public.event e
LEFT JOIN public.venue v ON e.venueid = v.venueid
WHERE e.venueid IS NOT NULL AND v.venueid IS NULL
GROUP BY e.venueid ORDER BY affected_events DESC;
~~~

The `event` → `venue` constraint was **actually created** with `NOT VALID`, which retains existing unmatched rows **but enforces the FK on future writes**:

~~~sql
ALTER TABLE public.event
  ADD CONSTRAINT fk_event_venue
  FOREIGN KEY (venueid) REFERENCES public.venue(venueid) NOT VALID;
~~~

Do not invent venue records, delete events, or claim that this relationship has passed historical validation. After any repair, `ALTER TABLE public.event VALIDATE CONSTRAINT fk_event_venue;` would perform the check.

### Other ten candidate FKs

Run each statement separately; if the source has an orphan, inspect it before deciding whether to use `NOT VALID` on that individual FK.

~~~sql
ALTER TABLE public.event ADD CONSTRAINT fk_event_category FOREIGN KEY (catid) REFERENCES public.category(catid);
ALTER TABLE public.event ADD CONSTRAINT fk_event_date FOREIGN KEY (dateid) REFERENCES public."date"(dateid);

ALTER TABLE public.listing ADD CONSTRAINT fk_listing_seller FOREIGN KEY (sellerid) REFERENCES public.users(userid);
ALTER TABLE public.listing ADD CONSTRAINT fk_listing_event FOREIGN KEY (eventid) REFERENCES public.event(eventid);
ALTER TABLE public.listing ADD CONSTRAINT fk_listing_date FOREIGN KEY (dateid) REFERENCES public."date"(dateid);

ALTER TABLE public.sales ADD CONSTRAINT fk_sales_listing FOREIGN KEY (listid) REFERENCES public.listing(listid);
ALTER TABLE public.sales ADD CONSTRAINT fk_sales_seller FOREIGN KEY (sellerid) REFERENCES public.users(userid);
ALTER TABLE public.sales ADD CONSTRAINT fk_sales_buyer FOREIGN KEY (buyerid) REFERENCES public.users(userid);
ALTER TABLE public.sales ADD CONSTRAINT fk_sales_event FOREIGN KEY (eventid) REFERENCES public.event(eventid);
ALTER TABLE public.sales ADD CONSTRAINT fk_sales_date FOREIGN KEY (dateid) REFERENCES public."date"(dateid);
~~~

Always check which FK names already exist before re-executing any statement:

~~~sql
SELECT conrelid::regclass AS table_name, conname AS fk_name,
       pg_get_constraintdef(oid) AS definition,
       convalidated AS validated
FROM pg_constraint
WHERE contype = 'f' AND connamespace = 'public'::regnamespace
ORDER BY table_name, fk_name;
~~~

**Evidence boundary:** `fk_event_venue NOT VALID` was confirmed working. The ten other FK definitions were supplied, but their final execution and `convalidated` states were **not independently documented** in this conversation.

## 5. Read-only `demo` user and Tableau connection

In the target database, create a reusable **NOLOGIN** role first (run only once):

~~~sql
CREATE ROLE tickit_readonly NOLOGIN;
~~~

Then Cloud SQL → **Users → Add user**, Built-in authentication, user `demo`, **select `tickit_readonly` as the explicit database role**. Do **not** leave the roles list empty: Cloud SQL can assign `cloudsqlsuperuser` to built-in users when no custom roles are selected. Keep the admin `postgres` password different and private.

After creating the seven tables, run as their administrator in the correct database:

~~~sql
GRANT CONNECT ON DATABASE postgres TO tickit_readonly;
GRANT USAGE ON SCHEMA public TO tickit_readonly;
GRANT SELECT ON TABLE
  public.category, public."date", public.event, public.listing,
  public.sales, public.users, public.venue
TO tickit_readonly;
GRANT tickit_readonly TO demo;
~~~

If `demo` was already assigned `tickit_readonly`, the repeated membership GRANT emits a harmless notice. Confirm effective privilege:

~~~sql
SELECT
  has_database_privilege('demo','postgres','CONNECT') AS can_connect,
  has_schema_privilege('demo','public','USAGE') AS can_use_schema,
  has_table_privilege('demo','public.category','SELECT') AS can_read,
  has_table_privilege('demo','public.category','INSERT') AS can_insert,
  has_table_privilege('demo','public.category','UPDATE') AS can_update,
  has_table_privilege('demo','public.category','DELETE') AS can_delete,
  pg_has_role('demo','cloudsqlsuperuser','member') AS is_admin;
~~~

Expected: `can_connect`, `can_use_schema`, `can_read` are true; `can_insert`, `can_update`, `can_delete` and `is_admin` are false. Check the other six tables too.

**2026 observed issue:** Tableau Flow could list the tables, yet `category` Clean step returned `permission denied for table category`. Granting read privileges fixed the SQL check: `can_read=true`, `can_insert=false`, `is_admin=false`. Merely listing tables in Tableau is **not proof** of table-level `SELECT`. A complete published Tableau Flow and concurrency test was **not independently recorded**.

## 6. Quick checklist for next offering

- [ ] Verify current AWS download, file formats, source dates, seven-table schema and row counts.
- [ ] Create a dedicated appropriately sized Cloud SQL PostgreSQL instance or confirm safe reuse, database name, TLS and IP allowlist.
- [ ] Create tables without FKs, import data **once** via the local Windows `psql \copy` client, and verify all seven row counts.
- [ ] For import errors, distinguish `\N` NULL handling, unexpected carriage returns, local vs server file path, and CMD vs PowerShell/psql prompts.
- [ ] Inspect the eleven FKs and each `convalidated` state; acknowledge real source orphan rows.
- [ ] Confirm the demo role grants `CONNECT`, `USAGE` and `SELECT` only, and **never `cloudsqlsuperuser`**.
- [ ] Perform an actual Tableau Cloud Flow input → join → publish/run → generated Data Source test with the read-only login.
- [ ] Stop the **dedicated** lab instance afterward if no other workload needs it; check remaining storage/IP costs.

**Public-repo hygiene:** No passwords, private connection strings, actual endpoints, student information, or credential-bearing screenshots in GitHub. 
