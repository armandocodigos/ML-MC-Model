def obtain_edges(dots):
    for k,v in dots.items():
        with open(v['file']) as f:
            raw_text = f.readlines()

        rows = [x.strip() for x in raw_text]
        rows = list(filter(lambda x: "->" in x, rows))
        rows = list(filter(lambda x: "color" in x, rows))
        rows = [x.split('[')[0].strip() for x in rows]
        rows = [x.replace(':s','') for x in rows]
        rows = [x.replace(':n','') for x in rows]

        heads = list(filter(lambda x: "_0" in x, rows))
        heads = [x.split('->')[0].strip() for x in heads]
        heads = [k + ' -> ' + x for x in heads]

        v['edges'] = heads + rows
    return dots
#------------------------------------------------------
import easygraph as eg
def obtain_easygraph(edges):
    G = eg.DiGraph()
    for edge in edges:
        e = edge.split('->')
        G.add_edge(e[0].strip(), e[1].strip())
    return G
#------------------------------------------------------
import graphviz
def obtain_graphviz(name, edges):
    g = graphviz.Digraph('SSA', filename='SSA_' + name)
    g.node(name)
    for edge in edges:
        e = edge.split('->')
        g.edge(e[0].strip(), e[1].strip())
    return g
#------------------------------------------------------