---
layout: default
title: "Module 2: Introduction to Data Visualization - IA 342"
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
  width: 2%;
  transition: width 0.25s ease;
}

.deck-stage {
  background: #ffffff;
  border: 1px solid #d0d7de;
  border-top: none;
  border-radius: 0 0 10px 10px;
  min-height: 600px;
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

/* Layout Variations */
.slide-center-box {
  max-width: 860px;
  margin: 2rem auto;
  text-align: center;
}

.slide-main-title {
  font-size: 2.6rem;
  margin: 0.5rem 0 0.8rem;
  color: #0969da;
}

.slide-subtitle {
  font-size: 1.3rem;
  color: #57606a;
  margin: 0 auto 1.8rem;
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
  max-width: 940px;
  margin: 1rem auto;
  font-size: 1.18rem;
  line-height: 1.75;
  color: #24292f;
}

.slide-visual-full {
  text-align: center;
  background: #f6f8fa;
  border: 1px solid #d0d7de;
  border-radius: 10px;
  padding: 1rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.03);
  margin: 0 auto;
}

.slide-visual-full img, .slide-visual-full svg {
  max-width: 100%;
  max-height: 500px;
  width: auto;
  height: auto;
  border-radius: 6px;
  display: block;
  margin: 0 auto;
}

.caption-text {
  text-align: center;
  font-size: 0.95rem;
  color: #57606a;
  margin-top: 0.8rem;
}

.video-container-large {
  position: relative;
  width: 100%;
  max-width: 940px;
  margin: 0 auto;
  padding-bottom: 52.8%; /* 16:9 aspect ratio */
  height: 0;
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
  height: 520px;
  border: 1px solid #d0d7de;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 4px 16px rgba(0,0,0,0.08);
  background: #ffffff;
  margin: 0 auto;
}

.activity-container-full iframe {
  width: 100%;
  height: 100%;
  border: 0;
  display: block;
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
  max-height: 420px;
  height: auto;
  border-radius: 4px;
  display: block;
  margin: 0 auto;
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

.deck-btn-lab {
  background: #1a7f37;
  color: #ffffff;
  border: 1px solid #1a7f37;
  border-radius: 8px;
  padding: 0.75rem 1.8rem;
  font-size: 1.1rem;
  font-weight: 600;
  text-decoration: none;
  display: inline-block;
  transition: background 0.15s ease;
}

.deck-btn-lab:hover {
  background: #14622b;
  color: #ffffff;
}

/* Fullscreen mode */
:fullscreen .deck-container,
:-webkit-full-screen .deck-container {
  max-width: 100vw;
  height: 100vh;
  margin: 0;
  display: flex;
  flex-direction: column;
}

:fullscreen .deck-stage,
:-webkit-full-screen .deck-stage {
  flex: 1;
  border-radius: 0;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
}

:fullscreen .slide.active,
:-webkit-full-screen .slide.active {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 1.5rem 3rem;
}

:fullscreen .slide-visual-full img,
:fullscreen .slide-visual-full svg,
:-webkit-full-screen .slide-visual-full img,
:-webkit-full-screen .slide-visual-full svg {
  max-height: 74vh;
}

:fullscreen .activity-container-full,
:-webkit-full-screen .activity-container-full {
  height: 75vh;
}

:fullscreen .video-container-large,
:-webkit-full-screen .video-container-large {
  max-width: 80vw;
  padding-bottom: 45vw;
}

@media (max-width: 860px) {
  .deck-stage { min-height: 480px; }
  .slide { padding: 1.5rem 1.2rem; }
  .slide-visual-full img, .slide-visual-full svg { max-height: 340px; }
  .activity-container-full { height: 420px; }
}
</style>

<div class="deck-container" id="lectureDeck">
  <div class="deck-nav-bar">
    <div class="deck-title-tag">
      <span>📊 IA 342 Week 2 Lecture</span>
      <span style="opacity: 0.4;">|</span>
      <span id="slideCounter">Slide 1 of 50</span>
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
      
<div class="slide-center-box">
  <h1 class="slide-main-title">Introduction to Data Visualization</h1>
  <p class="slide-subtitle">Visualization Methods, Technologies, and Tools for Intelligence Analysis</p>
  <div class="slide-card-lead">
    <p>This lecture explains <strong>why visualization helps us understand complex data</strong> and why <strong>human perception</strong> matters when we design charts, maps, and other visual evidence.</p>
  </div>
  <div style="margin-top: 2rem;">
    <button class="deck-btn-primary" onclick="changeSlide(1)">Start Presentation ▶</button>
  </div>
</div>

    </div>

    <!-- SLIDE 2: 01 — Why Visualization? -->
    <div class="slide" data-slide="2">
      <span class="slide-badge">Foundations</span>
      <h2>01 — Why Visualization?</h2>
      
<div class="slide-text-large">
  <p>Organizations can collect and store massive volumes of data.</p>
  <p>The core analytical challenge is not merely acquiring data; it is <strong>turning raw data into something human analysts can perceive, evaluate, and act upon</strong>.</p>
  <div class="alert-teaching-point" style="margin-top: 1.5rem;">
    <strong>Fundamental Question:</strong> What can a chart or visual pattern reveal that a table of summary numbers hides?
  </div>
</div>

    </div>

    <!-- SLIDE 3: 01 — Core Roles of Visualization in Analysis -->
    <div class="slide" data-slide="3">
      <span class="slide-badge">Analytical Framework</span>
      <h2>01 — Core Roles of Visualization in Analysis</h2>
      
<div class="slide-visual-full">
  <img src="../../assets/week-2/visualization-roles.svg" alt="Visualization supports pattern detection, anomaly detection, comparison, questioning, and communication" />
</div>
<p class="caption-text">Visualization is an active thinking tool for exploration, verification, and high-impact communication.</p>

    </div>

    <!-- SLIDE 4: 01A — From Data Overload to Insight -->
    <div class="slide" data-slide="4">
      <span class="slide-badge">Core Concept</span>
      <h2>01A — From Data Overload to Insight</h2>
      
<div class="slide-text-large">
  <p>Digital datasets can become cognitively overwhelming very quickly.</p>
  <p>Visualization transforms high-dimensional complexity into spatial representations that leverage human visual intelligence.</p>
  <p>The primary benefit is not cosmetic: effective visualizations make <strong>comparisons, trajectories, clusters, and anomalies</strong> immediately salient.</p>
</div>

    </div>

    <!-- SLIDE 5: 01A — Briefing: Why Data Visualization Matters -->
    <div class="slide" data-slide="5">
      <span class="slide-badge">Video Briefing</span>
      <h2>01A — Briefing: Why Data Visualization Matters</h2>
      
<div class="video-container-large">
  <iframe src="https://www.youtube-nocookie.com/embed/Xh3p4yKlEQs" title="Why Data Visualization Matters" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
<div class="media-caption">
  <span>Video 1 · <em>Why Data Visualization Matters — From Data Overload to Insight</em></span>
  · <a href="https://www.youtube.com/watch?v=Xh3p4yKlEQs" target="_blank">Open on YouTube ↗</a>
</div>

    </div>

    <!-- SLIDE 6: 02 — From Data to Decision -->
    <div class="slide" data-slide="6">
      <span class="slide-badge">Analytical Pipeline</span>
      <h2>02 — From Data to Decision</h2>
      
<div class="slide-text-large">
  <p>A foundational framework for intelligence analysis:</p>
  <ul style="font-size: 1.15rem; line-height: 1.8;">
    <li><strong>Data:</strong> Raw observations, sensor feeds, and unorganized records.</li>
    <li><strong>Information:</strong> Structured data organized into meaningful contexts.</li>
    <li><strong>Knowledge:</strong> Synthesized understanding built from context, experience, and patterns.</li>
    <li><strong>Decision / Strategy:</strong> Actionable intelligence applied to operational choices.</li>
  </ul>
</div>

    </div>

    <!-- SLIDE 7: 02 — The Data to Decision Transformation Flow -->
    <div class="slide" data-slide="7">
      <span class="slide-badge">Analytical Pipeline</span>
      <h2>02 — The Data to Decision Transformation Flow</h2>
      
<div class="slide-visual-full">
  <img src="../../assets/week-2/data-to-decision.svg" alt="Data to Decision flow: raw data becomes information, knowledge, and strategic decision" />
</div>
<p class="caption-text">Visualization accelerates the cognitive movement from raw facts to actionable strategy.</p>

    </div>

    <!-- SLIDE 8: 02 — Briefing: From Data to Strategy -->
    <div class="slide" data-slide="8">
      <span class="slide-badge">Video Briefing</span>
      <h2>02 — Briefing: From Data to Strategy</h2>
      
<div class="video-container-large">
  <iframe src="https://www.youtube-nocookie.com/embed/eqcv8KF07nM" title="From Data to Strategy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
<div class="media-caption">
  <span>Video 2 · <em>From Data to Strategy — How Raw Data Becomes Action</em></span>
  · <a href="https://youtu.be/eqcv8KF07nM" target="_blank">Open on YouTube ↗</a>
</div>

    </div>

    <!-- SLIDE 9: 03 — Anscombe's Quartet: Numbers Can Deceive -->
    <div class="slide" data-slide="9">
      <span class="slide-badge">Statistical Foundations</span>
      <h2>03 — Anscombe's Quartet: Numbers Can Deceive</h2>
      
<div class="slide-text-large">
  <p>Summary statistics can make fundamentally distinct datasets look completely identical.</p>
  <p>Consider four datasets (I, II, III, IV) with identical:</p>
  <ul style="font-size: 1.1rem; line-height: 1.7;">
    <li>Means: \( \bar{x} = 9.0, \bar{y} = 7.5 \)</li>
    <li>Sample Variances: \( s_x^2 = 11.0, s_y^2 = 4.12 \)</li>
    <li>Correlation Coefficient: \( r = 0.816 \)</li>
    <li>Linear Regression Fit: \( y \approx 3.0 + 0.5x \) (\( R^2 = 0.67 \))</li>
  </ul>
  <div class="alert-teaching-point">
    If we rely strictly on numerical summaries, we would conclude these datasets describe identical phenomena.
  </div>
</div>

    </div>

    <!-- SLIDE 10: 03 — Identical Summary Statistics Table -->
    <div class="slide" data-slide="10">
      <span class="slide-badge">Statistical Foundations</span>
      <h2>03 — Identical Summary Statistics Table</h2>
      
<div class="slide-visual-full">
  <img src="../../assets/week-2/anscombe-summary.svg" alt="Anscombe Quartet identical statistical summaries" />
</div>
<p class="caption-text">Every standard statistical summary metric is identical across all four datasets.</p>

    </div>

    <!-- SLIDE 11: 04 — But the Visual Patterns Are Completely Different -->
    <div class="slide" data-slide="11">
      <span class="slide-badge">Statistical Foundations</span>
      <h2>04 — But the Visual Patterns Are Completely Different</h2>
      
<div class="slide-text-large">
  <p>When the four datasets are plotted on scatter plots, their true distributions emerge:</p>
  <ul style="font-size: 1.1rem; line-height: 1.8;">
    <li><strong>Dataset I:</strong> Clean, standard linear relationship with expected variance.</li>
    <li><strong>Dataset II:</strong> Clear non-linear, quadratic curve (linear model is invalid).</li>
    <li><strong>Dataset III:</strong> Perfect linear correlation distorted by a single high outlier.</li>
    <li><strong>Dataset IV:</strong> Completely vertical cluster where one outlier controls the entire slope.</li>
  </ul>
  <div class="alert-takeaway">
    <strong>Key Rule:</strong> Never accept summary metrics without first inspecting the visual distribution.
  </div>
</div>

    </div>

    <!-- SLIDE 12: 04 — Anscombe's Quartet: Scatter Plots -->
    <div class="slide" data-slide="12">
      <span class="slide-badge">Statistical Foundations</span>
      <h2>04 — Anscombe's Quartet: Scatter Plots</h2>
      
<div class="slide-visual-full">
  <img src="../../assets/week-2/anscombe-quartet.svg" alt="Anscombe's Quartet showing four starkly different visual scatterplot distributions" />
</div>
<p class="caption-text">Francis Anscombe (1973): Graphs are essential to both data analysis and quality assurance.</p>

    </div>

    <!-- SLIDE 13: 05 — Visualization Is Part of Analysis -->
    <div class="slide" data-slide="13">
      <span class="slide-badge">Analytical Methodology</span>
      <h2>05 — Visualization Is Part of Analysis</h2>
      
<div class="slide-text-large">
  <p>Visualization is not just a presentation wrapper applied at the end of a project.</p>
  <p>It is an active investigative instrument throughout the analytical cycle:</p>
  <ul style="font-size: 1.1rem; line-height: 1.8;">
    <li><strong>Exploration:</strong> Discovering hidden relationships and unexpected trends.</li>
    <li><strong>Verification:</strong> Stress-testing analytical models and detecting anomalies.</li>
    <li><strong>Hypothesis Generation:</strong> Prompting sharper questions for deeper research.</li>
    <li><strong>Defensible Communication:</strong> Conveying evidence with transparency and rigor.</li>
  </ul>
</div>

    </div>

    <!-- SLIDE 14: 06 — What the Eye Notices First: Preattentive Processing -->
    <div class="slide" data-slide="14">
      <span class="slide-badge">Visual Perception</span>
      <h2>06 — What the Eye Notices First: Preattentive Processing</h2>
      
<div class="slide-text-large">
  <p>Human vision processes specific visual features <strong>preattentively</strong>—in under 250 milliseconds, before conscious visual search begins.</p>
  <p>Core preattentive dimensions include:</p>
  <ul style="font-size: 1.1rem; line-height: 1.7;">
    <li><strong>Color:</strong> Hue (qualitative category) and Lightness/Value (quantitative intensity).</li>
    <li><strong>Form:</strong> Size, Length, Width, Shape, Orientation, Curvature.</li>
    <li><strong>Spatial Position:</strong> 2D coordinate location and spatial grouping.</li>
    <li><strong>Motion:</strong> Direction and flicker.</li>
  </ul>
  <div class="alert-teaching-point">
    Preattentive design directs the viewer's cognitive attention to the most critical analytical signals first.
  </div>
</div>

    </div>

    <!-- SLIDE 15: 06 — Preattentive Visual Attributes Overview -->
    <div class="slide" data-slide="15">
      <span class="slide-badge">Visual Perception</span>
      <h2>06 — Preattentive Visual Attributes Overview</h2>
      
<div class="slide-visual-full">
  <img src="../../assets/week-2/preattentive-overview.svg" alt="Comprehensive overview of preattentive visual attributes" />
</div>
<p class="caption-text">Leveraging preattentive attributes enables viewers to parse complex displays effortlessly.</p>

    </div>

    <!-- SLIDE 16: 07 — Experiment: Find the 7s (Step 1 — Serial Search) -->
    <div class="slide" data-slide="16">
      <span class="slide-badge">Classroom Experiment</span>
      <h2>07 — Experiment: Find the 7s (Step 1 — Serial Search)</h2>
      
<div class="slide-visual-full">
  <img src="../../assets/week-2/digit-seven-plain.svg" alt="Dense field of digits without visual emphasis" />
</div>
<p class="caption-text"><strong>Classroom Task:</strong> Try to count every <strong>7</strong> in this grid. Notice the slow, sequential search required.</p>

    </div>

    <!-- SLIDE 17: 07 — Experiment: Find the 7s (Step 2 — Preattentive Pop-Out) -->
    <div class="slide" data-slide="17">
      <span class="slide-badge">Classroom Experiment</span>
      <h2>07 — Experiment: Find the 7s (Step 2 — Preattentive Pop-Out)</h2>
      
<div class="slide-visual-full">
  <img src="../../assets/week-2/digit-seven-highlighted.svg" alt="The exact same digit field with all sevens highlighted in blue" />
</div>
<div class="alert-takeaway" style="max-width: 900px; margin: 1rem auto 0;">
  <strong>Lesson:</strong> The underlying data did not change. Only visual encoding changed. Preattentive pop-out converts a high-effort cognitive task into instantaneous recognition.
</div>

    </div>

    <!-- SLIDE 18: 08 — Visual Encoding: Color Hue vs. Color Value -->
    <div class="slide" data-slide="18">
      <span class="slide-badge">Visual Encoding</span>
      <h2>08 — Visual Encoding: Color Hue vs. Color Value</h2>
      
<div class="slide-visual-full">
  <img src="../../assets/week-2/color-hue-value.svg" alt="Color hue for qualitative categories and color value for ordered quantitative differences" />
</div>
<p class="caption-text"><strong>Hue</strong> encodes qualitative categories. <strong>Lightness / Value</strong> encodes quantitative order and magnitude.</p>

    </div>

    <!-- SLIDE 19: 08 — Visual Encoding: Color Perception Depends on Context -->
    <div class="slide" data-slide="19">
      <span class="slide-badge">Visual Encoding</span>
      <h2>08 — Visual Encoding: Color Perception Depends on Context</h2>
      
<div class="slide-visual-full">
  <img src="../../assets/week-2/color-context.svg" alt="The exact same color swatch appears different depending on surrounding background context" />
</div>
<p class="caption-text">Surrounding background shades alter how human vision interprets foreground data marks.</p>

    </div>

    <!-- SLIDE 20: 09 — Visual Encoding: Shape and Orientation -->
    <div class="slide" data-slide="20">
      <span class="slide-badge">Visual Encoding</span>
      <h2>09 — Visual Encoding: Shape and Orientation</h2>
      
<div class="slide-visual-full">
  <img src="../../assets/week-2/shape-orientation.svg" alt="Shape and orientation encodings for qualitative categories and motion direction" />
</div>
<p class="caption-text">Effective for category distinction and direction of change; ineffective for precise quantitative comparison.</p>

    </div>

    <!-- SLIDE 21: 10 — Visual Encoding: Size Is Noticeable, but Hard to Measure -->
    <div class="slide" data-slide="21">
      <span class="slide-badge">Visual Encoding</span>
      <h2>10 — Visual Encoding: Size Is Noticeable, but Hard to Measure</h2>
      
<div class="slide-visual-full">
  <img src="../../assets/week-2/size-comparison.svg" alt="Comparison of 2D area circles illustrating the difficulty of accurate quantitative estimation" />
</div>
<p class="caption-text">Human vision easily recognizes ordinal size differences, but consistently misjudges exact 2D area proportions.</p>

    </div>

    <!-- SLIDE 22: 11 — Position Gives the Most Accurate Comparisons -->
    <div class="slide" data-slide="22">
      <span class="slide-badge">Visual Encoding Hierarchy</span>
      <h2>11 — Position Gives the Most Accurate Comparisons</h2>
      
<div class="slide-visual-full">
  <img src="../../assets/week-2/position-vs-size.svg" alt="Cleveland and McGill visual encoding accuracy hierarchy comparing position against area" />
</div>
<p class="caption-text">Cleveland & McGill (1984): <strong>Position on a common scale</strong> is the most accurate visual encoding channel.</p>

    </div>

    <!-- SLIDE 23: 12 — Chart Design: Order Changes the Question -->
    <div class="slide" data-slide="23">
      <span class="slide-badge">Chart Design</span>
      <h2>12 — Chart Design: Order Changes the Question</h2>
      
<div class="slide-visual-full">
  <img src="../../assets/week-2/sorted-vs-unsorted-bars.svg" alt="Unsorted versus value-sorted bar charts" />
</div>
<p class="caption-text">Sorting by value instantly answers rank, top performers, and spread without forcing serial lookup.</p>

    </div>

    <!-- SLIDE 24: 12A — When Charts Mislead: Truncated Axis Scales -->
    <div class="slide" data-slide="24">
      <span class="slide-badge">Design Ethics & Integrity</span>
      <h2>12A — When Charts Mislead: Truncated Axis Scales</h2>
      
<div class="slide-visual-full">
  <img src="../../assets/week-2/truncated-axis-original.svg" alt="Comparison of truncated axis versus zero baseline bar chart" />
</div>
<div class="alert-teaching-point" style="max-width: 900px; margin: 1rem auto 0;">
  Historical top U.S. tax rate: <strong>35% in 2012</strong> vs. <strong>39.6% in 2013</strong> (IRS Bulletin). Truncating the y-axis baseline distorts perceived growth by making a 13% increase look like a 400% jump.
</div>

    </div>

    <!-- SLIDE 25: 12A — Interactive: Truncated Axis Experiment -->
    <div class="slide" data-slide="25">
      <span class="slide-badge">Interactive Activity 1</span>
      <h2>12A — Interactive: Truncated Axis Experiment</h2>
      
<div class="activity-container-full">
  <iframe src="../../assets/week-2/truncated-axis-experiment.html" title="Truncated Axis Interactive Experiment"></iframe>
</div>

    </div>

    <!-- SLIDE 26: 12A — When Charts Mislead: Pretty vs. Useful Graphics -->
    <div class="slide" data-slide="26">
      <span class="slide-badge">Design Ethics & Integrity</span>
      <h2>12A — When Charts Mislead: Pretty vs. Useful Graphics</h2>
      
<div class="slide-visual-full">
  <img src="../../assets/week-2/decoration-vs-information-original.svg" alt="A synthetic decorative 76 percent infographic compared to an informative version with denominator, comparison, and source context" />
</div>
<div class="alert-teaching-point" style="max-width: 900px; margin: 1rem auto 0;">
  An infographic can be visually striking while concealing critical context: What was the question? What is the sample size (N)? What is the comparison benchmark? Who collected the data?
</div>

    </div>

    <!-- SLIDE 27: 12A — Interactive: Decoration vs. Informative Visuals -->
    <div class="slide" data-slide="27">
      <span class="slide-badge">Interactive Activity 2</span>
      <h2>12A — Interactive: Decoration vs. Informative Visuals</h2>
      
<div class="activity-container-full">
  <iframe src="../../assets/week-2/decoration-vs-information-experiment.html" title="Decoration vs Information Interactive Experiment"></iframe>
</div>

    </div>

    <!-- SLIDE 28: 13 — What Is Data Visualization? -->
    <div class="slide" data-slide="28">
      <span class="slide-badge">Course Core Philosophy</span>
      <h2>13 — What Is Data Visualization?</h2>
      
<div class="slide-text-large">
  <p>In this course, data visualization is defined as: <strong>the disciplined visual representation of data to amplify human cognition, pattern discovery, contextual comparison, and rigorous communication</strong>.</p>
  <p>The goal is never aesthetic decoration or visual complexity for its own sake.</p>
  <div class="alert-takeaway" style="margin-top: 1.5rem;">
    The ultimate benchmark of an analytical visualization is: <strong>Does it empower the user to understand evidence accurately and make sound judgments?</strong>
  </div>
</div>

    </div>

    <!-- SLIDE 29: 13 — Briefing: The Value of Data Visualization -->
    <div class="slide" data-slide="29">
      <span class="slide-badge">Video Briefing</span>
      <h2>13 — Briefing: The Value of Data Visualization</h2>
      
<div class="video-container-large">
  <iframe src="https://www.youtube-nocookie.com/embed/xekEXM0Vonc" title="The Value of Data Visualization" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
<div class="media-caption">
  <span>Video 3 · <em>The Value of Data Visualization — Understanding Complex Evidence</em></span>
  · <a href="https://www.youtube.com/watch?v=xekEXM0Vonc&t=1s" target="_blank">Open on YouTube ↗</a>
</div>

    </div>

    <!-- SLIDE 30: 14 — Visualization & Human Judgment in Intelligence -->
    <div class="slide" data-slide="30">
      <span class="slide-badge">Intelligence Analysis Focus</span>
      <h2>14 — Visualization & Human Judgment in Intelligence</h2>
      
<div class="slide-text-large">
  <p>In intelligence analysis, computers, algorithms, and AI models process vast raw inputs at superhuman speed.</p>
  <p>However, <strong>human analysts bear the ultimate responsibility for intelligence judgments, probability assessments, and strategic recommendations</strong>.</p>
  <p>Visualization is the essential cognitive interface that translates computational outputs into transparent visual evidence for rigorous human deliberation.</p>
</div>

    </div>

    <!-- SLIDE 31: 14 — The Intelligence Analysis Cognitive Flow -->
    <div class="slide" data-slide="31">
      <span class="slide-badge">Intelligence Analysis Focus</span>
      <h2>14 — The Intelligence Analysis Cognitive Flow</h2>
      
<div class="slide-visual-full">
  <img src="../../assets/week-2/ia-human-judgment-flow.svg" alt="Flow diagram showing movement from computational processing through visual evidence to human intelligence judgment" />
</div>
<p class="caption-text">Visual evidence bridges algorithmic processing and defensible human decision-making.</p>

    </div>

    <!-- SLIDE 32: 15 — Human Perception: We Cannot Always Trust Our Eyes -->
    <div class="slide" data-slide="32">
      <span class="slide-badge">Perception & Psychology</span>
      <h2>15 — Human Perception: We Cannot Always Trust Our Eyes</h2>
      
<div class="slide-visual-full">
  <img src="../../assets/week-2/perception-context.svg" alt="Diagram showing visual perception shaped by expectations, context, experience, and arrangement" />
</div>
<div class="alert-teaching-point" style="max-width: 900px; margin: 1rem auto 0;">
  Human vision is not an objective camera sensor. What we perceive is actively synthesized by cognitive expectations, surrounding context, past experience, and spatial arrangement.
</div>

    </div>

    <!-- SLIDE 33: 15A — Perceptual Distortion: The Müller-Lyer Illusion -->
    <div class="slide" data-slide="33">
      <span class="slide-badge">Perceptual Illusions</span>
      <h2>15A — Perceptual Distortion: The Müller-Lyer Illusion</h2>
      
<div class="slide-visual-full">
  <img src="../../assets/week-2/muller-lyer-original.svg" alt="Müller-Lyer visual illusion showing two equal vertical lines with inward and outward pointing arrow fins" />
</div>
<p class="caption-text"><strong>Classroom Question:</strong> Which center vertical segment appears longer? (Both center lines are mathematically identical in length).</p>

    </div>

    <!-- SLIDE 34: 15A — Interactive: Müller-Lyer Alignment & Reveal -->
    <div class="slide" data-slide="34">
      <span class="slide-badge">Interactive Activity 3</span>
      <h2>15A — Interactive: Müller-Lyer Alignment & Reveal</h2>
      
<div class="activity-container-full">
  <iframe src="../../assets/week-2/muller-lyer-experiment.html" title="Muller-Lyer Interactive Reveal Experiment"></iframe>
</div>

    </div>

    <!-- SLIDE 35: 16 — How Expectations Shape Perception (Richards J. Heuer Jr.) -->
    <div class="slide" data-slide="35">
      <span class="slide-badge">Psychology of Intelligence</span>
      <h2>16 — How Expectations Shape Perception (Richards J. Heuer Jr.)</h2>
      
<div class="slide-visual-full">
  <img src="../../assets/week-2/perception-mindset-loop.svg" alt="Heuer analytic mindset loop showing how prior expectations bias perception and interpretation" />
</div>
<div class="alert-takeaway" style="max-width: 900px; margin: 1rem auto 0;">
  Richards J. Heuer Jr. (<em>Psychology of Intelligence Analysis</em>): Mind-sets form rapidly and resist change. Visualization must be used to test alternative hypotheses—never to confirm preconceived conclusions.
</div>

    </div>

    <!-- SLIDE 36: 16A — Ambiguous Figures: Duck or Rabbit? -->
    <div class="slide" data-slide="36">
      <span class="slide-badge">Cognitive Ambiguity</span>
      <h2>16A — Ambiguous Figures: Duck or Rabbit?</h2>
      
<div class="slide-visual-full">
  <img src="https://commons.wikimedia.org/wiki/Special:Redirect/file/Duck-Rabbit_illusion.jpg" alt="Historic duck-rabbit ambiguous figure from Joseph Jastrow 1899" />
</div>
<div class="alert-teaching-point" style="max-width: 900px; margin: 1rem auto 0;">
  Joseph Jastrow (1899): The sensory stimulus remains 100% constant, yet cognitive interpretation shifts. Once an analyst sees one interpretation, conscious effort is required to perceive alternatives.
</div>

    </div>

    <!-- SLIDE 37: 16A — Ambiguous Figures: Young Woman or Older Woman? -->
    <div class="slide" data-slide="37">
      <span class="slide-badge">Cognitive Ambiguity</span>
      <h2>16A — Ambiguous Figures: Young Woman or Older Woman?</h2>
      
<div class="slide-visual-full">
  <img src="https://commons.wikimedia.org/wiki/Special:Redirect/file/My_Wife_and_My_Mother-in-Law.jpg" alt="W. E. Hill 1915 young woman and mother-in-law ambiguous figure" />
</div>
<div class="alert-teaching-point" style="max-width: 900px; margin: 1rem auto 0;">
  W. E. Hill (1915): Perception is an active cognitive construction. Analysts must remain vigilant against prematurely settling on a single interpretation of ambiguous signals.
</div>

    </div>

    <!-- SLIDE 38: 17 — Context Changes What We See: Simultaneous Contrast -->
    <div class="slide" data-slide="38">
      <span class="slide-badge">Perceptual Contrast</span>
      <h2>17 — Context Changes What We See: Simultaneous Contrast</h2>
      
<div class="slide-visual-full">
  <img src="../../assets/week-2/simultaneous-contrast-original.svg" alt="Simultaneous contrast demonstration showing two identical gray squares on dark and light panels" />
</div>
<p class="caption-text">The human visual system computes lightness and color relative to adjacent surrounding fields, not in absolute values.</p>

    </div>

    <!-- SLIDE 39: 17 — Interactive: Simultaneous Contrast Experiment -->
    <div class="slide" data-slide="39">
      <span class="slide-badge">Interactive Activity 4</span>
      <h2>17 — Interactive: Simultaneous Contrast Experiment</h2>
      
<div class="activity-container-full">
  <iframe src="../../assets/week-2/simultaneous-contrast-experiment.html" title="Redesigned Simultaneous Contrast Interactive Experiment"></iframe>
</div>

    </div>

    <!-- SLIDE 40: 17 — Briefing: Beau Lotto — Optical Illusions Show How We See -->
    <div class="slide" data-slide="40">
      <span class="slide-badge">Video Briefing</span>
      <h2>17 — Briefing: Beau Lotto — Optical Illusions Show How We See</h2>
      
<div class="video-container-large">
  <iframe src="https://www.youtube-nocookie.com/embed/mf5otGNbkuc" title="Beau Lotto TED Talk" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
<div class="media-caption">
  <span>Video 4 · <em>Beau Lotto: Optical illusions show how we see (TED)</em></span>
  · <a href="https://www.ted.com/talks/beau_lotto_optical_illusions_show_how_we_see" target="_blank">Open TED Talk ↗</a>
</div>

    </div>

    <!-- SLIDE 41: 17A — Afterimage Experiment: What Your Eyes Keep Seeing -->
    <div class="slide" data-slide="41">
      <span class="slide-badge">Neural Adaptation</span>
      <h2>17A — Afterimage Experiment: What Your Eyes Keep Seeing</h2>
      
<div class="slide-text-large">
  <p>When you fixate on a high-contrast image for several seconds, retinal photoreceptors undergo neural adaptation (fatigue).</p>
  <p>When the image switches to a neutral blank field, you temporarily perceive a complementary <strong>photonegative afterimage</strong>.</p>
  <div class="alert-teaching-point" style="margin-top: 1.5rem;">
    <strong>Classroom Experiment Protocol:</strong>
    <ol style="margin-top: 0.5rem; line-height: 1.7;">
      <li>Stare fixedly at the red dot on the nose for 15 seconds without moving your eyes.</li>
      <li>When the screen switches to white, keep looking at the center dot.</li>
    </ol>
  </div>
</div>

    </div>

    <!-- SLIDE 42: 17A — Interactive: Timed Afterimage Experiment -->
    <div class="slide" data-slide="42">
      <span class="slide-badge">Interactive Activity 5</span>
      <h2>17A — Interactive: Timed Afterimage Experiment</h2>
      
<div class="activity-container-full">
  <iframe src="../../assets/week-2/afterimage-experiment.html" title="Timed Afterimage Adaptation Experiment"></iframe>
</div>

    </div>

    <!-- SLIDE 43: 18 — Perspective Changes How Big Things Look -->
    <div class="slide" data-slide="43">
      <span class="slide-badge">Spatial Perception</span>
      <h2>18 — Perspective Changes How Big Things Look</h2>
      
<div class="slide-visual-full">
  <img src="../../assets/week-2/perspective-lines.svg" alt="Perspective cues make identical lines appear different in length" />
</div>
<p class="caption-text">Linear perspective cues (Ponzo Illusion) force the brain to rescale identical 2D marks based on implied 3D depth.</p>

    </div>

    <!-- SLIDE 44: 18 — Real-World Perspective & Depth Distortions -->
    <div class="slide" data-slide="44">
      <span class="slide-badge">Spatial Perception</span>
      <h2>18 — Real-World Perspective & Depth Distortions</h2>
      
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; max-width: 960px; margin: 0 auto;">
  <div class="slide-media-box">
    <img src="https://commons.wikimedia.org/wiki/Special:Redirect/file/Lotus_Illinois_railroad_tracks.jpg" alt="Lotus Illinois railroad tracks" style="max-height: 380px;" />
    <span style="font-size: 0.85em; color: #57606a;">Converging Lines Imply Depth (Ponzo Cue)</span>
  </div>
  <div class="slide-media-box">
    <img src="https://pd.w.org/2025/08/96968997de7b578b7.86567587.jpg" alt="Forced perspective at Washington Monument" style="max-height: 380px;" />
    <span style="font-size: 0.85em; color: #57606a;">Forced Perspective Scale Manipulation</span>
  </div>
</div>

    </div>

    <!-- SLIDE 45: 19 — Visual Noise Can Create False Patterns -->
    <div class="slide" data-slide="45">
      <span class="slide-badge">Design Integrity</span>
      <h2>19 — Visual Noise Can Create False Patterns</h2>
      
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; max-width: 960px; margin: 0 auto;">
  <div class="slide-media-box">
    <img src="../../assets/week-2/moire-grid.svg" alt="Dense repeated lines creating moire interference" style="max-height: 380px;" />
    <span style="font-size: 0.85em; color: #57606a;">Moiré Vibration & Optical Interference</span>
  </div>
  <div class="slide-media-box">
    <img src="https://commons.wikimedia.org/wiki/Special:Redirect/file/Hermann_grid_illusion.svg" alt="Hermann grid illusion" style="max-height: 380px;" />
    <span style="font-size: 0.85em; color: #57606a;">Hermann Grid: Ghost Gray Spots at Intersections</span>
  </div>
</div>

    </div>

    <!-- SLIDE 46: 19 — Chart Gridlines: Supporting vs. Competing Lines -->
    <div class="slide" data-slide="46">
      <span class="slide-badge">Design Integrity</span>
      <h2>19 — Chart Gridlines: Supporting vs. Competing Lines</h2>
      
<div class="slide-visual-full">
  <img src="../../assets/week-2/muted-gridlines.svg" alt="Comparison of intrusive heavy gridlines versus muted light supporting gridlines" />
</div>
<div class="alert-teaching-point" style="max-width: 900px; margin: 1rem auto 0;">
  Edward Tufte: Maximize the data-to-ink ratio. Supporting gridlines must remain visually subordinate so they do not compete with primary data marks.
</div>

    </div>

    <!-- SLIDE 47: 20 — Gestalt Principles: Closure -->
    <div class="slide" data-slide="47">
      <span class="slide-badge">Gestalt Psychology</span>
      <h2>20 — Gestalt Principles: Closure</h2>
      
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; max-width: 960px; margin: 0 auto;">
  <div class="slide-media-box">
    <img src="../../assets/week-2/gestalt-closure.svg" alt="Gestalt closure principle" style="max-height: 380px;" />
    <span style="font-size: 0.85em; color: #57606a;">Closure: Brain Fills In Missing Boundaries</span>
  </div>
  <div class="slide-media-box">
    <img src="https://commons.wikimedia.org/wiki/Special:Redirect/file/Kanizsa_triangle.svg" alt="Kanizsa triangle optical illusion" style="max-height: 380px;" />
    <span style="font-size: 0.85em; color: #57606a;">Kanizsa Triangle: Illusory Contour Boundaries</span>
  </div>
</div>

    </div>

    <!-- SLIDE 48: 21 — Gestalt Principles: Proximity & Grouping -->
    <div class="slide" data-slide="48">
      <span class="slide-badge">Gestalt Psychology</span>
      <h2>21 — Gestalt Principles: Proximity & Grouping</h2>
      
<div class="slide-visual-full">
  <img src="../../assets/week-2/gestalt-proximity.svg" alt="Gestalt proximity principle showing nearby marks naturally grouped" />
</div>
<p class="caption-text">Visual proximity establishes intuitive relationships without requiring heavy bounding borders or boxes.</p>

    </div>

    <!-- SLIDE 49: 22 — Week 2 Takeaways & Core Principles -->
    <div class="slide" data-slide="49">
      <span class="slide-badge">Lecture Summary</span>
      <h2>22 — Week 2 Takeaways & Core Principles</h2>
      
<div class="slide-text-large">
  <ol style="font-size: 1.15rem; line-height: 1.85; padding-left: 1.6rem;">
    <li><strong>Visualization is an active analytical tool</strong>, not cosmetic decoration.</li>
    <li><strong>Summary metrics alone hide critical patterns</strong> (Anscombe's Quartet).</li>
    <li><strong>Position on an aligned common scale</strong> provides the highest precision for quantitative comparison.</li>
    <li><strong>Human perception is context-dependent</strong> and subject to optical distortions and cognitive biases.</li>
    <li><strong>Disciplined visual design</strong> enables intelligence analysts to communicate evidence with clarity, rigor, and integrity.</li>
  </ol>
</div>

    </div>

    <!-- SLIDE 50: 22 — Applying Principles to Spatial Intelligence -->
    <div class="slide" data-slide="50">
      <span class="slide-badge">Next Steps · Lab 2</span>
      <h2>22 — Applying Principles to Spatial Intelligence</h2>
      
<div class="slide-visual-full">
  <img src="../../assets/week-2/week2-bridge-to-spatial.svg" alt="Transition from general data visualization to spatial intelligence and ArcGIS Business Analyst" />
</div>
<div style="text-align: center; margin-top: 1.5rem;">
  <a href="../../assignments/lab-2/" class="deck-btn-lab">
    Proceed to Lab 2: ArcGIS Business Analyst I ▶
  </a>
</div>

    </div>

  </div>
</div>

<script>
let currentSlide = 1;
const totalSlides = 50;

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
[Return to Course Home](../../) | [Go to Lab 2](../../assignments/lab-2/)
