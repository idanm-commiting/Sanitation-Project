# BA780 | Chicago Sanitation Complaints and Food Inspections (2010–2026)

**Status: executed and validated on all five user-supplied ZIP archives on October 14, 2026.**  
**Main notebook:** [`BA780_Integrated_Sanitation_Food_Analysis.ipynb`](BA780_Integrated_Sanitation_Food_Analysis.ipynb)

## Project question and scope

This project integrates the original Chicago 311 sanitation-analysis notebook and the team's `B03-V2.ipynb` approach to examine where and when sanitation complaints occur, alongside Chicago food-inspection outcomes. Analysis is descriptive; it does **not** establish that a complaint was about a particular restaurant or triggered an inspection.

The team's original and individual notebooks remain untouched in `archive/`. The revised notebook uses both data sources and recomputes all statistics, charts and conclusions from the archives.

## Verified data audit

| Quantity | Result |
|---|---:|
| Original sanitation rows | 266,702 |
| Removed repeated request-number rows | 811 |
| **Distinct 311 sanitation requests** | **265,891** |
| Repeated request IDs with conflicting closure dates | 780 |
| Peak complete sanitation year (2011–2025) | 2016, 20,927 |
| ZIP code with most recorded 311 requests | 60620, 12,190 |
| Four food-inspection parts combined | 315,488 records |
| Duplicated inspection IDs removed | 0 |
| Food inspections with missing/non-Chicago/nonstandard city label excluded | 576 |
| **Unique inspections labeled Chicago** | **314,912** |
| Graded Chicago inspections (Pass, Pass w/ Conditions or Fail) | 270,371 |
| Inspections resulting in Fail | 60,654 |
| **Overall graded failure share** | **22.43%** |

Sanitation coverage: January 24, 2010–September 24, 2026. Food-inspection coverage: January 4, 2010–September 14, 2026. Sanitation year **2010 has only 156 records** (sparse historical coverage) and 2026 is incomplete: do not compare these directly to complete years.

## Integrated findings and sample sizes

Sources are first grouped separately to **one row per standardized street address + calendar year**. Only then are they left-joined from food inspection address–years with `validate='one_to_one'`. This avoids artificially multiplying raw complaint and inspection rows.

- **160,849** distinct inspection address–years had usable address and year.
- **6,332** (3.94%) had a matching sanitation record under our exact normalized address-and-year matching rules.
- **14,747** inspections and **10,078** unique 311 requests occurred on the matched address–years; **these are co-located counts, not matched pairs**.

| Sanitation complaints at food-inspection address in same year | Address–years | Graded inspections | Fails | Failure share |
|---|---:|---:|---:|---:|
| 0 matching records | 154,517 | 257,933 | 57,556 | 22.31% |
| 1 | 4,800 | 9,440 | 2,302 | 24.39% |
| 2–4 | 1,310 | 2,568 | 684 | 26.64% |
| 5+ | 222 | 429 | 111 | 25.87% |

**Interpretation:** Food inspections in address–years with one or more matched sanitation complaints had somewhat higher unadjusted failure shares than the group with zero matched complaints. But the percentages are **not monotonically increasing** (5+ is lower than 2–4). The low address-year match coverage, selection of inspected businesses, unknown timing within each year, and unmeasured business/neighborhood factors prohibit causal conclusions. A nonmatch is **not** proof of no complaints or problems.

`results/food_annual_inspections.csv` also provides inspection counts and graded failure shares for every year, and `figures/08_food_fail_share_by_year.png` plots the full-year sequence. The full notebook contains the original sanitation charts, newly validated inspection graphs, and a four-sentence class reflection.

## Method and key safeguards

1. Parse creation/inspection dates with coercion; recalculate year from dates and report incomplete periods.
2. Deduplicate sanitation using `Request Number` and inspections using `Inspection ID`. For repeated sanitation request IDs, retain the row with the latest recorded nonmissing closure date **as a documented heuristic, not a verified service date**.
3. Normalize address case, whitespace, punctuation and bracketed annotations like `(1900W)`; exact text matching still misses address variants and may conflate multiple businesses sharing an address.
4. Filter inspection city to `CHICAGO` ignoring case and whitespace; **576** nonmatching/missing/nonstandard city labels are excluded rather than silently inferred.
5. Count `Fail` in the numerator; denominator is `Fail + Pass + Pass w/ Conditions`. Exclude `No Entry`, `Out of Business`, and other ungraded outcomes from the failure percentage.
6. Produce year/ZIP/community-area/ward counts, a spatial sample, status summary, guarded closure-time calculations, graded inspection time series and inspection failure shares by same-address/year complaint bands.
7. Save only aggregate CSV/JSON results and figures for GitHub, not individual records or violation narratives.

**Limitations:** Counts are not adjusted for population or facility density; 311 complaints can concern non-food properties; same-year comparisons ignore sequence; inspections are not a random sample; day-only closure records cannot support accurate hourly turnaround; address matching yields few exact matches. Do not present raw failures as citywide restaurant probabilities or suggest complaints cause failing results.

## Files

- `BA780_Integrated_Sanitation_Food_Analysis.ipynb`: fully executed Jupyter analysis with embedded outputs.
- `figures/`: eight notebook-produced PNG graphs (sanitation + food).
- `results/`: verified aggregate tables and machine-readable summary.
- `archive/`: unchanged original individual analysis and team V2 notebooks for provenance.
- `data/README.md`: expected ZIP filenames and archive sizes; raw data included **only** in the offline bundle.
- `tests/test_validation.py`: four automated synthetic checks for join cardinality, dates, address standardization and grading.

## Run locally / upload to GitHub

1. Install Python 3.10+ and run `python -m pip install -r requirements.txt`.
2. Put the five named archives in `data/` (already included in the **offline** ZIP; omitted from the **GitHub-ready** ZIP). For consistent ZIP filenames, see `data/README.md`.
3. From this project folder, open the notebook and run **all** cells. It saves `results/` and `figures/` automatically. The `data/` directory is read via the current working directory, so launch Jupyter from the project root.
4. Run `python -m pytest tests -q`. The final project passed all four tests and full notebook execution with the supplied archives.
5. To publish, extract the **GitHub-ready** ZIP, create a repository or branch, and upload the extracted project files using GitHub **Add file → Upload files**. Do **not** upload the ZIP itself or the raw archives. Suggested commit: `Integrate sanitation and V2 food inspections with validated address-year analysis`.

The code-only GitHub ZIP is appropriate for sharing. The offline dataset ZIP is intended for private execution/transfer; check applicable licensing and privacy requirements before distributing raw archives publicly.
