import pickle

import networkx as nx
import numpy as np
from scipy.spatial.distance import cosine
from sklearn.neighbors import kneighbors_graph


embeddings = np.load("data/embeddings/sentence_embeddings.npy")
sentences = pickle.load(open("data/embeddings/sentences.pkl", "rb"))

A = kneighbors_graph(embeddings, 5, mode="connectivity", include_self=False)
m = A.toarray()

G = nx.Graph()
edges = {}
for i in range(len(embeddings)):
    sent = embeddings[i]
    lst = list(m[i])
    indices = [j for j in range(len(lst)) if lst[j] > 0]
    weights = [float(cosine(sent, embeddings[k])) for k in indices]
    connected_sents = [sentences[i] for i in indices]
    G.add_node(i, label=sentences[i])
    keys = list(zip([i] * len(indices), indices))
    keys = [tuple(sorted(k)) for k in keys]
    d = dict(zip(keys, weights))
    for k, v in d.items():
        if k in edges:
            edges[k] = (edges[k] + v) / 2.0
        else:
            edges[k] = v

for k, v in edges.items():
    G.add_edge(k[0], k[1], weight=float(v))

nx.write_graphml(G, "data/graphs/full_graph.graphml")
