# TODO

Remaining work after the move to Colab (renaming, `DATA_URL` data loading, helper download, image URLs and Colab badges are done).

## Decisions

- [ ] Submission format: keep the Word template + screenshots on Brightspace, or have students submit the notebook (`.ipynb` download or Colab share link).
- [ ] Unused datasets: `acc_dataset.csv` (7.6 MB), `amazon.csv`, `twitter.csv` (5.7 MB), `smile-annotations-final.csv/.json` are not used by any notebook. Keep or remove?
- [ ] Licences: check that the Kaggle datasets in `datasets/` (UniComplaints, Titanic, TMDB movies, breast cancer) may be redistributed. The automobile and iris data come from UCI (CC BY 4.0, verify).
- [ ] Gym Members dataset (Projects 3 and 4) is not in the repo, so students must download it from Kaggle (needs an account) and upload it to Colab. Add it to `datasets/` (if the licence allows) or replace it.

## Before the course starts

- [ ] Merge to `main`: notebooks read data and images from the `main` branch, so new files (`iris.csv`, `automobile.csv`, `breast-cancer.csv`, moved images) only load after merging.
- [ ] Open every notebook via the README links in a real Colab session and run it top to bottom.

## Tutorial 1: Colab introduction

Part 1 describes Jupyter/JupyterHub and no longer matches what students see.

- [ ] Replace the toolbar diagram (`nb_diagram.png`) and the "Run Cell / Choose Cell Type" explanation with the Colab equivalents.
- [ ] Remove "Downloading Practicals" (Hub Control Panel) and `download_notebooks.png`; replace with *File → Save a copy in Drive*, and how to find the copy again.
- [ ] "Control flow" explains `In [ ]`, `In [*]`, `In [n]`; Colab shows a play button and `[n]` instead.
- [ ] "File → Download as" → *File → Download*.
- [ ] Add: runtime restarts (variables are lost), idle disconnects, uploaded files are deleted when the session ends.
- [ ] Part 2 asks to open the CSV in MS Excel; consider Google Sheets or `df.head()` as an alternative.
- [ ] Projects 1-4 still mention "Jupyter Notebook" and "Friday Project"/"Wednesday Tutorial"; check that these still fit the schedule.

## Code bugs

- [ ] Tutorial 3, all-vs-all correlation: `iris_df.corr(method='pearson')` fails on the text column. Use `iris_df.corr(method='pearson', numeric_only=True)` (also decide whether the numeric `species` column should be in the heatmap).
- [ ] Tutorial 3, k-means on iris: `iris_df.to_numpy()[:, :-1]` includes the `species` label column as a feature. Use `iris_df.iloc[:, :-2]` as in the elbow-method cell.
- [ ] Tutorial 3, k-means section: the iris loading code is in a markdown cell, preceded by an empty raw cell. Make it a code cell or remove both.
- [ ] Tutorial 4, iris decision tree: `feature_names = ["sepal length", "sepal length", ...]` should contain `"sepal width"`. Crashes on scikit-learn >= 1.9, silently wrong on older versions.
- [ ] Tutorial 4, evaluation: `np.random.randint(0, len(y_moons), 400)` samples with replacement and has no seed, so the split is not 400/100. Use `np.random.default_rng(RANDOM_STATE).permutation(...)` or `train_test_split`.
- [ ] Project 2: `df.explode(list('genres'))` explodes on the letters of "genres". The `genres` column is a string representation of a list, so it needs `df['genres'] = df['genres'].apply(ast.literal_eval)` followed by `df.explode('genres')`.

## Content corrections

- [ ] Tutorial 3, hierarchical clustering: "Average Linkage - distance between cluster centers" describes centroid linkage. Average linkage is the mean of all pairwise distances between the two clusters.
- [ ] Tutorial 3, Pearson correlation: "Two important assumptions made by pearson correlation are that both variables are normally distributed" - normality is only needed for the p-value (as stated correctly later in the notebook).
- [ ] Tutorial 3: "the numbers 0 through 10" → 0 through 9.
- [ ] Tutorial 1, data types guide: "Categorical - when data can be divided into groups and ranked" mixes up categorical and ordinal (nominal and ordinal are both categorical).
- [ ] Leftover "Boston" references: Tutorial 3 (dimensionality reduction intro), Tutorial 4 (RMSE explanation, cross-validation comment). The dataset was replaced by the automobile dataset and removed from scikit-learn.
- [ ] Tutorial 4: "Are these predictions what you expected from Question 29?" and "the lines that you thought about in Question 1" refer to old numbering.
- [ ] Tutorial 4, question 3.4 asks for precision and recall on iris but only accuracy is computed; multiclass precision/recall need an `average=` argument.
- [ ] Project 3: "Q2" is used twice (clustering and dimensionality reduction).
- [ ] Tutorial 1: string methods link points to the Python 2 docs.
- [ ] Tutorial 1: exercise cells contain leftover code (`ys + zs` under "add your two lists here"; the `enumerate` example under "add your code here" in 3.13).
- [ ] Tutorial 2: the min/max/mean per nationality is plotted with `plt.plot` as lines over a categorical axis; check whether this is intended as a bad example.
- [ ] Typos: Descrete, reltating, lean (learn), acheive, conisder, futher, inspact, replacting, happends, ading, Brighstpace, visalisation, Eploratory, bening, malignent, rroms, effificiency, Statsitics, incremently.

## Repo housekeeping

- [ ] `requirements.txt` does not install: `sklearn` should be `scikit-learn`, the `matplotlib == 3.1.0` pin is outdated, `wget` is not needed; add `plotnine` and `openpyxl` if kept. Only relevant for local use.
- [ ] `.gitignore`: add `pca_example.py` at the notebook level if people run notebooks locally (Tutorial 3 downloads it into the working directory).
- [ ] Optional: GitHub Action that executes all notebooks (e.g. with `nbclient`) on every push and on a schedule, to catch breakage from library updates in Colab.

## Larger content changes (later)

- [ ] Add references to Skiena, *The Data Science Design Manual*, per section. Currently only Tutorials 1 and 2 cite the book. Rough mapping: correlation (ch. 2), visualisation (ch. 6), models and evaluation (ch. 7), PCA/SVD (ch. 8), regression (ch. 9), distances, clustering and nearest neighbours (ch. 10), decision trees and neural networks (ch. 11).
- [ ] Tutorial 4 covers regression, classification, evaluation and deep learning (~2h45); consider splitting.
- [ ] Deep learning section: deepart.io is offline, the GPT-2 blog post (2019) is dated. Update the examples.
- [ ] External images (medium.com, blogspot, pbworks over http) may disappear; consider storing copies in the repo where the licence allows.
- [ ] Blocks 1-2 and Blocks 3-4 differ in style (comment style, answer cells, use of `plt.show()`); align.
