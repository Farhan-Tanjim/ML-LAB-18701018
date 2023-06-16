import numpy as np
import random


def kmeans(data, k):
    n = data.shape[0]
    m = data.shape[1]

    # randomly initialize the centroids
    centroids = np.array(random.sample(list(data), k))
    prev_centroids = np.zeros((k, m))
    clusters = np.zeros(n)

    # repeat until convergence
    while not np.allclose(centroids, prev_centroids):
        for i in range(n):
            distances = np.linalg.norm(data[i] - centroids, axis=1)
            clusters[i] = np.argmin(distances)

        prev_centroids = centroids
        centroids = np.array([data[clusters == i].mean(axis=0) for i in range(k)])

    return centroids, clusters


# Testing the implementation
data = np.array([[3.45], [3.78], [2.98], [3.24], [4], [3.9]])
k = 3
centroids, clusters = kmeans(data, k)
print("Final Centroids:", centroids)
print("Final Clusters:", clusters)
