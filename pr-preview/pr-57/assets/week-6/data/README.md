# Week 6: Diamonds cleaning practice

Download both files using GitHub's **Download raw file** control. Keep the raw CSVs unchanged and apply the transformations in Tableau Prep.

| File | Rows excluding header |
|---|---:|
| [diamonds_batch_a.csv](diamonds_batch_a.csv) | 10 |
| [diamonds_batch_b.csv](diamonds_batch_b.csv) | 12 |

## Source and teaching modifications

These files are a deliberately modified subset of the instructor's [course Diamonds dataset](https://github.com/xbwei/data-analysis-with-generative-ai/blob/main/diamonds.csv). The cleaning problems below were introduced for practice; they are not claims of defects in that source. These are not the unrelated 53,940-row ggplot2 diamonds dataset.

Fields: `IDNO`, `WEIGHT`, `COLOR`, `CLARITY`, `RATER`, `PRICE`.

- Spaces, capitalization and punctuation create equivalent label variants.
- Prices include thousands separators, a blank, and `not recorded`.
- IDs 2 and 152 each have one copied record across the two batches.
- ID 6 has zero weight; ID 7 has missing clarity.
- IDs 154 and 155 describe separate records even though their other attributes match.

## Checks

After standardizing labels and parsing price: union 22 rows; remove the two confirmed copied records to retain 20; exclude two missing prices to retain 18; exclude zero weight to retain 17. Keep ID 7 as `Unknown` clarity and keep both IDs 154 and 155. Final rater counts: GIA 6, IGI 5, HRD 6.

The files contain no student information, submissions, grades or credentials. They are raw exercise inputs, not completed Tableau flows or student outputs.
