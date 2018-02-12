import os,re
import porter
z=0
#initializing punctuation marks list and stop words list
punctuation_marks=[',','.','<','>','|',':','(',')','/','_','\\','?','-','!','#','%','^','&','*','_','+','~']
stop_word=open('stop_words.txt',"r").read().split('\n')
stri=os.getcwd()+"/comp.os.ms-windows.misc"
# cleaning data by removing punctuation marks
for root, dirs, files in os.walk(os.getcwd()+"/comp.os.ms-windows.misc"):
	for input_file in files:
		output_file='cleaned_data/'+input_file
		input_file='comp.os.ms-windows.misc/'+input_file
		f=open(input_file,"r")
		f_new=open(output_file,"w")
		for characters in f.read():
			if characters not in punctuation_marks:
				f_new.write(characters)
		f.close()
		f_new.close()

# stemming and removal of stop words
documents=[]
unique_words=set()
for root, dirs, files in os.walk(os.getcwd()+"/cleaned_data"):
	for input_file in files:
		output_file=input_file
		input_file='cleaned_data/'+input_file
		documents.append(output_file)
		f=open(input_file,"r")
		f_new=open("stemmed_data/"+output_file,"w")
		for line in f.readlines():
			words=line.split()	
			for word in words:
				word=word.lower()
				if word.isalpha()==False:
					continue
				if word not in stop_word:
					f_new.write(porter.stem(word)+" ")
					unique_words.add(porter.stem(word))
			f_new.write("\n")
		f.close()
		f_new.close()

#creating index list with document frequency and term frequency
document_frequency=dict()
term_frequency=dict()

#initializing term_frequency matrix
for term in unique_words:
	term_frequency[term]=dict()
	for root, dirs, files in os.walk(os.getcwd()+"/stemmed_data"):
		for input_file in files:
			term_frequency[term][input_file]=0

#building term_frequency matrix
for root, dirs, files in os.walk(os.getcwd()+"/stemmed_data"):
	for input_file in files:
		f_new=open("stemmed_data/"+input_file,"r")
		for line in f_new.readlines():
			words=line.split()	
			for word in words:
				word=word.lower()
				if word.isalpha()==False:
					continue
				if word not in stop_word:
					word=porter.stem(word)
					if word in unique_words:
						term_frequency[word][input_file]+=1
		f_new.close()

posting_list=dict()
# building document_frequency
for word in unique_words:
	document_frequency[word]=0
	posting_list[word]=[]
	for input_file in term_frequency[word].keys():
		if term_frequency[word][input_file]>0:
			posting_list[word].append(input_file)
			document_frequency[word]+=1

# example 
print('Document frequency of term "Made":')
print(document_frequency['made'])
print('Term frequency of term "Made":')
print (term_frequency['made'])
print('Posting List of term "Made":')
print(posting_list['made'])

import pickle

pickle.dump(posting_list,open("posting_list.dict", "wb"))
pickle.dump(documents,open("documents.dict", "wb"))