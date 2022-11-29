import os
def load_polybench(folder, subfolders):
    polybench = {}
    for each in subfolders:
        for subdir, dirs, files in os.walk(folder + os.sep + each):
            for file in files:
                if (file.endswith(".c") or file.endswith(".h")):
                    if (file[:-2] not in polybench):
                        polybench[file[:-2]] = {}
                    polybench[file[:-2]][file[-1]] = subdir + os.sep + file
    return polybench
def show_name(filename):
    return filename.split(os.sep)[-1]
#------------------------------------------------------------------------------------
def clean(filename):
    with open(filename, encoding='utf-8') as txt_file:
        raw_text = txt_file.read()
        while('*/' in raw_text):
            comment_start = raw_text.index('/*')
            comment_end = raw_text.index('*/')
            raw_text = raw_text[:comment_start] + raw_text[comment_end+2:]
        main_start = raw_text.index('int main')
        raw_text = raw_text[:main_start]
        rows = [x.strip() for x in raw_text.split('\n')]
        rows = list(filter(lambda x: len(x) > 0, rows))
        rows = list(filter(lambda x: "#" not in x, rows))
        rows = [(row[:row.index('//')] if ('//' in row) else row) for row in rows]
        rows = list(filter(lambda x: "POLYBENCH_DUMP_START;" not in x, rows))
        rows = list(filter(lambda x: "POLYBENCH_DUMP_BEGIN" not in x, rows))
        rows = list(filter(lambda x: "POLYBENCH_DUMP_END" not in x, rows))
        rows = list(filter(lambda x: "POLYBENCH_DUMP_FINISH;" not in x, rows))
        rows = list(filter(lambda x: "POLYBENCH_2D_ARRAY_DECL" not in x, rows))
        text = ' '.join(rows)
    return text
def replace(text, filename):
    text = text.replace('  ', ' ')
    text = text.replace('DATA_TYPE', 'float')
    text = text.replace('DATA_PRINTF_MODIFIER', '"%0.2f "')
    text = text.replace('SCALAR_VAL', '')
    text = text.replace('SQRT_FUN', 'sqrt')
    text = text.replace('EXP_FUN', 'exp')
    text = text.replace('POW_FUN', 'pow')
    text = text.replace('POLYBENCH_ARRAY', '*')
    text = text.replace('POLYBENCH_FREE_ARRAY', '(void*)')
    text = text.replace('POLYBENCH_DUMP_TARGET', 'stderr')
    return text
#------------------------------------------------------------------------------------
from c_dict import string_to_dict

def generate_ast(polybench):
    for k,v in polybench.items():
        v['text'] = None
        v['ast'] = None
        try:
            print('Program: {:<15} Source code...clean...'.format(k), end='')
            text = clean(v['c'])
            print('replace...', end='')
            text = replace(text, v['h'])
            print('Generate AST...', end='')
            ast_dict = string_to_dict(text)
            print('depurate...', end='')
            ast_dict = depurate_ast(ast_dict, False)
            print('OK!')
        except:
            print('NO!')
        else:
            v['text'] = text
            v['ast'] = ast_dict
#------------------------------------------------------------------------------------
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
def depurate_ast(ast, verbose, whitespaces=''):
    print('\n{}Inside of {}'.format(whitespaces,ast['_nodetype']) if verbose else '',end='')
    try:
        type_s = ast['_nodetype']
        for x in wrangling[type_s]['pop']:
            ast.pop(x)
        if ('list' in wrangling[type_s]):
            list_s = wrangling[type_s]['list']
            for i in range(len(ast[list_s])):
                ast[list_s][i] = depurate_ast(ast[list_s][i],verbose,whitespaces+'    ')
        if ('dict' in wrangling[type_s]):
            dict_l = wrangling[type_s]['dict']
            for i in range(len(dict_l)):
                if(ast[dict_l[i]] != None):
                    ast[dict_l[i]] = depurate_ast(ast[dict_l[i]],verbose,whitespaces+'    ')
    except:
        print('Error with {}!'.format(ast['_nodetype']))
    return ast
#------------------------------------------------------------------------------------
def show_depurate_ast(polybench, name):
    print(polybench[name]['text'], '\n')
    show_depurate_ast_r(polybench[name]['ast'])
    
def show_depurate_ast_r(ast, whitespaces=''):
    print('{}Inside of {}'.format(whitespaces,ast['_nodetype']))
    type_s = ast['_nodetype']
    if ('list' in wrangling[type_s]):
        list_s = wrangling[type_s]['list']
        for i in range(len(ast[list_s])):
            show_depurate_ast_r(ast[list_s][i],whitespaces+'    ')
    if ('dict' in wrangling[type_s]):
        dict_l = wrangling[type_s]['dict']
        for i in range(len(dict_l)):
            if(ast[dict_l[i]] != None):
                show_depurate_ast_r(ast[dict_l[i]],whitespaces+'    ')
#------------------------------------------------------------------------------------