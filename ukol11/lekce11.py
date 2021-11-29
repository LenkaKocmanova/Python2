import pandas
import requests

import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, silhouette_samples

datasets_url = (
    "https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets"
)

#r = requests.get(f"{datasets_url}/wine-quality.csv")
#open("wine-quality.csv", "wb").write(r.content)
#r = requests.get(f"{datasets_url}/wine-quality-targets.csv")
#open("wine-quality-targets.csv", "wb").write(r.content)

#r = requests.get(f"{datasets_url}/wine-regions.csv")
#open("wine-regions.csv", "wb").write(r.content)
#r = requests.get(f"{datasets_url}/wine-regions-targets.csv")
#open("wine-regions-targets.csv", "wb").write(r.content)

X = pandas.read_csv("wine-quality.csv")
print(X.head())

scaler = StandardScaler()
X = scaler.fit_transform(X)
print(X.shape)

tsne = TSNE(
    init="pca",
    n_components=2,
    perplexity=10,
    learning_rate="auto",
    random_state=0,
)
X = tsne.fit_transform(X)
print(X.shape)
plt.scatter(X[:, 0], X[:, 1], s=50)
model = KMeans(n_clusters=2, random_state=0)
labels = model.fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap="Set1")
centers = model.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c="black", s=200, alpha=0.5)
plt.show()

print(silhouette_score(X, labels))
