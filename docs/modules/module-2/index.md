---
layout: default
title: "Module 2: Introduction to Data Visualization - IA 342"
---

<style>
/* Presentation Slide Deck Styles */
.deck-container {
  max-width: 1120px;
  margin: 1.5rem auto 3rem;
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
  width: 3.5%;
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
  padding: 2.2rem 2.5rem;
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
  padding: 0.2rem 0.65rem;
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
.slide-layout-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2.2rem;
  align-items: center;
}
.slide-layout-grid.grid-right-wide {
  grid-template-columns: 0.95fr 1.05fr;
}
.slide-layout-single {
  max-width: 880px;
  margin: 0 auto;
}
.slide-body {
  font-size: 1.05rem;
  line-height: 1.6;
  color: #24292f;
}
.slide-body p {
  margin-top: 0;
  margin-bottom: 0.9rem;
}
.slide-body ul, .slide-body ol {
  margin-top: 0.4rem;
  margin-bottom: 0.9rem;
  padding-left: 1.4rem;
}
.slide-body li {
  margin-bottom: 0.35rem;
}
.slide-media-box {
  text-align: center;
  background: #f6f8fa;
  border: 1px solid #d0d7de;
  border-radius: 8px;
  padding: 0.75rem;
  box-shadow: 0 1px 3px rgba(0,0,0,0.03);
}
.slide-media-box img, .slide-media-box svg {
  max-width: 100%;
  max-height: 380px;
  height: auto;
  border-radius: 4px;
  display: block;
  margin: 0 auto;
}
.video-player-container {
  position: relative;
  width: 100%;
  padding-bottom: 56.25%;
  height: 0;
  overflow: hidden;
  border-radius: 8px;
  border: 1px solid #d0d7de;
  background: #000;
  box-shadow: 0 2px 8px rgba(0,0,0,0.12);
}
.video-player-container iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border: 0;
}
.activity-embed-container {
  width: 100%;
  height: 420px;
  border: 1px solid #d0d7de;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  background: #ffffff;
}
.activity-embed-container iframe {
  width: 100%;
  height: 100%;
  border: 0;
  display: block;
}
.alert-takeaway {
  background: #dafbe1;
  border-left: 4px solid #1a7f37;
  padding: 0.8rem 1rem;
  border-radius: 0 6px 6px 0;
  margin-top: 1rem;
  font-size: 0.96rem;
  color: #1a7f37;
  font-weight: 500;
  text-align: left;
}
.alert-teaching-point {
  background: #ddf4ff;
  border-left: 4px solid #0969da;
  padding: 0.8rem 1rem;
  border-radius: 0 6px 6px 0;
  margin-top: 1rem;
  font-size: 0.96rem;
  color: #0969da;
  font-weight: 500;
  text-align: left;
}
:fullscreen .deck-container, :-webkit-full-screen .deck-container {
  max-width: 100vw;
  height: 100vh;
  margin: 0;
  display: flex;
  flex-direction: column;
}
:fullscreen .deck-stage, :-webkit-full-screen .deck-stage {
  flex: 1;
  border-radius: 0;
  overflow-y: auto;
}
@media (max-width: 860px) {
  .slide-layout-grid, .slide-layout-grid.grid-right-wide {
    grid-template-columns: 1fr;
    gap: 1.4rem;
  }
  .deck-stage { min-height: 460px; }
  .slide { padding: 1.5rem 1.2rem; }
}
</style>

<div class="deck-container" id="lectureDeck">
  <div class="deck-nav-bar">
    <div class="deck-title-tag">
      <span>📊 IA 342 Week 2 Lecture</span>
      <span style="opacity: 0.4;">|</span>
      <span id="slideCounter">Slide 1 of 28</span>
    </div>
    <div class="deck-controls">
      <button class="deck-btn" id="prevBtn" onclick="changeSlide(-1)" title="Previous (← / PageUp)">◀ Prev</button>
      <button class="deck-btn" id="nextBtn" onclick="changeSlide(1)" title="Next (→ / Space / PageDown)">Next ▶</button>
      <button class="deck-btn" onclick="toggleFullScreen()" title="Fullscreen Mode">⛶ Fullscreen</button>
    </div>
  </div>
  <div class="deck-progress-track">
    <div class="deck-progress-fill" id="progressBar"></div>
  </div>
  <div class="deck-stage">
    <!-- SLIDE 1: Introduction to Data Visualization -->
    <div class="slide active" data-slide="1">
      
<div style="text-align: center; padding: 2.5rem 1rem;">
  <h1 style="font-size: 2.4rem; margin: 0.5rem 0; color: #0969da;">Introduction to Data Visualization</h1>
  <p style="font-size: 1.25rem; color: #57606a; max-width: 700px; margin: 0 auto 1.5rem;">
    Visualization Methods, Technologies, and Tools for Intelligence Analysis
  </p>
  <div style="max-width: 680px; margin: 0 auto; background: #f6f8fa; border: 1px solid #d0d7de; padding: 1.4rem 1.6rem; border-radius: 8px; text-align: left;">
    <p style="margin: 0; font-size: 1.05rem; line-height: 1.6; color: #24292f;">
      This lecture explains <strong>why visualization helps us understand complex data</strong> and why <strong>human perception</strong> matters when we design charts, maps, and other visual evidence.
    </p>
  </div>
  <div style="margin-top: 2rem;">
    <button class="deck-btn" style="background: #0969da; border-color: #0969da; padding: 0.65rem 1.6rem; font-size: 1.05rem;" onclick="changeSlide(1)">
      Start Presentation ▶
    </button>
  </div>
</div>

    </div>

    <!-- SLIDE 2: 01 — Why Visualization? -->
    <div class="slide" data-slide="2">
      <span class="slide-badge">Foundations</span>
      <h2>01 — Why Visualization?</h2>
      <div class="slide-layout-grid">
        <div class="slide-body">
          
<p>Organizations can collect and store huge amounts of data.</p>
<p>The challenge is not just getting data; it is <strong>turning data into something people can understand, interpret, and use</strong>.</p>
<div class="alert-teaching-point">
  <strong>Key Question:</strong> What can a chart or other visual show us that a table of raw numbers may hide?
</div>

        </div>
        <div>
          
<div class="slide-media-box">
  <img src="../../assets/week-2/visualization-roles.svg" alt="Visualization roles in analysis" />
</div>

        </div>
      </div>
    </div>

    <!-- SLIDE 3: 01A — From Data Overload to Insight -->
    <div class="slide" data-slide="3">
      <span class="slide-badge">Video Briefing</span>
      <h2>01A — From Data Overload to Insight</h2>
      <div class="slide-layout-grid grid-right-wide">
        <div class="slide-body">
          
<p>Digital data can become overwhelming very quickly. Visualization helps turn that complexity into something we can look at and understand.</p>
<p>The main benefit is not just making data look cleaner: a useful visualization makes <strong>comparisons, trends, patterns, and unusual values (anomalies)</strong> easy to see.</p>
<p style="font-size: 0.9em; color: #57606a;">▶ Click Play below to watch the briefing inside the slide:</p>

        </div>
        <div>
          
<div class="video-player-container">
  <iframe src="https://www.youtube-nocookie.com/embed/Xh3p4yKlEQs" title="Why Data Visualization Matters" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
<div style="margin-top: 0.4rem; text-align: center;"><a href="https://www.youtube.com/watch?v=Xh3p4yKlEQs" target="_blank" style="font-size: 0.85em; color: #57606a;">Open on YouTube ↗</a></div>

        </div>
      </div>
    </div>

    <!-- SLIDE 4: 02 — From Data to Decision -->
    <div class="slide" data-slide="4">
      <span class="slide-badge">Analytical Flow</span>
      <h2>02 — From Data to Decision</h2>
      <div class="slide-layout-grid">
        <div class="slide-body">
          
<p><strong>Data → Information → Knowledge → Decision / Strategy</strong></p>
<ul>
  <li><strong>Data:</strong> basic facts, records, and observations.</li>
  <li><strong>Information:</strong> data organized so that it starts to make sense.</li>
  <li><strong>Knowledge:</strong> understanding built from information, experience, and context.</li>
  <li><strong>Decision / Strategy:</strong> using that understanding to choose action.</li>
</ul>
<div class="video-player-container" style="margin-top: 0.6rem;">
  <iframe src="https://www.youtube-nocookie.com/embed/eqcv8KF07nM" title="From Data to Strategy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

        </div>
        <div>
          
<div class="slide-media-box">
  <img src="../../assets/week-2/data-to-decision.svg" alt="Data to Decision flow diagram" />
</div>

        </div>
      </div>
    </div>

    <!-- SLIDE 5: 03 — Numbers Can Look the Same -->
    <div class="slide" data-slide="5">
      <span class="slide-badge">Anscombe's Quartet — Part 1</span>
      <h2>03 — Numbers Can Look the Same</h2>
      <div class="slide-layout-grid">
        <div class="slide-body">
          
<p>Summary statistics can make very different datasets look completely identical.</p>
<p>Consider four datasets with nearly identical:</p>
<ul>
  <li>Means (x̄ = 9.0, ȳ = 7.5),</li>
  <li>Variances (s_x² = 11.0, s_y² = 4.12),</li>
  <li>Correlations (r = 0.816), and</li>
  <li>Linear regression lines (y ≈ 3.0 + 0.5x).</li>
</ul>
<p>If we only look at summary numbers, we assume they are the same.</p>

        </div>
        <div>
          
<div class="slide-media-box">
  <img src="../../assets/week-2/anscombe-summary.svg" alt="Summary statistics for Anscombe Quartet" />
</div>

        </div>
      </div>
    </div>

    <!-- SLIDE 6: 04 — But the Patterns Are Different -->
    <div class="slide" data-slide="6">
      <span class="slide-badge">Anscombe's Quartet — Part 2</span>
      <h2>04 — But the Patterns Are Different</h2>
      <div class="slide-layout-grid">
        <div class="slide-body">
          
<p>When we plot the same datasets, the differences become immediately obvious:</p>
<ul>
  <li><strong>Dataset I:</strong> standard linear relationship.</li>
  <li><strong>Dataset II:</strong> smooth quadratic curve.</li>
  <li><strong>Dataset III:</strong> tight linear cluster + one extreme outlier.</li>
  <li><strong>Dataset IV:</strong> vertical stack + one high outlier.</li>
</ul>
<div class="alert-takeaway">
  <strong>Takeaway:</strong> Before deciding what is important in a dataset, look at it visually.
</div>

        </div>
        <div>
          
<div class="slide-media-box">
  <img src="../../assets/week-2/anscombe-quartet.svg" alt="Anscombe Quartet scatter plots" />
</div>

        </div>
      </div>
    </div>

    <!-- SLIDE 7: 05 — Visualization Helps Us Analyze -->
    <div class="slide" data-slide="7">
      <span class="slide-badge">Core Concept</span>
      <h2>05 — Visualization Helps Us Analyze</h2>
      <div class="slide-layout-grid">
        <div class="slide-body">
          
<p>Visualization is not just decoration, and it is not only for people who call themselves 'visual learners.'</p>
<p>A good visualization helps analysts:</p>
<ul>
  <li>See patterns and relationships</li>
  <li>Find unusual values (anomalies/outliers)</li>
  <li>Compare groups effectively</li>
  <li>Ask better analytical questions</li>
  <li>Explain findings clearly and defensibly</li>
</ul>
<p>In IA 342, visualization is an <strong>integral part of the analysis</strong>.</p>

        </div>
        <div>
          
<div class="slide-media-box">
  <img src="../../assets/week-2/visualization-roles.svg" alt="Visualization roles in analysis" />
</div>

        </div>
      </div>
    </div>

    <!-- SLIDE 8: 06 — What the Eye Notices First -->
    <div class="slide" data-slide="8">
      <span class="slide-badge">Visual Perception</span>
      <h2>06 — What the Eye Notices First</h2>
      <div class="slide-layout-grid">
        <div class="slide-body">
          
<p>Some visual features are noticed <strong>almost immediately</strong> (under 250ms), before we consciously focus on individual objects. These are called <strong>preattentive attributes</strong>.</p>
<ul>
  <li><strong>Color:</strong> Hue (category), Value/Lightness (intensity)</li>
  <li><strong>Form:</strong> Size, Length, Width, Shape, Orientation</li>
  <li><strong>Spatial Position:</strong> 2D coordinate placement</li>
  <li><strong>Movement & Texture:</strong> Motion, density</li>
</ul>
<p>These features rapidly direct attention to what matters most.</p>

        </div>
        <div>
          
<div class="slide-media-box">
  <img src="../../assets/week-2/preattentive-overview.svg" alt="Preattentive attributes overview" />
</div>

        </div>
      </div>
    </div>

    <!-- SLIDE 9: 07 — Find the 7s -->
    <div class="slide" data-slide="9">
      <span class="slide-badge">Perception Experiment</span>
      <h2>07 — Find the 7s</h2>
      <div class="slide-layout-grid">
        <div class="slide-body">
          
<p><strong>Step 1:</strong> Count every <strong>7</strong> in the plain digit field on the left. It requires slow, serial scanning.</p>
<p><strong>Step 2:</strong> Look at the same field on the right with preattentive color emphasis.</p>
<div class="alert-teaching-point">
  <strong>Teaching Point:</strong> The data did not change; only the visual encoding changed. Proper visual hierarchy makes critical signals pop out instantly.
</div>

        </div>
        <div>
          
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.8rem;">
  <div class="slide-media-box">
    <img src="../../assets/week-2/digit-seven-plain.svg" alt="Dense field of digits plain" />
    <span style="font-size: 0.85em; color: #57606a;">Plain (Serial Search)</span>
  </div>
  <div class="slide-media-box">
    <img src="../../assets/week-2/digit-seven-highlighted.svg" alt="Field of digits highlighted" />
    <span style="font-size: 0.85em; color: #0969da; font-weight: 600;">Highlighted (Preattentive)</span>
  </div>
</div>

        </div>
      </div>
    </div>

    <!-- SLIDE 10: 08 — Color: Hue, Lightness, and Context -->
    <div class="slide" data-slide="10">
      <span class="slide-badge">Visual Encoding</span>
      <h2>08 — Color: Hue, Lightness, and Context</h2>
      <div class="slide-layout-grid">
        <div class="slide-body">
          
<p><strong>Hue (type of color):</strong> Best for separating qualitative categories or highlighting anomalies.</p>
<p><strong>Lightness / Value:</strong> Best for ordered or numeric differences (low to high).</p>
<p><strong>Context Warning:</strong> The human visual system judges colors relative to their surrounding background, not in isolation.</p>

        </div>
        <div>
          
<div style="display: flex; flex-direction: column; gap: 0.8rem;">
  <div class="slide-media-box">
    <img src="../../assets/week-2/color-hue-value.svg" alt="Color hue versus color value" />
  </div>
  <div class="slide-media-box">
    <img src="../../assets/week-2/color-context.svg" alt="Color context effect" />
  </div>
</div>

        </div>
      </div>
    </div>

    <!-- SLIDE 11: 09 — Shape and Orientation -->
    <div class="slide" data-slide="11">
      <span class="slide-badge">Visual Encoding</span>
      <h2>09 — Shape and Orientation</h2>
      <div class="slide-layout-grid">
        <div class="slide-body">
          
<p>Shape and direction are effective for showing categories, motion, or status:</p>
<ul>
  <li>Distinct symbols for distinct categories</li>
  <li>Upward arrows for increases / growth</li>
  <li>Downward arrows for decreases / loss</li>
</ul>
<p><strong>Limitation:</strong> Shapes and angles are poor visual encodings for precise quantitative comparisons.</p>

        </div>
        <div>
          
<div class="slide-media-box">
  <img src="../../assets/week-2/shape-orientation.svg" alt="Shape and orientation encodings" />
</div>

        </div>
      </div>
    </div>

    <!-- SLIDE 12: 10 — Size: Noticeable, but Hard to Measure -->
    <div class="slide" data-slide="12">
      <span class="slide-badge">Visual Encoding</span>
      <h2>10 — Size: Noticeable, but Hard to Measure</h2>
      <div class="slide-layout-grid">
        <div class="slide-body">
          
<p>Size easily communicates relative magnitude, but the human brain struggles to accurately calculate 2D area ratios.</p>
<p>We immediately see that Circle A is larger than Circle B, but estimating <em>by exactly how much</em> is prone to large perceptual errors (Stevens' Power Law).</p>

        </div>
        <div>
          
<div class="slide-media-box">
  <img src="../../assets/week-2/size-comparison.svg" alt="Size comparison difficulty" />
</div>

        </div>
      </div>
    </div>

    <!-- SLIDE 13: 11 — Position Gives More Accurate Comparisons -->
    <div class="slide" data-slide="13">
      <span class="slide-badge">Visual Encoding Ranking</span>
      <h2>11 — Position Gives More Accurate Comparisons</h2>
      <div class="slide-layout-grid">
        <div class="slide-body">
          
<p>Position along a common aligned scale (as in bar charts and scatter plots) is the <strong>most accurate visual encoding</strong> for quantitative comparison.</p>
<p>Small differences in height/position are evaluated with far higher precision than 2D areas, angles, or color saturations.</p>
<div class="alert-takeaway">
  <strong>Design Rule:</strong> Use position on a common scale when exact comparisons matter.
</div>

        </div>
        <div>
          
<div class="slide-media-box">
  <img src="../../assets/week-2/position-vs-size.svg" alt="Position versus size accuracy" />
</div>

        </div>
      </div>
    </div>

    <!-- SLIDE 14: 12 — Order Changes the Question -->
    <div class="slide" data-slide="14">
      <span class="slide-badge">Chart Design</span>
      <h2>12 — Order Changes the Question</h2>
      <div class="slide-layout-grid">
        <div class="slide-body">
          
<p>Alphabetical sorting forces users to search across the entire chart to find high/low performers.</p>
<p><strong>Sorting by value</strong> instantly answers critical analytical questions:</p>
<ul>
  <li>What is the highest / lowest value?</li>
  <li>Which items form the top 3?</li>
  <li>Where does a specific entity rank?</li>
</ul>
<p>Sorting is not merely formatting; it is <strong>question-driven design</strong>.</p>

        </div>
        <div>
          
<div class="slide-media-box">
  <img src="../../assets/week-2/sorted-vs-unsorted-bars.svg" alt="Unsorted versus sorted bar charts" />
</div>

        </div>
      </div>
    </div>

    <!-- SLIDE 15: 12A — When Charts Mislead: Truncated Axis -->
    <div class="slide" data-slide="15">
      <span class="slide-badge">Interactive Activity 1</span>
      <h2>12A — When Charts Mislead: Truncated Axis</h2>
      <div class="slide-layout-grid grid-right-wide">
        <div class="slide-body">
          
<p>The historical top tax rate was <strong>35% in 2012</strong> and <strong>39.6% in 2013</strong> (IRS Bulletin). The data values are identical, but truncating the baseline exaggerates the visual change.</p>
<div class="alert-teaching-point">
  <strong>Rule:</strong> Bar charts encode values as physical length. When the baseline starts above zero, the visual proportion is distorted.
</div>

        </div>
        <div>
          
<div class="activity-embed-container">
  <iframe src="../../assets/week-2/truncated-axis-experiment.html" title="Truncated Axis Interactive Experiment"></iframe>
</div>

        </div>
      </div>
    </div>

    <!-- SLIDE 16: 12A — When Charts Mislead: Pretty vs. Useful -->
    <div class="slide" data-slide="16">
      <span class="slide-badge">Interactive Activity 2</span>
      <h2>12A — When Charts Mislead: Pretty vs. Useful</h2>
      <div class="slide-layout-grid grid-right-wide">
        <div class="slide-body">
          
<p>An infographic can look visually appealing while conveying almost zero actionable information.</p>
<p>Useful visualizations provide essential analytical context:</p>
<ul>
  <li>Exact question asked & methodology</li>
  <li>Sample size (N) and denominator</li>
  <li>Benchmark comparison group</li>
  <li>Clear data provenance / source</li>
</ul>

        </div>
        <div>
          
<div class="activity-embed-container">
  <iframe src="../../assets/week-2/decoration-vs-information-experiment.html" title="Decoration vs Information Interactive Experiment"></iframe>
</div>

        </div>
      </div>
    </div>

    <!-- SLIDE 17: 13 — What Is Data Visualization? -->
    <div class="slide" data-slide="17">
      <span class="slide-badge">Video Briefing</span>
      <h2>13 — What Is Data Visualization?</h2>
      <div class="slide-layout-grid grid-right-wide">
        <div class="slide-body">
          
<p>Data visualization is the deliberate use of visual representations to make data easier to explore, understand, compare, and explain.</p>
<p>The goal is never aesthetic complexity for its own sake; the goal is <strong>clarity of human understanding</strong>.</p>
<p style="font-size: 0.9em; color: #57606a;">▶ Click Play below to watch the briefing inside the slide:</p>

        </div>
        <div>
          
<div class="video-player-container">
  <iframe src="https://www.youtube-nocookie.com/embed/xekEXM0Vonc" title="The Value of Data Visualization" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
<div style="margin-top: 0.4rem; text-align: center;"><a href="https://www.youtube.com/watch?v=xekEXM0Vonc" target="_blank" style="font-size: 0.85em; color: #57606a;">Open on YouTube ↗</a></div>

        </div>
      </div>
    </div>

    <!-- SLIDE 18: 14 — Visualization & Human Judgment -->
    <div class="slide" data-slide="18">
      <span class="slide-badge">Intelligence Context</span>
      <h2>14 — Visualization & Human Judgment</h2>
      <div class="slide-layout-grid">
        <div class="slide-body">
          
<p>In intelligence analysis, AI and algorithms process massive raw inputs, but <strong>human analysts bear the ultimate responsibility for judgment and action</strong>.</p>
<p>Visualization serves as the bridge between computational power and human cognitive evaluation, making patterns, context, and uncertainty transparent.</p>

        </div>
        <div>
          
<div class="slide-media-box">
  <img src="../../assets/week-2/ia-human-judgment-flow.svg" alt="Intelligence Analysis Judgment Flow" />
</div>

        </div>
      </div>
    </div>

    <!-- SLIDE 19: 15 — We Cannot Always Trust Our Eyes -->
    <div class="slide" data-slide="19">
      <span class="slide-badge">Perception & Psychology</span>
      <h2>15 — We Cannot Always Trust Our Eyes</h2>
      <div class="slide-layout-grid">
        <div class="slide-body">
          
<p>Human vision does not function like an objective video camera.</p>
<p>What we perceive is actively constructed from:</p>
<ul>
  <li>Prior expectations & mental models</li>
  <li>Surrounding visual context</li>
  <li>Past experience & training</li>
  <li>Spatial layout and arrangement</li>
</ul>

        </div>
        <div>
          
<div class="slide-media-box">
  <img src="../../assets/week-2/perception-context.svg" alt="Perception context factors" />
</div>

        </div>
      </div>
    </div>

    <!-- SLIDE 20: 15A — Same Length, Different Look: Müller-Lyer -->
    <div class="slide" data-slide="20">
      <span class="slide-badge">Interactive Activity 3</span>
      <h2>15A — Same Length, Different Look: Müller-Lyer</h2>
      <div class="slide-layout-grid grid-right-wide">
        <div class="slide-body">
          
<p>Which central vertical line looks longer?</p>
<p>Click <strong>Reveal Equal Lengths</strong> in the interactive panel to superimpose reference lines.</p>
<div class="alert-teaching-point">
  <strong>Lesson:</strong> Surrounding shapes heavily distort our perception of length and scale. Visual design choices directly alter perceived magnitude.
</div>

        </div>
        <div>
          
<div class="activity-embed-container">
  <iframe src="../../assets/week-2/muller-lyer-experiment.html" title="Muller-Lyer Interactive Experiment"></iframe>
</div>

        </div>
      </div>
    </div>

    <!-- SLIDE 21: 16 — How Expectations Shape What We See -->
    <div class="slide" data-slide="21">
      <span class="slide-badge">Heuer Intelligence Analysis</span>
      <h2>16 — How Expectations Shape What We See</h2>
      <div class="slide-layout-grid">
        <div class="slide-body">
          
<p>In <em>Psychology of Intelligence Analysis</em>, Richards J. Heuer Jr. notes:</p>
<ul>
  <li>We perceive what we expect to perceive.</li>
  <li>Initial mental mindsets form quickly and resist change.</li>
  <li>New evidence is assimilated into existing preconceptions.</li>
</ul>
<div class="alert-takeaway">
  <strong>Analytical Imperative:</strong> Use visualization to rigorously test alternative hypotheses, not to cherry-pick confirmation.
</div>

        </div>
        <div>
          
<div class="slide-media-box">
  <img src="../../assets/week-2/perception-mindset-loop.svg" alt="Perception mindset loop" />
</div>

        </div>
      </div>
    </div>

    <!-- SLIDE 22: 16A — The Same Image Can Have Multiple Meanings -->
    <div class="slide" data-slide="22">
      <span class="slide-badge">Cognitive Perception</span>
      <h2>16A — The Same Image Can Have Multiple Meanings</h2>
      <div class="slide-layout-grid">
        <div class="slide-body">
          
<p>Look at each image below: What do you see first? Can you shift your perception to see the alternate interpretation?</p>
<ul>
  <li><strong>Duck or Rabbit?</strong> (Jastrow, 1899)</li>
  <li><strong>Young Woman or Older Woman?</strong> (Hill, 1915)</li>
</ul>
<div class="alert-teaching-point">
  <strong>Lesson:</strong> The sensory input remains constant, but cognitive interpretation can shift entirely. Analysts must actively explore alternative explanations.
</div>

        </div>
        <div>
          
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.8rem;">
  <div class="slide-media-box">
    <img src="https://commons.wikimedia.org/wiki/Special:Redirect/file/Duck-Rabbit_illusion.jpg" alt="Duck or Rabbit illusion" />
    <span style="font-size: 0.8em; color: #57606a;">Duck or Rabbit?</span>
  </div>
  <div class="slide-media-box">
    <img src="https://commons.wikimedia.org/wiki/Special:Redirect/file/My_Wife_and_My_Mother-in-Law.jpg" alt="Young Woman or Older Woman" />
    <span style="font-size: 0.8em; color: #57606a;">Young / Older Woman</span>
  </div>
</div>

        </div>
      </div>
    </div>

    <!-- SLIDE 23: 17 — Simultaneous Contrast: Surrounding Context -->
    <div class="slide" data-slide="23">
      <span class="slide-badge">Interactive Activity 4 & Video</span>
      <h2>17 — Simultaneous Contrast: Surrounding Context</h2>
      <div class="slide-layout-grid grid-right-wide">
        <div class="slide-body">
          
<p>Our visual system computes color and brightness relative to surrounding fields. The two gray squares inside the experiment are <strong>100% identical (#71717A)</strong>.</p>
<div class="video-player-container" style="margin-top: 0.5rem;">
  <iframe src="https://www.youtube-nocookie.com/embed/mf5otGNbkuc" title="Beau Lotto TED Talk" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

        </div>
        <div>
          
<div class="activity-embed-container">
  <iframe src="../../assets/week-2/simultaneous-contrast-experiment.html" title="Redesigned Simultaneous Contrast Experiment"></iframe>
</div>

        </div>
      </div>
    </div>

    <!-- SLIDE 24: 17A — Afterimage Adaptation Experiment -->
    <div class="slide" data-slide="24">
      <span class="slide-badge">Interactive Activity 5</span>
      <h2>17A — Afterimage Adaptation Experiment</h2>
      <div class="slide-layout-grid grid-right-wide">
        <div class="slide-body">
          
<p><strong>Instructions:</strong> Stare fixedly at the red dot on the nose for 15 seconds without shifting your gaze. When the screen automatically switches to white, observe the photonegative afterimage.</p>
<div class="alert-takeaway">
  <strong>Takeaway:</strong> Neural adaptation creates persistent visual sensations that do not exist on the current physical screen.
</div>

        </div>
        <div>
          
<div class="activity-embed-container">
  <iframe src="../../assets/week-2/afterimage-experiment.html" title="Timed Afterimage Experiment"></iframe>
</div>

        </div>
      </div>
    </div>

    <!-- SLIDE 25: 18 — Perspective Changes How Big Things Look -->
    <div class="slide" data-slide="25">
      <span class="slide-badge">Perceptual Distortion</span>
      <h2>18 — Perspective Changes How Big Things Look</h2>
      <div class="slide-layout-grid">
        <div class="slide-body">
          
<p>Linear perspective and depth cues cause objects of identical dimensions to appear drastically different in scale (Ponzo Illusion).</p>
<p>In spatial and dashboard design, 3D effects and uncalibrated perspective introduce visual distortion.</p>

        </div>
        <div>
          
<div class="slide-media-box">
  <img src="../../assets/week-2/perspective-lines.svg" alt="Perspective line distortion" />
</div>

        </div>
      </div>
    </div>

    <!-- SLIDE 26: 19 — Visual Noise Can Create False Patterns -->
    <div class="slide" data-slide="26">
      <span class="slide-badge">Design Integrity</span>
      <h2>19 — Visual Noise Can Create False Patterns</h2>
      <div class="slide-layout-grid">
        <div class="slide-body">
          
<p>Excessive, high-contrast gridlines generate optical interference (Moiré vibrations) and false ghost spots (Hermann grid).</p>
<div class="alert-teaching-point">
  <strong>Design Principle:</strong> Gridlines and supporting layout containers should remain muted, letting the data marks remain primary.
</div>

        </div>
        <div>
          
<div style="display: flex; flex-direction: column; gap: 0.8rem;">
  <div class="slide-media-box">
    <img src="../../assets/week-2/moire-grid.svg" alt="Moire grid visual noise" />
  </div>
  <div class="slide-media-box">
    <img src="../../assets/week-2/muted-gridlines.svg" alt="Muted versus dark gridlines comparison" />
  </div>
</div>

        </div>
      </div>
    </div>

    <!-- SLIDE 27: 20 & 21 — Gestalt: Closure and Proximity -->
    <div class="slide" data-slide="27">
      <span class="slide-badge">Gestalt Psychology</span>
      <h2>20 & 21 — Gestalt: Closure and Proximity</h2>
      <div class="slide-layout-grid">
        <div class="slide-body">
          
<p><strong>Closure:</strong> The human brain automatically fills in missing lines to perceive a whole, recognizable shape (e.g. Kanizsa triangle).</p>
<p><strong>Proximity:</strong> Items placed close together are instinctively interpreted as belonging to the same group or category.</p>
<p>Good dashboard design leverages Gestalt principles through whitespace and grouping rather than heavy bounding boxes.</p>

        </div>
        <div>
          
<div style="display: flex; flex-direction: column; gap: 0.8rem;">
  <div class="slide-media-box">
    <img src="../../assets/week-2/gestalt-closure.svg" alt="Gestalt closure" />
  </div>
  <div class="slide-media-box">
    <img src="../../assets/week-2/gestalt-proximity.svg" alt="Gestalt proximity" />
  </div>
</div>

        </div>
      </div>
    </div>

    <!-- SLIDE 28: 22 — Week 2 Takeaways & Transition to Spatial -->
    <div class="slide" data-slide="28">
      <span class="slide-badge">Summary & Next Steps</span>
      <h2>22 — Week 2 Takeaways & Transition to Spatial</h2>
      <div class="slide-layout-grid">
        <div class="slide-body">
          
<ol style="padding-left: 1.2rem; line-height: 1.6;">
  <li>Visualization is an essential analytical tool, not mere cosmetic decoration.</li>
  <li>Summary numbers hide critical underlying distributions (Anscombe's Quartet).</li>
  <li>Position on an aligned scale provides the most accurate quantitative comparisons.</li>
  <li>Human perception is context-dependent and subject to optical and cognitive biases.</li>
  <li>Effective visual design enables analysts to communicate evidence with clarity and rigor.</li>
</ol>
<div style="margin-top: 1.5rem;">
  <a href="../../assignments/lab-2/index.md" class="deck-btn" style="background: #1a7f37; border-color: #1a7f37; padding: 0.6rem 1.4rem; font-size: 1.05rem; text-decoration: none;">
    Proceed to Lab 2: ArcGIS Business Analyst I ▶
  </a>
</div>

        </div>
        <div>
          
<div class="slide-media-box">
  <img src="../../assets/week-2/week2-bridge-to-spatial.svg" alt="Bridge from general data visualization to spatial intelligence" />
</div>

        </div>
      </div>
    </div>

  </div>
</div>

<script>
let currentSlide = 1;
const totalSlides = 28;

function updateDeck() {
  const slides = document.querySelectorAll('.slide');
  slides.forEach(slide => {
    const sNum = parseInt(slide.getAttribute('data-slide'));
    if (sNum === currentSlide) {
      slide.classList.add('active');
    } else {
      slide.classList.remove('active');
    }
  });

  document.getElementById('slideCounter').textContent = `Slide ${currentSlide} of ${totalSlides}`;
  document.getElementById('progressBar').style.width = `${(currentSlide / totalSlides) * 100}%`;
  
  document.getElementById('prevBtn').disabled = (currentSlide === 1);
  document.getElementById('nextBtn').disabled = (currentSlide === totalSlides);

  history.replaceState(null, null, `#slide-${currentSlide}`);
}

function changeSlide(direction) {
  const next = currentSlide + direction;
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
  const deck = document.getElementById('lectureDeck');
  if (!document.fullscreenElement) {
    if (deck.requestFullscreen) {
      deck.requestFullscreen();
    } else if (deck.webkitRequestFullscreen) {
      deck.webkitRequestFullscreen();
    }
  } else {
    if (document.exitFullscreen) {
      document.exitFullscreen();
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

window.addEventListener('DOMContentLoaded', () => {
  const hash = window.location.hash;
  if (hash && hash.startsWith('#slide-')) {
    const sNum = parseInt(hash.replace('#slide-', ''));
    if (!isNaN(sNum) && sNum >= 1 && sNum <= totalSlides) {
      currentSlide = sNum;
    }
  }
  updateDeck();
});
</script>

---
[Return to Course Home](../../index.md) | [Go to Lab 2](../../assignments/lab-2/index.md)
