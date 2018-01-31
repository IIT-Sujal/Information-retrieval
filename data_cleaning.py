import os,re
import porter
z=0
punctuation_marks=[',','.','<','>','|',':','(',')','/','_','\\','?','-','!','#','%','^','&','*','_','+','~']
stop_word=open('stop_words.txt',"r").read().split('\n')

# cleaning data by removing punctuation marks

for root, dirs, files in os.walk("/home/sujal/Desktop/IR-assignment/comp.os.ms-windows.misc"):
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
for root, dirs, files in os.walk("/home/sujal/Desktop/IR-assignment/cleaned_data"):
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
	
for term in unique_words:
	term_frequency[term]=dict()
	document_frequency[word]=0
	for root, dirs, files in os.walk("/home/sujal/Desktop/IR-assignment/stemmed_data"):
		for input_file in files:
			term_frequency[term][input_file]=0

for root, dirs, files in os.walk("/home/sujal/Desktop/IR-assignment/stemmed_data"):
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
for word in unique_words:
	for input_file in term_frequency[word].keys():
		if term_frequency[word][input_file]>0:
			document_frequency[word]+=1
print (document_frequency)