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