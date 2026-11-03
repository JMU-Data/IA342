---
layout: default
title: "Syllabus - IA 342"
---

# Syllabus - Fall 2026

**Last updated: November 3, 2026**  
*Revision: The Final Project working plan now uses assigned-state Gun Violence Archive incidents, Census ACS enrichment in Colab with optional Gemini assistance, Tableau Public dashboards, and a narrated Google Slides briefing with a Google Flow AI video. Detailed rubric and final instructions will follow; grading weights and established course policies are unchanged.*

**Course:** IA 342: Visualization Methods, Technologies, and Tools for Intelligence Analysis  
**Term:** Fall 2026  
**Instructor:** Dr. Xuebin Wei  
**Email:** [weixx@jmu.edu](mailto:weixx@jmu.edu)  
**Profile:** [Official JMU Faculty Profile](https://www.jmu.edu/cise/people/faculty/wei-xuebin.shtml)  
**Office Hours:** Monday and Wednesday, 9:30–11:00 AM

## Course Description

IA 342 focuses on Data Visualization, Business Intelligence, Visual Analytics, and Data Storytelling. While AI can analyze data for us, **humans still make decisions**; visualization supports human perception, judgment, communication, and accountability. Throughout this course, we will use industry-standard tools (ArcGIS, Tableau) to transform raw data into interactive dashboards and clear, evidence-based visual communications.

## Learning Goals

- **Perceive patterns and insights** through exploratory data visualization.
- **Design interactive visual analytics dashboards** that support human judgment.
- **Master industry-standard Business Intelligence platforms** such as Tableau and ArcGIS.
- **Communicate evidence-based data stories** to diverse stakeholders.
- **Maintain accountability and interpretability** in data-driven analytical workflows.

## Required Accounts & Resources

- **Textbook:** Wei, Xuebin, and Xinyue Ye. *Social Data Analytics in the Cloud with AI*. CRC Press / Routledge, 2024.  
  **Access:** [Official Textbook URL](https://www.taylorfrancis.com/books/mono/10.1201/9781003437611/social-data-analytics-cloud-ai-xuebin-wei-xinyue-ye) *(Freely accessible via JMU Wi-Fi or by logging in with a JMU account.)*
- **Google Account (Required):** Students must use the **Google account registered with their JMU email address** (`@dukes.jmu.edu` or `@jmu.edu`) that the instructor enrolled in the **shared 5,000 Google Skills credit pool**. Do not use a different, unenrolled personal Gmail account for the Google Skills assignment; check access to the course program and credits before starting.
- **ArcGIS & Tableau (Required):** Provided through JMU institutional licensing and SSO.
- **AI Tools:** Use only AI tools and features explicitly authorized for the relevant course activity. Google AI Pro is optional. See [AI Policy](#ai-policy).

## Email Communication Policy

- **Primary Method:** Emailing the instructor from your **JMU student account** is the primary method of communication.
- **Response Time:** The instructor typically responds within **1–2 business days**. Emails received after 5:00 PM will be treated as received on the next business day. The instructor does not normally respond to emails on weekends or JMU holidays.
- **Canvas Messages:** Canvas is strictly used for grades, course announcements, and logistics. **DO NOT** use the Canvas messaging system to contact the instructor; it is not regularly monitored and messages may be missed.

## AI Policy

**Updated October 7, 2026.** To ensure fairness, students may use **only AI tools and features explicitly authorized for each course activity**. **You are responsible for what you create with AI**, including the accuracy of your data, calculations, visualizations, and interpretations. Disclose any authorized AI use and do not share sensitive or private information with AI tools.

## Grading Breakdown

- **Attendance:** 20%
- **Labs:** 40%
- **Mini Project:** 10%
- **Google AI Skills:** 10% ([Google Skills Hands-on Lab Assignment](../assignments/google-skills/): this is a **100-point Canvas assignment**. One distinct passed hands-on Lab = **30/100 points**; two = **60/100**; three or more = **100/100**. Only activities with **Type: Lab** and **Passed** status count. Students must use the JMU-email-registered Google account enrolled in the instructor's **shared 5,000-credit pool**. The Lab completions and single screenshot upload must both be completed **by the due date and time shown in Canvas**; late work is not accepted.)
- **Final Project:** 20%

## Final Project — Proposed Format (Weeks 15–17)

**Working plan:** Investigate Gun Violence Archive (GVA) incidents in your **individually assigned U.S. state**, enrich the dataset with U.S. Census population and median household income, produce a professional **Tableau Public dashboard**, and communicate evidence-based findings in a **narrated Google Slides presentation lasting no more than five minutes**. The two workshop weeks provide four class meetings; a separate final-project assignment will provide the detailed rubric and deadline.

1. **GVA data acquisition and scope:** Use the [Gun Violence Archive query](https://www.gunviolencearchive.org/query) to download records for your assigned state and a clearly defined analysis period; preserve the raw CSV in your own Google Drive. Record download date, query filters, record counts, temporal coverage, and any export limits. If an export is capped, split the request into smaller date windows when practical and check duplicate Incident IDs. **Incomplete coverage is acceptable if documented; do not present a truncated extract as complete statewide data.**
2. **Census enrichment in Colab:** Use Google Colab and an authorized AI assistant (such as Gemini) to help retrieve **population** and **median household income** from the [Census ACS API](https://www.census.gov/data/developers/data-sets/acs-5year.html). Keep any Census API key in **Colab Secrets**; never embed it in code, shared output, or Tableau. Match to verified state/county or county-equivalent geography and distinguish Virginia-style independent cities from similarly named counties. Document unresolved or ambiguous locations. Record the **actual ACS estimate year and five-year period** separately from each incident's year—for example, 2025–2026 incidents may use the available **2020–2024 ACS estimates**, but must not be mislabeled as 2025 or 2026 Census estimates. Preserve the original incidents and save a separate cleaned/enriched CSV.
3. **Tableau Public analytics and verification:** Publish an approved, appropriately aggregated **Tableau Public Data Source** and develop a Workbook with informative charts, calculations, and a **clear interactive Dashboard**, including meaningful filters and actions. Verify incident totals with distinct Incident IDs, appropriate population-based comparisons, and the five-second design test. **Do not sum repeated population values across incident rows or infer rates from incomplete incident coverage without a clear limitation.** Cite GVA and Census, and follow all data-use and privacy requirements before publishing. **A Tableau Prep Flow is not required** for this project.
4. **AI-assisted analytical presentation:** Use **Google Flow** to create a short, non-graphic AI-generated video appropriate for a public-safety analysis. Integrate selected Tableau visuals, analytical findings, limitations, **voice-over**, an **AI avatar/presenter**, and the video (embedded or linked) into **Google Slides**. The entire narrated presentation, including the AI video, must be **five minutes or less**. Identify AI-generated scenes; do not represent them as footage of real incidents.

**Final deliverable:** Submit **one viewable Google Slides presentation link** through the final-project assignment, with links to the published **Tableau Public dashboard/Workbook and Data Source** for instructor inspection. Keep the Colab workflow and original/enriched data available for verification under the instructor's submission instructions; do not publicly expose raw sensitive data or API credentials. A separate Tableau Story, Tableau Prep Flow, or live classroom presentation is **not required**.

## Letter-Grade Scale

| Grade | Range | Grade | Range | Grade | Range | Grade | Range |
| :---: | :--- | :---: | :--- | :---: | :--- | :---: | :--- |
| **A** | 94 – 100% | **A-** | 90 – 93.99% | **B+** | 87 – 89.99% | **B** | 84 – 86.99% |
| **B-** | 80 – 83.99% | **C+** | 77 – 79.99% | **C** | 74 – 76.99% | **C-** | 70 – 73.99% |
| **D+** | 67 – 69.99% | **D** | 64 – 66.99% | **D-** | 61 – 63.99% | **F** | < 61% |

## Resubmission / Late Work / Project Policy

- **Before Deadline:** You may submit or revise your work multiple times before the deadline without a late penalty. The latest on-time version is used unless you choose to have a permitted later revision evaluated.
- **Late Penalty:** Late submissions incur a **10% penalty per day**, capped at a maximum 40% penalty, unless prior approval is obtained from the instructor.
- **Final Exam Week:** **No late submissions** are accepted during final exam week.
- **Projects:** Late submissions/resubmissions of the class projects will not be accepted.

## Automated Checks, Feedback, and Submission Timing

*Updated October 8, 2026.*

**Deterministic checks and instructor grading.** The instructor uses Python scripts for deterministic assignment checks, not generative AI to grade or modify student work. These scripts may post automatic comments that flag items for the instructor's manual review. Automated comments are not final grading decisions. The instructor determines grades and provides grading comments explaining point deductions.

**Feedback does not require a revision.** Automatic check comments and instructor grading comments explain the review results; they do not mean you must revise and resubmit your work.

**Late revisions, including after grading.** For labs and other assignments that permit late work, you may submit a revision after the deadline, including after a grade has been posted. If you want that revised version evaluated, the syllabus late penalty (**10% per day, up to 40%**) applies. A higher unpenalized score does not guarantee a higher final score after the penalty; resubmission is your choice. **Projects and final-exam-week submissions remain subject to their separate no-late/no-resubmission restrictions.**

**Effective submission time.** For the version of an assignment being graded, the official submission time is the **later of the Canvas submission timestamp and the latest modification timestamp of any required external work used in that version** (for example, GitHub files or Tableau Flows, Data Sources, and Workbooks). A GitHub or Tableau change made after the deadline is a **late revision if the updated work is used for grading**, even when the Canvas submission was on time. Do not overwrite on-time work after the deadline if you want the original version evaluated; an earlier Canvas timestamp does not make later edits on time.

## Technical Assignment Support

Technical assignments may require troubleshooting. Start assignments early and allow sufficient time to resolve technical issues. Requests for assistance made shortly before a deadline may not receive a response before the deadline and do not automatically excuse late submissions.

## Attendance / Excused Absence

Regular attendance is critical, as a significant portion of the learning happens in class through hands-on practice, critique, and discussion. 

- **Registered Section Attendance:** Students must attend the course section in which they are officially registered unless the instructor approves an exception in advance.
- **Unexcused Absences & Loss of Credit:** Absence, leaving early without permission, being late more than 20 minutes, or disrespectful/disturbing behavior results in **0 attendance points** for that meeting. Being late more than 5 minutes receives a late penalty.
- **Excused Absences:** Excused absences are strictly limited to: sickness/health issues; mandatory activities with written documentation; or other situations with instructor approval.

## Academic Integrity / Honor Code

All students are expected to abide by the JMU Honor Code. Plagiarism, including presenting unverified AI-generated content as your own original analysis without disclosure or responsibility, is a violation of the Honor Code. Please consult the [JMU Honor Code website](https://www.jmu.edu/honorcode/) for more details.

## Accessibility / Student Support

JMU is committed to creating a welcoming and accessible environment. If you have a documented disability and require accommodations, please register with the Office of Disability Services (ODS) and contact the instructor early in the semester to discuss your needs.

JMU offers numerous resources for student support, including the Science and Math Learning Center, the University Writing Center, and Counseling Center services. If you are facing academic or personal challenges, please utilize these resources or contact the instructor.

## Inclement Weather

In the event of inclement weather or university closures, we will follow the official JMU delays and cancellations policy. Please monitor your JMU student email and Canvas announcements for updates regarding makeup classes or adjusted assignment deadlines.

## Course Schedule (Fall 2026)

*Schedule updated: November 3, 2026 (Final Project, Weeks 15–17)*

Weeks 9–11 follow a consistent pattern: **Monday combines a focused explanation with a guided in-class exercise; Wednesday is an independent lab with instructor support.** Week 8 is one extended lab with no separate lecture. In this course, Tableau Online refers to the course Tableau Cloud site. Tableau Flow means a Tableau Prep data-preparation flow; Google Flow in Week 13 is the separate video-generation tool.

| Week / Dates | Lecture / Topic Focus | Hands-on Lab & Activities | Notes & Milestones |
| :--- | :--- | :--- | :--- |
| **Week 1**<br>Aug 24 – 28 | **Course Introduction & Cloud/AI Setup**<br>Why visualization matters; course workflow, expectations, and AI policy | Account verification; Tableau & ArcGIS institutional access; Google Cloud & AI environment setup | *Classes begin Wed, Aug 26*<br>*(Status: Completed)* |
| **Week 2**<br>Aug 31 – Sep 4 | **Introduction to Data Visualization**<br>Data → Information → Decision; Anscombe’s Quartet; visual perception, preattentive attributes & Gestalt principles; Heuer intelligence perception framing | **ArcGIS Business Analyst: Data & Reports → PDF**<br>Define study areas (rings/drive times), run standard reports, import/geocode CSV, setup custom variables & categories, build custom reports, and export PDF | Site selection, custom data & PDF reports |
| **Week 3**<br>Sep 7 – 11 | **Map Design & Spatial Intelligence**<br>Spatial intelligence framing for analysis; lat/long & coordinate fundamentals; classification (equal interval, quantile, natural breaks, std dev); choropleth & proportional symbol maps | **ArcGIS Business Analyst: Maps + Infographic + StoryMap → URL**<br>Color-coded thematic maps & classification, Smart Map Search & POI search, run infographics, build StoryMap combining maps, infographics & narrative, and publish URL | Thematic mapping, infographics & StoryMap (URL) |
| **Week 4**<br>Sep 14 – 18 | **Color Theory for Data Visualization**<br>Hue, saturation, value; sequential, diverging, categorical & alerting palettes; color vision deficiency & accessibility | **ArcGIS Business Analyst: Spatial Analysis + Dashboard → URL**<br>Suitability analysis (core), benchmark comparison / nearby analysis, export analysis layers, build interactive dashboard (map, indicators, charts), and publish URL | Spatial analysis & interactive dashboard (URL) |
| **Week 5**<br>Sep 21 – 25 | **Choosing and Critiquing Graphs**<br>Chart-selection principles; histograms, box plots, scatter/line/bar charts, axes/scales; identifying misleading visualizations | **Get Started with Tableau**<br>Data connection, basic sheets (bar, scatter), simple dashboard construction, and publishing workflow | Visual critique & core Tableau workflow |
| **Week 6**<br>Sep 28 – Oct 2 | **Data Preparation for Visual Analytics**<br>ETL pipelines, data quality, OLTP vs. OLAP, dimensions vs. measures, live vs. extract connections | **Tableau Prep / Tableau Flow**<br>Clean, transform, null handling, standardizing values, calculated fields, split, union, join, and outputting clean data | Data cleaning & preparation pipelines |
| **Week 7**<br>Oct 5 – 9 | **MINI PROJECT: ArcGIS Spatial Visualization**<br>Project kickoff, clinic, and instructor support *(No new lecture)* | **Mini Project Clinic & Studio**<br>[IA342 Mini Project](../assignments/mini-project/): Explore a randomly assigned U.S. state in ArcGIS Business Analyst & ArcGIS Dashboards with a thematic map, one analysis-result map (Benchmark, Suitability, or Nearby), interactive widget, and concise write-up | *Fall Break begins Wed, Oct 7*<br>*(Mon session: Project Clinic)*<br>**Mini Project Due** (Tue, Oct 6) → Public Dashboard URL |
| **Week 8**<br>Oct 12 – 16 | **Extended Lab: Tableau Relationships and Ticket Sales Analysis**<br>[Week 8 Lab Instructions](../assignments/lab-8/)<br>No separate lecture; table grain, relationships, and calculated fields | **One lab across both meetings**<br>• Mon: Connect PostgreSQL directly to a published Data Source; define six logical tables and five Relationships, check cardinality and totals, create calculations, and publish with a Live connection<br>• Wed: Short demonstration and hands-on visualization practice; create five chart worksheets and a dashboard in a Workbook, then export results to PDF | **Database access: Oct 12–16 only; instance stops after the Friday deadline.**<br>Publish **Data Source + Workbook** in `fall2026` and submit **one PDF** to Canvas by Fri, Oct 16, 11:59 p.m. Eastern Time.<br>Complete the work in class where possible. After shutdown, unfinished work requires preparing the original TICKIT files as separate tables and rebuilding the Relationships Data Source. Normal late penalties apply.<br><small>Instructor setup reference: <a href="https://github.com/JMU-Data/IA342/blob/main/maintainer-notes/tickit-cloudsql-pgadmin-runbook.md">TICKIT Cloud SQL / pgAdmin runbook</a>.</small> |
| **Week 9**<br>Oct 19 – 23 | **Visual Analytics in Tableau**<br>Drill-down, sort, group, sets, filters, trend/reference lines, parameters, and interactive exploration | **Mon: Explanation + guided in-class exercise**<br>**Wed: Independent Visual Analytics lab**<br>Parameters, sets, set actions, tooltips, interactive scatter plots, and mapping | Meaningful interaction and evidence-based exploration |
| **Week 10**<br>Oct 26 – 30 | **Dashboard Design**<br>Directed vs. exploratory discovery, KPIs, visual hierarchy, layout containers, eye-scanning, 5-second test, Shaffer 4Cs, Tufte/KISS principles | **Mon: Explanation + guided in-class exercise**<br>**Wed: Independent Dashboard Design lab**<br>Coordinated views, layout, interactivity, dynamic titles, device layouts, and publishing | Usability, visual hierarchy, and consistent filter behavior |
| **Week 11**<br>Nov 2 – 6 | **Calculations in Tableau**<br>Basic calculations, date/string/logical functions, aggregate calculations, table calculations (scope/direction), LOD expressions (FIXED, INCLUDE, EXCLUDE) | **Mon: Explanation + guided in-class exercise**<br>**Wed: Independent Calculations lab**<br>Calculated metrics, rates, moving averages, table calculations, and LOD; verify aggregation and denominators | Calculations must be used and interpreted in the visualizations |
| **Week 12**<br>Nov 9 – 13 | **FBI NIBRS Dashboards: Tableau Public and Gemini Canvas**<br>Traditional BI vs. AI-generated visualization; verification of data, joins, maps, and analytical claims | **Mon: Tableau Public (Virginia 2025 NIBRS)**<br>Download the two instructor-provided public CSVs (county/month/offense summary and offense-type lookup), store them in Google Drive, connect from Drive, relate the data using `offense_code`, and publish a small interactive Tableau Public dashboard.<br>**Wed: Gemini Canvas**<br>Use the **same two CSVs** to generate a lightweight dashboard that supports **in-browser CSV uploads and automatic chart updates**. Verify that it parses the actual files and joins on `offense_code` (without inventing data); compare its totals, time trends, categories, and geographic interpretation against Tableau. Export a standalone HTML dashboard and publish it through GitHub / GitHub Pages with a short AI validation summary. | **Learning objective:** Judge AI-generated visualizations against the source data and independently checked BI results; do not assume either tool is automatically correct.<br>Required Wednesday submission: working standalone static HTML/GitHub link (including CSV upload and data refresh) and concise validation summary; no embedded API keys, fabricated data, or Gemini API calls. After submitting, **Add Gemini Features** may be explored inside Gemini Canvas as an optional demonstration only—do not add them to the submitted HTML.<br>Tableau Public is for Week 12; the final project uses course Tableau Online. |
| **Week 13**<br>Nov 16 – 20 | **AI Video Visualization & Analytical Storytelling**<br>AI video as visual communication; storytelling accuracy vs. hallucination risks | **AI Video & Analytical Storytelling**<br>• Mon: Google Flow (visual/video synthesis supporting analytical findings)<br>• Wed: Google Vids (assembling analytical video briefing) | Multimodal visual communication |
| **Week 14**<br>Nov 23 – 27 | **Thanksgiving Holiday**<br>*(No Classes)* | — | University Closed |
| **Week 15**<br>Nov 30 – Dec 4 | **Final Project Workshop: GVA + Census Data Preparation**<br>Assigned-state incidents, data scope, Census geography, and transparent AI-assisted preparation *(No new lecture)* | **Mon: GVA download → Google Drive → Colab**<br>Export incidents for your assigned state; document date coverage and export limits; store the original CSV. Use Colab/Gemini and a Census API key stored in Secrets to retrieve population and median household income for verified counties/county-equivalents and relevant ACS estimate periods.<br>**Wed: Validate → Save enriched CSV → Tableau Public Data Source**<br>Resolve independent-city/county name collisions and document unmatched locations; preserve distinct Incident IDs, actual incident years, and Census vintage; save a new CSV. Prepare an appropriate public Data Source and start the Workbook. | **Milestones:** Raw and enriched datasets, inspectable Colab workflow, documented matches/unmatched locations, and Tableau Public Data Source. **No Tableau Prep Flow or student PostgreSQL setup.** Incomplete but honestly documented GVA coverage can be used. |
| **Week 16**<br>Dec 7 – 11 | **Final Project Workshop: Interactive Visual Analytics and Storytelling**<br>Tableau calculations, five-second design, filter actions, and responsible multimedia communication *(No new lecture)* | **Mon: Tableau Public Charts & Dashboard**<br>Build and verify appropriate maps, comparisons and trends, calculations, readable labels, sources, filters, and dashboard actions. Do not double-count population repeated across incident records; explain limits on incident coverage and population-based interpretation.<br>**Wed: Google Flow + Narrated Google Slides**<br>Generate a non-graphic AI video; combine selected Tableau visualizations, evidence and limitations with voice-over and an AI avatar/presenter. Link the Tableau Public Workbook and source. Keep the entire presentation within five minutes. | Workshop outcomes: Published, permission-compliant **Tableau Public Data Source + Workbook/Dashboard**, and a draft **narrated Google Slides briefing**. Instructor reviews data accuracy and interactive behavior. No Tableau Story. |
| **Week 17**<br>Dec 12 – 18 | **Final Exam Week**<br>Final-project submission only *(No live classroom presentations)* | **Final Project: Google Slides Briefing (≤ 5 minutes)**<br>Submit a viewable Slides link containing evidence-based conclusions, Tableau visualizations, voice-over, an avatar, and a non-graphic Google Flow video; include working links to the Tableau Public Dashboard/Workbook and Data Source. Keep the Colab analysis available for instructor verification according to final instructions. | **Final Project Due** at the time announced in the final-project assignment.<br>**Late submissions are not accepted.** |
