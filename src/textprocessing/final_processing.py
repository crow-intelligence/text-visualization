import networkx as nx

G = nx.read_graphml("data/graphs/backbone3.graphml")

page_ranks = nx.algorithms.link_analysis.pagerank_alg.pagerank(G, weight="weight")

page_ranks = {
    k: v for k, v in sorted(page_ranks.items(), key=lambda item: item[1], reverse=True)
}


with open("data/processed/sentences.tsv", "w") as outfile:
    h = "sentid\tlength\tcluster\tpr\n"
    outfile.write(h)
    for node in G.nodes:
        sent = G.nodes[node]["label"]
        o = (
            node
            + "\t"
            + str(len(sent))
            + "\t"
            + str(page_ranks[node])
            + "\n"
        )
        outfile.write(o)

with open("data/processed/top_sents.txt", "w") as outfile:
    for s in list(page_ranks.keys())[:10]:
        outfile.write(G.nodes[s]["label"] + "\n")
