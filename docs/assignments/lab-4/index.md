---
layout: default
title: "Lab 4: Virginia County Analysis, Infographic, and Interactive Dashboard - IA 342"
---
# Lab 4 â€” Virginia County Analysis, Infographic, and Interactive Dashboard

**IA342 Â· Week 4 Â· Updated after instructor walkthrough**

Continue your existing Business Analyst project. This lab uses **Virginia as the study area** and compares **county-level geographies across the state**.

You will create:

1. one **Benchmark comparison** map;
2. one **Suitability analysis** map;
3. one **Virginia infographic**;
4. one **interactive ArcGIS Dashboard** that brings them together.

**Submit:** one working dashboard viewing URL to Canvas.

---

## 1. Save Virginia as a site

Open your existing `firstname_lastname_arcgis` project.

You already created **Rockingham County** in the earlier lab. Keep it. For this lab, create only one new site: **Virginia**.

1. Go to **Maps â†’ Define areas â†’ Select geography**.
2. Search for **Virginia**.
3. Select the **Virginia** state geography.
4. Save it as a site. The name **Virginia** is fine.

![Select Virginia as a site](../../assets/week-4/screenshots/Screenshot%202026-09-08%20213759.png)

> **Important:** Virginia must exist as a saved site before you run the two analyses below. The analyses will use Virginia as the **area of interest**, but the units being analyzed will be **Counties**.

---

## 2. Analysis 1 â€” Benchmark comparisons

### What does Benchmark comparisons do?

Benchmark comparisons answers:

> **Which areas are above or below a reference value?**

Here, we will compare county-level areas inside Virginia and use the **median** of those county-level values as the reference.

### 2.1 Select the correct geography

This part is slightly tricky.

1. Make sure the **Virginia site is the current site** on the map.
2. Go to **Maps â†’ Run analysis â†’ Benchmark comparisons**.
3. For **Select location type**, choose **Geographies or hexagons**.

**Do not choose `Your sites`.** If you choose the Virginia site directly as a site, Business Analyst treats Virginia as one single area. We want all county-level geographies inside Virginia.

![Choose Geographies or hexagons](../../assets/week-4/screenshots/Screenshot%202026-09-08%20214055.png)

4. In **Area of interest**, choose **Current site**. Because Virginia is the current site, the pane may then display **Virginia**.
5. Keep **Geographies** selected.
6. Set **Level of detail = Counties**.

![Use Virginia as the area of interest and Counties as the level of detail](../../assets/week-4/screenshots/Screenshot%202026-09-08%20214109.png)

> Virginia has independent cities that may appear as county-equivalent geographies. Keep the geography set returned by Business Analyst.

### 2.2 Select variables and run the comparison

Select:

- **2026 Total Population (Esri)**
- **2026 Median Household Income (Esri)**

Then:

1. Turn on **Median** in **Statistics**.
2. Set **Comparison method = Above and below benchmark**.
3. Set **Benchmark = Median**.
4. Use **2026 Median Household Income** as the map variable.
5. Inspect the table and map. Identify at least one county-level area above the median and one below it.

The benchmark is the **median of the county-level areas in this analysis**. It is not the single statewide Virginia median household income value.

![Benchmark comparison result](../../assets/week-4/screenshots/Screenshot%202026-09-08%20214254.png)

### 2.3 Save the Benchmark layer

Click **Save layer** and name it:

`lastname_benchmark`

> **Tip:** ArcGIS services can occasionally take a while to save an analysis layer. If the Save process appears slow, give it time to finish before clicking repeatedly or refreshing the page.

### 2.4 Export the Benchmark map now

Do this **before moving to Suitability analysis**.

Because Benchmark and Suitability are separate analysis workflows, export each one while that analysis is open.

1. Keep/open the saved **Benchmark comparisons** layer.
2. Go to **Share results â†’ ArcGIS web map**.
3. Export the map content as a **new hosted feature service**.
4. Include the Benchmark analysis layer.
5. Name the web map:

`lastname_benchmark_map`

You should end this step with a Benchmark **web map** and its associated **hosted feature layer** in ArcGIS Online.

![Export the Benchmark analysis as its own hosted web map](../../assets/week-4/screenshots/Screenshot%202026-09-08%20215912.png)

[Esri: Run benchmark comparisons](https://doc.arcgis.com/en/business-analyst/web/benchmark-comparisons.htm)  
[Esri: Share web maps and layers](https://doc.arcgis.com/en/business-analyst/web/share-maps.htm)

---

## 3. Analysis 2 â€” Suitability analysis

### What does Suitability analysis do?

Suitability analysis combines several criteria into one score so you can:

> **rank areas under a set of assumptions that you define.**

The score is not an objective statement that one county is "best." Your variable choices, weights, scoring, and classification all affect the result.

### 3.1 Use Virginia counties again

1. Make **Virginia** the current site.
2. Go to **Maps â†’ Run analysis â†’ Suitability analysis**.
3. Choose **Geographies or hexagons**.
4. Set **Area of interest = Current site**.
5. Keep **Geographies** selected.
6. Set **Level of detail = Counties**.

### 3.2 Manually select the three criteria

Click:

**Select criteria â†’ Add variables from data browser**

Then search for and **manually check each of these three variables**. Do not rely on a Featured list or automatically generated criteria list.

#### Criterion 1 â€” Total Population

Select:

**2026 Total Population (Esri)**

For this current Esri variable, keep **Calculation = Default**. The latest Total Population variable in the walkthrough did not present a separate Count calculation option.

![Select 2026 Total Population](../../assets/week-4/screenshots/Screenshot%202026-09-08%20214638.png)

#### Criterion 2 â€” Median Household Income

Select:

**2026 Median Household Income (Esri)**

Use **Calculation = Median**.

![Select 2026 Median Household Income](../../assets/week-4/screenshots/Screenshot%202026-09-08%20214707.png)

#### Criterion 3 â€” Bachelor's Degree

Search for:

`Bachelor's Degree`

Select:

**2026 Population Age 25+: Bachelor's Degree (Esri)**

Use **Calculation = Percentage**.

This variable measures the **population age 25 and older with a bachelor's degree**.

![Select Population Age 25+ Bachelor's Degree](../../assets/week-4/screenshots/Screenshot%202026-09-08%20214828.png)

After selection, your three criteria should look similar to this:

![Three suitability criteria](../../assets/week-4/screenshots/Screenshot%202026-09-08%20214943.png)

### 3.3 Set influence and weights

Keep **Positive influence** for all three criteria.

Then click **Adjust weights** and choose your own reasonable weights.

- The weights should total **100%**.
- Do **not** simply copy the instructor screenshot.
- Your weights should reflect what you think is more or less important in this practice model.
- You will add one short line in the dashboard explaining your chosen weights.

![Adjust suitability weights](../../assets/week-4/screenshots/Screenshot%202026-09-08%20215013.png)

### 3.4 Use a consistent scoring method

In **Scoring method**:

- **Preset method:** `Combine values (default)`
- **Final score scale:** `0 to 100`

Using 0â€“100 makes the final score easier to interpret.

![Use Combine values and a 0-to-100 final score](../../assets/week-4/screenshots/Screenshot%202026-09-08%20215129.png)

### 3.5 Choose a classification

Open **Class options**.

Choose a reasonable classification method and number of classes for your map. Available methods include:

- **Natural breaks**
- **Quantile**
- **Equal interval**

You may choose the method that makes the statewide county pattern easiest to read.

Use a **sequential color ramp** for the final suitability score. You may adjust the ramp direction, transparency, and outline so the county pattern is readable.

![Choose classification options](../../assets/week-4/screenshots/Screenshot%202026-09-08%20215209.png)

![Style the final Suitability map with a sequential color ramp](../../assets/week-4/screenshots/Screenshot%202026-09-08%20215226.png)

### 3.6 Save the Suitability layer

Save the layer as:

`lastname_suitability`

Record the highest-ranked county-level area and its score.

### 3.7 Export the Suitability map now

Export this analysis **separately** from the Benchmark map.

1. Keep/open the **Suitability analysis** layer.
2. Go to **Share results â†’ ArcGIS web map**.
3. Export the map content as a **new hosted feature service**.
4. Include the Suitability analysis layer.
5. Name the web map:

`lastname_suitability_map`

You should now have **two separate analysis web maps**:

- `lastname_benchmark_map`
- `lastname_suitability_map`

![Export the Suitability analysis as its own hosted web map](../../assets/week-4/screenshots/Screenshot%202026-09-08%20215452.png)

[Esri: Perform a suitability analysis](https://doc.arcgis.com/en/business-analyst/web/suitability-analysis.htm)  
[Esri: Suitability analysis reference](https://doc.arcgis.com/en/business-analyst/web/understand-suitability-analysis.htm)  
[Esri: Share web maps and layers](https://doc.arcgis.com/en/business-analyst/web/share-maps.htm)

---

## 4. Run one Virginia infographic

The infographic is different from the county-level analysis maps.

Because you are selecting the saved **Virginia** site, this standalone infographic summarizes **Virginia as one statewide site**. It does not automatically show one panel for every county.

### 4.1 Run the standalone infographic

1. Go to **Reports â†’ Run reports â†’ Run infographics**.
2. Select the **Virginia** site.
3. Manually select **Demographic Summary**.
4. Click **Run now**.
5. Identify at least two useful statewide indicators.

![Select Demographic Summary for the Virginia site and run it](../../assets/week-4/screenshots/Screenshot%202026-09-08%20220053.png)

The result should be a statewide Virginia infographic, similar to this:

![Standalone Virginia Demographic Summary infographic](../../assets/week-4/screenshots/Screenshot%202026-09-08%20220020.png)

### 4.2 Understand what is and is not saved

This **Reports â†’ Run infographics** run is a one-time output. It is **not saved back into your Business Analyst project as a reusable project item**. If you close it without exporting it, that particular run is gone and you would need to run the infographic again.

If you want to keep this standalone output, export it. Available formats in the walkthrough included:

- PDF
- Image
- Dynamic HTML
- Excel

![Export options for the standalone infographic](../../assets/week-4/screenshots/Screenshot%202026-09-08%20220038.png)

> **Important:** The infographic you run here and the infographic used later in the Dashboard workflow are **two separate runs**. In Step 5, Business Analyst asks you to choose/run the infographic again. That second run is embedded in the dashboard as **Embedded content**. It does not reuse this standalone output.

[Esri: Create infographics and reports](https://doc.arcgis.com/en/business-analyst/web/create-infographics-and-reports.htm)

---

## 5. Create the Virginia dashboard

Go to:

**Maps â†’ Share results â†’ ArcGIS Dashboards**

This starts a **new infographic run for the dashboard**. The dashboard does not reuse the standalone infographic output from Step 4.

First choose **One site â†’ Different infographics**:

![Choose One site â†’ Different infographics](../../assets/week-4/screenshots/Screenshot%202026-09-08%20220539.png)

Choose:

- **Dashboard type:** `One site, Different infographics`
- **Site:** Virginia
- **Infographic:** Demographic Summary
- **Default infographic display:** Auto
- **Title:** `Virginia Analysis and Demographics`

![Select Virginia and Demographic Summary](../../assets/week-4/screenshots/Screenshot%202026-09-08%20220527.png)

Set the display to **Auto**, enter the dashboard title, and create the dashboard. The sharing choices on this screen are optional because you will complete the final public-sharing workflow later from ArcGIS Online item pages.

![Set display, title, and dashboard creation options](../../assets/week-4/screenshots/Screenshot%202026-09-08%20220601.png)

Create the dashboard.

The generated dashboard should contain the **embedded infographic**. Depending on the Business Analyst output, it may also contain a default **Virginia base/location map**.

For this lab:

- **keep the embedded infographic**;
- if a default Virginia/base map appears and it is only a location map, **delete it**;
- then add the Benchmark and Suitability maps **one at a time** in Step 6.1.

Do not worry if your first Dashboard view does not look exactly like the instructor example. The required final layout is defined in Step 6.

[Esri: Create a dashboard](https://doc.arcgis.com/en/business-analyst/web/arcgis-dashboards.htm)

---

## 6. Build the final interactive dashboard

Your finished dashboard must contain **at least four analytical elements**:

1. **Virginia Demographic Summary infographic**
2. **Benchmark map**
3. **Suitability map**
4. **One additional data widget**

### 6.1 Add both maps

Use **Add element** to add dashboard components. The menu includes Map, Map legend, Serial chart, Indicator, Gauge, Rich text, Embedded content, and other elements.

![Use Add element to build the dashboard](../../assets/week-4/screenshots/Screenshot%202026-09-08%20220903.png)

Add a **Map** element for:

- `lastname_benchmark_map`
- `lastname_suitability_map`

For **both maps**:

- give the element a clear title;
- turn on the **Legend**;
- turn on the **Scale bar** when the layout allows it;
- keep the maps large enough to read the county pattern.

Add the maps **one at a time**. The example below shows the dashboard after the Benchmark map has been added beside the embedded infographic. Your second analysis map will be added the same way.

![Dashboard after adding the first analysis map](../../assets/week-4/screenshots/Screenshot%202026-09-08%20220759.png)

### 6.2 Add one data widget

Add one additional element that summarizes a meaningful numeric variable.

You may use:

- **Indicator**
- **Gauge**
- **Serial / bar chart**

For example, you could display **Median Household Income** or another meaningful field from one of your analysis layers.

Give the widget a clear title. For example, an Indicator can summarize the **Average** of the `2026 Median Household Income` field from the Benchmark comparisons layer.

![Choose the layer, statistic, and field for a data widget](../../assets/week-4/screenshots/Screenshot%202026-09-08%20221112.png)

![Example data widget with a clear title](../../assets/week-4/screenshots/Screenshot%202026-09-08%20221059.png)

### 6.3 Make the dashboard interactive

Choose one of your two maps as the **source map**.

Configure actions so interaction with that map affects other elements.

At minimum:

1. Use **Filter** to update your data widget and any compatible target layer/element.
2. Use **Set extent** so the other map follows the source map's extent.

A useful pattern is:

**Benchmark map â†’ filters data widget + sets Suitability map extent**

or the reverse.

Use **Map actions** and/or **Layer actions** to choose the targets that should respond.

![Choose Filter targets and the other map from Map actions](../../assets/week-4/screenshots/Screenshot%202026-09-08%20221206.png)

![Configure map actions for filtering and linked extent](../../assets/week-4/screenshots/Screenshot%202026-09-08%20221244.png)

If you add a layer-selection action, you may also let clicking a county filter other compatible elements.

[Esri: Configure actions for dashboard elements](https://doc.arcgis.com/en/dashboards/latest/create-and-share/configuring-actions-on-dashboard-elements.htm)

### 6.4 Add a very short story / methods note

Add a small **Rich text** element with no more than about three short bullets.

Include:

- what the Benchmark map compares;
- your three Suitability criteria and chosen weights;
- one useful finding from the dashboard.

Keep this concise. The dashboard should remain visual.

---

## 7. Share everything publicly

ArcGIS Dashboards does not require a separate **Publish** button. Save the dashboard, then manage sharing from ArcGIS Online item pages.

### 7.1 Share every dependency

Go to **My Content** or the dashboard item page.

Make sure **Everyone (public)** can access:

- the Dashboard;
- the Benchmark web map;
- the Benchmark hosted feature layer;
- the Suitability web map;
- the Suitability hosted feature layer;
- any Business Analyst-generated web map or hosted layer still listed under **Items used** by the dashboard.

Your content list may look similar to this:

![Related dashboard items in ArcGIS Online](../../assets/week-4/screenshots/Screenshot%202026-09-08%20222150.png)

The dashboard item page also shows **Items used**. Use that list as your final dependency checklist. You will return to this same item page in Step 7.3 to copy the public dashboard URL.

### 7.2 Enable Public data collection when required

In the instructor walkthrough, the Business Analyst-exported hosted feature layers were editable, so ArcGIS required the **Public data collection** approval before they could be shared publicly.

For each affected hosted feature layer:

1. Open the layer's **item page**.
2. Open **Settings**.
3. Find **Public data collection**.
4. Turn on:

**Approve this layer to be shared with the public when editing is enabled.**

![Enable Public data collection for an editable hosted feature layer](../../assets/week-4/screenshots/Screenshot%202026-09-08%20222021.png)

Then return to **Share** and set the item to **Everyone (public)**.

![Set the hosted feature layer sharing level to Everyone (public)](../../assets/week-4/screenshots/Screenshot%202026-09-08%20222034.png)

> This setting is specifically a safety approval for publicly shared layers when editing is enabled.

[Esri: Manage hosted feature layer editing](https://doc.arcgis.com/en/arcgis-online/manage-data/manage-editing-hfl.htm)

### 7.3 Copy and test the dashboard URL

Return to the **Dashboard item page** in ArcGIS Online. Do **not** use the Edit Dashboard address from the browser.

In the item page's **Details** panel, find **URL** and click **Copy**. This is the viewing URL you will submit.

![Copy the viewing URL from the Dashboard item page](../../assets/week-4/screenshots/Screenshot%202026-09-08%20222218.png)

Open a new **Incognito / Private** browser window and paste that copied URL.

Confirm that:

- the infographic loads;
- both maps load;
- the data widget loads;
- the legend(s) appear;
- your interaction works;
- no sign-in prompt blocks the dashboard.

![Public dashboard tested in an Incognito window](../../assets/week-4/screenshots/Screenshot%202026-09-08%20222250.png)

### Instructor functional example

The following dashboard is a **functionality example only**. Do not copy its visual design or values. Your own dashboard must work with your own analysis outputs.

https://www.arcgis.com/apps/dashboards/e59a89f479e4488db289575d1ef4c063#

---

## 8. Submission

Submit **one dashboard viewing URL** to Canvas.

Before submitting, open it once more in a Private / Incognito window.

---

## Rubric â€” 100 points

| Component | Required evidence | Points |
|---|---|---:|
| **Benchmark map** | Virginia county-level Benchmark analysis with a correct median benchmark and its own working exported web map | 20 |
| **Suitability map** | Virginia county-level Suitability analysis, three manually selected criteria, student-chosen weights, 0â€“100 score, readable classification and sequential color ramp, exported as its own working web map | 20 |
| **Virginia infographic** | Standalone Virginia Demographic Summary run completed and understood as a one-time output; dashboard contains its own embedded Virginia infographic run | 20 |
| **Interactive dashboard design** | Embedded infographic + two maps + one data widget; map legends; concise methods/findings text; at least one working filter and linked map extent/action | 20 |
| **Sharing and submission** | Dashboard and all required dependencies public, editable hosted layers approved for public data collection when required, dashboard verified in Private/Incognito mode, correct viewing URL submitted | 20 |
| **Total** | | **100** |
---
[Return to Course Home](../../) | [Return to Module 4](../../modules/module-4/)