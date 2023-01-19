wrangling ={'FileAST':{'pop':['coord'],'list':'ext'},
            'FuncDef':{'pop':['coord','param_decls'],'dict':['decl','body']},
            'Decl':{'pop':['quals','align','funcspec','coord','bitsize'],'dict':['type']},
            'FuncDecl':{'pop':['coord','args'],'dict':['type']},
            'TypeDecl':{'pop':['quals','align','coord'],'dict':['type']},
            'IdentifierType':{'pop':['coord']},
            'Compound':{'pop':['coord'],'list':'block_items'},
            'Assignment':{'pop':['coord'],'dict':['lvalue','rvalue']},
            'UnaryOp':{'pop':['coord'],'dict':['expr']},
            'ID':{'pop':['coord']},
            'Cast':{'pop':['coord','to_type'],'dict':['expr']},
            'For':{'pop':['coord','init','cond','next'],'dict':['stmt']},
            'ArrayRef':{'pop':['coord'],'dict':['name','subscript']},
            'BinaryOp':{'pop':['coord'],'dict':['left','right']},
            'If':{'pop':['coord'],'dict':['cond','iftrue','iffalse']},
            'Constant':{'pop':['coord']},
            'FuncCall':{'pop':['coord'],'dict':['name','args']},
            'ExprList':{'pop':['coord'],'list':'exprs'},
            'TernaryOp':{'pop':['coord'],'dict':['cond','iftrue','iffalse']},
            'ArrayDecl':{'pop':['coord','dim_quals'],'dict':['type','dim']},
            'Typedef':{'pop':['coord','quals','storage'],'dict':['type']}}
#------------------------------------------------------------------------------------
import graphviz
def summarize_ast(polybench, name, multiple=True):
    g = graphviz.Digraph('AST', filename='AST_' + name, strict=not multiple)
    g.node(name)
    summarize_ast_r(polybench[name]['ast'], g, name, multiple)
    return g
#------------------------------------------------------------------------------------
def obtain_label(graph, v1, v2):
    tail_name = graph._quote_edge(v1)
    head_name = graph._quote_edge(v2)
    search = tail_name + " -> " + head_name
    value = 0
    for x in graph.body:
        if (search in x):
            value = int(x.split('=')[-1][:-1])
    return value
#------------------------------------------------------------------------------------
def has_edge(graph, v1, v2):
    tail_name = graph._quote_edge(v1)
    head_name = graph._quote_edge(v2)
    search = tail_name + " -> " + head_name
    #print(len(graph.body), graph.body[-1])
    return any([(search in x) for x in graph.body])
#------------------------------------------------------------------------------------
def summarize_ast_r(ast, graph, father_name, multiple=True):
    type_s = ast['_nodetype']
    if (multiple):
        graph.edge(father_name, type_s)
    elif (not has_edge(graph, father_name, type_s)):
        graph.edge(father_name, type_s, label='1')
    else:
        value = obtain_label(graph, father_name, type_s)
        graph.edge(father_name, type_s, label=str(value +1))
    if ('list' in wrangling[type_s]):
        list_s = wrangling[type_s]['list']
        for i in range(len(ast[list_s])):
            summarize_ast_r(ast[list_s][i], graph, type_s, multiple)
    if ('dict' in wrangling[type_s]):
        dict_l = wrangling[type_s]['dict']
        for i in range(len(dict_l)):
            if(ast[dict_l[i]] != None):
                summarize_ast_r(ast[dict_l[i]], graph, type_s, multiple)
#------------------------------------------------------------------------------------
def unique_ast(polybench, name):
    g = graphviz.Digraph('AST', filename='AST_' + name)
    g.node(name)
    total = unique_ast_r(polybench[name]['ast'], g, name, 0)
    return g
#------------------------------------------------------------------------------------
def unique_ast_r(ast, graph, father_name, count):
    type_s = ast['_nodetype']
    child_name = type_s+'_'+str(count)
    graph.edge(father_name, child_name)
        
    if ('list' in wrangling[type_s]):
        list_s = wrangling[type_s]['list']
        for i in range(len(ast[list_s])):
            count = unique_ast_r(ast[list_s][i], graph, child_name, count+1)
    if ('dict' in wrangling[type_s]):
        dict_l = wrangling[type_s]['dict']
        for i in range(len(dict_l)):
            if(ast[dict_l[i]] != None):
                count = unique_ast_r(ast[dict_l[i]], graph, child_name, count+1)
    return count