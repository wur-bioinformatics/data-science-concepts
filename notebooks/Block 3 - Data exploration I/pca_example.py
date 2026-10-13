import numpy as np
import seaborn as sns
from sklearn.decomposition import PCA

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, _ = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

def _make_pca_example_figure():
    np.random.seed(0)
    X1 = np.random.normal(0, 15, 50)
    X2 = X1 + np.random.normal(0, 10, 50)
    X3 = X1 + np.random.normal(0, 10, 50)

    dat = np.array([X1, X2, X3]).T
    mu = dat.mean(axis=0)

    n_comp = 2

    pca = PCA(n_components=2).fit(dat)

    fig = plt.figure(figsize=(10,5))
    ax1 = fig.add_subplot(121, projection='3d')
    ax2 = fig.add_subplot(122)

    p1_latent = np.array([
        [0, -30],
        [0, 30]
    ])
    p1 = np.dot(p1_latent, pca.components_[:n_comp,:]) + mu[0]

    p2_latent = np.array([
        [-80, 0],
        [80, 0]
    ])
    p2 = np.dot(p2_latent, pca.components_[:n_comp,:]) + mu[1]

    ax1.scatter(X1, X2, X3)
    ax1.set_xlim((-50, 50))
    ax1.set_ylim((-50, 50))
    ax1.set_zlim((-50, 50))
    ax1.set_title('Data space')
    ax1.set_xlabel('X1')
    ax1.set_ylabel('X2')
    ax1.set_zlabel('X3')

    a1 = Arrow3D(*p1.T, mutation_scale=20, lw=3, arrowstyle="-|>", color="green")
    ax1.add_artist(a1)

    a2 = Arrow3D(*p2.T, mutation_scale=20, lw=3, arrowstyle="-|>", color="orange")
    ax1.add_artist(a2)

    ax2.scatter(*pca.transform(dat).T)
    ax2.arrow(*p1_latent[0], *(p1_latent[1] - p1_latent[0]), 
            head_width=5, head_length=1.5, linewidth=3, color='green')
    ax2.arrow(*p2_latent[0], *(p2_latent[1] - p2_latent[0]), 
            head_width=1, head_length=7, linewidth=3, color='orange')
    ax2.set_xlim((-90, 90))
    ax2.set_ylim((-50, 50))
    ax2.set_title('Principal component space')
    ax2.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0] * 100:.4}% variance)')
    ax2.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1] * 100:.3}% variance)')

    fig.tight_layout(pad=5)

def make_pca_example_figure():
    import numpy as np
    import seaborn as sns
    from sklearn.decomposition import PCA

    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

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
