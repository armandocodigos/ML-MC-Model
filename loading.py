import pickle
def load_model(filename):
    return pickle.load(open(filename, 'rb'))
#------------------------------------------------------
def load_chats(filename):
    return pickle.load(open(filename, 'rb'))
#------------------------------------------------------
def save_file(file, filename):
    pickle.dump(file, open(filename, 'wb'))
    print('File saved successfully')
#------------------------------------------------------
import os
def clean_embeddings(mydir=".\\Embeddings\\"):
    for f in os.listdir(mydir):
        if f.endswith(".csv"):
            os.remove(os.path.join(mydir, f))
#------------------------------------------------------
def append_file(name, filename, values):
    file = ".\\Embeddings\\" + filename + ".csv"
    with open(file, "a") as f:
        f.write(name + ',' + ','.join([str(i) for i in list(values)]) + '\n')
#------------------------------------------------------
import csv
def clean_graph_regex(headers, filename="graph_regex"):
    file =".\\Embeddings\\" + filename + ".csv"
    if os.path.exists(file):
        os.remove(file)
    with open(file, 'w', newline='') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(headers)
#------------------------------------------------------
def load_dots(folder):
    dots = {}
    for subdir, dirs, files in os.walk(folder):
        for file in files:
            if (file.endswith(".dot")):
                dots[file.split('.')[0]] = {'file':subdir + os.sep + file}
    return dots
#------------------------------------------------------