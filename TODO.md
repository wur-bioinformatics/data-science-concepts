# TODO

Remaining work after the move to Colab (renaming, data loading, course package, image URLs, Colab badges and the Tutorial 1 Colab introduction are done).

## Decisions

- [ ] Submission format: keep the Word template + screenshots on Brightspace, or have students submit the notebook (`.ipynb` download or Colab share link).
- [ ] Unused datasets: `acc_dataset.csv` (7.6 MB), `amazon.csv`, `twitter.csv` (5.7 MB), `smile-annotations-final.csv/.json` are not used by any notebook, and `top_1000_popular_movies_tmdb.csv` (4.9 MB) is no longer used since Project 2 dropped the movies dataset. Keep or remove?
- [ ] Licences: check that the Kaggle datasets in `datasets/` (UniComplaints, Titanic, TMDB movies, breast cancer) may be redistributed. The automobile and iris data come from UCI (CC BY 4.0, verify).
- [ ] Kaggle accounts: blocks 1 and 2 have students download datasets from Kaggle and upload them with `files.upload()`, so every student needs a Kaggle account. The Gym Members dataset (Projects 2-4) is only available that way, Uni Complaints and Titanic are also in `datasets/` (used from block 3 onwards via `DATA_URL`). Add Gym Members to `datasets/` if the licence allows.

## Before the course starts

- [ ] PyPI: add a pending trusted publisher for `data-science-concepts` (owner `wur-bioinformatics`, repository `data-science-concepts`, workflow `package.yml`, environment `pypi`), create the `pypi` environment in the GitHub repository settings, and publish release `v2026.0.0`. Tutorials 3 and 4 install the package, so they fail until this release exists.
- [ ] Open every notebook via the README links in a real Colab session and run it top to bottom.

## Tutorial 1: Colab introduction

The introduction has been rewritten for Colab. Remaining:

- [ ] Stray `<bu>` tag in the second cell.
- [ ] "File -> Download as" → *File → Download*.
- [ ] Add: idle disconnects, and that uploaded files are deleted when the session ends (relevant now that blocks 1-2 use `files.upload()`).
- [ ] The Colab screenshots (`colab.png`, `Colab homepage.png`, `downloading dataset.png`) are linked from a personal repository (`ajholstege/datascienceconcepts-tutorial`) and two filenames contain spaces. Copy them into this repository (e.g. next to the notebook) so they do not break if that repository changes.
- [ ] `notebooks/block1_introduction/download_notebooks.png` is no longer used (the "Hub Control Panel" section was removed); delete it.
- [ ] Part 2 asks to open the CSV in MS Excel; consider Google Sheets or `df.head()` as an alternative.
- [ ] Projects 1-4 mention "Friday Project"/"Wednesday Tutorial"; check that these still fit the schedule.

## Code bugs

- [ ] Tutorial 3, all-vs-all correlation: `iris_df.corr(method='pearson')` fails on the text column. Use `iris_df.corr(method='pearson', numeric_only=True)` (also decide whether the numeric `species` column should be in the heatmap).
- [ ] Tutorial 3, k-means on iris: `iris_df.to_numpy()[:, :-1]` includes the `species` label column as a feature. Use `iris_df.iloc[:, :-2]` as in the elbow-method cell.
- [ ] Tutorial 3, k-means section: the iris loading code is in a markdown cell, preceded by an empty raw cell. Make it a code cell or remove both.
- [ ] Tutorial 4, iris decision tree: `feature_names = ["sepal length", "sepal length", ...]` should contain `"sepal width"`. Crashes on scikit-learn >= 1.9, silently wrong on older versions.
- [ ] Tutorial 4, evaluation: `np.random.randint(0, len(y_moons), 400)` samples with replacement and has no seed, so the split is not 400/100. Use `np.random.default_rng(RANDOM_STATE).permutation(...)` or `train_test_split`.
- [ ] Project 2: `pd.read_csv('...', lineterminator='\n')` - the `lineterminator` argument was only needed for the movies dataset, which is no longer in the list. Remove it.

## Content corrections

- [ ] Tutorial 3, hierarchical clustering: "Average Linkage - distance between cluster centers" describes centroid linkage. Average linkage is the mean of all pairwise distances between the two clusters.
- [ ] Tutorial 3, Pearson correlation: "Two important assumptions made by pearson correlation are that both variables are normally distributed" - normality is only needed for the p-value (as stated correctly later in the notebook).
- [ ] Tutorial 3: "the numbers 0 through 10" → 0 through 9.
- [ ] Tutorial 1, data types guide: "Categorical - When data can be divided into groups and ranked" mixes up categorical and ordinal (nominal and ordinal are both categorical).
- [ ] Leftover "Boston" references: Tutorial 3 (dimensionality reduction intro), Tutorial 4 (RMSE explanation, cross-validation comment). The dataset was replaced by the automobile dataset and removed from scikit-learn.
- [ ] Tutorial 4: "Are these predictions what you expected from Question 29?" and "the lines that you thought about in Question 1" refer to old numbering.
- [ ] Tutorial 4, question 3.4 asks for precision and recall on iris but only accuracy is computed; multiclass precision/recall need an `average=` argument.
- [ ] Project 3: "Q2" is used twice (clustering and dimensionality reduction).
- [ ] Tutorial 1: string methods link points to the Python 2 docs.
- [ ] Tutorial 1: exercise cells contain leftover code (`ys + zs` under "add your two lists here"; the `enumerate` example under "add your code here" in 3.13).
- [ ] Tutorial 2: the min/max/mean per nationality is plotted with `plt.plot` as lines over a categorical axis; check whether this is intended as a bad example.
- [ ] Typos: Descrete, replacting, happends, Brighstpace, Eploratory, bening, malignent, rroms, effificiency, incremently.

## Repo housekeeping

- [ ] `requirements.txt` does not install: `sklearn` should be `scikit-learn`, the `matplotlib == 3.1.0` pin is outdated, `wget` is not needed; add `plotnine` and `openpyxl` if kept. Only relevant for local use.
- [ ] Optional: GitHub Action that executes all notebooks (e.g. with `nbclient`) on every push and on a schedule, to catch breakage from library updates in Colab.

## Larger content changes (later)

- [ ] Course package: consider a `plot_regression_diagnostics(y, y_pred)` helper for the predicted vs. true / residuals / residual histogram plot that is repeated 7 times in Tutorial 4 (trade-off: students no longer see the plotting code).
- [ ] Add references to Skiena, *The Data Science Design Manual*, per section. Currently only Tutorials 1 and 2 cite the book. Rough mapping: correlation (ch. 2), visualisation (ch. 6), models and evaluation (ch. 7), PCA/SVD (ch. 8), regression (ch. 9), distances, clustering and nearest neighbours (ch. 10), decision trees and neural networks (ch. 11).
- [ ] Tutorial 4 covers regression, classification, evaluation and deep learning (~2h45); consider splitting.
- [ ] Deep learning section: deepart.io is offline, the GPT-2 blog post (2019) is dated. Update the examples.
- [ ] External images (medium.com, blogspot, pbworks over http) may disappear; consider storing copies in the repo where the licence allows.
- [ ] Blocks 1-2 and Blocks 3-4 differ in style (comment style, answer cells, use of `plt.show()`); align.
