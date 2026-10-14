import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def plot_decision_boundary(X, y, feature_names, clf, ax=None, proba=True):
    """
    Utility function for plotting a binary classication boundary in a 2D dataset
    This function does not work for any other classification problem (e.g. multiclass) or feature dimensionality
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(10,10))
    # Plot the decision boundary by assigning a color to each point in the mesh [x_min, x_max]x[y_min, y_max].
    x_min, x_max = X[feature_names[0]].min() - 1, X[feature_names[0]].max() + 1
    y_min, y_max = X[feature_names[1]].min() - 1, X[feature_names[1]].max() + 1
    step = 0.05
    xx, yy = np.meshgrid(np.arange(x_min, x_max, step),
                         np.arange(y_min, y_max, step))

    # Predict on all data points
    if proba:
        Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
    else:
        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
        
    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, alpha=0.6, cmap="RdYlBu_r")

    # Plot data points
    sns.scatterplot(data=X, x=feature_names[0], y=feature_names[1], hue=y, s=30, palette="RdYlBu_r", ax=ax, edgecolor='black')
