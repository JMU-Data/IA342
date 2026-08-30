# IA342 — Week 2 Source Package

This folder is the canonical authoring package for Week 2 of IA342, Fall 2026.

## Files

- `lecture.md` — canonical lecture content for **Introduction to Data Visualization**. It is written as slide-like Markdown so the local build system can render a presentation-style web experience without PowerPoint or Google Slides.
- `lab.md` — canonical student-facing instructions for **ArcGIS Business Analyst I — Study Areas, Reports, and Infographics**.
- `assets.json` — media manifest for original visuals, instructor screenshots, external video/image URLs, provenance, licensing notes, placement, status, and alt text.
- `assets/` — lecture visual assets.
- `assets/screenshots/` — instructor-created screenshots from the current ArcGIS Business Analyst interface.

## Current media status

- **23 original SVG lecture visuals are ready** in `assets/`.
- **2 original afterimage experiment images are ready** in `assets/` (`afterimage-negative-portrait.png` and `afterimage-blank-fixation.png`).
- **7 ArcGIS screenshots remain pending** and will be supplied by the instructor after testing the live interface.
- External references are recorded in `assets.json`; they are links/embeds or provenance references, not copied third-party slide images.

## Markdown preview convention

Human-readable preview is a first-class requirement for the source package.

- When a lecture asset already exists, `lecture.md` embeds it directly with a relative Markdown image path such as `![alt text](assets/example.svg)`. This allows AntiGravity/VS Code Markdown Preview to show the teaching visual next to the corresponding content.
- Machine-oriented media metadata remains in nearby HTML comments (for example `<!-- asset: ... -->`) and in `assets.json`; HTML comments do not clutter the normal Markdown preview.
- When a lab screenshot is still missing, `lab.md` shows a visible **Screenshot pending** callout plus a hidden `screenshot-slot` comment. This avoids broken-image placeholders while the instructor is still testing the live product.
- After a screenshot is supplied and mapped, replace the pending callout with a normal relative Markdown image reference to the actual file in `assets/screenshots/`.
- Instructor screenshot filenames remain flexible. The canonical filename in `assets.json` is a publishing preference, not a capture-time requirement.

## Language style

Week 2 lecture text should use **plain, spoken English** that is easy to explain aloud in class.

- Prefer short sentences and common words.
- Write as an instructor would naturally speak, not like a journal article.
- Keep technical terms only when students need to learn them.
- When a technical term is necessary, explain it immediately in simple words. For example: **preattentive attributes** = visual features our eyes notice almost immediately.
- Prefer direct wording such as **look at**, **show**, **compare**, **check**, **combine**, and **well-supported** instead of harder synonyms when the meaning is the same.
- Avoid unnecessary academic wording such as **inspect**, **synthesize**, **defensible**, **magnitude**, or **contextual** when simpler English works.
- Put one main idea in each sentence or bullet when possible.
- The goal is language that is easy for both the instructor and students to understand, while keeping the important course concepts accurate.

## Interactive perception experiment

Week 2 now includes an original **afterimage adaptation experiment**.

- `afterimage-negative-portrait.png` is the first-state stimulus. The viewer fixates on the red dot on the nose for about 15 seconds.
- `afterimage-blank-fixation.png` is the second-state screen. It uses the same canvas size and the same fixation-point coordinates.
- `afterimage-experiment.html` is a self-contained timed prototype that switches automatically from the portrait to the blank screen without requiring the viewer to move their gaze.
- In ordinary Markdown Preview, `lecture.md` shows the first image and places the blank screen inside a collapsible Step 2 section.
- In the final web lecture, AntiGravity should provide a **Start experiment** control, display the stimulus for 15 seconds, automatically switch to the blank screen for 8 seconds, and allow restart.
- Do not overlay explanatory text on the blank screen while the afterimage is being observed.
- This experiment should remain deterministic; do not replace the timed two-image sequence with generative video.

## Production responsibilities

### Chat / cloud authoring

- restructure old course content,
- maintain `lecture.md`, `lab.md`, and `assets.json`,
- create original SVG diagrams and precise teaching visuals,
- find and verify useful external image/video URLs,
- record provenance, licensing, attribution, and placement,
- avoid copying third-party visual assets from the old slide deck when the teaching idea can be recreated.

### Instructor

- run ArcGIS Business Analyst using the same environment students will use,
- verify current menu names, reports, and AI Assistant availability,
- capture screenshots while testing,
- place screenshots anywhere inside `assets/screenshots/`.

**Screenshot filenames do not have to match the canonical names in `assets.json`.** The manifest names are preferred publishing names only. AntiGravity may map or rename screenshots during ingestion.

### AntiGravity / local publishing

- consume the Markdown and media manifest,
- render `lecture.md` as a slide-like web lecture,
- render the timed afterimage interaction from the `afterimage-face` manifest entry,
- resolve each visual by asset ID through `assets.json`,
- embed/link external video only where the manifest marks it for use,
- map instructor screenshot filenames to the appropriate screenshot asset IDs,
- render `lab.md` as student instructions,
- publish resulting content to the GitHub course site and Canvas,
- do not rewrite teaching content unless explicitly requested.

## Media policy for Week 2

1. Prefer original vector diagrams for teaching concepts.
2. Product UI is represented with current instructor screenshots, not AI-generated screenshots.
3. External video should normally be linked or embedded from the official/original host rather than downloaded.
4. External photos should only be downloaded/rehosted when licensing clearly permits it and the attribution requirements are captured in `assets.json`.
5. A source URL may be retained only as provenance even when the actual lecture uses an original redraw.

## External references currently retained

- **The Value of Data Visualization** — YouTube link/embed, optional after lecture screen 13.
- **Beau Lotto: Optical illusions show how we see** — TED / official TED YouTube, optional after screen 17.
- **Psychology of Intelligence Analysis** — Richards J. Heuer Jr., official CIA source, supplemental reading for screen 16.
- **Lotus, Illinois railroad tracks** — Wikimedia Commons source retained as provenance/optional licensed photo for the perspective example; the lecture itself uses an original SVG.
- **Graphs in Statistical Analysis** — F. J. Anscombe (1973), primary scholarly source for screens 03–04.
