---
course: IA342
week: 11
term: Fall 2026
title: "Lab 11: Calculations in Tableau"
content_type: lab
language: en
---

[Open the interactive Lab 11 handout](./)

# Lab 11: Calculations in Tableau

**IA342 · Week 11 · November 2–6, 2026**  
**Deadline:** See Canvas.

## Objectives

- Get familiar with basic calculations in Tableau.
- Learn how to create a Tableau Story.

## Data

- COVID-19 data from **1Point3Acres**, provided on Canvas.
- County population and median household income from the **US Census**, provided as `pop_income.csv` on Canvas.

**Class plan:** On **Monday**, finish and publish **both the flow and the calculation-ready data source** (Steps 1–3). On **Wednesday**, connect to the published data source to build the six worksheets, dashboard, and Story (Steps 4–7).

**Screenshot note:** The older screenshots were created for **Lab 10** and may show a different project/name or older **Export Flow / Export Data** labels. Follow the current text and interface: *publish the flow*, *run it to create a data source*, then *edit and publish the same data source*. New Lab 11 screenshots are **placed alongside the original examples**, except the redundant old Synchronize Axis screenshot, which is omitted because the new screenshot shows the same command. Where two images appear for one operation, the first may show the menu and the second the settings dialog. Use **`fall2026`**, the **Lab 11 names**, and **lowercase source field names** below.

## 1. Download the data

Download `pop_income.csv` from this week's Canvas module. Reuse the original COVID `case.csv` file from Week 9, or download it again from Canvas.

For this class dataset, cases and deaths are **daily new counts**. Population and income describe each county for the census reference period.

## 2. Create a new flow to clean and join the data

### a. Add the COVID file

Add `case.csv` to a new Prep flow. Keep and name these fields as in the original lab:

| Field | Data type |
|---|---|
| `case_id` | Number; an identifier |
| `date` | Date |
| `state` | String |
| `county` | String |
| `cases` | Number |
| `deaths` | Number |
| `fips` | String |

Remove `Source Row Number` and `recovered_count` if present.

![COVID input fields and data types](assets/screenshots/image1.webp)

### b. Clean the COVID data

Add a Clean step. Following the original lab, filter out null `fips` values and negative or null cases/deaths. Keep valid zero counts. Check the date type, and assign the **State/Province** geographic role to state and **County** to county.

![COVID cleaning steps](assets/screenshots/image2.webp)

### c. Add the population and income file

Add `pop_income.csv`. Keep `pop` and `income` as numeric fields. Keep `NAME`, `state_fips`, and `county_fips` as strings. Remove the generated source row number if present.

![Population and income input fields](assets/screenshots/image3.webp)

### d. Create the census FIPS field

In a Clean step for the population table, create a field named **fips**:

```tableau
[state_fips] + [county_fips]
```

Keep the state code as **two characters** and the county code as **three characters**, including leading zeros. For example, `01` + `001` gives `01001`. Both join keys must use the same five-character format.

![Create the census fips field](assets/screenshots/image4.webp)

### e. Join the two tables

Join the COVID table to the population table using **COVID `fips` = census `fips`**. Use an **inner join**, as in the original lab. Each county should have one census record, so a daily COVID record matches one population record.

![Inner join on FIPS](assets/screenshots/image5.webp)

### f. Clean the joined table

Add a Clean step after the join. Remove redundant fields from the census side: `NAME`, `state_fips`, `county_fips`, and its duplicate `fips` field. Retain the COVID `fips` field.

The output should contain these nine fields: **fips, case_id, date, state, county, cases, deaths, pop, income**.

![Remove redundant fields after the join](assets/screenshots/image6.webp)

### g. Add the data output

Add an **Output** step and choose **Published data source** as its destination. Name it **`firstname_lastname_lab11_data`** in **`fall2026`**. This is the joined **data output**, not the flow definition. Older screenshots may call this *Export Data* or *Publish as Data Source*; the wording varies by Tableau version.

![Configure the published data source output](assets/screenshots/image7.webp)

### h. Publish the flow and run it

**Publish the flow** as **`firstname_lastname_lab11_flow`** in `fall2026` (saves the flow definition). Then **run the flow once** to create **`firstname_lastname_lab11_data`** (writes the output data). These are **two separate published objects**. A flow export/download is not a substitute for publishing and running the flow.

Keep the existing Week 9 COVID source unchanged. There should be only **one Lab 11 data source**; Step 3 edits and republishes that same item.

![Publish the flow and run its output](assets/screenshots/image8.webp)

## 3. Edit the published data source and create calculations (Monday)

**Work in the existing Lab 11 published data source, not in a workbook.** After the flow finishes, go to **Explore → `fall2026` → `firstname_lastname_lab11_data`** and click **Edit Data Source**. Open its **Scratchpad**.

![Open the published Lab 11 data source and choose Edit Data Source](assets/screenshots/published-source.webp)

### a. Create the hierarchy and inspect the records

1. Convert `case_id` to a **dimension**, if necessary.
2. Drag `county` onto `state` to create the **state → county** hierarchy.

   ![Create a state–county hierarchy in the data source](assets/screenshots/hierarchy.webp)

3. Put `case_id`, `fips`, `deaths`, `cases`, and `pop` on **Rows** in the Scratchpad. Filter to one state/county so you can compare daily records. Tableau may display `ATTR()` around these fields in the text view.

   ![Review daily cases, deaths, and repeated county population](assets/screenshots/daily-rows.webp)

**Before calculating, look at the numbers.** In the example screenshot, `fips = 51660` has `pop = 53,273` on many different `case_id` records. The `cases` and `deaths` fields change from day to day, but the population does not. **Daily cases/deaths are new observations; repeating the same 53,273 residents does not create new residents.**

### b. Create the calculated fields in this data source

Use the **lowercase field names** shown in the new screenshots: `deaths`, `cases`, `fips`, and `pop`. For consistency, the formulas below are written entirely in lowercase; Tableau may display function keywords in uppercase.

**death rate** — calculate the overall reported deaths-to-cases ratio by aggregating **before** dividing.

```tableau
zn(sum(zn([deaths])) / sum(zn([cases])))
```

![Valid death rate formula](assets/screenshots/death-formula.webp)

**fixed pop** — calculate a single population value per county (per `fips`) instead of adding the population on each daily record.

```tableau
{ fixed [fips] : avg([pop]) }
```

![Valid fixed pop formula](assets/screenshots/fixed-formula.webp)

**case rate** — use the LOD-based county population as the denominator component.

```tableau
zn(sum(zn([cases])) / sum(zn([fixed pop])))
```

![Valid case rate formula](assets/screenshots/case-formula.webp)

**Syntax versus meaning:** “The calculation is valid” only confirms Tableau accepts the expression. Check the **numeric result** at one county and again at a broader grouping. The denominator should reflect the population represented by the selected counties, **not the number of daily rows**. LOD results are reconciled with the view's level of detail, so changing the grouping can affect the final aggregate. If the denominator is unexpectedly multiplied, stop and inspect the aggregation rather than trusting a valid formula.

**About `zn()`:** it replaces null results with zero. If a denominator is zero, a ratio is undefined, even when `zn()` displays zero. The historical lab uses “death rate” to mean reported deaths divided by reported cases.

### c. Create income bins and format the rates

1. Right-click `income` in the Scratchpad data pane and select **Create → Bins**. Use the new screenshot to find the menu.

   ![Screenshot 2026-10-30 101511: Create income bins from the data pane](assets/screenshots/income-bin-create-menu.png)

2. In the **Edit Bins** dialog, name the field **`income (bin)`** and set **Size of bins = 10,000**. The original screenshot shows the setting to enter.

   ![Original Lab screenshot: Edit Bins income, size 10,000](assets/screenshots/image10.png)

3. Format **death rate** and **case rate** as percentages. You will use **`income (bin)`** for Step 4(e), *Cases and deaths by income group*.

### d. Compare the numbers (guided check; no extra submission)

Use the actual data-source values and the interactive examples together. Change the number of dates or the group and explain what changes—and what should **not** change.

**Population:** Two counties have populations 1,000 and 2,000. With two daily rows per county, `sum([pop])` adds to 6,000, even though the represented population is **3,000**. Adding another date with zero new cases should not increase the population.

<!-- demonstration:population -->

**Ratio:** Four daily records have cases 10, 90, 20, and 80 and deaths 1, 3, 2, and 4. The average of the four individual ratios is **7.0833%**, but the combined rate is **10 / 200 = 5%**. For a group-wide ratio, aggregate the numerator and denominator first.

<!-- demonstration:ratio -->

### e. Publish the edited data source again

While editing **`firstname_lastname_lab11_data`**, click **Publish**, **not Publish As**. This saves the new fields and hierarchy back to the **same published Lab 11 data source** in `fall2026`. Do not create another data source or overwrite the original Week 9 COVID data source. If Tableau asks which existing source to update, verify the Lab 11 name before continuing.

![Publish the updated Lab 11 data source to fall2026](assets/screenshots/publish-source.webp)

**Monday completion check:** Reopen the published Lab 11 data source and confirm **death rate**, **fixed pop**, **case rate**, income bins, the state–county hierarchy, and the intended numeric results are present. Confirm that the **flow** and the **one Lab 11 data source** both appear in `fall2026`. Later flow runs may refresh or replace the data source and affect its calculations, so if the flow is run again, verify these fields and republish the data source if needed.

**Stop after Step 3 on Monday.** Wednesday begins with the workbook in Step 4.

## 4. Create the following six worksheets (Wednesday)

Open **`firstname_lastname_lab11_data`** and create a new **workbook** using the fields, calculations, bins, and state–county hierarchy already published on Monday. You do not need to recreate them inside the workbook. Publish the workbook after completing its Story.

**Consistent colors throughout this lab:** **cases and case rate = blue**; **deaths and death rate = orange**. For a count-and-moving-average pair, use bars and a darker line in the same color family. For rate maps, use light-to-dark shades of the matching color. Older screenshots may use different colors; follow this rule when creating the new views.

### a. Weekly cases and deaths with moving averages

Create one worksheet named **Weekly Cases and Deaths**, with cases in the upper panel and deaths in the lower panel, as in the original example.

1. **Create the base chart.** Put **`date`** on Columns at the continuous **Week** level, retaining the year. Put **`sum([cases])`** and **`sum([deaths])`** on Rows to create two panels. Set the original measures to **bars**: cases are **blue** and deaths are **orange**.

2. **Add a moving average.** Add a second copy of `sum([cases])`. On this second measure, select **Quick Table Calculation → Moving Average**.

   ![Screenshot 2026-10-30 132147: Quick Table Calculation → Moving Average](assets/screenshots/weekly-moving-menu.png)

3. **Set the calculation window.** In **Edit Table Calculation**, select **Moving Calculation → Average**, **Previous values = 5**, **Next values = 0**, and check **Current value**. Compute along the weekly dates in chronological order. Set the moving-average mark to **Line**.

   ![Moving average settings from the original lab](assets/screenshots/image11.webp)

4. **Combine bars and line.** On the second cases measure, choose **Dual Axis**.

   ![Screenshot 2026-10-30 132231: Dual Axis on the moving-average measure](assets/screenshots/weekly-dual-axis.png)

5. **Synchronize the axes.** Right-click the secondary axis and choose **Synchronize Axis**. The new screenshot shows the command; the older duplicate screenshot is intentionally not repeated.

   ![Screenshot 2026-10-30 132252: Synchronize Axis in the current Tableau interface](assets/screenshots/weekly-sync-axis.png)

6. **Repeat for deaths and set the colors.** Add the same moving average and dual-axis setup to the lower deaths panel. In Marks / **Edit Colors**, use **blue bars and a darker-blue average line for cases**, and **orange bars and a darker-orange average line for deaths**.

   ![Screenshot 2026-10-30 132409: Cases blue and deaths orange with matching moving-average lines](assets/screenshots/weekly-edit-colors.png)

7. **Check the finished chart.** Use the original screenshot to compare the two-panel layout with your worksheet.

   ![Weekly cases and deaths worksheet layout](assets/screenshots/image13.webp)

The moving average uses **the current week and five preceding weeks** when all six positions are available. At the beginning of the series, Tableau uses the available weeks.

### b. Case rate per state

Create a map showing **case rate per state**. Put **case rate** on Color and use a **blue** color scale (lighter blue for lower rates; darker blue for higher rates). Keep **case rate = blue**, consistent with the cases chart.

![Case rate per state map](assets/screenshots/image14.webp)

### c. Death rate per county

Create a map showing **death rate per county** with an **orange** color scale (lighter orange for lower rates; darker orange for higher rates). Keep **death rate = orange**, consistent with the deaths chart. Use the state/county hierarchy and keep counties distinct by their `fips` identifiers.

![Death rate per county map](assets/screenshots/image15.webp)

### d. Median income per county

Create a map of **median income per county**, with a diverging palette. Use `avg([income])` for each county so its income is not added repeatedly across dates.

![Median income per county map](assets/screenshots/image16.webp)

### e. Cases and deaths by income group

Create one worksheet named **Income Groups**. Put **`income (bin)`** on Columns and `sum([cases])` and `sum([deaths])` on Rows to form two panels.

Use bars. On the **Cases** Marks card, put **case rate** on Color and use a **blue** palette. On the **Deaths** Marks card, put **death rate** on Color and use an **orange** palette. Preserve these two color families throughout the workbook.

![Cases and deaths by income group in one worksheet](assets/screenshots/image17.webp)

### f. Median income versus death rate

Create a scatterplot with **`avg([income])`** on the horizontal axis and **death rate** on the vertical axis. Put **`fips`** on Detail so each mark represents one county. Use **orange** marks for the death-rate view.

1. Add a **Trend Line** from the Analytics pane to show the overall income–death-rate association. Compare with the original chart screenshot.

   ![County median income versus death rate with a trend line](assets/screenshots/image18.webp)

2. Add a **horizontal median reference line** for **death rate**: in **Analytics → Reference Line**, drop a line on the view, choose **Table** scope, set **Value = AGG(death rate)** and **Computation = Median**, and display the computation as the label. The new screenshot shows the *Edit Line* dialog. Keep **both** the trend line and the median reference line.

   ![Screenshot 2026-10-30 133026: Add a table-wide median reference line for death rate](assets/screenshots/scatter-median-reference.png)

## 5. Combine four views in a dashboard

Create a dashboard containing:

- The case rate per state map.
- The death rate per county map.
- The median income per county map.
- The median income versus death rate scatterplot.

Enable **Use as Filter** on the state case-rate map. Selecting a state should filter the county-level views.

The original screenshot shows the layout. Keep the county-income aggregation from Step 4 when building your own views.

![Dashboard layout with the state map used as a filter](assets/screenshots/image19.webp)

## 6. Organize the charts and dashboard in a Story

After the instructor's demonstration, create a **Story**. A story point presents a worksheet or dashboard with a saved view state and a caption. Follow the original sequence, checking each screenshot as you build its point:

1. **Story point 1 — Weekly Cases and Deaths.** Add the time-series worksheet and write a short caption about the trends.

   ![Story point 1 weekly cases and deaths](assets/screenshots/image20.webp)

2. **Story point 2 — Income Groups.** Add the cases/deaths-by-income-group worksheet and write a short caption.

   ![Story point 2 income groups](assets/screenshots/image21.webp)

3. **Story point 3 — Virginia (VA).** Add the dashboard, select Virginia on the state map, and click **Update** to save the selection for this point.

   ![Story point 3 dashboard with Virginia selected](assets/screenshots/image22.webp)

4. **Story point 4 — New York (NY).** **Duplicate** the Virginia point, switch the state selection to New York, and click **Update** again.

   ![Story point 4 dashboard with New York selected](assets/screenshots/image23.webp)

Return to the Virginia and New York points to confirm that each keeps its own saved selection. Both Story points should show the intended dashboard state, not the most recently edited state.

## 7. Publish the completed workbook

Publish the finished workbook as **`firstname_lastname_lab11`** in **`fall2026`**, including the six worksheets, dashboard, and Story.

## Submission and evaluation

Publish these three objects before the deadline:

| Object | Name | Points | What will be checked |
|---|---|---:|---|
| **Flow (Monday)** | `firstname_lastname_lab11_flow` | **30** | Both cleaned inputs, correct `fips` join, and data output |
| **Published data source (Monday)** | `firstname_lastname_lab11_data` | **30** | Joined records, `death rate` / `fixed pop` / `case rate`, `income (bin)` at 10,000, hierarchy, numeric verification, and final publish |
| **Workbook — worksheets, dashboard, and Story** | `firstname_lastname_lab11` | **40** | Six worksheets, consistent cases-blue/deaths-orange colors, moving averages, scatterplot trend and median lines, functioning dashboard filter, and four Story points |
| **Total** | | **100** | |

The final submission time is determined by the **last-modified time on Tableau Cloud / Online**. Changes after the deadline are subject to the course syllabus's late policy.

**There is no submission on Canvas.** Use the deadline posted there.
