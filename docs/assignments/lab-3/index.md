---
layout: default
title: "Lab 3: ArcGIS Business Analyst II — Thematic Maps, Report, and StoryMap - IA 342"
---

# Lab 3 — ArcGIS Business Analyst II

## Thematic Maps, Report, and StoryMap

This is the second of three connected ArcGIS Business Analyst labs.

- **Week 2:** create the Business Analyst project, JMU site, data, and PDF report.
- **Week 3:** continue the same project, create thematic maps, and publish a StoryMap.
- **Week 4:** continue the project again for spatial analysis and a dashboard.

You will use the **same Business Analyst project** from Week 2:

`firstname_lastname_arcgis`

## Final product

Submit **one public ArcGIS StoryMap URL**.

Your StoryMap will combine four map views with short explanations and the report you already created in Week 2.

## Learning goals

By the end of this lab, you should be able to:

- create and reuse saved sites in Business Analyst,
- create a choropleth map and compare classification methods,
- create a proportional-symbol map,
- use Smart Map Search with two variables,
- run a point-of-interest search,
- export several Business Analyst layers into one hosted web map,
- build a StoryMap with separate map views and concise analytical text, and
- publish the StoryMap and all required map layers for anonymous public access.

## Before you begin

1. Open your Week 2 project: `firstname_lastname_arcgis`.
2. Confirm that the saved **James Madison University** site still contains the 5-, 10-, and 15-minute drive-time areas.
3. Confirm that your Week 2 report is still listed under previously run reports.
4. Check credit estimates before running credit-consuming tools.

---

# Session 1 — Build the Spatial Views

## Step 1 — Define and save Rockingham County as a site

Do this once at the beginning. After the site is saved, reuse it in the mapping tools instead of searching for Rockingham County again and again.

1. Open **Define areas → Select geography**.
2. Search for `Rockingham County`.
3. Under **Counties**, select **Rockingham County, VA**.
4. Finish the selection and save it as a site. Keep the clear name:

`Rockingham County, VA`

![Select Rockingham County, VA and save it as a site](../../assets/week-3/screenshots/Screenshot%202026-09-03%20120339.png)

For the rest of the lab, when a tool asks for an **Area of interest**, choose **Your sites** and select the saved Rockingham County site.

![Reuse the saved Rockingham County site as the area of interest](../../assets/week-3/screenshots/Screenshot%202026-09-03%20120414.png)

---

## Step 2 — Map 1: median household income choropleth

1. Open **Create maps → Color-coded maps**.
2. For **Area of interest**, choose the saved **Rockingham County, VA** site.
3. Use **Block Groups** when available and readable.
4. Choose **Median Household Income**.
5. Use **Counts and amounts (color)**.
6. Turn on classification and use **five classes**.
7. Compare these methods:
   - **Natural breaks**
   - **Equal interval**
   - **Quantile**
8. Look at the histogram and how the map changes.
9. Choose the method that gives the most useful view for your map.
10. Choose a clear sequential color ramp.
11. Save the layer as:

`lastname_income_choropleth`

![Median Household Income choropleth for the saved Rockingham County site](../../assets/week-3/screenshots/Screenshot%202026-09-03%20120548.png)

![Compare Natural breaks, Equal interval, and Quantile](../../assets/week-3/screenshots/Screenshot%202026-09-03%20120621.png)

---

## Step 3 — Map 2: total population with proportional symbols

1. Create another **Color-coded map**.
2. Select the saved **Rockingham County, VA** site as the Area of interest.
3. Use the same geography level as the income map.
4. Choose **Total Population**.
5. Change the style to **Counts and amounts (size)**.
6. Use a simple circle symbol.
7. Adjust minimum and maximum symbol size so the map remains readable.
8. Add some transparency if symbols overlap.
9. Keep the size legend available.
10. Save the layer as:

`lastname_population_symbols`

![Total Population shown with proportional symbols](../../assets/week-3/screenshots/Screenshot%202026-09-03%20121019.png)

---

## Step 4 — Smart Map Search: combine population and income

Smart Map Search is an **identification tool**. The goal is to define a meaningful combination of criteria and see which areas match it.

1. Open **Create maps → Smart map search**.
2. Choose the saved **Rockingham County, VA** site as the Area of interest.
3. Use the same small-area geography when possible.
4. Add these two variables:
   - **Total Population**
   - **Median Household Income**
5. Use the histograms to define a meaningful question. Examples:
   - areas with **higher population and lower income**,
   - areas with **higher population and higher income**, or
   - another clear combination that you can explain.
6. Set the ranges yourself. There is **no required percentage of areas that must match**.
7. Review the matching areas.
8. Save the layer as:

`lastname_smart_map`

![Smart Map Search using Total Population and Median Household Income](../../assets/week-3/screenshots/Screenshot%202026-09-03%20121609.png)

---

## Step 5 — Grocery-store POI search near JMU

1. Open **Create maps → Points of interest (POI) search**.
2. For **Area of interest**, choose your saved **James Madison University** site.
3. Keep the full Week 2 JMU site with its **5-, 10-, and 15-minute drive-time rings**. The map should show all three rings; the outer study area extends to 15 minutes.
4. Search for **grocery stores** or the closest grocery/supermarket category available.
5. Review the returned places and the map.
6. Save the layer as:

`lastname_jmu_grocery_poi`

![Grocery-store POI search using the saved JMU site](../../assets/week-3/screenshots/Screenshot%202026-09-03%20121959.png)

Record the category and the number of returned places for later use in the StoryMap.

A POI search shows locations in the selected data source. It does not prove affordability, quality, or actual travel behavior.

---

# Session 2 — Share the Maps and Build the StoryMap

## Step 6 — Export the four map layers as one hosted web map

1. Return to the map contents and turn on the four required saved layers:
   - `lastname_income_choropleth`
   - `lastname_population_symbols`
   - `lastname_smart_map`
   - `lastname_jmu_grocery_poi`
2. Choose **Share results → ArcGIS web map**.
3. Name the web map:

`lastname_firstname_lab3_maps`

4. Select all four required layers.
5. **Check `Export map layers in a new hosted feature service`. This is required for this lab.**
6. Share/create the map.

![Share all four layers and export them in a new hosted feature service](../../assets/week-3/screenshots/Screenshot%202026-09-03%20123642.png)

One web map can contain all four layers. Later, in StoryMaps, you will reuse the same web map and turn different layers on or off for each section.

---

## Step 7 — Create the StoryMap from Business Analyst

1. Choose **Share results → ArcGIS StoryMaps**.
2. Add the saved JMU site when the workflow asks for a site.
3. In **Configure items**:
   - keep the map/site content you need,
   - turn **Infographic OFF**,
   - turn **Reports ON** so the previously run Week 2 report is included.
4. Name the story:

`lastname_firstname_lab3_story`

5. Create the draft and open it in the StoryMaps builder.

![Configure the StoryMap with Reports on and Infographic off](../../assets/week-3/screenshots/Screenshot%202026-09-03%20124546.png)

6. Edit the StoryMap cover so the title clearly identifies your Lab 3 story.

![Edit the StoryMap title, subtitle, and author information](../../assets/week-3/screenshots/Screenshot%202026-09-03%20124830.png)

Your **story title** should be clear and specific. Adding your name, professional contact information, LinkedIn, or portfolio link is **optional**. If you plan to keep the StoryMap as a portfolio item, you may add those details.

### About the report

The report is supporting content from Week 2. In a signed-out public view, the report download may still require an ArcGIS login or display a download error. **That is acceptable for this lab.**

The graded public-access requirement applies to the StoryMap itself and the required maps/layers. The maps must display to an anonymous viewer.

---

## Step 8 — Add the maps and write the explanations in the StoryMap

Start with a short introduction. Then create four map sections. You may use a **Sidecar** or separate map blocks.

For each map section, follow the same sequence:

1. **Add the map.** Use **Add → Map** and select `lastname_firstname_lab3_maps`.

![Add a map block to the StoryMap](../../assets/week-3/screenshots/Screenshot%202026-09-03%20124945.png)

2. Turn on only the layer that this section is explaining. Then open the map **Options** and make sure **Legend** is enabled.

![Enable the legend for the map](../../assets/week-3/screenshots/Screenshot%202026-09-03%20125009.png)

3. **Add information here.** Add the short written explanation directly beside the map so the reader can see the evidence and interpretation together.

![Add information beside the map](../../assets/week-3/screenshots/Screenshot%202026-09-03%20125105.png)

Use the same web map more than once; simply change which layer is visible for each section.

### Map section 1 — Income choropleth

Show `lastname_income_choropleth` and add a short paragraph that explains:

- what the color represents,
- which classification method you selected and why, and
- one visible spatial pattern.

### Map section 2 — Population proportional symbols

Show `lastname_population_symbols` and explain:

- what symbol size represents, and
- one visible population pattern.

### Map section 3 — Smart Map Search

Show `lastname_smart_map` and explain:

- the two variables,
- the ranges/criteria you selected, and
- what the matching areas have in common.

### Map section 4 — Grocery POIs

Show `lastname_jmu_grocery_poi` and explain:

- the category and the JMU drive-time site (5-, 10-, and 15-minute rings),
- how many places were returned, and
- one useful observation or limitation.

Keep the writing concise. A few clear sentences for each map are enough. **A separate conclusion section is not required.**

### Optional finishing details

These items are **optional** and are not graded:

- a short source note naming Esri Business Analyst demographic data, the POI data source shown in the interface, and the date you created the maps;
- your name;
- professional contact information;
- a LinkedIn or portfolio link.

If you plan to use the StoryMap later as a portfolio item, these details can make the final product more useful.

### Instructor example

Use this published example to understand the expected structure and public behavior:

[Instructor Week 3 StoryMap example](https://storymaps.arcgis.com/stories/81dace0741044e1196003c0bb81d1d10)

The example shows the general layout and public map behavior, but its explanatory text is intentionally incomplete. **Your submission must include the short explanations listed above.** A polished StoryMap can also become a useful portfolio item; name and contact details remain optional.

---

## Step 9 — Publish everything needed for the maps to work publicly

1. In StoryMaps, click **Publish**.
2. Set the StoryMap sharing level to **Everyone (Public)**.

![Publish the StoryMap to Everyone (Public)](../../assets/week-3/screenshots/Screenshot%202026-09-03%20124045.png)

3. When ArcGIS shows **Content sharing** and says that the map or layers require sharing updates, choose **Update sharing**.

![Update sharing for the web map and its related layers](../../assets/week-3/screenshots/Screenshot%202026-09-03%20124122.png)

4. Verify the web map itself is shared with **Everyone (public)**.
5. Verify each hosted feature layer used by the map is also public. In the instructor test, the web map contains four hosted layers.

![Verify the web map and hosted layers are shared with Everyone](../../assets/week-3/screenshots/Screenshot%202026-09-03%20124132.png)

6. Copy the **published viewing URL**. Do not submit an edit/builder URL.

---

## Step 10 — Required private/incognito test

Before you submit:

1. Sign out of ArcGIS completely.
2. Open a new **private/incognito browser window**.
3. Paste the published StoryMap URL.
4. Move through every map section.
5. Confirm that:
   - the StoryMap opens without a login,
   - all four maps/layers display,
   - legends and labels are readable, and
   - there is no missing-map or restricted-layer message.

The Week 2 report may still fail to download while signed out. **That report-download error is acceptable.** The four required maps must remain visible.

If a map does not appear, return to ArcGIS, make the web map and the related hosted layers public, republish if needed, and test again.

---

# Submission

Submit **one public StoryMap viewing URL** to Canvas.

Your StoryMap should be named:

`lastname_firstname_lab3_story`

Do not submit screenshots, a PDF, the Business Analyst project URL, or a StoryMap edit link.

## Final check

Before submitting, confirm that:

- you continued the same Business Analyst project from Week 2,
- Rockingham County was saved once as a site and reused in the mapping tools,
- the StoryMap contains four required map views,
- the Week 2 report is included as supporting content,
- each map has its short explanation,
- the StoryMap, web map, and required hosted map layers are public, and
- the complete StoryMap has passed the signed-out private/incognito test.

---

# Grading rubric — 100 points

| Requirement | Points |
|---|---:|
| **Maps and spatial analysis:** correct income choropleth, population proportional symbols, Smart Map Search, and grocery POI map; appropriate classification/symbology | 50 |
| **StoryMap content and organization:** all four map views, concise explanations beside the correct maps, and the Week 2 report | 30 |
| **Public publication and access:** submitted viewing URL opens while signed out and all required maps/layers display in a private/incognito browser | 20 |
| **Total** | **100** |

Partial credit within each category is based on how much of the required work is present and correct.

## Official references

- [Create color-coded maps](https://doc.arcgis.com/en/business-analyst/web/color-coded-maps.htm)
- [Use Smart Map Search](https://doc.arcgis.com/en/business-analyst/web/smart-map-search.htm)
- [Map points of interest](https://doc.arcgis.com/en/business-analyst/web/points-of-interest-search.htm)
- [Create a story from Business Analyst](https://doc.arcgis.com/en/business-analyst/web/story-map.htm)
- [Share items with everyone](https://doc.arcgis.com/en/arcgis-online/share-maps/share-items.htm)

---
[Return to Course Home](../../) | [Return to Module 3](../../modules/module-3/)
