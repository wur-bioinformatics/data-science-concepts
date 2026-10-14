"""Helper functions for the Concepts in Data Science practicals (Wageningen University)."""
from importlib.metadata import version

from .decision_boundary import plot_decision_boundary
from .pca_example import make_pca_example_figure

__version__ = version("data-science-concepts")
__all__ = ["make_pca_example_figure", "plot_decision_boundary"]
