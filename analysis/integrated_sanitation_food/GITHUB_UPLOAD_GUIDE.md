# Contributing the integrated BA780 analysis to Sanitation-Project

**Target repository:** https://github.com/idanm-commiting/Sanitation-Project

This folder is a self-contained, additional analysis. **Do not replace the existing repository README, existing team notebooks, or raw datasets.**

## Add through the GitHub website

1. Download and extract `BA780_Sanitation_Project_Repo_Safe_Upload.zip`.
2. Sign in to GitHub and open the target repository. Make sure you have contributor/write access; otherwise use a fork and pull request.
3. In the repository root, select **Add file → Upload files**.
4. Drag the extracted **analysis** folder (not the ZIP) into the upload region. Confirm paths appear under `analysis/integrated_sanitation_food/`.
5. For the commit, select **Create a new branch** rather than committing directly to the shared default branch. Suggested branch: `add-verified-sanitation-food-analysis`.
6. Suggested commit title: `Add validated BA780 sanitation and food inspection analysis`.
7. Open a pull request and ask the team to review before merging.

## What's included

- Executed combined notebook using original and V2 methods, verified on all five source archives
- Eight figures and seven aggregate result files
- Archived snapshots of both source notebooks
- Four synthetic validation tests, dependency list and a self-contained README
- `data/README.md` documents the raw ZIPs to supply locally

## Re-running the notebook

The input ZIP archives are deliberately NOT committed. Place the five source ZIP files listed in `data/README.md` into this folder's `data/` subfolder. In a terminal launched from **this folder**, run `python -m pip install -r requirements.txt`, then start Jupyter and run all cells of the notebook. The code reads data relative to the active notebook working directory.

Run tests with `python -m pytest tests -q` from this folder.

## Review points for BA780

The merged analysis uses only exact normalized street-address + calendar-year matching, which is **not proof that a complaint was about a restaurant or caused an inspection**. Preserve the sample sizes, methods and limitations in the README. 2010 sanitation coverage is sparse and 2026 is incomplete.

Prepared for a separate branch/pull request; not yet published or merged.
