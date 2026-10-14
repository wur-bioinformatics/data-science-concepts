import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.decomposition import PCA


def make_pca_example_figure():
    """Interactive figure of PCA on a simulated 3D dataset: the data space with the
    first two principal components (left) and the projection onto those components (right)."""
    np.random.seed(0)
    X1 = np.random.normal(0, 15, 50)
    X2 = X1 + np.random.normal(0, 10, 50)
    X3 = X1 + np.random.normal(0, 10, 50)

    dat = np.array([X1, X2, X3]).T
    mu = dat.mean(axis=0)

    n_comp = 2

    pca = PCA(n_components=2).fit(dat)
    latent_points = pca.transform(dat).T

    pc1_latent = np.array([
        [0, -30],
        [0, 30]
    ])
    pc1 = np.dot(pc1_latent, pca.components_[:n_comp,:]) + mu[0]

    pc2_latent = np.array([
        [-80, 0],
        [80, 0]
    ])
    pc2 = np.dot(pc2_latent, pca.components_[:n_comp,:]) + mu[1]

    fig = make_subplots(
        specs=[[
            dict(type='scene'),
            dict(type='xy')
        ]],
        subplot_titles=['Data space (3D)', 'Principal Component space (2D)'],
        rows=1, 
        cols=2)

    # Data space (3D)
    fig.add_trace(
        go.Scatter3d(
            x=X1,
            y=X2,
            z=X3,
            mode='markers',
            marker=dict(
                size=4,
                color='darkblue',
                opacity=.7
            ),
            showlegend=False
        ),
        row=1,col=1
    )

    fig.add_trace(
        go.Scatter3d(
            x=pc1.T[0],
            y=pc1.T[1],
            z=pc1.T[2],
            mode='lines',
            marker=dict(
                color='orange'
            ),
            showlegend=False
        ),
        row=1,col=1
    )

    fig.add_trace(
        go.Scatter3d(
            x=pc2.T[0],
            y=pc2.T[1],
            z=pc2.T[2],
            mode='lines',
            marker=dict(
                color='darkgreen'
            ),
            showlegend=False
        ),
        row=1,col=1
    )

    # Latent space (2D)
    fig.add_trace(
        go.Scatter(
            x=latent_points[0], 
            y=latent_points[1], 
            mode='markers',
            marker=dict(
                size=8,
                color='darkblue',
                opacity=.7
            ),
            showlegend=False
        ),
        row=1,
        col=2
    )

    fig.add_trace(
        go.Scatter(
            x=pc1_latent.T[0],
            y=pc1_latent.T[1],
            mode='lines',
            marker=dict(
                color='orange'
            ),
            showlegend=False
        ),
        row=1,col=2
    )

    fig.add_trace(
        go.Scatter(
            x=pc2_latent.T[0],
            y=pc2_latent.T[1],
            mode='lines',
            marker=dict(
                color='darkgreen'
            ),
            showlegend=False
        ),
        row=1,col=2
    )

    fig.update_xaxes(
        title_text=f'PC1 ({pca.explained_variance_ratio_[0] * 100:.4}% variance)', 
        range=(-100, 100), 
        row=1, 
        col=2
    )
    fig.update_yaxes(
        title_text=f'PC2 ({pca.explained_variance_ratio_[1] * 100:.3}% variance)', 
        range=(-50, 50), 
        row=1, 
        col=2
    )


    fig.update_layout(margin=dict(l=0, r=40, b=100, t=100))
    #fig.show()
    return fig
