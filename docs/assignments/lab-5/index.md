---
layout: default
title: "Lab 5: Get Started with Tableau Online - IA 342"
---
# Lab 5 — Get Started with Tableau Online

**IA342 · Dr. Wei · Week 5: September 21–25, 2026**

Build **three worksheets and one interactive dashboard** with the course Diamonds dataset, then publish both your data source and workbook in the shared **`fall2026`** Tableau project. **There is no Canvas submission for this lab.**

Tableau now calls the hosted service **Tableau Cloud**. In this course, “Tableau Online” means the JMU Tableau site that Dr. Wei invites you to use—not Tableau Public.

## What you will learn

You will upload a CSV as a published data source, correct a field role, build two bar charts and one scatter plot, combine the three views in a dashboard, add an interactive filter, and publish work that Dr. Wei can open directly in Tableau.

---

## Part 1 — Monday: Activate Your Tableau Account and Set Up MFA

We will do the account setup together in class.

1. Open the Tableau invitation sent to your **JMU email address** and click **Sign In**.
2. If Tableau asks you to create an account, use your **James Madison University email address** so the account matches the invitation. If you already have a Tableau account under that JMU email, sign in to it.
3. When Tableau asks you to **Register a Verification Method**, choose **One-Time Password Generator** at the bottom of the list. **Do not choose the other verification methods for this course setup.**
4. On the next screen, Tableau will show a QR code. Open your authenticator app, scan the QR code shown on **your own screen**, and enter the generated verification code. Dr. Wei recommends **Okta Verify**, which JMU already uses.
5. Keep your QR setup code and verification codes private. Do not send or post them.
6. After setup, confirm that you can sign in to the JMU Tableau site.

If the invitation is missing, check junk/spam and ask Dr. Wei to confirm the invited address. Do not create a second Tableau account with a different email just to get around an access problem.

---

## Part 2 — Wednesday: Work Only in the `fall2026` Project

After signing in, choose **Explore** and open the course project **`fall2026`**. In Tableau terminology this is a *project*; for this lab, think of it as the shared course folder.

![Open Explore and enter the fall2026 course project](../../assets/week-5/screenshots/Screenshot%202026-09-18%20103626.png)

**Important:** Create this lab’s data source and workbook **inside `fall2026`**. Do **not** use Personal Space and do not create this lab in another project.

---

## Part 3 — Publish the Diamonds Data Source

Download the course [diamonds.csv](https://github.com/xbwei/data-analysis-with-generative-ai/blob/main/diamonds.csv). The file has **308 records** and six fields: `IDNO`, `WEIGHT`, `COLOR`, `CLARITY`, `RATER`, and `PRICE`.

### 3.1 Start a published data source

Inside `fall2026`, choose **New → Published Data Source**.

![Choose New and Published Data Source inside fall2026](../../assets/week-5/screenshots/Screenshot%202026-09-18%20103639.png)

Choose **Files → Upload from computer**, then select `diamonds.csv`.

![Upload the diamonds CSV from your computer](../../assets/week-5/screenshots/Screenshot%202026-09-18%20103757.png)

### 3.2 Make `IDNO` a dimension

Tableau may initially place `IDNO` under **Measures** because it contains numbers. It is actually an identifier, not a quantity to add together.

**Drag `IDNO` from Measures up into Dimensions.**

![Move IDNO from Measures to Dimensions](../../assets/week-5/screenshots/Screenshot%202026-09-18%20103832.png)

This is important because later we will use `IDNO` to control the **level of detail** in the scatter plot.

### 3.3 Publish the data source to `fall2026`

Use **Publish As** and name the data source exactly:

```text
firstname_lastname_lab5
```

Use this **same exact name** later for your workbook. Make sure the selected project is **`fall2026`**.

![Publish the data source into the fall2026 project](../../assets/week-5/screenshots/Screenshot%202026-09-18%20103901.png)

Return to `fall2026`. You should now see the published data source. Open its menu and choose **New Workbook**.

![Create a new workbook from your published data source](../../assets/week-5/screenshots/Screenshot%202026-09-18%20103926.png)

---

## Part 4 — Worksheet 1: Number of Diamond Records by Rater

Create the first worksheet.

1. Put `RATER` on **Rows**.
2. Put `IDNO` on **Columns**.
3. Open the `IDNO` pill menu and choose **Measure → Count**. You want **CNT(IDNO)**, not `SUM(IDNO)`.
4. Use a horizontal bar chart.
5. Give the chart a clear title such as **Number of diamond records**.

![Change IDNO to Count](../../assets/week-5/screenshots/Screenshot%202026-09-18%20104036.png)

Your unfiltered chart should show:

| RATER | Record count |
|---|---:|
| GIA | 151 |
| HRD | 79 |
| IGI | 78 |
| **Total** | **308** |

![Completed Records by Rater worksheet](../../assets/week-5/screenshots/Screenshot%202026-09-18%20104122.png)

A longer bar means more records from that rater **in this dataset**. It does not by itself say anything about quality or overall market share.

---

## Part 5 — Worksheet 2: Average Price by Clarity

Create a second worksheet.

1. Put `CLARITY` on **Rows**.
2. Put `PRICE` on **Columns**.
3. Change the aggregation from **Sum** to **Average** so the pill reads **AVG(PRICE)**.

![Change Price from Sum to Average](../../assets/week-5/screenshots/Screenshot%202026-09-18%20104148.png)

4. **Sort the bars from highest to lowest average price.** Do not leave them in the default category order.
5. Keep a zero baseline and make the title clear that the chart shows an average.

![Sort Average Price by Clarity from highest to lowest](../../assets/week-5/screenshots/Screenshot%202026-09-18%20104220.png)

After sorting, **IF has the lowest average price in this sample**. That gives us the question for the dashboard:

**Why are IF diamonds cheaper on average in this dataset?**

Do not assume clarity alone causes the difference. The dashboard will let us inspect the records behind that average.

---

## Part 6 — Worksheet 3: Price versus Weight at the Record Level

Create a third worksheet.

1. Put `WEIGHT` on **Columns** and `PRICE` on **Rows**.
2. Put `IDNO` on **Detail** on the Marks card.
3. Put `COLOR` on **Color**.
4. Use circle marks and keep a readable color legend.
5. Give the chart a clear title such as **Price vs Weight**.

![Record-level scatter plot with IDNO on Detail and COLOR on Color](../../assets/week-5/screenshots/Screenshot%202026-09-18%20104335.png)

### The important idea: level of detail

Once `IDNO` is on **Detail**, each mark represents one diamond record. In this dataset each `IDNO` identifies one row, so `SUM(PRICE)` and `AVG(PRICE)` give the same position for that one-record mark. The same is true for `WEIGHT`.

**For this worksheet, the important choice is not SUM versus AVG. The important choice is whether the view is at the individual-record level.**

Without `IDNO` on Detail, Tableau can collapse many rows into only a few aggregated marks. With `IDNO` on Detail, the view should represent all **308 records** before filtering.

### Optional practice — What Does One Mark Represent?

Use this activity only if you want to compare one overall average, group averages, and record-level marks. It is **not another graded deliverable**.

<div style="width: 100%; max-width: 980px; margin: 1.5rem auto; border: 1px solid #d0d7de; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
  <iframe id="scatter-agg-iframe" src="../../assets/week-5/scatter-aggregation.html" title="What does one mark represent?" loading="lazy" onload="resizeLabIframe(this)" style="width: 100%; min-height: 520px; border: 0; display: block;" sandbox="allow-scripts allow-same-origin"></iframe>
</div>
<script>
function resizeLabIframe(ifr) {
  if (!ifr) return;
  try {
    if (ifr.contentDocument && ifr.contentDocument.body) {
      var h = Math.max(
        ifr.contentDocument.body.scrollHeight || 0,
        ifr.contentDocument.documentElement.scrollHeight || 0
      );
      if (h > 50) ifr.style.height = (h + 4) + 'px';
    }
  } catch (e) {}
  try {
    if (ifr.contentWindow) {
      ifr.contentWindow.postMessage({ type: 'ia342-request-height' }, '*');
    }
  } catch (e) {}
}
window.addEventListener('message', function(e) {
  if (e.data && e.data.type === 'ia342-frame-height' && typeof e.data.height === 'number') {
    var ifr = document.getElementById('scatter-agg-iframe');
    if (ifr) ifr.style.height = (e.data.height + 4) + 'px';
  }
});
</script>

[Open the aggregation practice by itself](../../assets/week-5/scatter-aggregation.html).

---

## Part 7 — Build the Interactive Dashboard

Create one dashboard named **Diamonds Overview** and place all three worksheets on it:

- **Records by Rater**
- **Average Price by Clarity**
- **Price vs Weight**

Keep the scatter plot large enough to inspect individual records. Keep the bar-chart labels and color legend readable.

Make **Average Price by Clarity** interactive by turning it into a dashboard filter. Select **IF** and confirm that the other two views update.

![Dashboard with IF selected as an interactive filter](../../assets/week-5/screenshots/Screenshot%202026-09-18%20104439.png)

Use the filtered dashboard to investigate the question from Worksheet 2:

- What weights do the IF records have?
- How are those IF records distributed across raters?
- What changes when you compare IF with the other clarity groups?

The purpose is to investigate **why IF has a low average price in this sample**, not to claim that one variable alone causes the price difference.

Clear the selection when you finish so the published dashboard opens with all records shown.

---

## Part 8 — Publish the Workbook

Use **Publish** or **Publish As** and save the workbook in **`fall2026`**. Name the workbook exactly the same as the data source:

```text
firstname_lastname_lab5
```

![Publish the workbook to fall2026, not Personal Space](../../assets/week-5/screenshots/Screenshot%202026-09-18%20104513.png)

Return to `fall2026` and confirm that you can see **both** your workbook and your data source.

![Final fall2026 project showing both the workbook and data source](../../assets/week-5/screenshots/Screenshot%202026-09-18%20104546.png)

Reopen the workbook and verify:

- all three worksheets are present;
- the dashboard is present;
- the IF filter works and can be cleared;
- the workbook opens with the intended Diamonds data source;
- your work is in `fall2026`, not Personal Space.

---

## Submission and Late Policy

There is **nothing to submit on Canvas**. Dr. Wei will grade the published workbook directly in Tableau.

### Submission time

**Your submission time is the workbook’s Last Modified time in Tableau Online.**

- **At or before the deadline:** on time.
- **After the deadline:** late; the syllabus late-work penalty applies.

The **workbook** timestamp is the one used for the lateness decision. The data-source timestamp is not a second submission clock.

The final `fall2026` view shows where that **Modified** timestamp appears.

### After grading

After grading, Dr. Wei may move completed work into a **Lab 5** subfolder. If your workbook/data source has been moved there, that means it has been processed; do not move it back unless asked.

### Shared-project etiquette

`fall2026` is a shared course project, so you may be able to see other students’ work.

- Do **not** copy another student’s workbook or use it as your own submission.
- Do **not** delete, rename, move, overwrite, or otherwise alter another student’s workbook or data source.
- Work only on your own items.

Shared-project activity is not anonymous. Course and platform records can be reviewed if there is a question about copying, deletion, or other changes.

---

## Grading Rubric — 100 Points

There is **nothing to submit on Canvas**. Dr. Wei will grade the published Tableau work directly in `fall2026`.

<div style="overflow-x: auto; margin: 1.5rem 0 2rem;">
  <table style="width: 100%; border-collapse: collapse; font-size: 0.95rem; line-height: 1.5; border: 1px solid #d0d7de; border-radius: 6px;">
    <thead>
      <tr style="background-color: #f6f8fa; border-bottom: 2px solid #d0d7de;">
        <th style="padding: 0.75rem 1rem; text-align: left; width: 25%; font-weight: 600; color: #1f2328;">Criterion</th>
        <th style="padding: 0.75rem 1rem; text-align: left; width: 63%; font-weight: 600; color: #1f2328;">Full-credit requirements</th>
        <th style="padding: 0.75rem 1rem; text-align: right; width: 12%; font-weight: 600; color: #1f2328;">Points</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border-bottom: 1px solid #d0d7de;">
        <td style="padding: 0.75rem 1rem; font-weight: 600; color: #1f2328; vertical-align: top;">Data Source</td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">A published Diamonds data source named <code>firstname_lastname_lab5</code> is available in <code>fall2026</code>, opens correctly, and has <code>IDNO</code> treated as a <strong>Dimension</strong>.</td>
        <td style="padding: 0.75rem 1rem; text-align: right; font-weight: 600; color: #1f2328; vertical-align: top;">20</td>
      </tr>
      <tr style="border-bottom: 1px solid #d0d7de; background-color: #fafbfc;">
        <td style="padding: 0.75rem 1rem; font-weight: 600; color: #1f2328; vertical-align: top;">Worksheet 1 &mdash; Records by Rater</td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">Correctly uses <code>RATER</code> and <code>CNT(IDNO)</code> and clearly shows the number of records by rater.</td>
        <td style="padding: 0.75rem 1rem; text-align: right; font-weight: 600; color: #1f2328; vertical-align: top;">20</td>
      </tr>
      <tr style="border-bottom: 1px solid #d0d7de;">
        <td style="padding: 0.75rem 1rem; font-weight: 600; color: #1f2328; vertical-align: top;">Worksheet 2 &mdash; Average Price by Clarity</td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">Correctly uses <code>AVG(PRICE)</code> by <code>CLARITY</code> and is sorted from highest to lowest average price.</td>
        <td style="padding: 0.75rem 1rem; text-align: right; font-weight: 600; color: #1f2328; vertical-align: top;">20</td>
      </tr>
      <tr style="border-bottom: 1px solid #d0d7de; background-color: #fafbfc;">
        <td style="padding: 0.75rem 1rem; font-weight: 600; color: #1f2328; vertical-align: top;">Worksheet 3 &mdash; Price vs Weight</td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">Uses <code>WEIGHT</code> and <code>PRICE</code>, with <code>IDNO</code> on <strong>Detail</strong> for record-level marks and <code>COLOR</code> on <strong>Color</strong>.</td>
        <td style="padding: 0.75rem 1rem; text-align: right; font-weight: 600; color: #1f2328; vertical-align: top;">20</td>
      </tr>
      <tr style="border-bottom: 2px solid #d0d7de;">
        <td style="padding: 0.75rem 1rem; font-weight: 600; color: #1f2328; vertical-align: top;">Interactive Dashboard</td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;"><strong>Diamonds Overview</strong> contains all three required worksheets in a readable layout. <strong>Average Price by Clarity</strong> filters the other views, the filter can be cleared, and the published dashboard opens with all records shown.</td>
        <td style="padding: 0.75rem 1rem; text-align: right; font-weight: 600; color: #1f2328; vertical-align: top;">20</td>
      </tr>
    </tbody>
    <tfoot>
      <tr style="background-color: #f6f8fa; font-weight: bold;">
        <td colspan="2" style="padding: 0.75rem 1rem; text-align: right; color: #1f2328;">Total:</td>
        <td style="padding: 0.75rem 1rem; text-align: right; color: inherit; font-size: 1.05rem;">100</td>
      </tr>
    </tfoot>
  </table>
</div>

---
[Return to Course Home](../../) | [Return to Module 5](../../modules/module-5/)
