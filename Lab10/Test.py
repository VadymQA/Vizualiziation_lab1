import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn.datasets import load_digits, load_iris
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import TruncatedSVD
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import RandomTreesEmbedding
from sklearn.manifold import (
    Isomap,
    LocallyLinearEmbedding,
    MDS,
    SpectralEmbedding,
    TSNE,
)
from sklearn.neighbors import NeighborhoodComponentsAnalysis
from sklearn.pipeline import make_pipeline
from sklearn.random_projection import SparseRandomProjection
from time import time

iris = load_iris()
X, y = iris.data, iris.target
n_samples, n_features = X.shape
n_neighbors = 30

def plot_embedding_3d(X, title):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    X = MinMaxScaler().fit_transform(X)

    for label in set(iris.target):
        ax.scatter(
            *X[y == label].T,
            marker=f"${label}$",
            s=60,
            color=plt.cm.Dark2(label),
            alpha=0.425,
            zorder=2,
        )
    ax.set_title(title)
    ax.grid(True)

embeddings = {
    "Random projection embedding": SparseRandomProjection(
        n_components=3, random_state=42
    ),
    "Truncated SVD embedding": TruncatedSVD(n_components=3),
    "Linear Discriminant Analysis embedding": LinearDiscriminantAnalysis(
        n_components=2  # LDA can only output n_classes - 1 dimensions, which is 2 for iris dataset.
    ),
    "Isomap embedding": Isomap(n_neighbors=n_neighbors, n_components=3),
    "Standard LLE embedding": LocallyLinearEmbedding(
        n_neighbors=n_neighbors, n_components=3, method="standard"
    ),
    "Modified LLE embedding": LocallyLinearEmbedding(
        n_neighbors=n_neighbors, n_components=3, method="modified"
    ),
    "Hessian LLE embedding": LocallyLinearEmbedding(
        n_neighbors=n_neighbors, n_components=3, method="hessian"
    ),
    "LTSA LLE embedding": LocallyLinearEmbedding(
        n_neighbors=n_neighbors, n_components=3, method="ltsa"
    ),
    "MDS embedding": MDS(
        n_components=3, n_init=1, max_iter=120, n_jobs=2, normalized_stress="auto"
    ),
    "Random Trees embedding": make_pipeline(
        RandomTreesEmbedding(n_estimators=200, max_depth=5, random_state=0),
        TruncatedSVD(n_components=3),
    ),
    "Spectral embedding": SpectralEmbedding(
        n_components=3, random_state=0, eigen_solver="arpack"
    ),
    "t-SNE embedding": TSNE(
        n_components=3,
        n_iter=500,
        n_iter_without_progress=150,
        n_jobs=2,
        random_state=0,
    ),
    "NCA embedding": NeighborhoodComponentsAnalysis(
        n_components=3, init="pca", random_state=0
    ),
}

projections, timing = {}, {}
for name, transformer in embeddings.items():
    if name.startswith("Linear Discriminant Analysis"):
        data = X.copy()
        data.flat[:: X.shape[1] + 1] += 0.01  # Make X invertible
    else:
        data = X

    print(f"Computing {name}...")
    start_time = time()
    projections[name] = transformer.fit_transform(data, y)
    timing[name] = time() - start_time

for name in timing:
    title = f"{name} (time {timing[name]:.3f}s)"
    plot_embedding_3d(projections[name], title)

plt.show()
