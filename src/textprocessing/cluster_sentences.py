import pickle

import numpy as np
from numpy import dot
from numpy.linalg import norm
from sklearn.cluster import KMeans

embeddings = np.load("data/embeddings/sentence_embeddings.npy")
sentences = pickle.load(open("data/embeddings/sentences.pkl", "rb"))

clustering = KMeans(n_clusters=10, random_state=42).fit(embeddings)
clusters = set(clustering.labels_)
print(len(clusters))
labels = clustering.labels_
centers = clustering.cluster_centers_


def get_centroid(center):
    cos_sim = dot(embeddings, center) / (norm(embeddings) * norm(center))
    try:
        idx = int(np.where(cos_sim == max(cos_sim))[0])
    except Exception as e:
        # if we have more than one sentences
        idx = int(np.where(cos_sim == max(cos_sim))[0][0])
    return sentences[idx]


for cl in clusters:
    indices = [i for i in range(len(labels)) if labels[i] == cl]
    sents = [sentences[i] for i in indices]
    sents = "\n".join(sents)
    fname = f"data/clusters/{cl}.txt"
    with open(fname, "w") as outfile:
        outfile.write(sents)

with open("data/processed/lines.tsv", "w") as outfile:
    h = "sent\tlen\tcluster\n"
    outfile.write(h)
    for i in range(len(sentences)):
        o = sentences[i] + "\t" + str(len(sentences[i])) + "\t" + str(labels[i]) + "\n"
        outfile.write(o)


with open("data/processed/centroids.tsv", "w") as outfile:
    h = "cluster\tsentence\n"
    outfile.write(h)
    for c in range(len(centers)):
        o = str(c) + "\t" + get_centroid(centers[c]) + "\n"
        outfile.write(o)
