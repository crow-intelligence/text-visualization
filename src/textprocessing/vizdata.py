import pickle
from os import listdir
from os.path import isfile, join

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

with open("data/embeddings/sentences.pkl", "rb") as infile:
    sentences = pickle.load(infile)

df = pd.read_csv("data/processed/sentences.tsv",
                 sep="\t",
                 encoding="utf-8")
sentid_length = dict(zip(df["sentid"], df["length"]))
sentid_pr = dict(zip(df["sentid"], df["pr"]))

sentids = list(sentid_pr.keys())
pagerank_values = np.array(list(sentid_pr.values())).reshape(-1, 1)
scaler = MinMaxScaler()
scaler.fit(pagerank_values)
pagerank_scaled = scaler.transform(pagerank_values).flatten().tolist()

sentid_pr_normed = dict(zip(sentids, pagerank_scaled))

in_path = "data/clusters"
fs = [f for f in listdir(in_path) if isfile(join(in_path, f))]
sentence_cluster = {}

for f in fs:
    cluster = int(f.split(".")[0])
    with open(join(in_path, f), "r") as infile:
        sents = infile.read().split("\n")
        for s in sents:
            sentence_cluster[s] = cluster

with open("data/processed/linevizdata.tsv", "w") as outfile:
    h = "sentid\tlength\tcluster\tpagerank\n"
    outfile.write(h)
    for sentid, length in sentid_length.items():
        sent = sentences[sentid]
        cluster = str(sentence_cluster[sent])
        pagerank = str(sentid_pr_normed[sentid])
        o = str(sentid) + "\t" + str(length) + "\t" + cluster + "\t" + \
            pagerank + "\n"
        outfile.write(o)
