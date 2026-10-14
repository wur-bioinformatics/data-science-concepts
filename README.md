# _INF34306_ Concepts in Data Science

Notebooks and datasets for Concepts in Data Science practicals.

### Using the notebooks

The notebooks are meant to be used in [Google Colab](https://colab.research.google.com). Open a notebook with one of the links below, then use *File → Save a copy in Drive* to keep your changes.

| Block | Tutorial | Project |
|---|---|---|
| 1 - Introduction | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wur-bioinformatics/data-science-concepts/blob/main/notebooks/block1_introduction/tutorial_1.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wur-bioinformatics/data-science-concepts/blob/main/notebooks/block1_introduction/project_1.ipynb) |
| 2 - Python libraries, Visualization, and the Grammar of Graphics | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wur-bioinformatics/data-science-concepts/blob/main/notebooks/block2_visualisation/tutorial_2.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wur-bioinformatics/data-science-concepts/blob/main/notebooks/block2_visualisation/project_2.ipynb) |
| 3 - Data exploration I | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wur-bioinformatics/data-science-concepts/blob/main/notebooks/block3_exploration_1/tutorial_3.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wur-bioinformatics/data-science-concepts/blob/main/notebooks/block3_exploration_1/project_3.ipynb) |
| 4 - Data exploration II | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wur-bioinformatics/data-science-concepts/blob/main/notebooks/block4_exploration_2/tutorial_4.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wur-bioinformatics/data-science-concepts/blob/main/notebooks/block4_exploration_2/project_4.ipynb) |

In blocks 1 and 2, students download the datasets from Kaggle themselves and upload them to Colab (`files.upload()`). From block 3 onwards, the notebooks read datasets directly from this repository on GitHub (`DATA_URL` in the notebooks). Note that this points to the `main` branch: files that are not on `main` yet will not load.

### Repository structure

Notebooks with exercises and examples are in the `notebooks` folder, with one subfolder per block. Datasets (when not available through APIs) are in the `datasets` folder, with informative filenames.

```
|-- README.md
|-- TODO.md
|-- datasets
|   |-- UniComplaints.csv
|   |-- anscombe_quartet.csv
|   |-- automobile.csv
|   |-- breast-cancer.csv
|   |-- iris.csv
|   |-- titanic.csv
|   |-- top_1000_popular_movies_tmdb.csv
|   `-- ... (not used by the current notebooks, see TODO.md)
|-- notebooks
|   |-- block1_introduction
|   |   |-- tutorial_1.ipynb
|   |   `-- project_1.ipynb
|   |-- block2_visualisation
|   |   |-- tutorial_2.ipynb
|   |   `-- project_2.ipynb
|   |-- block3_exploration_1
|   |   |-- tutorial_3.ipynb
|   |   `-- project_3.ipynb
|   `-- block4_exploration_2
|       |-- tutorial_4.ipynb
|       `-- project_4.ipynb
|-- pyproject.toml
|-- requirements.txt
`-- src
    `-- data_science_concepts   (course package, see below)
```

Images used in the notebooks are stored next to the notebooks and linked by their GitHub URL, because Colab does not resolve relative image paths.

### Course package

Helper functions used in the notebooks (e.g. `plot_decision_boundary`) are in the `data-science-concepts` package in `src/data_science_concepts`. The notebooks install it with

```python
%pip install -q "data-science-concepts==2026.*"
import data_science_concepts as dsc
```

To release a new version, create a GitHub release with a tag of the form `vYEAR.MINOR.PATCH` (e.g. `v2026.0.1`). The `Package` workflow (`.github/workflows/package.yml`) builds the package and publishes it to [PyPI](https://pypi.org/project/data-science-concepts/); the version number is taken from the tag. Notebooks pin the course year, so a release for the next year (`v2027.0.0`) does not affect notebooks of the current year.
