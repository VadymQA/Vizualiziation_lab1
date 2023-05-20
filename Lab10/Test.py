import matplotlib.pyplot as plt
from sklearn.datasets import fetch_olivetti_faces

olivetti = fetch_olivetti_faces()
X, y = olivetti.data, olivetti.target
n_samples, n_features = X.shape
n_neighbors = 30

fig, axs = plt.subplots(nrows=10, ncols=10, figsize=(6, 6))
for idx, ax in enumerate(axs.ravel()):
    ax.imshow(X[idx].reshape((64, 64)), cmap=plt.cm.gray)
    ax.axis("off")
_ = fig.suptitle("A selection from the Olivetti faces dataset", fontsize=16)

plt.plot()