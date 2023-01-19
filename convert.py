import easygraph as eg
def convert_unique(listviz):
    G = eg.DiGraph()
    for edge in listviz:
        e = edge.split('->')
        G.add_edge(e[0].strip(), e[1].strip())
    return G
#------------------------------------------------------------------------------------
def convert_sum(listviz):
    G = eg.DiGraph()
    for edge in listviz:
        e = edge.split(' ')
        G.add_edge(e[0].strip(), e[2],
                   weight=int(e[3].split('=')[-1][:-1]))
    return G
#------------------------------------------------------------------------------------