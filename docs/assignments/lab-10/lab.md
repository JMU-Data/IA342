# Lab 10 — Dashboard Design in Tableau

**IA342 · Week 10 · October 26–30, 2026**  
**Monday:** create five worksheets · **Wednesday:** design, test, and publish one interactive dashboard

## Objectives

- Reuse the **published Week 9 COVID Data Source**. Do not publish a second Data Source.
- Build **four charts (3.1–3.4) and one totals table (3.5)** in a new workbook.
- Arrange the views intentionally, working with **Automatic size, layout containers, Floating and Tiled objects, legends, images, Text, and Blank objects**.
- Connect the state map to other views, add useful titles, and create a thoughtful **Phone layout**.

**Student deliverable:** One workbook named **`firstname_lastname_lab10`** in the **`fall2026`** Tableau Online project. Replace `firstname_lastname` with your own name. No new Data Source and no Canvas file upload.

> **Screenshot guide.** These screenshots were captured by the instructor in Tableau Online on **October 22, 2026**. Their demo values, sheet labels during editing, and account names are illustrations—not numbers to copy. Follow the written instructions and name the final worksheets **3.1–3.5**.

## Part I — Monday: Prepare the individual views

### 1. Download a COVID-related image (**required**)

Find a relevant COVID-related image that you are **allowed to reuse**, download it to your computer, and save its creator/source URL and any attribution or license information. You will insert this file into the dashboard in Step 4.7. The image is **required**, not an optional decoration. Use a meaningful photo or illustration rather than an unrelated graphic.

**Respect image and logo rights.** Being available online does not mean an image is free to reuse. Check its license/terms. Corporate and university logos can have additional trademark or brand restrictions; do not assume you can use them without permission.

### 2. Create the Week 10 workbook using the Week 9 Data Source

1. Open **Tableau Online → `fall2026`** and locate your published **`firstname_lastname_week9_covid_data`** Data Source.
2. Open the Data Source menu and choose **New Workbook**. You are starting a new workbook from the existing published Data Source, *not* copying the Week 9 workbook.
3. Save it as **`firstname_lastname_lab10`**. Leave the Week 9 Data Source and workbook unchanged.
4. Create and rename worksheets **3.1, 3.2, 3.3, 3.4, and 3.5** as you complete the steps below.

The data are from the historical class exercise. They are **not live COVID reporting**. Use `Confirmed Count`, `Death Count`, `Confirmed Date`, and the geographic fields shown in your Data pane.

![Open New Workbook from the existing Week 9 COVID Data Source.](screenshots/Screenshot%202026-10-22%20150546.png)

### 3.1 — Line chart: Cases and deaths by week

1. Add **`WEEK(Confirmed Date)`** on Columns and **`SUM(Death Count)`**, **`SUM(Confirmed Count)`** on Rows.
2. Use **Line** marks, displaying deaths in **orange** and cases in **blue**, as illustrated.
3. Keep the weekly axis and the labels readable; do not hide either measure's scale. Rename the worksheet **3.1**.

![Worksheet 3.1 — two weekly line charts, deaths in orange and cases in blue.](screenshots/Screenshot%202026-10-22%20151148.png)

### 3.2 — Bar chart: Cases and deaths by county

1. Add **`County Name` only** to Rows. **Do not add `State Name`** to Rows for this worksheet.
2. Put **`SUM(Death Count)`** and **`SUM(Confirmed Count)`** on Columns, side by side.
3. Make two horizontal bar panes (orange for deaths and blue for cases). Sort counties so the comparison is useful; keep county labels legible.
4. Rename the worksheet **3.2**. Later, the dashboard's state-map filter will narrow which counties are displayed; you do **not** need to build a separate State Name row grouping.

![Worksheet 3.2 — county names on Rows, death and confirmed count bars side by side.](screenshots/Screenshot%202026-10-22%20151246.png)

### 3.3 — Build a dual-axis state map (follow the sequence)

**Step A — Create a filled map (choropleth).** On a fresh worksheet, select **`State Name`** and **`Confirmed Count`** in the Data pane. Open **Show Me → Filled Map**. Check that states are colored according to `SUM(Confirmed Count)`; this becomes the background layer.

![3.3 Step A — select State Name and Confirmed Count, then choose Filled Map in Show Me.](screenshots/Screenshot%202026-10-22%20151731.png)

**Step B — Copy the map layer.** Duplicate **`Latitude (generated)`** on the Rows shelf so the worksheet has **two maps**, one above the other. In the Marks cards, you can now edit the two Latitude layers separately. Leave the first filled-map layer as the cases layer.

![3.3 Step B — two Latitude (generated) pills create two map layers before dual axis.](screenshots/Screenshot%202026-10-22%20151750.png)

**Step C — Make the second layer show deaths.** Select the **second `Latitude (generated)` Marks card** (not `All`). Remove `SUM(Confirmed Count)` from **Color** on that card, change the Marks type to **Circle** if needed, and place **`SUM(Death Count)` on Size**. Keep `State Name` as the state-level geographic detail. You should now see the cases choropleth above and death-sized circles below.

![3.3 Step C — the lower map uses Death Count on Size, not cases on Color.](screenshots/Screenshot%202026-10-22%20151805.png)

**Step D — Overlay the maps.** Open the menu on the **second `Latitude (generated)`** pill and select **Dual Axis**. The state fill and death circles become a single overlaid map.

![3.3 Step D — choose Dual Axis from the second generated latitude pill.](screenshots/Screenshot%202026-10-22%20151815.png)

**Step E — Finish the marks.** In the second layer's Marks card, change the death circles to **orange**. The resulting view shows a cases-filled state choropleth with orange circles sized by deaths. Confirm that both legends are visible and rename the worksheet **3.3**.

![3.3 Step E — final dual-axis state map, with a cases fill and orange death circles.](screenshots/Screenshot%202026-10-22%20151840.png)

### 3.4 — County map: Duplicate 3.3 and drill down

1. **Duplicate worksheet 3.3**, then rename the copy **3.4**.
2. In the **Marks** area, use the geographic hierarchy to **expand `State Name` to `County Name`**. The map changes from state to county detail while keeping the dual-axis structure.
3. Check the result against the screenshot. Keep the existing two map layers; no extra geographic fields are needed.

![3.4 Step 1 — duplicate the completed worksheet 3.3.](screenshots/Screenshot%202026-10-22%20151939.png)

![3.4 Step 2 — expand State Name to County Name in the Marks geographic hierarchy.](screenshots/Screenshot%202026-10-22%20152006.png)

### 3.5 — Totals table

1. Create worksheet **3.5**, showing **total Confirmed Count and total Death Count** as a compact text table using Measure Names / Measure Values.
2. Format the numbers so they fit their cells and are easy to read. **No extra color changes are required** for this table.
3. Check **Fit → Entire View** (or the available equivalent) so the totals fit cleanly in the allocated space.

![3.5 Step 1 — compact text table with Confirmed Count and Death Count.](screenshots/Screenshot%202026-10-22%20152210.png)

![3.5 Step 2 — use Fit / Entire View to keep both totals visible.](screenshots/Screenshot%202026-10-22%20152223.png)

![3.5 Final — formatted total values, ready for the dashboard.](screenshots/Screenshot%202026-10-22%20153313.png)

**Monday checkpoint:** Your new workbook has exactly the **five required worksheets**, all using the published Week 9 Data Source. Save your work. You will arrange these into one dashboard on Wednesday.

## Part II — Wednesday: Build the dashboard

### 4.1 — Create a dashboard; set Size to Automatic

Create a new Dashboard and set **Size → Automatic**. We are using **Automatic**, not a fixed width/height. As the available window changes, the layout needs to remain readable.

![4.1 — the dashboard size menu with Automatic selected.](screenshots/Screenshot%202026-10-22%20153354.png)

### 4.2 — Add 3.5 first

Drag worksheet **3.5** onto the blank dashboard first. It will serve as the totals panel. You can resize the panel by dragging its edges or the boundaries of the surrounding containers.

### 4.3 — Check Dashboard and Layout views

Switch between the **Dashboard** and **Layout** tabs in the editing panel. The **Layout** view exposes the item hierarchy: a dashboard contains layout containers, and containers contain sheets, legends, Text, Blank, and other items. Select different items in the hierarchy and observe which area is highlighted. **Moving or resizing one container affects its contents.**

![4.2–4.3 — totals worksheet added and the Layout panel showing its container position.](screenshots/Screenshot%202026-10-22%20153450.png)

### 4.4 — Add 3.3; make its legends Floating

Drag **3.3** onto the dashboard. If a legend is hidden, open the small drop-down triangle on that worksheet's dashboard item and use **Legends → Show legend**. Move the **3.3 legends to Floating**, then drag them into useful positions that do not hide the map.

**Why Floating?** Floating objects can be placed freely, even on top of another item. That flexibility has a tradeoff: because they use positioned coordinates rather than participating in a tiled container, they may overlap or appear poorly aligned when an **Automatic** dashboard resizes. You must check the result at different window sizes.

![4.4 — use the dashboard-item menu to switch a legend to Floating.](screenshots/Screenshot%202026-10-22%20153528.png)

![4.4 — floating legends can be moved independently around the state map.](screenshots/Screenshot%202026-10-22%20153715.png)

### 4.5 — Place 3.4 below the totals panel; keep its legends Tiled

Drag **3.4** into the **Tiled** layout beneath the **3.5 totals panel**, as shown in the instructor's dashboard arrangement. If Tableau does not show a legend automatically, use the worksheet's drop-down menu to enable it. Keep the **3.4 legends Tiled** and place them within the appropriate container.

**Why Tiled here?** County-map content changes with the selected state. A **Tiled** legend remains part of its container's layout rather than floating at a fixed overlay position, which usually makes it more predictable as the content or screen size changes. It is less free-form than Floating, but better suited to a responsive layout. Adjust the container boundaries to allocate stable space for the county map and its legends.

![4.5 — worksheet menu for Legends and the Tiled option while arranging 3.4.](screenshots/Screenshot%202026-10-22%20153855.png)

### 4.6 — Add 3.1 and 3.2; fine-tune the layout

Drag **3.1** (weekly trend) and **3.2** (county bars) into the remaining dashboard space. Your finished **Default** layout must include **all four charts and the totals table**. Revisit **Dashboard → Layout** to resize containers and keep charts, legends, and titles readable. Avoid covering the data with Floating items.

### 4.7 — Insert your downloaded COVID image (**required**)

1. In the **Objects** pane, select **Image** and **drag → drop → release** it onto the dashboard.
2. In the **Edit Image Object** dialog, choose **Insert Image File → Choose** and upload the COVID image downloaded in Step 1. You may also use **Link to Image** when the image URL is stable and its reuse rights allow it.
3. Optionally set **URL Opened When Image Is Clicked** to an appropriate source or information page. Add meaningful **Alt Text** and adjust **Fit Image / Center Image** if helpful.
4. Make room for the image without shrinking the analytical views so much that they become unreadable. Record the image's source and reuse/credit details in the dashboard.

Do not use a company or university logo unless its applicable trademark/brand policy permits your use. In an instructional demo, it is better to use a clearly reusable image than assume a logo is unrestricted.

![4.7 — drag Image into a container; choose Insert Image File, optional link and Alt Text.](screenshots/Screenshot%202026-10-22%20154216.png)

![4.7 — image container placed on the dashboard before uploading the file.](screenshots/Screenshot%202026-10-22%20154507.png)

### 4.8 — Add Text and Blank objects

Use **Text** for short descriptions and source credits. At minimum, identify **your name**, the historical COVID Data Source (original source: **1Point3Acres**), and your image credit. If helpful, state the data period shown in your workbook.

Use **Blank** objects to control **spacing and relative positions within a Tiled container**. Think of Blank as intentional breathing room between objects, rather than an empty chart. You can resize the Blank object's area to help align and balance nearby sheets.

![4.8 — Text editor for author and data-source attribution.](screenshots/Screenshot%202026-10-22%20154444.png)

### 4.9 — Enable the **3.3 State map** as a filter

1. Select the **3.3 State map** on the dashboard.
2. Open the item's drop-down menu or its small filter icon and choose **Use as Filter**.
3. Try selecting a state. It should filter the connected **3.1, 3.2, 3.4, and 3.5** views; the **3.3 map itself** should remain usable so you can select another state.
4. Clear the selection and confirm that the other views return to the full set. If necessary, inspect the dashboard filter action and its target-sheet behavior.

![4.9 — the state-map item menu: Use as Filter.](screenshots/Screenshot%202026-10-22%20154707.png)

### 4.10 — Tell the user how to interact

Edit the **3.3 map title** to make its action obvious. For example:

> **Number of Cases and Deaths — Select a state to see the details**

A user should be able to discover the interaction without your standing beside them. Use **select** rather than assuming the user has a mouse.

![4.10 — edit the state-map title and add a short instruction.](screenshots/Screenshot%202026-10-22%20154653.png)

### 4.11 — Create useful **dynamic** titles

Edit the titles of the **county comparison (3.2)** and **county map (3.4)** so the selected state is reflected in the title. Open each sheet's title editor and use **Insert → State Name** (or the available field/filter token). **Do not type a literal fixed state name**.

You may choose your own clear wording for **3.1 and 3.2** titles and for the overall dashboard. The screenshots show a title-editing technique, not an exact sentence you must copy. Test after selecting a state, then clear it and verify the title matches what is displayed.

![4.11 — title editor: use the Insert menu to select State Name.](screenshots/Screenshot%202026-10-22%20154735.png)

![4.11 — dynamic title example using the State Name token.](screenshots/Screenshot%202026-10-22%20154750.png)

### 4.12 — Hide the default title for 3.5

When the totals are already explained by the dashboard layout, open the **3.5** item menu and choose **Hide Title**. This removes a redundant worksheet label; it **does not remove the table**.

![4.12 — hiding the 3.5 worksheet title.](screenshots/Screenshot%202026-10-22%20154333.png)

### 4.13 — Add a meaningful dashboard title

Turn on **Show dashboard title** and edit the title to describe the actual content, for example **COVID Cases and Deaths in the USA**. You can format key words but keep the text simple and readable. Do not use only “Dashboard 1” or “Lab 10” as your displayed title.

![4.13 — editing the overall dashboard title.](screenshots/Screenshot%202026-10-22%20154942.png)

### 4.14 — Improve the arrangement using containers and Blank

Review the **Layout** item hierarchy again. A **Horizontal container** groups objects side by side; a **Vertical container** stacks objects. Resize the containers to make map selection and labels comfortable. Use **Blank** as a spacer when needed. Check that Floating objects and Tiled legends do not cover other content when you resize the browser window.

### 4.15 — Design the **Phone** layout

Choose **Phone** in the device-layout panel. Rearrange the most useful information for a narrow screen: for example, move the **totals to the top**, followed by the state map and key charts. You can **remove less essential items from the Phone layout** (such as the decorative COVID image) without deleting them from the Default dashboard. Verify that the titles and state selection still make sense on a phone.

![4.15 — instructor Phone layout: totals first, image removed from Phone layout.](screenshots/Screenshot%202026-10-22%20155140.png)

### 4.16 — Hide worksheet tabs used in the dashboard

After the five sheets are placed and the dashboard works, use the worksheet tab menu to **Hide** the worksheets that are included in the dashboard. This keeps the published navigation focused on the dashboard. Do not delete the sheets. The hide option applies to worksheets already used on the dashboard; do not assume unused sheets can be hidden the same way.

![4.16 — Hide worksheet from the sheet tab after it is included in the dashboard.](screenshots/Screenshot%202026-10-22%20155215.png)

## Publish and verify

1. **Publish / Save** the completed workbook in the **`fall2026`** Tableau Online project as **`firstname_lastname_lab10`** (replace with your own name). This is the **only new published item** for Lab 10.
2. Open the published dashboard in **viewing mode**. Confirm that the **Default** view looks complete, the **state map updates the other charts**, and your titles and legends are readable.
3. Open the **Phone** layout (or use the Tableau mobile app on your phone if you want). Installing the Tableau app is **optional**; it is not a separate submission requirement.
4. Keep the workbook linked to your **existing Week 9 COVID Data Source**. **Do not publish an additional Data Source** and **do not upload a file to Canvas**. The published workbook is the submission. Follow the deadline and late policy shown in Canvas/the syllabus.

![Final example — published dashboard in viewing mode with the source map, detail views, titles and totals.](screenshots/Screenshot%202026-10-22%20155354.png)

## Grading Rubric — 100 points

| Criterion | Full-credit evidence | Points |
| --- | --- | ---: |
| **Five worksheets (3.1–3.5)** | All four required charts and the totals table are complete, correctly configured, and readable, including the two dual-axis maps. | **50** |
| **Dashboard layout and design** | Clear layout and visual hierarchy; effective use of containers, Floating/Tiled legends, labels, color, required COVID image, and text/spacing. State-map filtering and dynamic titles work correctly. The dashboard is easy to understand at first glance. | **40** |
| **Phone layout and publication** | Phone layout prioritizes important content; the correctly named `firstname_lastname_lab10` workbook is published and checked in viewing mode using the existing Week 9 Data Source. | **10** |
| **TOTAL** |  | **100** |

The three categories are graded as a whole. Partial credit may be given within each category, without a separate point breakdown for individual steps.

## Checklist before you finish

- [ ] I downloaded and used one COVID-related image with appropriate permission/credit.
- [ ] My five worksheets **3.1–3.5** match the required charts/table; **3.2 uses only County Name on Rows**.
- [ ] The state and county maps use the two-layer Dual Axis technique, with the county map created from a copy of the state map.
- [ ] My Default dashboard uses **Automatic** and contains the four charts plus totals.
- [ ] 3.3 selects a state; the other views respond; clearing the selection restores them.
- [ ] The titles, legends, colors, image credit, Text, and spacing make sense.
- [ ] I reviewed the Phone layout and published **one new workbook**, not a new Data Source.
