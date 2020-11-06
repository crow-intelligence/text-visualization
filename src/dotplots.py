import pickle

import numpy as np
from PIL import Image
from scipy.sparse import csc_matrix

embeddings = np.load("data/embeddings/sentence_embeddings.npy")
sentences = pickle.load(open("data/embeddings/sentences.pkl", "rb"))
n = embeddings.shape[0]
data = []
row = []
col = []

threshold = 0.15


for i in range(n):
    print(f"working on {i} we have {len(data)} similar objects")
    s = embeddings[i]
    dist = np.linalg.norm(embeddings-s, axis=1)
    for j in range(n):
        if dist[j] < threshold:
            data.append(1)
            row.append(int(j/100))
            col.append(int(i/100))

n_shape = (max(row)*15, max(col)*15)
M = csc_matrix((data, (row, col)), shape=n_shape,  dtype=np.uint8)
M_array = M.toarray().tobytes()

img = Image.frombytes(data=M_array, mode="1", size=(1000, 1000),)
img.save("imgs/dotplot.jpg", "JPEG")
