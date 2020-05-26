import pickle

import nltk
import numpy as np
from sentence_transformers import SentenceTransformer

with open("data/raw_cleaned/war_and_peace.txt", "r") as infile:
    corpus = infile.read().strip().replace("\n", " ")

corpus = corpus.replace("”", "").replace("‘", "").replace("“", "")
corpus = corpus.replace("....", ".")
corpus = corpus.replace("—", " ").replace("...", ".")
corpus = corpus.replace("..", ".")
corpus = corpus.replace("“", "")
corpus = corpus.replace("*", "")


def filter_sentence(sent):
    tokens = nltk.tokenize.word_tokenize(sent)
    wds = [e.lower() for e in tokens if e.isalpha()]
    return " ".join(wds)

sentences = nltk.sent_tokenize(corpus)
sentences2vectorize = [filter_sentence(s) for s in sentences]

model = SentenceTransformer("bert-base-nli-mean-tokens")
sentence_embeddings = model.encode(sentences2vectorize)

s2 = np.asarray(sentence_embeddings)
with open("data/embeddings/sentence_embeddings.npy", "wb") as outfile:
    np.save(outfile, s2)

with open("data/embeddings/sentences.pkl", "wb") as outfile:
    pickle.dump(sentences, outfile)
