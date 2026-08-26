import os
from playwright.sync_api import sync_playwright
import markdown

css = """
* { box-sizing: border-box; }
@page {
    margin: 1in;
    size: letter;
}
body {
    font-family: 'Georgia', 'Times New Roman', serif;
    line-height: 1.6;
    color: #2b2b2b;
    margin: 0;
    padding: 0;
    font-size: 11pt;
}
.container {
    padding: 0;
}
.header {
    text-align: center;
    margin-bottom: 2em;
}
.header h1 {
    color: #1a4471;
    font-size: 24pt;
    font-family: 'Segoe UI', Arial, sans-serif;
    font-weight: 700;
    margin-bottom: 0.5em;
    border-bottom: 2px solid #1a4471;
    padding-bottom: 0.3em;
}
.header p {
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 12pt;
    line-height: 1.6;
    margin: 0;
}
h2 { 
    color: #1a4471; 
    font-family: 'Segoe UI', Arial, sans-serif;
    margin-top: 1.5em; 
    border-bottom: 1px solid #d3d3d3;
    padding-bottom: 0.3em;
    font-size: 16pt;
    font-weight: 700;
}
ul, ol { 
    margin-bottom: 1em; 
    padding-left: 2em;
}
li {
    margin-bottom: 0.5em;
}
strong {
    font-weight: 700;
}
a {
    color: #1a4471;
    text-decoration: none;
}
.phase-box {
    border: 1px solid #d0d7de;
    border-left: 4px solid #1a4471;
    padding: 1.2em;
    margin-bottom: 1.2em;
    background-color: #f6f8fa;
    border-radius: 4px;
}
.phase-box h3 {
    margin-top: 0;
    color: #1a4471;
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 12pt;
    margin-bottom: 0.5em;
}
.phase-box ul {
    margin-bottom: 0;
}
table { 
    width: 100%; 
    border-collapse: collapse; 
    margin-bottom: 1.5em; 
    font-family: 'Segoe UI', Arial, sans-serif;
}
th, td { 
    border: 1px solid #d3d3d3; 
    padding: 10px; 
    text-align: left; 
}
th { 
    color: #1a4471;
    background-color: #f9f9f9; 
    font-weight: 600;
}
"""

md_body = """
## Course Description

This course provides a comprehensive introduction to statistical computing and data analysis using **R** and **S-PLUS**. Moving beyond basic spreadsheets, we explore data processing pipelines, exploratory data analysis, and advanced statistical modeling. Students will apply modern programming techniques to practical data mining and quantitative analysis scenarios.

## Learning Goals

Upon completion of this course, students are expected to:

- Differentiate and utilize the core data structures and programming paradigms in R and S-PLUS.
- Collect, clean, and manipulate real-world datasets for statistical analysis.
- Apply robust statistical models and hypothesis testing to derive actionable insights.
- Develop professional, interpretable data visualizations and reproducible reports.
- Address ethical and security considerations in data management and analysis.

## IA342 Learning Journey

<div class="phase-box">
    <h3>PHASE 1 — Fundamentals of R & S-PLUS</h3>
    <ul>
        <li>Environment setup, syntax, and basic operations.</li>
        <li>Data structures: vectors, matrices, data frames, and lists.</li>
    </ul>
</div>

<div class="phase-box">
    <h3>PHASE 2 — Data Wrangling & Cleaning</h3>
    <ul>
        <li>Importing and exporting data from diverse sources.</li>
        <li>Data manipulation, merging, filtering, and missing value imputation.</li>
    </ul>
</div>

<div class="phase-box">
    <h3>PHASE 3 — Statistical Modeling & Visualization</h3>
    <ul>
        <li>Descriptive statistics and probability distributions.</li>
        <li>Linear models, ANOVA, and diagnostic plotting.</li>
        <li>Creating publication-ready graphics and exploratory plots.</li>
    </ul>
</div>

<div class="phase-box">
    <h3>PHASE 4 — Final Project</h3>
    <ul>
        <li>End-to-end quantitative data analysis workflow.</li>
        <li>Reproducible research reporting and final presentation.</li>
    </ul>
</div>

## Required Textbook / Resources

Venables, W. N., and Ripley, B. D. *Modern Applied Statistics with S*. 4th ed., Springer, 2002.

*(Note: Refer to Canvas for any specific JMU free-access instructions for required software and materials.)*

## Communication Policy

- **Primary Contact:** You must use your **JMU student email** to contact the instructor.
- **Canvas Usage:** Canvas is strictly used for grades, official announcements, and basic logistics.
- **DO NOT** use the Canvas messaging system to contact the instructor. It will not be monitored.

## AI Policy

AI tools (such as ChatGPT, Copilot, etc.) are part of this course, and may be expected or required in specific assignments. You may use Artificial Intelligence to assist with data analysis and script construction as instructed. However, you are strictly responsible for the output you submit. You must **inspect, test, verify, correct, and explain** any AI-assisted work. Blindly copying and pasting AI output without understanding it is a violation of the learning objectives and academic integrity.

## Grading Breakdown

| Category | Weight |
| --- | --- |
| Attendance | 20% |
| Labs | 40% |
| Projects (Total)<br>- *Mini Project (10%)*<br>- *Final Project (20%)* | 30% |
| Professional Certificate | 10% |

## Letter-Grade Scale

- **A:** 94.00 – 100% | **A-:** 90.00 – 93.99%
- **B+:** 87.00 – 89.99% | **B:** 84.00 – 86.99% | **B-:** 80.00 – 83.99%
- **C+:** 77.00 – 79.99% | **C:** 74.00 – 76.99% | **C-:** 70.00 – 73.99%
- **D+:** 67.00 – 69.99% | **D:** 64.00 – 66.99% | **D-:** 61.00 – 63.99%
- **F:** < 61%

## Resubmission / Late Work / Project Policy

- **Resubmission:** You are allowed to resubmit assignments multiple times *before* the deadline. Only the final submission made prior to the deadline will be graded.
- **Late Work:** Late submissions will incur a **10% penalty per day**, but no more than 40% of the total amount, unless prior arrangements have been made.
- **Final Exam Week:** **No late submissions** will be accepted during the final exam week.
- **Class Projects:** Late submissions/resubmissions of the class projects will **not** be accepted.

## Attendance / Excused Absence

Attendance is mandatory and constitutes a significant portion (20%) of your grade. Attendance will be taken at every class meeting. Absence, early leaving without permission, being late more than 20 minutes, or disrespectful/disturbing behavior will result in 0 points each time. Being late more than 5 minutes will result in a late penalty.

Absences can be excused for: Sickness or health issues, mandatory activities with written documents, or other situations with the instructor's approval.

## Academic Integrity / Honor Code

All students are expected to adhere to the JMU Honor Code. While AI use is permitted and encouraged as defined in the AI policy, plagiarizing another student's work, fabricating data, or presenting unverified AI output as original thought without proper testing and explanation is strictly prohibited and will be reported to the Honor Council.

## Accessibility / Student Support

JMU is committed to creating a universally accessible learning environment. If you have a documented disability and require accommodations, please register with the Office of Disability Services (ODS) and contact the instructor as soon as possible.

JMU offers numerous resources to support your academic and personal success. If you are struggling, please reach out to the JMU Counseling Center or Learning Centers.

## Inclement Weather

During the semester, there may be days during which the class will not meet due to inclement weather. Please check Canvas for the latest class arrangement and refer to the official JMU policy.
"""

html_content = markdown.markdown(md_body, extensions=['tables'])

full_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Syllabus - IA 342: R and S-PLUS</title>
    <style>{css}</style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>IA 342: Data Analysis with R and S-PLUS</h1>
            <p><strong>James Madison University • Intelligence Analysis</strong><br>
            <strong>Term:</strong> Fall 2026<br>
            <strong>Instructor:</strong> Dr. Xuebin Wei (weixx@jmu.edu)<br>
            <strong>Office Hours:</strong> Monday and Wednesday, 9:30–11:00 AM</p>
        </div>
        {html_content}
    </div>
</body>
</html>
"""

html_path = os.path.abspath("syllabus_rsplus.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(full_html)

def generate_pdf():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            executable_path=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        )
        page = browser.new_page()
        page.goto(f"file:///{html_path}")
        page.pdf(
            path="Syllabus_IA342_R_SPLUS.pdf",
            format="Letter",
            margin={"top": "1in", "right": "1in", "bottom": "1in", "left": "1in"},
            print_background=True
        )
        browser.close()

if __name__ == "__main__":
    generate_pdf()
