---
layout: default
title: "Module 5: Types of Graphs and Visual Analytics - IA 342"
---

<style>
/* Presentation Slide Deck Styles */
.deck-container {
  max-width: 1180px;
  margin: 1rem auto 2.5rem;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  color: #1f2328;
}

.deck-nav-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #1f2328;
  color: #f0f6fc;
  padding: 0.65rem 1.25rem;
  border-radius: 10px 10px 0 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.15);
  user-select: none;
}

.deck-title-tag {
  font-size: 0.95rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 0.6rem;
}

.deck-controls {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.deck-btn {
  background: #32383f;
  color: #f0f6fc;
  border: 1px solid #444c56;
  border-radius: 6px;
  padding: 0.4rem 0.85rem;
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.15s ease;
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
}

.deck-btn:hover:not(:disabled) {
  background: #0969da;
  border-color: #0969da;
  color: #ffffff;
}

.deck-btn:disabled {
  opacity: 0.35;
  cursor: not-allowed;
}

.deck-progress-track {
  width: 100%;
  height: 4px;
  background: #2d333b;
}

.deck-progress-fill {
  height: 100%;
  background: #2da44e;
  width: 1.33%;
  transition: width 0.25s ease;
}

.deck-stage {
  background: #ffffff;
  border: 1px solid #d0d7de;
  border-top: none;
  border-radius: 0 0 10px 10px;
  min-height: 560px;
  box-shadow: 0 6px 20px rgba(0,0,0,0.06);
  position: relative;
  overflow: hidden;
}

.slide {
  display: none;
  padding: 2.2rem 2.8rem;
  box-sizing: border-box;
  animation: slideFadeIn 0.2s ease-out;
}

.slide.active {
  display: block;
}

@keyframes slideFadeIn {
  from { opacity: 0.2; transform: translateY(6px); }
  to { opacity: 1; transform: translateY(0); }
}

.slide-badge {
  display: inline-block;
  background: #ddf4ff;
  color: #0969da;
  border: 1px solid rgba(84, 174, 255, 0.4);
  padding: 0.22rem 0.7rem;
  border-radius: 2em;
  font-size: 0.78rem;
  font-weight: 600;
  margin-bottom: 0.6rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.slide h2 {
  margin-top: 0;
  margin-bottom: 1.2rem;
  color: #1f2328;
  font-size: 1.65rem;
  border-bottom: 2px solid #eaeef2;
  padding-bottom: 0.45rem;
}

.slide-center-box {
  max-width: 860px;
  margin: 1.5rem auto;
  text-align: center;
}

.slide-main-title {
  font-size: 2.6rem;
  margin: 0.5rem 0 0.8rem;
  color: #0969da;
  font-weight: 700;
}

.slide-subtitle {
  font-size: 1.25rem;
  color: #57606a;
  margin-bottom: 1.8rem;
}

.slide-card-lead {
  background: #f6f8fa;
  border: 1px solid #d0d7de;
  padding: 1.6rem 2rem;
  border-radius: 10px;
  text-align: left;
  font-size: 1.12rem;
  line-height: 1.7;
}

.slide-text-large {
  max-width: 960px;
  margin: 0.8rem auto 1.2rem;
  font-size: 1.12rem;
  line-height: 1.7;
  color: #24292f;
}

.slide-visual-full {
  text-align: center;
  background: #f6f8fa;
  border: 1px solid #d0d7de;
  border-radius: 10px;
  padding: 0.8rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.03);
  margin: 1rem auto;
}

.slide-visual-full img, .slide-visual-full svg {
  max-width: 100%;
  max-height: 520px;
  width: auto;
  height: auto;
  border-radius: 6px;
  display: block;
  margin: 0 auto;
}

.caption-text {
  text-align: center;
  font-size: 0.92rem;
  color: #57606a;
  margin-top: 0.8rem;
  line-height: 1.5;
}

.figure-pair {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
  margin: 1.2rem 0;
}

.figure-pair figure {
  margin: 0;
  min-width: 0;
  text-align: center;
}

.figure-pair img {
  width: 100%;
  max-height: 480px;
  object-fit: contain;
  border-radius: 6px;
  border: 1px solid #d0d7de;
  background: #ffffff;
  display: block;
  margin: 0 auto 0.5rem;
}

.figure-pair figcaption {
  font-size: 0.92rem;
  text-align: center;
  font-weight: 600;
  color: #57606a;
}

.video-container-large {
  position: relative;
  width: 100%;
  max-width: 940px;
  margin: 1rem auto;
  aspect-ratio: 16 / 9;
  overflow: hidden;
  border-radius: 10px;
  border: 1px solid #d0d7de;
  background: #000;
  box-shadow: 0 4px 16px rgba(0,0,0,0.15);
}

.video-container-large iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border: 0;
}

.media-caption {
  text-align: center;
  margin-top: 0.6rem;
  font-size: 0.92rem;
  color: #57606a;
}

.activity-container-full {
  width: 100%;
  max-width: 100%;
  border: 1px solid #d0d7de;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 4px 16px rgba(0,0,0,0.08);
  background: #f8fafc;
  margin: 1rem auto;
  height: auto;
}

.activity-container-full iframe,
.slide iframe:not(.youtube) {
  width: 100% !important;
  max-width: 100% !important;
  min-height: 480px;
  border: 0;
  display: block;
  box-sizing: border-box;
  transition: height 0.15s ease-out;
}

.alert-takeaway {
  background: #dafbe1;
  border-left: 4px solid #1a7f37;
  padding: 1rem 1.25rem;
  border-radius: 0 8px 8px 0;
  font-size: 1.05rem;
  color: #1a7f37;
  font-weight: 500;
  line-height: 1.6;
  margin: 1rem 0;
}

.alert-teaching-point {
  background: #ddf4ff;
  border-left: 4px solid #0969da;
  padding: 1rem 1.25rem;
  border-radius: 0 8px 8px 0;
  font-size: 1.05rem;
  color: #0969da;
  font-weight: 500;
  line-height: 1.6;
  margin: 1rem 0;
}

.deck-btn-primary {
  background: #0969da;
  color: #ffffff;
  border: 1px solid #0969da;
  border-radius: 8px;
  padding: 0.75rem 1.8rem;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.15s ease;
}

.deck-btn-primary:hover {
  background: #0858b9;
}

/* Fullscreen Mode */
.deck-container:fullscreen,
.deck-container:-webkit-full-screen {
  max-width: 100vw;
  width: 100vw;
  height: 100vh;
  margin: 0;
  box-sizing: border-box;
  background: #111827;
  display: flex;
  flex-direction: column;
}

.deck-container:fullscreen .deck-stage,
.deck-container:-webkit-full-screen .deck-stage {
  flex: 1;
  min-height: 0;
  border-radius: 0;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  background: #ffffff;
}

.deck-container:fullscreen .slide.active,
.deck-container:-webkit-full-screen .slide.active {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  overflow-y: auto;
  padding: 1.5rem clamp(1.5rem, 4vw, 4rem);
  box-sizing: border-box;
}

.deck-container:fullscreen .slide-visual-full,
.deck-container:-webkit-full-screen .slide-visual-full {
  width: 100%;
  flex: 1;
  min-height: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.deck-container:fullscreen .slide-visual-full img,
.deck-container:fullscreen .slide-visual-full svg,
.deck-container:-webkit-full-screen .slide-visual-full img,
.deck-container:-webkit-full-screen .slide-visual-full svg {
  max-width: 100%;
  max-height: calc(100vh - 9rem);
  width: auto;
  height: auto;
  object-fit: contain;
}

.deck-container:fullscreen .video-container-large,
.deck-container:-webkit-full-screen .video-container-large {
  max-width: none;
  width: min(88vw, calc((100vh - 9rem) * 16 / 9));
  height: min(49.5vw, calc(100vh - 9rem));
  aspect-ratio: auto;
  position: relative;
}

.deck-container:fullscreen .video-container-large iframe,
.deck-container:-webkit-full-screen .video-container-large iframe {
  position: absolute;
  top: 0; left: 0;
  width: 100%;
  height: 100%;
}

.deck-container:fullscreen .activity-container-full,
.deck-container:-webkit-full-screen .activity-container-full {
  width: 100%;
  height: calc(100vh - 9rem);
}

@media (max-width: 860px) {
  .deck-stage { min-height: 480px; }
  .slide { padding: 1.5rem 1.2rem; }
  .slide-visual-full img, .slide-visual-full svg { max-height: 340px; }
  .activity-container-full { height: auto; }
  .figure-pair { grid-template-columns: 1fr; }
}
</style>


<div class="deck-container" id="lectureDeck">
  <div class="deck-nav-bar">
    <div class="deck-title-tag">
      <span>IA 342 Week 5 Lecture</span>
      <span style="opacity: 0.4;">|</span>
      <span id="slideCounter">Slide 1 of 75</span>
    </div>
    <div class="deck-controls">
      <button class="deck-btn" id="prevBtn" onclick="changeSlide(-1)" title="Previous (&larr; / PageUp)">&#9664; Prev</button>
      <button class="deck-btn" id="nextBtn" onclick="changeSlide(1)" title="Next (&rarr; / Space / PageDown)">Next &#9654;</button>
      <button class="deck-btn" onclick="toggleFullScreen()" title="Fullscreen Mode">&#9974; Fullscreen</button>
    </div>
  </div>
  <div class="deck-progress-track">
    <div class="deck-progress-fill" id="progressBar"></div>
  </div>

  <div class="deck-stage">
    <!-- SLIDE 1: Title Screen -->
    <div class="slide active" data-slide="1">
      <div class="slide-center-box">
        <span class="slide-badge">Lecture 05 &middot; Types of Graphs &amp; Visual Analytics</span>
        <h1 class="slide-main-title">Types of Graphs and Visual Analytics</h1>
        <p class="slide-subtitle">Read and Choose Graphs &middot; Relationships &amp; Encodings &middot; Tableau Foundations</p>

        <!-- Course Roadmap Progress Indicator -->
        <div style="margin: 1.25rem auto 1.5rem; max-width: 840px; background: #ffffff; border: 1px solid #d0d7de; border-radius: 8px; padding: 0.85rem 1.2rem; box-shadow: 0 1px 3px rgba(0,0,0,0.04);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.6rem;">
            <span style="font-size: 0.8rem; font-weight: 700; text-transform: uppercase; color: #57606a; letter-spacing: 0.5px;">Semester Course Roadmap</span>
            <span style="font-size: 0.78rem; font-weight: 600; color: #0969da; background: #ddf4ff; padding: 0.15rem 0.55rem; border-radius: 12px; border: 1px solid rgba(84,174,255,0.3);">Module 5 of 6</span>
          </div>
          <div style="display: flex; align-items: center; justify-content: space-between; gap: 0.35rem; font-size: 0.8rem; flex-wrap: wrap;">
            <span style="padding: 0.22rem 0.55rem; background: #f6f8fa; border: 1px solid #d0d7de; border-radius: 4px; color: #57606a;">1. Intro</span>
            <span style="color: #8c959f;">&rarr;</span>
            <span style="padding: 0.22rem 0.55rem; background: #f6f8fa; border: 1px solid #d0d7de; border-radius: 4px; color: #57606a;">2. Vis Foundations</span>
            <span style="color: #8c959f;">&rarr;</span>
            <span style="padding: 0.22rem 0.55rem; background: #f6f8fa; border: 1px solid #d0d7de; border-radius: 4px; color: #57606a;">3. Map Design &amp; Spatial</span>
            <span style="color: #8c959f;">&rarr;</span>
            <span style="padding: 0.22rem 0.55rem; background: #f6f8fa; border: 1px solid #d0d7de; border-radius: 4px; color: #57606a;">4. Color Theory</span>
            <span style="color: #8c959f;">&rarr;</span>
            <span style="padding: 0.22rem 0.65rem; background: #0969da; border: 1px solid #0969da; border-radius: 4px; color: #ffffff; font-weight: 600; box-shadow: 0 1px 3px rgba(9,105,218,0.3);">&#9654; 5. BI &amp; Tableau (Current)</span>
            <span style="color: #8c959f;">&rarr;</span>
            <span style="padding: 0.22rem 0.55rem; background: #f6f8fa; border: 1px solid #d0d7de; border-radius: 4px; color: #57606a;">6. Storytelling</span>
          </div>
        </div>

        <div class="slide-card-lead">
          <p><strong>IA 342 &mdash; Visualization Methods, Technologies, and Tools for Intelligence Analysis</strong></p>
          <p>Dr. Xuebin Wei &middot; IA342 &middot; Week 5 &middot; Fall 2026</p>
          <div class="slide-visual-full" style="margin: 1rem 0;">
            <img src="../../assets/week-5/graph-structure.svg" alt="Types of Graphs and Visual Analytics" />
          </div>
          <div class="caption-text">
            <em>Connecting analytical questions to visual encodings, chart critique, and Tableau visual analytics foundations.</em>
          </div>
          <div style="margin-top: 1.5rem; text-align: center;">
            <button class="deck-btn-primary" onclick="changeSlide(1)">Start Lecture &#9654;</button>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 2: 01 — GIF — Clear Off the Table -->
    <div class="slide" data-slide="2">
      <span class="slide-badge">Read and choose a graph</span>
      <h2>01 &mdash; GIF &mdash; Clear Off the Table</h2>
<div class="slide-text-large">
<p>Watch how alignment, whitespace, borders and numeric precision change the readability of a table.</p>
<div class="alert-teaching-point"><strong>Discuss:</strong> Which changes help you find a value, and which help you compare values? The example uses invented wrestling statistics; it is a design demonstration, not a factual sports dataset.</div>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/darkhorse-table.gif" alt="Clear Off the Table — the data tables edition" />
</div>




<p class="caption-text"><em>Animation: Joey Cherdarchuk / Darkhorse, <a href="https://darkhorsevisualization.com/blog/clear-off-the-table">Clear Off the Table — Remove to Improve: The Data Tables Edition</a> (March 27, 2014).</em></p>
    </div>

    <!-- SLIDE 3: 02 — Elements of a Graph: Axes and Units -->
    <div class="slide" data-slide="3">
      <span class="slide-badge">Read and choose a graph</span>
      <h2>02 &mdash; Elements of a Graph: Axes and Units</h2>
<div class="slide-text-large">
<p>Locate the <strong>data region</strong>, horizontal and vertical <strong>scales</strong>, <strong>tick marks</strong>, <strong>tick labels</strong>, <strong>axis labels</strong>, and <strong>grid lines</strong>.</p>
<p>A tick label states a value; an axis label identifies the variable and unit. Here, the x-axis orders days and the y-axis measures requests. Axis placement alone does not establish causation.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/graph-structure.svg" alt="Elements of Standard Graphs I: Structure" />
</div>





    </div>

    <!-- SLIDE 4: 03 — Elements of a Graph: Marks and Context -->
    <div class="slide" data-slide="4">
      <span class="slide-badge">Read and choose a graph</span>
      <h2>03 &mdash; Elements of a Graph: Marks and Context</h2>
<div class="slide-text-large">
<p>Now identify the <strong>data paths</strong>, <strong>reference line</strong>, <strong>neatline/frame</strong>, <strong>legend</strong>, <strong>data labels</strong>, <strong>title</strong>, and <strong>data source</strong>.</p>
<p>A path needs an identifiable meaning. A reference line should be named: target, average, or benchmark. The title should be unambiguous, efficient, and economical.</p>
<div class="alert-teaching-point"><strong>Try it:</strong> Explain the constructed chart without seeing the underlying table. Which element tells you what 80 means? Which one tells you what 60 means?</div>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/graph-elements.svg" alt="Elements of Standard Graphs II: Meaning" />
</div>





    </div>

    <!-- SLIDE 5: 04 — Reading 1 — Match the Relationship to the Encoding -->
    <div class="slide" data-slide="5">
      <span class="slide-badge">Read and choose a graph</span>
      <h2>04 &mdash; Reading 1 &mdash; Match the Relationship to the Encoding</h2>
<div class="slide-text-large">
<p>Select a <strong>relationship</strong>, then try <strong>points, lines, bars, or boxes</strong>. The chart and explanation change together. Some choices are appropriate only for a particular task.</p>
<div class="alert-teaching-point"><strong>Try:</strong> Compare Ranking → Points with Ranking → Lines. Then compare Correlation → Points with Correlation → Bars. Why does “bars” mean a table lens in the second case, rather than a scatter plot?</div>
</div>


<div class="activity-container-full">
  <iframe src="../../assets/week-5/relationship-encoding.html" title="Explore relationships and encodings from the Graph Selection Matrix" loading="lazy" onload="resizeIframe(this)" sandbox="allow-scripts allow-same-origin"></iframe>
</div>
<p style="text-align: center; margin-top: 0.5rem; font-size: 0.95rem;">
  <a href="../../assets/week-5/relationship-encoding.html" target="_blank" rel="noopener">Open this activity on its own</a>
</p>


<p class="caption-text"><em>Framework: Stephen Few, <a href="https://www.perceptualedge.com/articles/misc/Graph_Selection_Matrix.pdf">Graph Selection Matrix</a>, course edition ©2004–2012. The interactive examples are new classroom illustrations, not screenshots from the reading.</em></p>
    </div>

    <!-- SLIDE 6: 05 — Reading 1 — Change the Question, Change the Chart -->
    <div class="slide" data-slide="6">
      <span class="slide-badge">Read and choose a graph</span>
      <h2>05 &mdash; Reading 1 &mdash; Change the Question, Change the Chart</h2>
<div class="slide-text-large">
<p>Use the <strong>same 308 diamond records</strong> to ask four different questions. Notice what one bar or point represents in each view.</p>
<div class="alert-teaching-point"><strong>Explain:</strong> Why does a category count need a different arrangement from a price distribution? Does a bar below the overall mean mean that a diamond has a negative price?</div>
</div>


<div class="activity-container-full">
  <iframe src="../../assets/week-5/question-chart.html" title="Switch analytical questions using one Diamonds dataset" loading="lazy" onload="resizeIframe(this)" sandbox="allow-scripts allow-same-origin"></iframe>
</div>
<p style="text-align: center; margin-top: 0.5rem; font-size: 0.95rem;">
  <a href="../../assets/week-5/question-chart.html" target="_blank" rel="noopener">Open this activity on its own</a>
</p>


<p class="caption-text"><em>Relationship framework: Stephen Few, <a href="https://www.perceptualedge.com/articles/misc/Graph_Selection_Matrix.pdf">Graph Selection Matrix</a>. Data: <a href="https://github.com/xbwei/data-analysis-with-generative-ai/blob/main/diamonds.csv">course Diamonds dataset</a>. Questions and interactive views are course applications.</em></p>
    </div>

    <!-- SLIDE 7: 06 — Logarithms — Start with Powers of Ten -->
    <div class="slide" data-slide="7">
      <span class="slide-badge">Read the scale</span>
      <h2>06 &mdash; Logarithms &mdash; Start with Powers of Ten</h2>
<div class="slide-text-large">
<p>A <strong>base-10 logarithm</strong> asks: <strong>“What power of 10 produces this number?”</strong> Start at 1 and multiply by 10 at each step.</p>
<p>For example, <strong>the base-10 logarithm of 100 is 2</strong>: the exponent tells us where 100 sits on this scale. The zero in <strong>10<sup>0</sup></strong> is an exponent; it does <strong>not</strong> make the result zero.</p>
<p><strong>Arithmetic:</strong> equally spaced values might be <strong>0, 100, 200, 300</strong>—the same amount is added each time. <strong>Logarithmic:</strong> equally spaced values might be <strong>1, 10, 100, 1,000</strong>—the same factor is multiplied each time.</p>
<p>A standard log axis has <strong>no zero value</strong>. Its tick labels usually show the original values, not the log-scale positions. Next, use this idea to read the two original scale examples.</p>
</div>




<div style="overflow-x: auto; margin: 1.2rem 0;">
  <table style="width: 100%; border-collapse: collapse; font-size: 0.95rem; line-height: 1.5; border: 1px solid #d0d7de; border-radius: 6px;">
    <thead>
      <tr style="background-color: #f6f8fa; border-bottom: 2px solid #d0d7de;">
        <th style="padding: 0.75rem 1rem; text-align: left; font-weight: 600; color: #1f2328;">Power of ten</th>
        <th style="padding: 0.75rem 1rem; text-align: left; font-weight: 600; color: #1f2328;">Read it aloud</th>
        <th style="padding: 0.75rem 1rem; text-align: left; font-weight: 600; color: #1f2328;">Value</th>
        <th style="padding: 0.75rem 1rem; text-align: left; font-weight: 600; color: #1f2328;">Log-scale position</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border-bottom: 1px solid #d0d7de;">
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;"><strong>10<sup>0</sup> = 1</strong></td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">Ten to the power of zero equals one</td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">1</td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">0</td>
      </tr>
      <tr style="border-bottom: 1px solid #d0d7de;" style="background-color: #fafbfc;">
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;"><strong>10<sup>1</sup> = 10</strong></td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">Ten to the power of one equals ten</td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">10</td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">1</td>
      </tr>
      <tr style="border-bottom: 1px solid #d0d7de;">
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;"><strong>10<sup>2</sup> = 100</strong></td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">Ten squared equals one hundred</td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">100</td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">2</td>
      </tr>
      <tr style="border-bottom: 1px solid #d0d7de;" style="background-color: #fafbfc;">
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;"><strong>10<sup>3</sup> = 1,000</strong></td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">Ten cubed equals one thousand</td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">1,000</td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">3</td>
      </tr>
    </tbody>
  </table>
</div>


    </div>

    <!-- SLIDE 8: 07 — Arithmetic versus Semi-Log — What Makes a Straight Line? -->
    <div class="slide" data-slide="8">
      <span class="slide-badge">Read the scale</span>
      <h2>07 &mdash; Arithmetic versus Semi-Log &mdash; What Makes a Straight Line?</h2>
<div class="slide-text-large">
<p><strong>Arithmetic:</strong> Equal <strong>absolute changes</strong> over equal x-intervals make a straight line. For example, adding the same number each year is a constant amount of change.</p>
<p><strong>Semi-log:</strong> Equal <strong>proportional changes</strong> over equal x-intervals make a straight line. For example, increasing by the same percentage each year is a constant rate of growth.</p>
<p>Here, <strong>x stays arithmetic</strong> in both charts. Only the y-scale changes. Equal tick spacing does not make every dataset straight; the pattern of change must also be constant in the relevant sense.</p>
</div>

<div class="figure-pair"><figure><img src="../../assets/week-5/original-arithmetic.png" alt="Arithmetic-scale example"><figcaption>Arithmetic: constant amount of change → straight line</figcaption></figure><figure><img src="../../assets/week-5/original-semilog.png" alt="Semi-logarithmic-scale example"><figcaption>Semi-log: constant proportional growth → straight line</figcaption></figure></div>




    </div>

    <!-- SLIDE 9: 08 — Semi-Log versus Log-Log — Check Both Axes -->
    <div class="slide" data-slide="9">
      <span class="slide-badge">Read the scale</span>
      <h2>08 &mdash; Semi-Log versus Log-Log &mdash; Check Both Axes</h2>
<div class="slide-text-large">
<p><strong>Semi-log:</strong> x uses equal differences; y uses equal ratios. A straight line shows the same proportional change in y for each equal step in x.</p>
<p><strong>Log-log:</strong> both x and y use equal ratios. A straight line shows a consistent proportional relationship: multiplying x by a given factor corresponds to multiplying y by a consistent factor.</p>
<p><strong>Read the horizontal labels first.</strong> In semi-log, the same horizontal distance means the same amount of x; in log-log, it means the same ratio of x. Neither transformed axis has an ordinary zero baseline.</p>
</div>

<div class="figure-pair"><figure><img src="../../assets/week-5/original-semilog.png" alt="Semi-logarithmic example"><figcaption>Semi-log: arithmetic x, logarithmic y</figcaption></figure><figure><img src="../../assets/week-5/original-loglog.png" alt="Log-log example"><figcaption>Log-log: logarithmic x and y</figcaption></figure></div>




    </div>

    <!-- SLIDE 10: 09 — Bar Chart — Compare Values by Length -->
    <div class="slide" data-slide="10">
      <span class="slide-badge">Compare categories: bars and their pitfalls</span>
      <h2>09 &mdash; Bar Chart &mdash; Compare Values by Length</h2>
<div class="slide-text-large">
<p>A bar starts at a baseline and uses <strong>length</strong> to represent a count, average, rate, or other stated value. Its width normally does not encode data.</p>
<p>Use a zero baseline for an ordinary magnitude bar chart. Sort when ranking is the task; retain chronological or other meaningful order when that matters.</p>
<div class="alert-teaching-point"><strong>Read:</strong> What is the measure? What is the unit? Which two values are easiest to compare?</div>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/labels-horizontal.svg" alt="Horizontal bars showing category values on a common baseline" />
</div>





    </div>

    <!-- SLIDE 11: 10 — Real Case — SAS Adds a Twisting 3D Baseline -->
    <div class="slide" data-slide="11">
      <span class="slide-badge">Compare categories: bars and their pitfalls</span>
      <h2>10 &mdash; Real Case &mdash; SAS Adds a Twisting 3D Baseline</h2>
<div class="slide-text-large">
<p>The perspective, curved baseline, and angled bars compete with the quantities. Which year-to-year comparison can you read confidently?</p>
<p>Depth does not encode a separate variable here. It makes a two-dimensional comparison harder.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/old-sas-3d.png" alt="Bad Example: A Revenue Chart with a Twisting Baseline" />
</div>




<p class="caption-text"><em>Graphic publisher: SAS Institute, February 4, 2009 press release. <a href="https://www.perceptualedge.com/blog/?p=410">Public archived reproduction and contemporary critique</a>: Stephen Few, <i>Data Visualization and Dog Food</i> (2009).</em></p>
    </div>

    <!-- SLIDE 12: 11 — Remove the 3D Effect: Restore a Flat Baseline -->
    <div class="slide" data-slide="12">
      <span class="slide-badge">Compare categories: bars and their pitfalls</span>
      <h2>11 &mdash; Remove the 3D Effect: Restore a Flat Baseline</h2>
<div class="slide-text-large">
<p>Use a flat baseline, readable units, and unambiguous positions. A revenue chart should make amounts and growth comparable, not require the reader to mentally undo perspective.</p>
<p>The example below uses <strong>illustrative company data</strong>, not a reconstructed SAS historical series.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/revenue-flat.svg" alt="Remove Depth, Restore Comparison" />
</div>





    </div>

    <!-- SLIDE 13: 12 — Label Problem — Rotate the Chart, Not the Reader -->
    <div class="slide" data-slide="13">
      <span class="slide-badge">Compare categories: bars and their pitfalls</span>
      <h2>12 &mdash; Label Problem &mdash; Rotate the Chart, Not the Reader</h2>
<div class="slide-text-large">
<p>Long category names make rotated labels hard to scan and align with the corresponding bars.</p>
<div class="alert-teaching-point"><strong>Try it:</strong> Find the largest category, then read its full name. Is the effort coming from the data or from the layout?</div>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/labels-vertical.svg" alt="Bad Example: Rotate the Chart, Not the Reader" />
</div>





    </div>

    <!-- SLIDE 14: 13 — Readable Labels — Keep the Values, Change the Orientation -->
    <div class="slide" data-slide="14">
      <span class="slide-badge">Compare categories: bars and their pitfalls</span>
      <h2>13 &mdash; Readable Labels &mdash; Keep the Values, Change the Orientation</h2>
<div class="slide-text-large">
<p>Keep the same category values. Use horizontal bars, horizontal text, meaningful order, and direct value labels.</p>
<p>The redesign reduces the work needed to identify and compare categories. It does not change the underlying data.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/labels-horizontal.svg" alt="Redesign: Horizontal Bars and Readable Labels" />
</div>





    </div>

    <!-- SLIDE 15: 14 — Reading 2 — Watch a Chart Become Clearer -->
    <div class="slide" data-slide="15">
      <span class="slide-badge">Compare categories: bars and their pitfalls</span>
      <h2>14 &mdash; Reading 2 &mdash; Watch a Chart Become Clearer</h2>
<div class="slide-text-large">
<p>Follow a visual cleanup sequence: <strong>labels and order → reduce visual competition → restore useful context</strong>. The values stay fixed.</p>
<p><strong>At each step:</strong> What became easier to compare? What information must not disappear? Keep units, a meaningful scale, and an identified reference even when removing decoration.</p>
</div>


<div class="activity-container-full">
  <iframe src="../../assets/week-5/chart-cleanup.html" title="Step-by-step visual chart cleanup" loading="lazy" onload="resizeIframe(this)" sandbox="allow-scripts allow-same-origin"></iframe>
</div>
<p style="text-align: center; margin-top: 0.5rem; font-size: 0.95rem;">
  <a href="../../assets/week-5/chart-cleanup.html" target="_blank" rel="noopener">Open this activity on its own</a>
</p>


<p class="caption-text"><em>Principles adapted from Jeffrey A. Shaffer, <a href="https://dataplusscience.com/files/Shaffer%204C%20-%20Clean%20Examples.pdf">“Clean” Examples</a>. This interactive chart uses illustrative data; the next page retains the reading’s actual worked example.</em></p>
    </div>

    <!-- SLIDE 16: 15 — Reading 2 — What the Finished Chart Still Contains -->
    <div class="slide" data-slide="16">
      <span class="slide-badge">Compare categories: bars and their pitfalls</span>
      <h2>15 &mdash; Reading 2 &mdash; What the Finished Chart Still Contains</h2>
<div class="slide-text-large">
<p>The final example does more than remove lines: it <strong>orders the bars</strong>, uses readable labels, states the <strong>unit</strong>, and adds a <strong>named target</strong> and a conclusion in the title. The source and date remain visible.</p>
<p><strong>Read the claim:</strong> 23 − 16 = 7. The title’s claim can be checked against the displayed bar and target. “Clean” does not mean “no context.”</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/shaffer-clean-worked.png" alt="Shaffer’s final fruit-sales example, with title, target, units, source and date" />
</div>




<p class="caption-text"><em>Figure and worked teaching example: Jeffrey A. Shaffer, <a href="https://dataplusscience.com/files/Shaffer%204C%20-%20Clean%20Examples.pdf#page=4">“Clean” Examples, p. 4</a> (2011). Cropped to the final chart, retaining its attribution. This is the reading’s example, not newly collected fruit-sales data.</em></p>
    </div>

    <!-- SLIDE 17: 16 — Interactive — A Truncated Baseline Changes the Impression -->
    <div class="slide" data-slide="17">
      <span class="slide-badge">Compare categories: bars and their pitfalls</span>
      <h2>16 &mdash; Interactive &mdash; A Truncated Baseline Changes the Impression</h2>
<div class="slide-text-large">
<p>The constructed values remain 94, 96, and 100. Change only the displayed bar baseline from zero to 90.</p>
<p><strong>Ask:</strong> Which representation makes the difference appear larger? What proportion do the <em>drawn lengths</em> imply? Do the labels repair the first impression?</p>
<p><a href="../../assets/week-5/bar-baseline.html" target="_blank" rel="noopener">Open this experiment by itself</a>.</p>
</div>


<div class="activity-container-full">
  <iframe src="../../assets/week-5/bar-baseline.html" title="Interactive: Does 100 Look Six Units Larger Than 94?" loading="lazy" onload="resizeIframe(this)" sandbox="allow-scripts allow-same-origin"></iframe>
</div>
<p style="text-align: center; margin-top: 0.5rem; font-size: 0.95rem;">
  <a href="../../assets/week-5/bar-baseline.html" target="_blank" rel="noopener">Open this activity on its own</a>
</p>



    </div>

    <!-- SLIDE 18: 17 — Real Case — Grouped Bars Compare Category Sales -->
    <div class="slide" data-slide="18">
      <span class="slide-badge">Compare categories: bars and their pitfalls</span>
      <h2>17 &mdash; Real Case &mdash; Grouped Bars Compare Category Sales</h2>
<div class="slide-text-large">
<p><strong>Did pharmacy sales grow?</strong> Use a grouped bar chart to compare the same category across years on a common zero-based scale.</p>
<p>The dark-blue <strong>Pharmacy</strong> bar rises from <strong>$11.015 billion to $11.388 billion</strong>: about <strong>3.4% growth</strong>. The legend identifies all five product categories, with the same colors on the following two slides.</p>
<p><strong>Do not stop at the part.</strong> Has pharmacy also become a larger proportion of Kroger’s sales? The next two arrangements use these same data to answer different questions.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/kroger-grouped.svg" alt="Kroger grouped sales bars for fiscal 2019 and 2020" />
</div>




<p class="caption-text"><em>Data: The Kroger Co., <a href="https://www.sec.gov/Archives/edgar/data/56873/000155837021003706/R10.htm">FY 2020 Form 10-K, Note 1 — Disaggregated Revenues</a>, fiscal 2019 and 2020. New plots of the reported data; displayed in USD billions rather than the filing’s USD millions.</em></p>
    </div>

    <!-- SLIDE 19: 18 — Real Case — Stacked Bars Preserve Total Size -->
    <div class="slide" data-slide="19">
      <span class="slide-badge">Compare categories: bars and their pitfalls</span>
      <h2>18 &mdash; Real Case &mdash; Stacked Bars Preserve Total Size</h2>
<div class="slide-text-large">
<p>Stack the same five product categories within each year. The complete bar is <strong>total sales</strong>; its segments are the components.</p>
<p>Total sales rise from <strong>$122.286 billion to $132.498 billion</strong>, about <strong>8.4%</strong>—faster than the pharmacy component. The dark-blue pharmacy segment is larger in dollars, but that does not yet tell us its share.</p>
<p>Use <strong>ordinary stacked/component bars</strong> to show both the whole and its parts. Only the bottom segment shares the zero baseline; grouped bars can make an interior component easier to compare.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/kroger-stacked.svg" alt="Kroger stacked sales bars preserve different annual totals" />
</div>




<p class="caption-text"><em>Data: The Kroger Co., <a href="https://www.sec.gov/Archives/edgar/data/56873/000155837021003706/R10.htm">FY 2020 Form 10-K, Note 1 — Disaggregated Revenues</a>, fiscal 2019 and 2020. New plots of the reported data; displayed in USD billions rather than the filing’s USD millions.</em></p>
    </div>

    <!-- SLIDE 20: 19 — Real Case — 100% Stacked Bars Reveal the Changing Mix -->
    <div class="slide" data-slide="20">
      <span class="slide-badge">Compare categories: bars and their pitfalls</span>
      <h2>19 &mdash; Real Case &mdash; 100% Stacked Bars Reveal the Changing Mix</h2>
<div class="slide-text-large">
<p>Now divide each component by <strong>that year’s total sales</strong>. Every full bar becomes 100%; the dollar totals remain visible below it.</p>
<p><strong>Both are true: pharmacy sales increased, while pharmacy’s share fell from 9.0% to 8.6%.</strong> The whole grew faster than this part. These are proportions of <strong>Kroger’s own sales</strong>, not its share of the entire pharmacy market.</p>
<p><strong>Choose by question:</strong> grouped bars compare category amounts; ordinary stacked bars retain total size; <strong>100% stacked (percentage component) bars</strong> compare the mix. Here, “component” describes parts of a whole; it does not automatically mean percentages.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/kroger-percent.svg" alt="Kroger pharmacy sales rise in dollars but fall from nine to eight point six percent of total sales" />
</div>




<p class="caption-text"><em>Data: The Kroger Co., <a href="https://www.sec.gov/Archives/edgar/data/56873/000155837021003706/R10.htm">FY 2020 Form 10-K, Note 1 — Disaggregated Revenues</a>, fiscal 2019 and 2020. New plots of the reported data; displayed in USD billions rather than the filing’s USD millions.</em></p>
    </div>

    <!-- SLIDE 21: 20 — Diverging Bar Chart — Deviation around a Reference -->
    <div class="slide" data-slide="21">
      <span class="slide-badge">Compare categories: bars and their pitfalls</span>
      <h2>20 &mdash; Diverging Bar Chart &mdash; Deviation around a Reference</h2>
<div class="slide-text-large">
<p>A diverging bar places values on either side of a meaningful midpoint: zero change, a benchmark, or a balanced response point.</p>
<p>Identify whether the measure is an absolute difference, a percent change, or a percentage-point difference. The sign and direction should be clear without color alone.</p>
<div class="alert-teaching-point"><strong>Read:</strong> Which area is furthest below the benchmark? Is a difference of −12 percentage points the same as −12 percent?</div>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/diverging.svg" alt="Diverging Bar Chart" />
</div>





    </div>

    <!-- SLIDE 22: 21 — Pareto Chart — Ranked Bars plus Cumulative Contribution -->
    <div class="slide" data-slide="22">
      <span class="slide-badge">Compare categories: bars and their pitfalls</span>
      <h2>21 &mdash; Pareto Chart &mdash; Ranked Bars plus Cumulative Contribution</h2>
<div class="slide-text-large">
<p>A Pareto chart combines descending category values with cumulative contribution. Read the bars and the cumulative line as different encodings, with explicit scales.</p>
<p>Synchronized and independent axes can change how tightly the bars and cumulative line appear related. Read both scales before comparing positions.</p>
<p><strong>Here:</strong> the first two categories contribute 70% and the first three 85%. The cumulative line shows how quickly a small number of categories account for most of the total.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/pareto.svg" alt="Pareto Chart: Which Categories Accumulate Most?" />
</div>





    </div>

    <!-- SLIDE 23: 22 — Histogram — One Dataset, Different Bin Widths -->
    <div class="slide" data-slide="23">
      <span class="slide-badge">Distributions and paired measurements</span>
      <h2>22 &mdash; Histogram &mdash; One Dataset, Different Bin Widths</h2>
<div class="slide-text-large">
<p>A <strong>histogram</strong> counts observations within ordered numerical intervals. Here x is <strong>diamond PRICE</strong> and y is the <strong>number of records</strong> in each bin.</p>
<p>Change only the bin width. The 308 records stay the same; the apparent shape and tallest bin may change. Ask which peaks persist and whether an average hides the upper tail.</p>
<p><strong>Bar chart versus histogram:</strong> category bars can be ranked; histogram bins must retain their numerical order. These examples use equal-width bins.</p>
<p><details><summary>Additional reference: a histogram with a cumulative line</summary><p>Bars give interval counts. A cumulative line answers how much lies at or below successive values. Read its separate scale.</p><img src="../../assets/week-5/original-histogram.png" alt="Instructor’s histogram with cumulative line"></details></p>
</div>


<div class="activity-container-full">
  <iframe src="../../assets/week-5/histogram-bins.html" title="Change the price histogram bin width" loading="lazy" onload="resizeIframe(this)" sandbox="allow-scripts allow-same-origin"></iframe>
</div>
<p style="text-align: center; margin-top: 0.5rem; font-size: 0.95rem;">
  <a href="../../assets/week-5/histogram-bins.html" target="_blank" rel="noopener">Open this activity on its own</a>
</p>



    </div>

    <!-- SLIDE 24: 23 — Box Plot — Compare the Middle, Spread and Tails -->
    <div class="slide" data-slide="24">
      <span class="slide-badge">Distributions and paired measurements</span>
      <h2>23 &mdash; Box Plot &mdash; Compare the Middle, Spread and Tails</h2>
<div class="slide-text-large">
<p>A box plot summarizes a distribution through position. The median identifies its middle, and the box spans Q1 to Q3—the middle half of the ordered values.</p>
<p>Several boxes make it possible to compare distributions without showing every mark. Check both location and spread; similar medians can conceal different variability.</p>
<p><strong>Read the chart:</strong> Which group is higher? Which has the wider middle half? Neither question requires a zero baseline for the position scale.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/original-boxplot.png" alt="Box Plot: A Compact Distribution Summary" />
</div>





    </div>

    <!-- SLIDE 25: 24 — Box Plot — What the Whiskers and Density Mean -->
    <div class="slide" data-slide="25">
      <span class="slide-badge">Distributions and paired measurements</span>
      <h2>24 &mdash; Box Plot &mdash; What the Whiskers and Density Mean</h2>
<div class="slide-text-large">
<p>A box summarizes the middle half of a distribution. <strong>IQR = Q3 − Q1</strong>. The density curve shows what a compact box can hide about shape.</p>
<p>The picture uses an idealized normal distribution. In the sample-based examples, whiskers end at the furthest observations within <strong>1.5 × IQR</strong> of a box edge; points beyond them are shown separately. A separately plotted point is not automatically an error.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/original-box-density.png" alt="Box Plots, Density, and Whiskers" />
</div>




<p class="caption-text"><em>Figure: Jhguch (original) and Chen-Pan Liao (vector redraw), <a href="https://commons.wikimedia.org/wiki/File:Boxplot_vs_PDF.svg">Boxplot vs PDF</a>, <a href="https://creativecommons.org/licenses/by-sa/2.5/">CC BY-SA 2.5</a>. Cropped to show the box and density panels.</em></p>
    </div>

    <!-- SLIDE 26: 25 — Interactive — Reveal Records Behind the Boxes -->
    <div class="slide" data-slide="26">
      <span class="slide-badge">Distributions and paired measurements</span>
      <h2>25 &mdash; Interactive &mdash; Reveal Records Behind the Boxes</h2>
<div class="slide-text-large">
<p>Show and hide individual diamond records. Compare the median, the middle half, and the tails by clarity.</p>
<p><strong>Ask:</strong> Which details become visible only when the observations are shown? Would your audience need a short “how to read this chart” explanation?</p>
<p><a href="../../assets/week-5/boxplot-records.html" target="_blank" rel="noopener">Open this experiment by itself</a>.</p>
</div>


<div class="activity-container-full">
  <iframe src="../../assets/week-5/boxplot-records.html" title="Interactive: Reveal the Records Behind the Boxes" loading="lazy" onload="resizeIframe(this)" sandbox="allow-scripts allow-same-origin"></iframe>
</div>
<p style="text-align: center; margin-top: 0.5rem; font-size: 0.95rem;">
  <a href="../../assets/week-5/boxplot-records.html" target="_blank" rel="noopener">Open this activity on its own</a>
</p>



    </div>

    <!-- SLIDE 27: 26 — Scatter Plot — Start with Two Numerical Variables -->
    <div class="slide" data-slide="27">
      <span class="slide-badge">Distributions and paired measurements</span>
      <h2>26 &mdash; Scatter Plot &mdash; Start with Two Numerical Variables</h2>
<div class="slide-text-large">
<p>Each dot pairs <strong>WEIGHT on the x-axis</strong> with <strong>PRICE on the y-axis</strong> for one diamond record. The markers have the same size.</p>
<p>Read direction, curvature, spread, clusters, and unusual observations. <strong>Two numerical variables are enough for a scatter plot.</strong> There is no required size, color, or shape variable.</p>
<p><strong>Next:</strong> keep these two axes and add an optional visual channel. A visible association alone does not establish causation.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/scatter-price-weight.png" alt="Two-variable scatter plot of Price versus Weight with equal-size circles" />
</div>





    </div>

    <!-- SLIDE 28: 27 — Scatter Plot — Size Is an Optional Third Encoding -->
    <div class="slide" data-slide="28">
      <span class="slide-badge">Distributions and paired measurements</span>
      <h2>27 &mdash; Scatter Plot &mdash; Size Is an Optional Third Encoding</h2>
<div class="slide-text-large">
<p>This is the second original example. <strong>The axes are still WEIGHT and PRICE.</strong> Marker size now distinguishes <strong>CLARITY</strong>, as shown by the size legend.</p>
<p><strong>Compare with the previous slide:</strong> what information was added, and what became harder to see when large circles overlap? Remove the size encoding and the two-variable scatter plot still works.</p>
<p>CLARITY is an ordered grade, not a quantity with meaningful ratios: a circle twice as large does <strong>not</strong> mean “twice as clear.” Size, color, or shape should be added only when the extra variable helps answer the question, and its meaning must be explained.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/original-scatter.png" alt="The same Price versus Weight scatter plot with an optional Clarity size legend" />
</div>





    </div>

    <!-- SLIDE 29: 28 — Line Chart — Order and Elapsed Time Matter -->
    <div class="slide" data-slide="29">
      <span class="slide-badge">Read change through time</span>
      <h2>28 &mdash; Line Chart &mdash; Order and Elapsed Time Matter</h2>
<div class="slide-text-large">
<p>A line connects observations in a meaningful order. Its slope is interpretable only when horizontal spacing represents the intended intervals.</p>
<p>Use direct labels or a clear legend for multiple series. Do not imply observations between measured points that the data do not support.</p>
<p><strong>Ask:</strong> What does a line segment mean between two consecutive weeks?</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/line-order.svg" alt="Line Graph: Meaningful Order and Elapsed Time" />
</div>





    </div>

    <!-- SLIDE 30: 29 — Real Case — Fox News Compresses Unequal Time Intervals -->
    <div class="slide" data-slide="30">
      <span class="slide-badge">Read change through time</span>
      <h2>29 &mdash; Real Case &mdash; Fox News Compresses Unequal Time Intervals</h2>
<div class="slide-text-large">
<p>Compare the three time intervals: <strong>9 months, 6 months, and 15 months</strong>. They should not occupy similar horizontal distances on an elapsed-time axis.</p>
<p>The broadcast’s straight-looking path does not faithfully show these intervals. Inspect its numerical spacing as well as its labels. This is a historical design critique, not current labor-market analysis.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/old-unequal-time.png" alt="Bad Example: Unequal Time, Equal Space" />
</div>




<p class="caption-text"><em>Graphic publisher: Fox News, <i>America’s Newsroom</i>, June 30, 2010. <a href="https://www.mediamatters.org/fox-news/updated-worst-chart-ive-seen-all-day">Public archival capture</a>: Media Matters, Jocelyn Fong (see UPDATE2).</em></p>
    </div>

    <!-- SLIDE 31: 30 — Redesign — Put the Four Observations at Their Dates -->
    <div class="slide" data-slide="31">
      <span class="slide-badge">Read change through time</span>
      <h2>30 &mdash; Redesign &mdash; Put the Four Observations at Their Dates</h2>
<div class="slide-text-large">
<p>Place the same four labeled observations at their actual dates and use a consistent vertical scale.</p>
<p>The two middle observations are much closer in time than the final pair. Connecting only these four points still omits what happened between them.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/time-corrected.svg" alt="Redesign: Put Time Back on the Axis" />
</div>




<p class="caption-text"><em>Data: rounded numbers shown in the <a href="https://www.mediamatters.org/fox-news/updated-worst-chart-ive-seen-all-day">June 2010 Fox News graphic</a>. Newly plotted for the spacing comparison; not a newly verified or updated BLS series.</em></p>
    </div>

    <!-- SLIDE 32: 31 — Interactive — Equal Labels Versus Elapsed Days -->
    <div class="slide" data-slide="32">
      <span class="slide-badge">Read change through time</span>
      <h2>31 &mdash; Interactive &mdash; Equal Labels Versus Elapsed Days</h2>
<div class="slide-text-large">
<p>These are <strong>constructed</strong> values observed on days 1, 2, 11, and 31—not reconstructed news data. Each observation increases by 10 units.</p>
<p>Switch the spacing and compare the slopes. A 10-unit change in one day is not the same rate as a 10-unit change over twenty days.</p>
<p><a href="../../assets/week-5/time-spacing.html" target="_blank" rel="noopener">Open this experiment by itself</a>.</p>
</div>


<div class="activity-container-full">
  <iframe src="../../assets/week-5/time-spacing.html" title="Interactive: Equal Labels Versus Elapsed Days" loading="lazy" onload="resizeIframe(this)" sandbox="allow-scripts allow-same-origin"></iframe>
</div>
<p style="text-align: center; margin-top: 0.5rem; font-size: 0.95rem;">
  <a href="../../assets/week-5/time-spacing.html" target="_blank" rel="noopener">Open this activity on its own</a>
</p>



    </div>

    <!-- SLIDE 33: 32 — Real Case — An 8.6% Label Plotted near 9.0% -->
    <div class="slide" data-slide="33">
      <span class="slide-badge">Read change through time</span>
      <h2>32 &mdash; Real Case &mdash; An 8.6% Label Plotted near 9.0%</h2>
<div class="slide-text-large">
<p>The last point is labeled <strong>8.6%</strong>, but appears near <strong>9.0%</strong> and above the earlier <strong>8.8%</strong> point.</p>
<p><strong>Diagnose:</strong> Read the scale and point positions before accepting the apparent trend. Adding a correct text label does not repair an incorrectly positioned mark.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/old-misplaced-point.png" alt="Bad Example: Labels Cannot Rescue Bad Geometry" />
</div>




<p class="caption-text"><em>Graphic publisher: Fox News, December 12, 2011. <a href="https://www.mediamatters.org/fox-news/today-dishonest-fox-news-charts">Public archival capture</a>: Media Matters, Zachary Pleat.</em></p>
    </div>

    <!-- SLIDE 34: 33 — Redesign — Make the Point Positions Match the Labels -->
    <div class="slide" data-slide="34">
      <span class="slide-badge">Read change through time</span>
      <h2>33 &mdash; Redesign &mdash; Make the Point Positions Match the Labels</h2>
<div class="slide-text-large">
<p>Use one consistent scale and place every point at the value in its label. November now appears below March and October.</p>
<p>This redraw uses the broadcast’s displayed values to test its geometry, not a replacement official statistical series.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/point-corrected.svg" alt="Correct the Point Positions" />
</div>




<p class="caption-text"><em>Data: labels in the <a href="https://www.mediamatters.org/fox-news/today-dishonest-fox-news-charts">Fox News graphic of December 12, 2011</a>.</em></p>
    </div>

    <!-- SLIDE 35: 34 — Category Dot Plot — One Summary per Category -->
    <div class="slide" data-slide="35">
      <span class="slide-badge">Specialized comparisons: dots, lollipops and slopes</span>
      <h2>34 &mdash; Category Dot Plot &mdash; One Summary per Category</h2>
<div class="slide-text-large">
<p>Each row is a team. Each dot locates <strong>one team’s percentage</strong> on a shared numerical scale. More dots are not required to make it a dot plot; the useful comparison is among the category values.</p>
<p>This introductory example starts at <strong>zero</strong>. Unlike a bar, a standalone dot encodes <strong>position</strong>, not length from a baseline. A clearly labeled nonzero range can be appropriate when the purpose is to compare small differences. The next page shows the effect explicitly.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/near-equal-dots.svg" alt="Eight team percentages on a zero-to-100 scale" />
</div>




<p class="caption-text"><em>Category dot plots and nonzero quantitative scales: Stephen Few, <a href="https://www.perceptualedge.com/articles/misc/Graph_Selection_Matrix.pdf">Graph Selection Matrix</a>, Ranking and Nominal Comparison rows. Values shown here are illustrative.</em></p>
    </div>

    <!-- SLIDE 36: 35 — Bar versus Dot Plot — Compare the Same Data Side by Side -->
    <div class="slide" data-slide="36">
      <span class="slide-badge">Specialized comparisons: dots, lollipops and slopes</span>
      <h2>35 &mdash; Bar versus Dot Plot &mdash; Compare the Same Data Side by Side</h2>
<div class="slide-text-large">
<p>Both charts show the <strong>same teams, values, order, and units</strong>. Start with identical 0–100% axes. Then try the clearly labeled dot-only zoom.</p>
<p><strong>Distinguish:</strong> A narrower dot-plot scale emphasizes small differences; it does not make those differences larger in the data. Do not use the same zoom to turn the bars into misleading truncated lengths.</p>
</div>


<div class="activity-container-full">
  <iframe src="../../assets/week-5/bar-dot-comparison.html" title="Compare bar and dot encodings on identical data" loading="lazy" onload="resizeIframe(this)" sandbox="allow-scripts allow-same-origin"></iframe>
</div>
<p style="text-align: center; margin-top: 0.5rem; font-size: 0.95rem;">
  <a href="../../assets/week-5/bar-dot-comparison.html" target="_blank" rel="noopener">Open this activity on its own</a>
</p>



    </div>

    <!-- SLIDE 37: 36 — Lollipop Chart — A Dot with a Stem -->
    <div class="slide" data-slide="37">
      <span class="slide-badge">Specialized comparisons: dots, lollipops and slopes</span>
      <h2>36 &mdash; Lollipop Chart &mdash; A Dot with a Stem</h2>
<div class="slide-text-large">
<p>A lollipop combines a thin stem with a dot at its endpoint. It can reduce the visual mass of bars while retaining a clear ending position.</p>
<p>Read the <strong>center</strong> of the dot, not the outer edge. A large marker can make the endpoint appear to extend beyond a target.</p>
<p>Because the stem represents length, a lollipop does not automatically solve the baseline problem. When only position is needed, remove the stem and use a dot plot.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/lollipop.svg" alt="Lollipop Chart" />
</div>





    </div>

    <!-- SLIDE 38: 37 — Lollipop Pitfall — The Center Is the Value -->
    <div class="slide" data-slide="38">
      <span class="slide-badge">Specialized comparisons: dots, lollipops and slopes</span>
      <h2>37 &mdash; Lollipop Pitfall &mdash; The Center Is the Value</h2>
<div class="slide-text-large">
<p>The center of a lollipop endpoint encodes its value. A large marker can extend beyond a threshold even when its center does not.</p>
<p>Use modest, consistent marker sizes. Do not accidentally turn endpoint area into a second, unexplained quantity.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/marker-threshold.svg" alt="Lollipop Pitfall: Read the Center, Not the Edge" />
</div>





    </div>

    <!-- SLIDE 39: 38 — Slopegraph / Slope Plot — Compare Two States -->
    <div class="slide" data-slide="39">
      <span class="slide-badge">Specialized comparisons: dots, lollipops and slopes</span>
      <h2>38 &mdash; Slopegraph / Slope Plot &mdash; Compare Two States</h2>
<div class="slide-text-large">
<p>A slopegraph uses position to compare values or ranks at two endpoints. Direction shows increase or decrease; endpoint positions reveal relative standing.</p>
<p>Direct labels often work better than a long legend. Keep scales consistent, and state whether values are counts, percentages, or ranks.</p>
<p><strong>Caution:</strong> connecting two endpoints does not show what happened between them. Do not substitute a slopegraph when the intervening time pattern is essential.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/slopegraph.svg" alt="Slopegraph / Slope Plot" />
</div>





    </div>

    <!-- SLIDE 40: 39 — Slope Plot — Forecast and Observed Values -->
    <div class="slide" data-slide="40">
      <span class="slide-badge">Specialized comparisons: dots, lollipops and slopes</span>
      <h2>39 &mdash; Slope Plot &mdash; Forecast and Observed Values</h2>
<div class="slide-text-large">
<p>A slope plot can compare two conditions, not only “before” and “after.” Here, the endpoints compare a forecast with its observed outcome, in the same units.</p>
<div class="alert-teaching-point"><strong>Read:</strong> Which estimate was too high? Which was too low? Crossing lines do not automatically make a graph wrong, but label collisions may make it unreadable.</div>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/forecast-slope.svg" alt="Slope Plot: Forecast Versus Observed" />
</div>





    </div>

    <!-- SLIDE 41: 40 — Sparkline / Sparkbar — Trends in a Small Space -->
    <div class="slide" data-slide="41">
      <span class="slide-badge">Specialized comparisons: dots, lollipops and slopes</span>
      <h2>40 &mdash; Sparkline / Sparkbar &mdash; Trends in a Small Space</h2>
<div class="slide-text-large">
<p>A sparkline is a compact line graphic placed alongside text or a number; a sparkbar uses small bars. Their role is to add a pattern without consuming a large chart area.</p>
<p>Small trend graphics can sit beside a numerical value, a table row, or a short explanation. Surrounding words, dates, endpoints, or ranges supply essential context.</p>
<p><strong>Read these constructed rows:</strong> which series is rising, which is falling, and which has the largest count? Do not compare heights across independently scaled rows.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/sparklines.svg" alt="Sparkline / Sparkbar" />
</div>





    </div>

    <!-- SLIDE 42: 41 — Scale Experiment — One Shared Axis versus Two Axes -->
    <div class="slide" data-slide="42">
      <span class="slide-badge">Specialized comparisons: dots, lollipops and slopes</span>
      <h2>41 &mdash; Scale Experiment &mdash; One Shared Axis versus Two Axes</h2>
<div class="slide-text-large">
<p>This activity uses a <strong>bar series and a line series in the same chart</strong>, then changes only the axis design.</p>
<p><a href="../../assets/week-5/shared-dual-axes.html" target="_blank" rel="noopener">Open the axis comparison on its own</a>.</p>
<p><strong>Left:</strong> the bars (monthly requests) and line (success rate) are forced onto one shared y-axis. Because the units differ, the percentage line is compressed near the bottom.</p>
<p><strong>Right:</strong> the bars use the <strong>left axis</strong> and the line uses the <strong>right axis</strong>. Both patterns become visible, but moving the right-axis maximum makes the line look steeper or flatter even though its values do not change.</p>
<p><strong>Teaching point:</strong> a dual-axis chart can make unlike units readable together, but it can also manufacture a visual relationship. Read both axes before comparing slopes or heights.</p>
</div>


<div class="activity-container-full">
  <iframe src="../../assets/week-5/shared-dual-axes.html" title="Compare a bar and line on one shared axis versus separate left and right axes" loading="lazy" onload="resizeIframe(this)" sandbox="allow-scripts allow-same-origin"></iframe>
</div>
<p style="text-align: center; margin-top: 0.5rem; font-size: 0.95rem;">
  <a href="../../assets/week-5/shared-dual-axes.html" target="_blank" rel="noopener">Open this activity on its own</a>
</p>



    </div>

    <!-- SLIDE 43: 42 — Pie Chart — Verify the Whole before Drawing Sectors -->
    <div class="slide" data-slide="43">
      <span class="slide-badge">Show parts of a whole and relative size</span>
      <h2>42 &mdash; Pie Chart &mdash; Verify the Whole before Drawing Sectors</h2>
<div class="slide-text-large">
<p>A pie uses sectors to represent parts of one whole. Before drawing it, ask whether categories are mutually exclusive, collectively meaningful, and sum to the stated whole.</p>
<p>Shaffer’s reading recommends bars for comparison and 100% stacked bars for part-to-whole, and advises against pie charts. For this lecture, compare that recommendation with the specific reading task: close values, many categories, and precise ranking are especially difficult in a pie.</p>
<p>Compare the same illustrative proportions as a simple pie and a bar chart.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/pie-vs-bar.svg" alt="Pie Chart: First Verify the Whole" />
</div>





    </div>

    <!-- SLIDE 44: 43 — Real Case — A Broadcast Pie Adds to 193% -->
    <div class="slide" data-slide="44">
      <span class="slide-badge">Show parts of a whole and relative size</span>
      <h2>43 &mdash; Real Case &mdash; A Broadcast Pie Adds to 193%</h2>
<div class="slide-text-large">
<p><strong>Diagnose the chart, not the politics:</strong> 70 + 63 + 60 = 193. These are separate favorable ratings, not mutually exclusive pieces of one vote. A person can hold a favorable opinion of more than one person.</p>
<p>The original graphic also labels the results as “backing” candidates. That is not the same question as favorability.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/fox-chicago-193.png" alt="Fox Chicago graphic showing Palin 70%, Huckabee 63%, Romney 60% in one pie" />
</div>




<p class="caption-text"><em>Graphic publisher: Fox Chicago, November 2009. Public archival reproduction: <a href="https://flowingdata.com/2009/11/26/fox-news-makes-the-best-pie-chart-ever/">Nathan Yau / FlowingData</a>; contemporary report and poll explanation: <a href="https://archive.thinkprogress.org/foxs-fuzzy-math-193-percent-of-the-public-support-palin-huckabee-and-romney-6b5293868b6f/">Ben Armbruster / ThinkProgress</a>. Historical chart critique, not current polling.</em></p>
    </div>

    <!-- SLIDE 45: 44 — Redesign — Keep Each Rating’s Denominator -->
    <div class="slide" data-slide="45">
      <span class="slide-badge">Show parts of a whole and relative size</span>
      <h2>44 &mdash; Redesign &mdash; Keep Each Rating’s Denominator</h2>
<div class="slide-text-large">
<p>Use separate bars and name the measure <strong>favorable opinion</strong>. The total across bars need not be 100% because the groups overlap.</p>
<p>Do not divide each number by 193 just to make a pie fit: that would change the meaning from percentage of respondents to share of all favorable responses to these three names.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/favorability-bars.svg" alt="The historical favorability percentages redrawn as three separate bars" />
</div>




<p class="caption-text"><em>Data: the displayed percentages and survey interpretation in the <a href="https://archive.thinkprogress.org/foxs-fuzzy-math-193-percent-of-the-public-support-palin-huckabee-and-romney-6b5293868b6f/">November 2009 report</a>. New teaching redraw; the original survey microdata were not obtained.</em></p>
    </div>

    <!-- SLIDE 46: 45 — Real Case — A Pie Distorted beyond Recognition -->
    <div class="slide" data-slide="46">
      <span class="slide-badge">Show parts of a whole and relative size</span>
      <h2>45 &mdash; Real Case &mdash; A Pie Distorted beyond Recognition</h2>
<div class="slide-text-large">
<p>The labels report 42%, 29%, 19%, 8%, and 2%. Before reading those numbers, can you judge the ranking or estimate the differences from the shapes?</p>
<p>Perspective, texture, and decorative ovals compete with the sectors. Having correct numeric labels does not make distorted visual geometry useful.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/razorfish-pie.jpg" alt="Published Razorfish pie graphic with multiple-axis perspective, texture and distorted sectors" />
</div>




<p class="caption-text"><em>Graphic publisher identified as Razorfish, reporting frequency of sharing recommendations online. Public reproduction and contemporaneous analysis: Robert Kosara, <a href="https://eagereyes.org/blog/2010/march-chart-madness#the-worst-pie-chart-ever">“The Worst Pie Chart Ever,” March Chart Madness</a> (2010), tracing the find to Glen Turpin. The underlying survey was not independently verified.</em></p>
    </div>

    <!-- SLIDE 47: 46 — Redesign — Let the Same Labels Become Comparable Lengths -->
    <div class="slide" data-slide="47">
      <span class="slide-badge">Show parts of a whole and relative size</span>
      <h2>46 &mdash; Redesign &mdash; Let the Same Labels Become Comparable Lengths</h2>
<div class="slide-text-large">
<p>The bars use the <strong>same displayed percentages</strong>. Ranking and differences are now visible on one baseline.</p>
<p><strong>Task change:</strong> ranking is easier here, while the pie’s intended part-to-whole framing is less visually prominent. Choose the encoding for the question, not only for appearance.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/sharing-bars.svg" alt="The five percentages from the Razorfish graphic as ranked horizontal bars" />
</div>




<p class="caption-text"><em>Data transcribed from the graphic reproduced in <a href="https://eagereyes.org/blog/2010/march-chart-madness">Kosara’s 2010 critique</a>. New teaching redraw, not a new survey.</em></p>
    </div>

    <!-- SLIDE 48: 47 — Many Categories — Small Pie Sectors Are Hard to Rank -->
    <div class="slide" data-slide="48">
      <span class="slide-badge">Show parts of a whole and relative size</span>
      <h2>47 &mdash; Many Categories &mdash; Small Pie Sectors Are Hard to Rank</h2>
<div class="slide-text-large">
<p>A crowded pie makes ranking and small differences difficult to judge. Moving the values to a legend adds repeated visual searching.</p>
<p><strong>Ask:</strong> Can you reliably rank the middle-sized suppliers without reading every percentage?</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/many-slices.svg" alt="Bad Pie: Too Many Categories" />
</div>





    </div>

    <!-- SLIDE 49: 48 — Use Ranked Bars when the Question Is Ranking -->
    <div class="slide" data-slide="49">
      <span class="slide-badge">Show parts of a whole and relative size</span>
      <h2>48 &mdash; Use Ranked Bars when the Question Is Ranking</h2>
<div class="slide-text-large">
<p>The same shares are aligned to one scale and ordered from largest to smallest.</p>
<p>Pie charts can work for a few clearly different parts of a meaningful whole. Use bars when precise comparisons, many categories, or ranking are central to the question.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/many-bars.svg" alt="A Sorted Bar Chart Makes the Ranking Explicit" />
</div>





    </div>

    <!-- SLIDE 50: 49 — GIF — Salvaging the Pie -->
    <div class="slide" data-slide="50">
      <span class="slide-badge">Show parts of a whole and relative size</span>
      <h2>49 &mdash; GIF &mdash; Salvaging the Pie</h2>
<div class="slide-text-large">
<p>Watch the changes to depth, labels, color, and chart type. Identify the point at which the comparison becomes easier.</p>
<p>A clean design is not simply a less decorated design: the encoding itself may need to change.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/darkhorse-pie.gif" alt="GIF: Salvaging the Pie" />
</div>




<p class="caption-text"><em>Animation: Joey Cherdarchuk / Darkhorse, <a href="https://darkhorsevisualization.com/blog/salvaging-the-pie">Salvaging the Pie</a> (2014).</em></p>
    </div>

    <!-- SLIDE 51: 50 — Treemap — Nested Areas for Hierarchy and Composition -->
    <div class="slide" data-slide="51">
      <span class="slide-badge">Show parts of a whole and relative size</span>
      <h2>50 &mdash; Treemap &mdash; Nested Areas for Hierarchy and Composition</h2>
<div class="slide-text-large">
<p>A treemap partitions area into nested rectangles. Area represents magnitude; containment represents hierarchical membership.</p>
<p>Read the constructed example: East contains three categories totaling 60, West two totaling 40. Identify the largest region, then its largest component.</p>
<p><strong>Tradeoff:</strong> treemaps show a large hierarchy compactly, but close rectangle areas are harder to compare than positions on a common scale.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/treemap.svg" alt="Treemap: Hierarchy and Part-to-Whole" />
</div>





    </div>

    <!-- SLIDE 52: 51 — Interactive — Guess the Bubble Area Ratio -->
    <div class="slide" data-slide="52">
      <span class="slide-badge">Show parts of a whole and relative size</span>
      <h2>51 &mdash; Interactive &mdash; Guess the Bubble Area Ratio</h2>
<div class="slide-text-large">
<p><strong>First guess, then measure.</strong> Is circle B twice as large, four times as large, or something else? Enter an area estimate for each pair.</p>
<p>For bubbles to encode a quantity correctly, <strong>area</strong> must be proportional to that quantity: radius is proportional to its square root. Position in a packed-bubble layout may have no numerical meaning.</p>
</div>


<div class="activity-container-full">
  <iframe src="../../assets/week-5/bubble-area-game.html" title="Guess the area ratio and reveal the correct value" loading="lazy" onload="resizeIframe(this)" sandbox="allow-scripts allow-same-origin"></iframe>
</div>
<p style="text-align: center; margin-top: 0.5rem; font-size: 0.95rem;">
  <a href="../../assets/week-5/bubble-area-game.html" target="_blank" rel="noopener">Open this activity on its own</a>
</p>



    </div>

    <!-- SLIDE 53: 52 — Donut and Concentric Displays — What Is Being Compared? -->
    <div class="slide" data-slide="53">
      <span class="slide-badge">Show parts of a whole and relative size</span>
      <h2>52 &mdash; Donut and Concentric Displays &mdash; What Is Being Compared?</h2>
<div class="slide-text-large">
<p>This example includes concentric circles and donuts. Both require care about what is being compared: radius, area, arc, or a proportion of a whole.</p>
<p>A donut is still a sector-based part-to-whole chart. The hole can hold a useful summary, but it does not cure many categories or close-value comparisons.</p>
<p>For concentric rings, the same angle spans different arc lengths at different radii. A reader should not be asked to compare those lengths as if the radii were equal.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/donut.svg" alt="Concentric Circles and Donut Charts" />
</div>





    </div>

    <!-- SLIDE 54: 53 — Bullet Graph — Actual, Target and Qualitative Ranges -->
    <div class="slide" data-slide="54">
      <span class="slide-badge">Targets, schedules and other chart forms</span>
      <h2>53 &mdash; Bullet Graph &mdash; Actual, Target and Qualitative Ranges</h2>
<div class="slide-text-large">
<p>A bullet graph combines an actual value, a comparison or target marker, and contextual ranges on a compact scale.</p>
<div class="alert-teaching-point"><strong>Read:</strong> Which mark shows actual performance? Which shows the target? What do the background bands mean? They must be defined, not merely colored.</div>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/bullet.svg" alt="Bullet Graph: Actual Compared with a Target" />
</div>




<p class="caption-text"><em>Concept reference: Stephen Few, <a href="https://www.perceptualedge.com/articles/misc/Bullet_Graph_Design_Spec.pdf">Bullet Graph Design Specification</a>.</em></p>
    </div>

    <!-- SLIDE 55: 54 — Bullet Graph — Read Whether Lower Is Better -->
    <div class="slide" data-slide="55">
      <span class="slide-badge">Targets, schedules and other chart forms</span>
      <h2>54 &mdash; Bullet Graph &mdash; Read Whether Lower Is Better</h2>
<div class="slide-text-large">
<p>For response time, a shorter wait is desirable. Here, the target is <strong>10 minutes or less</strong>.</p>
<p>Interpret the actual bar and background ranges according to the meaning of the measure. Do not reuse “high = good” colors or labels without checking their logic.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/bullet-response.svg" alt="Bullet Graph: Lower Can Be Better" />
</div>





    </div>

    <!-- SLIDE 56: 55 — Before Normalizing — Name the Denominator -->
    <div class="slide" data-slide="56">
      <span class="slide-badge">Targets, schedules and other chart forms</span>
      <h2>55 &mdash; Before Normalizing &mdash; Name the Denominator</h2>
<div class="slide-text-large">
<p>Return to the pharmacy example: <strong>pharmacy sales divided by total sales</strong> gives the product category’s share of the business. A higher numerator does not guarantee a higher fraction.</p>
<p>For a part-to-whole question, use <strong>the whole</strong> as the denominator. For a target question, use <strong>the target</strong>. These produce different percentages and answer different questions; do not call both simply “performance.”</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/retail-denominator.svg" alt="Kroger pharmacy revenue and share use different denominators in fiscal 2019 and 2020" />
</div>




<p class="caption-text"><em>Data: The Kroger Co., <a href="https://www.sec.gov/Archives/edgar/data/56873/000155837021003706/R10.htm">FY 2020 Form 10-K, Note 1 — Disaggregated Revenues</a>, fiscal 2019 and 2020. New plots of the reported data; displayed in USD billions rather than the filing’s USD millions.</em></p>
    </div>

    <!-- SLIDE 57: 56 — Target Comparison — Normalize Only for the Stated Question -->
    <div class="slide" data-slide="57">
      <span class="slide-badge">Targets, schedules and other chart forms</span>
      <h2>56 &mdash; Target Comparison &mdash; Normalize Only for the Stated Question</h2>
<div class="slide-text-large">
<p>The denominator is now a <strong>target</strong>, rather than the total number of stores. We are asking a different question: how much of the target has each group achieved?</p>
<p>A common raw scale may make the smallest organization’s performance nearly invisible. Separate scales show local variation but weaken direct magnitude comparison.</p>
<p>Normalize actual values to each group’s target when performance against target is the question. Keep raw values available so that normalization does not erase scale.</p>
<p><strong>Read the constructed example:</strong> A has the largest output, while B is the only group above target. Those statements are compatible.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/target-normalization.svg" alt="Redesign Case: Large and Small Targets" />
</div>





    </div>

    <!-- SLIDE 58: 57 — Gantt Chart — Start, Finish and Overlap -->
    <div class="slide" data-slide="58">
      <span class="slide-badge">Targets, schedules and other chart forms</span>
      <h2>57 &mdash; Gantt Chart &mdash; Start, Finish and Overlap</h2>
<div class="slide-text-large">
<p>A Gantt chart uses start position and bar length to show an interval or duration. Tasks can overlap; that overlap can be part of the analysis.</p>
<p>Read the constructed schedule: collection and cleaning overlap, but analysis begins later. The bar is not a magnitude from zero—it extends from a start to an end on a time axis.</p>
<p><strong>Boundary:</strong> this is a lecture example, not an additional required Tableau worksheet.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/gantt.svg" alt="Gantt Chart" />
</div>





    </div>

    <!-- SLIDE 59: 58 — Waterfall Chart — Additions and Deductions -->
    <div class="slide" data-slide="59">
      <span class="slide-badge">Targets, schedules and other chart forms</span>
      <h2>58 &mdash; Waterfall Chart &mdash; Additions and Deductions</h2>
<div class="slide-text-large">
<p>A waterfall explains how successive positive and negative contributions connect a starting total to an ending total. The intermediate bars float between running totals.</p>
<p>Read each delta, check its sign, and verify the final arithmetic. Clearly distinguish starting/ending totals from contributions.</p>
<p><strong>Ask:</strong> Which contribution changes the total most? Would stacked bars communicate the same sequence correctly?</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/waterfall.svg" alt="Waterfall Chart" />
</div>





    </div>

    <!-- SLIDE 60: 59 — Highlight Table and Heat Map — Values plus Color -->
    <div class="slide" data-slide="60">
      <span class="slide-badge">Targets, schedules and other chart forms</span>
      <h2>59 &mdash; Highlight Table and Heat Map &mdash; Values plus Color</h2>
<div class="slide-text-large">
<p>This example uses <strong>highlight table</strong> for a matrix with values and colored cells, and <strong>heat map</strong> for a color-coded matrix emphasizing the pattern.</p>
<p>The numeric labels help exact lookup; the color helps detect clusters. Choose a suitable palette, show its scale, and distinguish missing values from low values.</p>
<p><strong>Terminology clarification:</strong> names vary across software. Identify the actual marks and encoding instead of relying only on the chart-menu label.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/highlight-heat.svg" alt="Highlight Table and Heat Map" />
</div>





    </div>

    <!-- SLIDE 61: 60 — Word Cloud — A Language Overview -->
    <div class="slide" data-slide="61">
      <span class="slide-badge">Targets, schedules and other chart forms</span>
      <h2>60 &mdash; Word Cloud &mdash; A Language Overview</h2>
<div class="slide-text-large">
<p>A word cloud emphasizes repeated terms through <strong>font size</strong>. This richer example contains 46 distinct terms; it illustrates a language overview rather than an exact ranking.</p>
<p><strong>Inspect:</strong> Which topics stand out? Can you reliably tell whether “context” occurs more often than “design”? Word length and layout also affect prominence.</p>
<p>Before interpreting a real corpus, check tokenization, stop words, merged variants, and whose text is included. Use a ranked frequency chart for precise counts. <strong>This example uses illustrative word frequencies, not text collected from students.</strong></p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/word-cloud.svg" alt="Illustrative word cloud about visual analytics" />
</div>





    </div>

    <!-- SLIDE 62: 61 — Clock and Radial Graphs — A Research Example -->
    <div class="slide" data-slide="62">
      <span class="slide-badge">Targets, schedules and other chart forms</span>
      <h2>61 &mdash; Clock and Radial Graphs &mdash; A Research Example</h2>
<div class="slide-text-large">
<p>Clock graphs can arrange time or direction around a circle. The original research example below is a related <strong>radar chart</strong>, with a different variable on each spoke—not an hourly cycle.</p>
<p><strong>How to read it:</strong> Choose one spoke, read its scale, then compare the four colored profiles. The legend identifies household, population, employment, and average-road-density measures. The values can be negative; the center is not an ordinary zero baseline.</p>
<p><strong>Ask:</strong> Which relationships differ across the profiles? Reordering the spokes changes the polygon shapes, so do not interpret the enclosed area as a total.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/road-network-radar.png" alt="Road-network research radar chart: correlations with socioeconomic variables" />
</div>




<p class="caption-text"><em>Figure 9 (network-index correlations, Atlanta) from Wei, X., &amp; Yao, X. A. (2014). <a href="https://doi.org/10.1111/gean.12064">The Random Walk Value for Ranking Spatial Characteristics in Road Networks</a>. <em>Geographical Analysis, 46</em>(4), 411–434. DOI: 10.1111/gean.12064.</em></p>
    </div>

    <!-- SLIDE 63: 62 — Sankey Diagram — Follow the Flow between Categories -->
    <div class="slide" data-slide="63">
      <span class="slide-badge">Targets, schedules and other chart forms</span>
      <h2>62 &mdash; Sankey Diagram &mdash; Follow the Flow between Categories</h2>
<div class="slide-text-large">
<p>A Sankey diagram connects quantities across stages. Link widths encode flow, and the relevant balance should reconcile.</p>
<p>In this illustration, 100 units of supply split into 60 units of useful energy and 40 units of losses. Separate pies would not show the connection as directly.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/energy-flow.svg" alt="Sankey: Trace Flow, Not Just Separate Totals" />
</div>




<p class="caption-text"><em>Public real-data example: <a href="https://www.iea.org/data-and-statistics/data-tools/energy-sankey">International Energy Agency — Energy Sankey</a>.</em></p>
    </div>

    <!-- SLIDE 64: 63 — Apply Both Readings before the Final Case -->
    <div class="slide" data-slide="64">
      <span class="slide-badge">Apply the readings: one integrated case</span>
      <h2>63 &mdash; Apply Both Readings before the Final Case</h2>
<div class="slide-text-large">
<p>Use the readings for two different decisions:</p>
<p>This four-step sequence is our classroom synthesis—not a verbatim list from either reading. Next, test it on a real graphic that combines several relationships.</p>
</div>




<div style="overflow-x: auto; margin: 1.2rem 0;">
  <table style="width: 100%; border-collapse: collapse; font-size: 0.95rem; line-height: 1.5; border: 1px solid #d0d7de; border-radius: 6px;">
    <thead>
      <tr style="background-color: #f6f8fa; border-bottom: 2px solid #d0d7de;">
        <th style="padding: 0.75rem 1rem; text-align: left; font-weight: 600; color: #1f2328;">Step</th>
        <th style="padding: 0.75rem 1rem; text-align: left; font-weight: 600; color: #1f2328;">Decision</th>
        <th style="padding: 0.75rem 1rem; text-align: left; font-weight: 600; color: #1f2328;">Basis</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border-bottom: 1px solid #d0d7de;">
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;"><strong>1. Relationship</strong></td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">Time series, ranking, distribution, correlation, or another featured relationship?</td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">Few’s matrix</td>
      </tr>
      <tr style="border-bottom: 1px solid #d0d7de;" style="background-color: #fafbfc;">
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;"><strong>2. Encoding</strong></td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">Which values must be compared by point position, line, bar length, or box?</td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">Few’s matrix</td>
      </tr>
      <tr style="border-bottom: 1px solid #d0d7de;">
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;"><strong>3. Cleanup</strong></td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">Can labels, order, grids, borders, and depth be improved without changing values?</td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">Shaffer’s examples</td>
      </tr>
      <tr style="border-bottom: 1px solid #d0d7de;" style="background-color: #fafbfc;">
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;"><strong>4. Context</strong></td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">Are units, reference, title, date and source still available?</td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">Shaffer’s examples</td>
      </tr>
    </tbody>
  </table>
</div>

<p class="caption-text"><em>Readings: Stephen Few, <a href="https://www.perceptualedge.com/articles/misc/Graph_Selection_Matrix.pdf">Graph Selection Matrix</a>; Jeffrey A. Shaffer, <a href="https://dataplusscience.com/files/Shaffer%204C%20-%20Clean%20Examples.pdf">“Clean” Examples</a>.</em></p>
    </div>

    <!-- SLIDE 65: 64 — Final Graph Case — Minard’s Original Graphic -->
    <div class="slide" data-slide="65">
      <span class="slide-badge">Apply the readings: one integrated case</span>
      <h2>64 &mdash; Final Graph Case &mdash; Minard’s Original Graphic</h2>
<div class="slide-text-large">
<p>Read the full graphic before simplifying it. Locate the <strong>route</strong>, <strong>band width</strong>, <strong>direction</strong>, <strong>branches</strong>, and <strong>temperature with dates</strong>.</p>
<div class="alert-teaching-point"><strong>Discuss:</strong> Which encoding answers “where”? Which answers “how many”? How do the temperature labels connect to the return journey? The following video explains the graphic; no separate zoom activity is needed.</div>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/original-minard.png" alt="Charles Joseph Minard’s original 1869 campaign graphic" />
</div>




<p class="caption-text"><em>Graphic: Charles Joseph Minard (1869), <a href="https://commons.wikimedia.org/wiki/File:Minard.png">public-domain original</a>.</em></p>
    </div>

    <!-- SLIDE 66: 65 — Watch — Reading Minard with Numberphile -->
    <div class="slide" data-slide="66">
      <span class="slide-badge">Apply the readings: one integrated case</span>
      <h2>65 &mdash; Watch &mdash; Reading Minard with Numberphile</h2>
<div class="slide-text-large">
<p>James Grime explains how several kinds of information work together in Minard’s graphic. As you watch, identify the encodings rather than trying to memorize every historical detail.</p>
<p><strong>After watching:</strong> What would be lost if we retained only the starting and ending quantities?</p>
</div>



<div class="video-container-large">
  <iframe class="youtube" src="https://www.youtube-nocookie.com/embed/3T7jMcstxY0?rel=0" title="The Greatest Ever Infographic — Numberphile" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>
<div class="media-caption">
  <a href="https://www.youtube.com/watch?v=3T7jMcstxY0" target="_blank" rel="noopener">Watch on YouTube</a>
</div>

<p class="caption-text"><em>Video: Numberphile, <em>The Greatest Ever Infographic</em>, featuring James Grime. The title is the publisher’s appraisal, not an objective ranking of all graphics.</em></p>
    </div>

    <!-- SLIDE 67: 66 — Final Comparison — What Two Endpoints Leave Out -->
    <div class="slide" data-slide="67">
      <span class="slide-badge">Apply the readings: one integrated case</span>
      <h2>66 &mdash; Final Comparison &mdash; What Two Endpoints Leave Out</h2>
<div class="slide-text-large">
<p>These two labeled endpoints make the scale of losses immediately apparent. They remove the route, the divisions and returns of groups, dates, and temperature.</p>
<p>Neither representation wins for every question. Compare a quick count question with a route-specific historical question.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/minard-endpoints.svg" alt="Minard: What a Simpler Chart Leaves Out" />
</div>




<p class="caption-text"><em>Data: two quantities labeled in <a href="https://commons.wikimedia.org/wiki/File:Minard.png">Minard’s 1869 graphic</a>.</em></p>
    </div>

    <!-- SLIDE 68: 67 — From Graphs to Business Intelligence -->
    <div class="slide" data-slide="68">
      <span class="slide-badge">From graphs to Tableau</span>
      <h2>67 &mdash; From Graphs to Business Intelligence</h2>
<div class="slide-text-large">
<p>Business intelligence brings data connection, visual analysis, dashboards, and sharing into a working environment.</p>
<p><strong>Tableau</strong> and <strong>Microsoft Power BI</strong> are two major platforms. Both support building and sharing analytical reports; this course will use Tableau for the next sequence of labs.</p>
<p>The software does not choose the right question or verify a claim for you.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/bi-workflow.svg" alt="From data connection to shared analytical dashboards" />
</div>




<p class="caption-text"><em>Product references: <a href="https://www.tableau.com/why-tableau/what-is-tableau">Tableau</a>; <a href="https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview">Microsoft Power BI</a>.</em></p>
    </div>

    <!-- SLIDE 69: 68 — Tableau Cloud, Desktop and Public Are Different -->
    <div class="slide" data-slide="69">
      <span class="slide-badge">From graphs to Tableau</span>
      <h2>68 &mdash; Tableau Cloud, Desktop and Public Are Different</h2>
<div class="slide-text-large">
<p><strong>Tableau Cloud</strong>, formerly Tableau Online, is the hosted site we will use. <strong>Tableau Desktop</strong> is an installed authoring application. <strong>Tableau Public</strong> is a free platform for learning, sharing, and building a public portfolio.</p>
<p>Public is not a student-only edition, and publishing to Public is not submitting to our course’s Cloud project.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/tableau-products.svg" alt="Three Tableau environments and their different roles" />
</div>




<p class="caption-text"><em>Official product descriptions: <a href="https://www.tableau.com/products/cloud-bi">Cloud</a>, <a href="https://www.tableau.com/products/desktop">Desktop</a>, and <a href="https://www.tableau.com/blog/what-is-tableau-public">Public</a>.</em></p>
    </div>

    <!-- SLIDE 70: 69 — Prep, Server and Next — Other Roles in the Product Family -->
    <div class="slide" data-slide="70">
      <span class="slide-badge">From graphs to Tableau</span>
      <h2>69 &mdash; Prep, Server and Next &mdash; Other Roles in the Product Family</h2>
<div class="slide-text-large">
<p>Product names describe different roles, not interchangeable places to submit an assignment.</p>
</div>




<div style="overflow-x: auto; margin: 1.2rem 0;">
  <table style="width: 100%; border-collapse: collapse; font-size: 0.95rem; line-height: 1.5; border: 1px solid #d0d7de; border-radius: 6px;">
    <thead>
      <tr style="background-color: #f6f8fa; border-bottom: 2px solid #d0d7de;">
        <th style="padding: 0.75rem 1rem; text-align: left; font-weight: 600; color: #1f2328;">Product</th>
        <th style="padding: 0.75rem 1rem; text-align: left; font-weight: 600; color: #1f2328;">Main role</th>
        <th style="padding: 0.75rem 1rem; text-align: left; font-weight: 600; color: #1f2328;">Where it fits in this course</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border-bottom: 1px solid #d0d7de;">
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;"><strong>Tableau Prep</strong></td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">Prepare, combine, and clean data</td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">Data-preparation work comes later</td>
      </tr>
      <tr style="border-bottom: 1px solid #d0d7de;" style="background-color: #fafbfc;">
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;"><strong>Tableau Server</strong></td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">Organization-managed analytics deployment</td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">Not the hosted course site</td>
      </tr>
      <tr style="border-bottom: 1px solid #d0d7de;">
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;"><strong>Tableau Next</strong></td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">Agentic analytics integrated with the Salesforce ecosystem</td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">Context only; not required for this lab</td>
      </tr>
    </tbody>
  </table>
</div>

<p class="caption-text"><em>Official references: <a href="https://www.tableau.com/products/tableau">Tableau platform</a>; <a href="https://www.tableau.com/products/prep">Tableau Prep</a>; <a href="https://www.tableau.com/blog/what-is-tableau-einstein">Tableau Next</a>.</em></p>
    </div>

    <!-- SLIDE 71: 70 — What Can Students Use for Free? -->
    <div class="slide" data-slide="71">
      <span class="slide-badge">From graphs to Tableau</span>
      <h2>70 &mdash; What Can Students Use for Free?</h2>
<div class="slide-text-large">
<div class="alert-takeaway"><strong>Edition names matter:</strong> Tableau also offers a <strong>Desktop Free Edition</strong> for local analysis. It is distinct from Public Edition and from licensed Professional Edition. Do not assume that every free desktop edition can publish to Cloud.</div>
<p>No software purchase or Desktop installation is required for this week’s browser lab.</p>
</div>




<div style="overflow-x: auto; margin: 1.2rem 0;">
  <table style="width: 100%; border-collapse: collapse; font-size: 0.95rem; line-height: 1.5; border: 1px solid #d0d7de; border-radius: 6px;">
    <thead>
      <tr style="background-color: #f6f8fa; border-bottom: 2px solid #d0d7de;">
        <th style="padding: 0.75rem 1rem; text-align: left; font-weight: 600; color: #1f2328;">Route</th>
        <th style="padding: 0.75rem 1rem; text-align: left; font-weight: 600; color: #1f2328;">What it provides</th>
        <th style="padding: 0.75rem 1rem; text-align: left; font-weight: 600; color: #1f2328;">What to remember</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border-bottom: 1px solid #d0d7de;">
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;"><strong>Individual learning: Tableau Desktop Public Edition</strong></td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">Free software for learning and publishing to Tableau Public</td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">Not student-only. It cannot publish to our Tableau Cloud course project.</td>
      </tr>
      <tr style="border-bottom: 1px solid #d0d7de;" style="background-color: #fafbfc;">
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;"><strong>Instructor-requested Student Course License</strong></td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">Tableau Desktop and Prep Builder for the course period</td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">Requested by the instructor, not a guaranteed personal full-license entitlement.</td>
      </tr>
      <tr style="border-bottom: 1px solid #d0d7de;">
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;"><strong>Instructor-provided Tableau Cloud site</strong></td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">Browser-based authoring and sharing in the course environment</td>
        <td style="padding: 0.75rem 1rem; color: #24292f; vertical-align: top;">This is our starting point; use the invitation and assigned project.</td>
      </tr>
    </tbody>
  </table>
</div>

<p class="caption-text"><em>Current official references, checked September 15, 2026: <a href="https://www.tableau.com/academic/students">Tableau for Students</a>; <a href="https://www.tableau.com/academic/teaching">Tableau for Teaching</a>; <a href="https://help.tableau.com/current/pro/desktop/en-us/desktop_comparison.htm">Desktop edition comparison</a>.</em></p>
    </div>

    <!-- SLIDE 72: 71 — In Class — Accept Your Tableau Invitation -->
    <div class="slide" data-slide="72">
      <span class="slide-badge">From graphs to Tableau</span>
      <h2>71 &mdash; In Class &mdash; Accept Your Tableau Invitation</h2>
<div class="slide-text-large">
<p>We will set up the course account together before beginning the browser lab.</p>
<p>Open the Tableau invitation in your <strong>JMU email account</strong> and click <strong>Sign In</strong>.</p>
<p>If Tableau asks you to create an account, use your <strong>James Madison University email address</strong> so the Tableau account matches the invitation. If you already have a Tableau account under that JMU email, sign in to it.</p>
<p><strong>Do not create a second account with another email address just to get around an access problem.</strong></p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/screenshots/Screenshot%202026-09-17%20200100.png" alt="Tableau invitation sent to the JMU email account" />
</div>





    </div>

    <!-- SLIDE 73: 72 — In Class — Choose One-Time Password Generator -->
    <div class="slide" data-slide="73">
      <span class="slide-badge">From graphs to Tableau</span>
      <h2>72 &mdash; In Class &mdash; Choose One-Time Password Generator</h2>
<div class="slide-text-large">
<p>When Tableau asks you to <strong>Register a Verification Method</strong>, choose the bottom option:</p>
<p><strong>One-Time Password Generator</strong></p>
<p>For this course setup, <strong>do not choose Salesforce Authenticator, Security Key, or Built-In Authenticator</strong>.</p>
<p>On the next screen, Tableau will show a QR code. Scan the QR code shown on <strong>your own screen</strong> with an authenticator app, then enter the generated code. The instructor recommends <strong>Okta Verify</strong>, which JMU already uses.</p>
<div class="alert-takeaway"><strong>Security:</strong> the QR setup code and verification codes are private. Do not photograph, share, or post them. The course materials intentionally do not reproduce the live QR code.</div>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/screenshots/Screenshot%202026-09-17%20201840.png" alt="Tableau verification-method screen with One-Time Password Generator as the bottom option" />
</div>





    </div>

    <!-- SLIDE 74: 73 — In Class — Enter the `fall2026` Course Project -->
    <div class="slide" data-slide="74">
      <span class="slide-badge">From graphs to Tableau</span>
      <h2>73 &mdash; In Class &mdash; Enter the `fall2026` Course Project</h2>
<div class="slide-text-large">
<p>After account setup, choose <strong>Explore</strong> and open <strong><code>fall2026</code></strong>.</p>
<p>In Tableau terminology, <code>fall2026</code> is a <strong>project</strong>. For this course, think of it as the shared class folder.</p>
<p><strong>For Lab 5, create everything inside <code>fall2026</code>:</strong> the published data source, workbook, worksheets, and dashboard. Do <strong>not</strong> work in Personal Space for this assignment.</p>
<p><strong>Next:</strong> <a href="../../assignments/lab-5/">Open Lab 5</a> for the complete screenshot-based workflow, three worksheets, one interactive dashboard, and the Lab 5 rubric.</p>
</div>
<div class="slide-visual-full">
  <img src="../../assets/week-5/screenshots/Screenshot%202026-09-18%20103626.png" alt="Tableau Explore view showing the fall2026 course project" />
</div>





    </div>

    <!-- SLIDE 75: 74 — Watch — What Is Tableau? | Salesforce -->
    <div class="slide" data-slide="75">
      <span class="slide-badge">From graphs to Tableau</span>
      <h2>74 &mdash; Watch &mdash; What Is Tableau? | Salesforce</h2>
<div class="slide-text-large">
<p>Watch the <strong>official Salesforce overview of Tableau</strong>. Connect the chart choices in this lecture with a visual analytics workflow: bring in data, explore it, and communicate the result.</p>
<div class="alert-teaching-point"><strong>Watch for:</strong> how the tool connects an analytical question to a visual view, and how people use the result. Then use the preceding account/project screens to enter <strong>our course’s Tableau Cloud site</strong>.</div>
</div>



<div class="video-container-large">
  <iframe class="youtube" src="https://www.youtube-nocookie.com/embed/HlKCe_YKlPI?rel=0" title="What is Tableau? | Salesforce" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>
<div class="media-caption">
  <a href="https://www.youtube.com/watch?v=HlKCe_YKlPI" target="_blank" rel="noopener">Watch “What is Tableau? | Salesforce” on YouTube</a>
</div>

<p class="caption-text"><em>Video: Salesforce, <em>What is Tableau?</em> The instructor-selected video is embedded directly from YouTube; internet access is required. It is an introduction, not a substitute for the lab.</em></p>
    </div>
  </div>
</div>

<script>
function resizeIframe(ifr) {
  if (!ifr) return;
  try {
    if (ifr.contentWindow) {
      ifr.contentWindow.postMessage({ type: 'ia342-request-height' }, '*');
    }
  } catch (e) {}
}

window.addEventListener('message', function(e) {
  if (e.data && e.data.type === 'ia342-frame-height' && typeof e.data.height === 'number') {
    var iframes = document.querySelectorAll('.activity-container-full iframe');
    iframes.forEach(function(ifr) {
      if (ifr.contentWindow === e.source) {
        var newH = Math.ceil(e.data.height);
        var curH = parseFloat(ifr.style.height) || 0;
        if (Math.abs(curH - newH) >= 2) {
          ifr.style.height = newH + 'px';
        }
      }
    });
  }
});

var currentSlide = 1;
var totalSlides = 75;

function updateDeck() {
  var slides = document.querySelectorAll('.slide');
  slides.forEach(function(s) {
    s.classList.remove('active');
  });

  var activeEl = document.querySelector('.slide[data-slide="' + currentSlide + '"]');
  if (activeEl) {
    activeEl.classList.add('active');
    var activeIframes = activeEl.querySelectorAll('.activity-container-full iframe');
    activeIframes.forEach(function(ifr) {
      resizeIframe(ifr);
      setTimeout(function() { resizeIframe(ifr); }, 80);
      setTimeout(function() { resizeIframe(ifr); }, 300);
    });
  }

  var counterEl = document.getElementById('slideCounter');
  if (counterEl) {
    counterEl.textContent = 'Slide ' + currentSlide + ' of ' + totalSlides;
  }

  var barEl = document.getElementById('progressBar');
  if (barEl) {
    barEl.style.width = ((currentSlide / totalSlides) * 100) + '%';
  }
  
  var prevBtn = document.getElementById('prevBtn');
  if (prevBtn) {
    prevBtn.disabled = (currentSlide === 1);
  }
  
  var nextBtn = document.getElementById('nextBtn');
  if (nextBtn) {
    nextBtn.disabled = (currentSlide === totalSlides);
  }

  if (window.history && window.history.replaceState) {
    window.history.replaceState(null, null, '#slide-' + currentSlide);
  }
}

function changeSlide(direction) {
  var next = currentSlide + direction;
  if (next >= 1 && next <= totalSlides) {
    currentSlide = next;
    updateDeck();
  }
}

function goToSlide(slideNum) {
  if (slideNum >= 1 && slideNum <= totalSlides) {
    currentSlide = slideNum;
    updateDeck();
  }
}

function toggleFullScreen() {
  var deck = document.getElementById('lectureDeck');
  if (!deck) return;
  if (!document.fullscreenElement && !document.webkitFullscreenElement) {
    if (deck.requestFullscreen) {
      deck.requestFullscreen();
    } else if (deck.webkitRequestFullscreen) {
      deck.webkitRequestFullscreen();
    }
  } else {
    if (document.exitFullscreen) {
      document.exitFullscreen();
    } else if (document.webkitExitFullscreen) {
      document.webkitExitFullscreen();
    }
  }
}

document.addEventListener('keydown', function(event) {
  if (event.target.tagName === 'INPUT' || event.target.tagName === 'TEXTAREA') return;

  if (event.key === 'ArrowRight' || event.key === ' ' || event.key === 'PageDown') {
    event.preventDefault();
    changeSlide(1);
  } else if (event.key === 'ArrowLeft' || event.key === 'PageUp') {
    event.preventDefault();
    changeSlide(-1);
  } else if (event.key === 'Home') {
    event.preventDefault();
    goToSlide(1);
  } else if (event.key === 'End') {
    event.preventDefault();
    goToSlide(totalSlides);
  }
});

window.addEventListener('DOMContentLoaded', function() {
  var hash = window.location.hash;
  if (hash && hash.indexOf('#slide-') === 0) {
    var sNum = parseInt(hash.replace('#slide-', ''), 10);
    if (!isNaN(sNum) && sNum >= 1 && sNum <= totalSlides) {
      currentSlide = sNum;
    }
  }
  updateDeck();
});
</script>

---
[Return to Course Home](../../) | [Go to Lab 5](../../assignments/lab-5/)
