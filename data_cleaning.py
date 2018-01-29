import os,re
import porter
z=0
punctuation_marks=[',','.','<','>','|',':','(',')','/','_','\\','?','-','!','#','%','^','&','*','_']
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

for root, dirs, files in os.walk("/home/sujal/Desktop/IR-assignment/cleaned_data"):
	for input_file in files:
		output_file=input_file
		input_file='cleaned_data/'+input_file
		f=open(input_file,"r")
		f_new=open("stemmed_data/"+output_file,"w")
		for line in f.readlines():
			words=line.split()	
			for word in words:
				word=word.lower()
				if word not in stop_word:
					f_new.write(porter.stem(word)+" ")
			f_new.write("\n")
		f.close()
		f_new.close()

#creating index list with document frequency and term frequency

