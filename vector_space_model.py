import pickle
from indexing import punctuation_marks
posting_list = pickle.load(open("posting_list.dict", "rb"))
documents = sorted(pickle.load(open("documents.dict", "rb")))
print("hi")