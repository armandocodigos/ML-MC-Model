from easygraph.functions.graph_embedding import deepwalk
def embeddingDW(G):
    return deepwalk(G)
#------------------------------------------------------------------------------------
import numpy as np
def graphDW(G):
    DW = deepwalk(G)
    average = np.zeros(128)
    for k,v in DW[0].items():
        average += v
    average /= len(DW[0])
    return average
#------------------------------------------------------------------------------------
from easygraph.functions.graph_embedding import node2vec
def graphN2V(G, pv=1.0, qv=1.0, w=False):
    N2V = None
    if (w):
        N2V = node2vec(G, p=pv, q=qv, weight_key='weight')
    else:
        N2V = node2vec(G, p=pv, q=qv)
    average = np.zeros(128)
    for k,v in N2V[0].items():
        average += v
    average /= len(N2V[0])
    return average
#------------------------------------------------------------------------------------
def count_graph_regex(G, graph_regex):
    start = [k for k in G.adj.keys() if k.startswith(graph_regex[0])]
    for step in graph_regex[1:]:
        results = []
        for key in start:
            intermediate = [k for k in G.adj[key].keys() if k.startswith(step)]
            results.extend(intermediate)
        start = results
    return len(start)
#------------------------------------------------------------------------------------
def graph_regex(G, graph_regex_list):
    occurrences = []
    for regex in graph_regex_list:
        occurrences.append(count_graph_regex(G, regex))
    return occurrences
#------------------------------------------------------------------------------------