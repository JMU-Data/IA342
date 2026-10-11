---
layout: default
title: "Lab 8: Ticket Sales Visualization with Tableau Relationships - IA342"
---

# Week 8 Lab — Ticket Sales Visualization with Tableau Relationships

**IA342 · Week 8 · October 12 and 14, 2026**

| Item | Requirement |
|---|---|
| Monday | Create and publish a Live **Data Source** with six related tables |
| Wednesday | Create five charts and one **Dashboard** in a Workbook |
| Deadline | **Friday, October 16, 2026, 11:59 p.m. Eastern Time** |
| Submission | Publish your **Data Source and Workbook** in `fall2026`, and submit **one PDF** to Canvas |

**Strongly recommended:** finish the Data Source on Monday and the Dashboard/PDF on Wednesday. The class PostgreSQL database will be stopped after Friday's deadline. Starting again from raw files later is much more tedious.

Name your work `firstname_lastname_week8_tickit_data`, `firstname_lastname_week8_tickit_workbook`, and `firstname_lastname_week8_tickit.pdf`. Substitute your own first and last names.

## Dataset

Use the class PostgreSQL connection: database **`postgres`**, schema **`public`**, username **`demo`**. Find the server address and password in **Canvas**; do not put credentials in your PDF or public files.

- [TICKIT ER diagram](https://dataedo.com/samples/html/Tickit/doc/Tickit_16/modules/Tickit_diagram_136/module.html)
- [AWS TICKIT data download (ZIP)](https://docs.aws.amazon.com/redshift/latest/gsg/samples/tickitdb.zip) · [Table and field definitions](https://docs.aws.amazon.com/redshift/latest/dg/c_sampledb.html)

The full TICKIT database has seven tables, but **this Lab uses six**: `sales`, `listing`, `event`, `category`, `venue`, and `users`. The seventh table, `date`, is not needed.

---

# Monday — Build the Data Source

## 1. Connect to PostgreSQL

In Tableau Cloud, open the **`fall2026`** project → **New → Published Data Source** → **Connectors → PostgreSQL**. Enter:

| Connection setting | Value |
|---|---|
| **Server** | Get the current server address from **Canvas** |
| **Port** | `5432` |
| **Database** | `postgres` |
| **Username** | `demo` |
| **Password** | Get the current password from **Canvas** |
| **Require SSL** | **Checked** |

Choose schema **`public`** after connecting. Click **Sign In**. Use the course settings supplied in Canvas, even if an example screenshot shows an older connection.

![PostgreSQL connection screen: enter the server and password supplied through Canvas](screenshots/Screenshot%202026-10-11%20104717.png)

## 2. Add six separate tables

Start with **`sales`**. Drag **`listing`** next to it on the top-level Data Source canvas and connect **`sales.Listid = listing.Listid`**. A sale may belong to a listing, so `sales` is **Many** and `listing` is **One**.

![First, connect sales and listing using Listid (Many to One)](screenshots/Screenshot%202026-10-11%20104846.png)

*The screenshot shows the two tables, the relationship fields, and the Many → One settings.*

Next add **`event`**, **`category`**, **`venue`**, and **`users`** as separate logical tables. Complete their Relationships in Step 3.

## 3. Define five Relationships

| Relationship fields | Cardinality |
|---|---|
| `sales.listid` = `listing.listid` | Many → One |
| `listing.eventid` = `event.eventid` | Many → One |
| `event.catid` = `category.catid` | Many → One |
| `event.venueid` = `venue.venueid` | Many → One |
| `sales.sellerid` = `users.userid` | Many → One |

Use `sales.sellerid` (seller), **not** `sales.buyerid`. Your canvas should have **six tables and five relationship lines**.

![Six-table TICKIT data model, highlighting sales.Sellerid = users.Userid](screenshots/Screenshot%202026-10-11%20105146.png)

*This finished model shows how `sales.Sellerid` connects to `users.Userid`, along with the other four Relationships.*

## 4. Set One-to-Many Relationships

For each relationship, use the **Many → One** direction in Step 3 and keep **Some records match** on both sides. For example, several sales can share the same listing ID. The first screenshot in Step 2 shows where to select these options.

## 5. Organize the fields

**Move IDs to Dimensions.** In the Data Source Scratchpad, right-click an ID such as **`Salesid`** and choose **Convert to Dimension**; it identifies a record rather than an amount of money.

![Move Salesid to Dimensions](screenshots/sealsid%20to%20dimesion.png)

*The `Salesid` field now appears as a Dimension.*

**Set geographic data types (roles).** Assign **`Venuecity` → City** and **`Venuestate` → State/Province**, so Tableau can place event venues on a map.

![Assign Tableau geographic roles to Venuecity and Venuestate](screenshots/Screenshot%202026-10-11%20105421.png)

*The globe icons indicate geographic fields.*

**Format dollar amounts.** Set **`Pricepaid`**, **`Commission`**, and **`Totalprice`** to **USD ($)**.

![Set Default Properties / Number Format to USD](screenshots/Screenshot%202026-10-11%20105539.png)

*Choose USD currency formatting for the money fields.*

## 6. Create two calculated fields

In the Scratchpad choose **Create Calculated Field**. Use the exact names, underscores, and input-field capitalization below.

**`Seller_Proceeds`** — amount received after commission, used for the map in Chart 5:

```tableau
[Pricepaid] - [Commission]
```

![Formula and exact name of Seller_Proceeds](screenshots/Screenshot%202026-10-11%20105819.png)

*This is sale revenue after commission, not a complete calculation of profit.*

**`Realized_Price_per_Ticket`** — the realized amount per ticket, used in the **Chart 3 Scatter Plot Tooltip**:

```tableau
IF [Qtysold] > 0 THEN
    [Pricepaid] / [Qtysold]
END
```

![Formula and exact name of Realized_Price_per_Ticket](screenshots/Screenshot%202026-10-11%20105911.png)

*Keep this field: the new Chart 3 screenshot shows its value in the Tooltip.*

`Pricepaid` is already the total amount paid for a sale; do **not** multiply it by `Qtysold`.

## 7. Create two Hierarchies

A **Hierarchy** groups related dimensions into levels. Use the **+** control to explore a broad level first, then drill down into more detail **on the same chart** — for example, category group → category name, or state → city.

**Category Hierarchy:** in `category`, drag **`Catname` onto `Catgroup`**. Name it **`Category`** (`Catgroup → Catname`).

![Create the Category hierarchy by dragging Catname onto Catgroup](screenshots/Screenshot%202026-10-11%20110014.png)

*Expand Category in Chart 1 to compare group totals with individual category names.*

**Venue Hierarchy:** in `venue`, drag **`Venuecity` onto `Venuestate`**. Name it **`Venue_Location`** (`Venuestate → Venuecity`).

![Create the Venue_Location hierarchy by dragging Venuecity onto Venuestate](screenshots/Screenshot%202026-10-11%20110105.png)

*Expand from state to city to explore where events were held.*

## 8. Quick Data Check

Use **Scratchpad → Marks → Text** to compare counts and totals **without creating another worksheet**. The two screenshots illustrate why Sales and Listing are separate tables.

First put **`CNT(Salesid)`** and **`SUM(Totalprice)`** on **Text**.

![Scratchpad: CNT(Salesid) and SUM(Totalprice) displayed on Text](screenshots/Screenshot%202026-10-11%20110437.png)

*In the original sample, this shows **172,456 sales** and the aggregate listing value.*

Next replace **`CNT(Salesid)`** with **`CNT(Listid (Listing))`**, keeping **`SUM(Totalprice)`**.

![Scratchpad: CNT(Listid) and SUM(Totalprice) displayed on Text](screenshots/Screenshot%202026-10-11%20110535.png)

*Now you see **192,497 listings**. The listing total remains the same: Relationships do not simply repeat the full listing amount once per sale.*

## 9. Publish the Data Source

Select **Live** and publish as **`firstname_lastname_week8_tickit_data`** to **`fall2026`**. In the Publish dialog, **check `Embed credentials`**, so your Workbook can reuse this connection. Confirm the Data Source appears in the course project.

![Select fall2026 and Embed credentials before publishing](screenshots/Screenshot%202026-10-11%20110635.png)

---

# Wednesday — Build the Workbook and Dashboard

**Screenshot note:** Use the field names and final chart titles in the written instructions if an intermediate screenshot shows a draft title.

## 10. Open your Workbook

In `fall2026`, open your published Data Source → **New Workbook**. Save as **`firstname_lastname_week8_tickit_workbook`**. Use this Data Source for all five worksheets.

## 11. Chart 1 — Sales Revenue by Category (Bar Chart)

Create **`01_Category_Revenue`**. Place the **Category** Hierarchy on **Rows** and **`SUM(Pricepaid)`** on **Columns**; choose **Bar** and sort by revenue.

Expand the **+** next to Category to move from `Catgroup` to `Catname`. Try both levels to see how revenue changes when grouped differently. If a **Null** category appears, you may use **Exclude** for this worksheet.

To display each category's share of total revenue, use **Quick Table Calculation → Percent of Total** on the revenue measure.

![Choose Percent of Total for the category revenue chart](screenshots/Screenshot%202026-10-11%20111638.png)

*The calculation displays each category's contribution to the total revenue in the view.*

Show the percentage on **Label** and title the chart **Sales Revenue by Event Category**.

![Completed category revenue bar chart with percentage labels](screenshots/Screenshot%202026-10-11%20111905.png)

*You should see category bars and their revenue percentages.*

**In-class check:** Which event category has the highest total `Pricepaid`?

## 12. Chart 2 — Distribution by Listing Total Price (Histogram)

Create **`02_Listing_Price_Distribution`**.

1. In the **`listing`** table, first select **`Totalprice`**, then choose **Create → Bins**.
2. Name the new field **`Totalprice (bin)`** and set **Bin Size = 500**.

![Create Totalprice bins with a size of USD 500](screenshots/Screenshot%202026-10-11%20112443.png)

*This groups each listing's total price into $500 intervals — not individual ticket prices.*

3. Put **`Totalprice (bin)`** on **Columns** and **`CNT(Salesid)`** on **Rows**. Choose **Bar**.
4. Try bin sizes **250**, **500**, and **1,000**; return to **500** for the final version.
5. Title the chart **Sales Transactions by Listing Value — USD 500 Bins**.

*Each bar counts sales transactions associated with listings in that price interval.*

**In-class check:** Which $500 listing-value bin contains the most sales transactions?

## 13. Chart 2 — Add Running Total, Percentage, and a Line

Continue working in **`02_Listing_Price_Distribution`** — this is still **one worksheet**, not an additional chart submission.

1. Drag another copy of **`CNT(Salesid)`** to **Rows**. Tableau will temporarily display two charts. On the second measure choose **Quick Table Calculation → Running Total**.

![Use Quick Table Calculation: Running Total on the second count](screenshots/Screenshot%202026-10-11%20112643.png)

*Running Total accumulates sales counts from the smallest to the largest price bin.*

2. Open **Edit Table Calculation** on the second measure. Select **Add secondary calculation → Percent of Total** and use **Table (Across)** for the bin direction.

![Add Percent of Total as a secondary calculation](screenshots/Screenshot%202026-10-11%20113205.png)

*The second measure is now a cumulative **percentage** instead of a raw count.*

3. In the **Marks** cards, keep the first measure as **Bar** and change the second to **Line**. Then choose **Dual Axis** on the second measure.

![Combine the bar chart and cumulative line with Dual Axis](screenshots/Screenshot%202026-10-11%20113235.png)

*The left axis shows transaction counts; the right axis shows percentages. Do not synchronize these different numeric units.*

4. Set the **bars to blue** and the **line to yellow/orange**, as in the example.

![Blue sales-count bars with a yellow-orange cumulative percentage line](screenshots/Screenshot%202026-10-11%20113313.png)

*The cumulative line should rise toward 100% as listing-value bins increase.*

## 14. Chart 3 — Average Listing vs. Sale Amount (Scatter Plot)

Create **`03_Venue_Amount_Comparison`**.

1. Put **`AVG(Totalprice)`** on **Columns** and **`AVG(Pricepaid)`** on **Rows**. Add **`Venueid`** to **Detail** and **`Catname`** to **Color**; choose **Circle** marks.

![Create the scatter plot with average listing and sale amounts](screenshots/Screenshot%202026-10-11%20113800.png)

*Each dot represents a venue/category combination.*

2. On **Color → Edit Colors**, choose Tableau's **Color Blind** palette for the event categories.

3. Add **`AVG(Realized_Price_per_Ticket)`**, `Venuename`, `Venuecity`, and `Venuestate` to the **Tooltip** before annotating any marks.

![Scatter plot Tooltip showing AVG(Realized_Price_per_Ticket) and venue details](screenshots/Screenshot%202026-10-11%20141551.png)

*Hover over a dot to check the listing amount, sale amount, realized price per ticket, and venue.*

4. From **Analytics**, add a **Trend Line**. Keep **Linear** as the model type. In **Trend Lines Options**, **uncheck `Allow a trend line per color`** to use one overall trend line.

![Linear Trend Line options: Allow a trend line per color unchecked](screenshots/Screenshot%202026-10-11%20113858.png)

*One trend line summarizes the overall relationship between the two measures.*

5. Try changing the axis range or scale, then return to **linear axes**. Right-click an interesting high-value dot and choose **Annotate → Mark**.

![Choose Annotate Mark for a scatter plot point](screenshots/Screenshot%202026-10-11%20114118.png)

*The mark annotation identifies a selected venue/category after its Tooltip fields are available.*

6. Title the chart **Average Listing Amount vs. Average Sale Amount by Venue and Category**.

**In-class check:** Which venue has the highest average sale amount in this view?

## 15. Chart 4 — Sales vs. Listings by Seller (Bullet Graph)

Create **`04_Sales_vs_Listings_by_Seller`**.

1. Select **`users.Lastname`**, **`listing.Totalprice`**, and **`sales.Pricepaid`** together. Choose **Show Me → Bullet Graph**.

![Select Lastname, Totalprice, and Pricepaid and choose Bullet Graph](screenshots/Screenshot%202026-10-11%20115629.png)

*Use Lastname for the seller grouping. The screenshot may show an earlier draft title; follow the final title below.*

2. Verify that the bar shows **`SUM(Pricepaid)`** and the reference marker shows **`SUM(Totalprice)`**. Sort sellers by **`SUM(Pricepaid)`**, highest first.

3. Put **`Lastname`** on **Filters → Top/Bottom → Top 10 by `SUM(Totalprice)`**.

![Top 10 seller last names filtered by SUM(Totalprice)](screenshots/Screenshot%202026-10-11%20135108.png)

*Compare the two dollar amounts for the ten selected last names.*

4. Title the chart **Sales Revenue vs. Total Listing Value by Seller**.

**In-class check:** Among the displayed Top 10 last names, which has the highest `SUM(Pricepaid)`?

**Note:** A last name may represent multiple sellers. Listing value and sales revenue are different amounts; neither is seller profit.

## 16. Chart 5 — Seller Proceeds by City (Symbol Map)

Create **`05_Proceeds_by_Venue_City`**.

1. Select **`Venuecity`** and **`Seller_Proceeds`**, then choose **Show Me → Symbol Map**.
2. Put **`SUM(Seller_Proceeds)`** on **Size** and **`Venuestate`** on **Detail** for geographic context. Title the map **Seller Proceeds by Event Venue City**.

![Symbol Map showing Seller_Proceeds by event venue city](screenshots/Screenshot%202026-10-11%20115919.png)

*Larger marks indicate more Seller_Proceeds for the corresponding event venue city.*

**In-class check:** Which venue city has the highest total `Seller_Proceeds`?

## 17. Build the Dashboard

Create **`Ticket Sales Dashboard`** and place the five worksheets as shown:

| Location | Chart |
|---|---|
| Top left | Category Revenue |
| Top right | Histogram + cumulative line |
| **Middle left** | **Seller Bullet Graph** |
| **Middle right** | **Venue Scatter Plot** |
| Bottom | Symbol Map |

Keep each chart's **legend close to its chart**. Try a simple **Username/Lastname filter** or **Use as Filter** on the Seller Bullet Graph to see where those sellers' events took place. Clear selections before exporting.

![Updated five-view Dashboard with Realized_Price_per_Ticket in the scatter Tooltip](screenshots/Screenshot%202026-10-11%20141606.png)

*The updated Dashboard includes all five charts, and the Scatter Tooltip displays the realized per-ticket price.*

## 18. Publish and Submit

1. **Publish** the Workbook in `fall2026` with all **five Worksheets and one Dashboard**.
2. From the Dashboard choose **Download → PDF**. Check that the five charts, labels, and legends are readable.
3. Submit **one PDF** to the Week 8 assignment in **Canvas**. No written answers to the in-class questions are required.

**Final deliverables:** **Published Data Source + Published Workbook + one PDF**. The instructor checks the Tableau items separately; only the PDF is uploaded to Canvas.

## Grading — 100 points

| Item | Points | Main requirement |
|---|---:|---|
| **Published Data Source** | **35** | Six tables, five Relationships, fields, hierarchies, and calculated fields |
| **Published Workbook** | **15** | Five worksheets, one Dashboard, uses your published Data Source |
| **PDF report** | **50** | Readable final Dashboard and accurate charts, labels, and comparisons |
| **Total** | **100** | Data Source + Workbook + PDF |

The instructor may award partial credit when work is incomplete or inaccurate.

## If the Class Database Is No Longer Available

The course PostgreSQL database will be stopped after **Friday, October 16, 2026, at 11:59 p.m. Eastern Time**. Because the classroom Data Source uses a **Live** connection, it cannot query the stopped database.

If you have not finished, you must download the [AWS TICKIT data ZIP](https://docs.aws.amazon.com/redshift/latest/gsg/samples/tickitdb.zip) and create a replacement Data Source from the original files yourself. **Tableau Cloud accepts the TXT files directly**; Excel conversion and Tableau Flow are not needed.

| File | Original table | Delimiter |
|---|---|---|
| `sales_tab.txt` | `sales` | Tab |
| `listings_pipe.txt` | `listing` | Pipe (`\|`) |
| `allevents_pipe.txt` | `event` | Pipe (`\|`) |
| `category_pipe.txt` | `category` | Pipe (`\|`) |
| `venue_pipe.txt` | `venue` | Pipe (`\|`) |
| `allusers_pipe.txt` | `users` | Pipe (`\|`) |

The seventh file, `date2008_pipe.txt`, is not needed for this lab.

These files **do not have column headers**. After uploading them as separate tables in **one Data Source**, set the correct Tab/pipe delimiters and rename the imported columns **in their original order**, using the [AWS field definitions](https://docs.aws.amazon.com/redshift/latest/dg/c_sampledb.html). Then set field types, rebuild the five Relationships, create the calculated fields/hierarchies, reconnect your Workbook, and export/submit your PDF. This extra work is your responsibility.

The usual syllabus late penalty applies: **10% per day, up to 40%**, unless the instructor has approved an exception. The database will not be restarted solely for late submissions.

---

[Return to Course Home](../../) | [Return to Syllabus](../../syllabus/)
