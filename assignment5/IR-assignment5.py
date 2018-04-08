doc_info=open("results.test","r")

doc_list=[[],[],[]]

#creating entire doc list
for line in doc_info:
	line=line.split("\t")
	line[4]=float(line[4])
	line[3]=int(line[3])
	line[0]=int(line[0])
	line[5]=line[5][:-1]
	doc_list[line[0]%3].append(line)

qrel=open("qrels.test","r")

relevant_list=[]

#creating relevance list for a particular query
for line in qrel:
	line=line.split(" ")
	line[3]=int(line[3][:-1])
	line[0]=int(line[0])
	line[1]=int(line[1])
	relevant_list.append(line)

rel={}

#sorting document list according to query
for i in range(0,3):
	rel[i]=[]
	doc_list[i].sort(key=lambda x:(x[0],x[3]))

#finding relevant documents for a particular query
for i in relevant_list:
	if i[3]==1:
		rel[i[0]%3].append(i[2])

#calculating AP
average_precision=[]
for i in range(0,3):
	total_doc_encounter=0.0
	ap=0.0
	rel_docs_encounter=0.0
	total_rel_docs=len(rel[i])
	for j in doc_list[i]:
		total_doc_encounter+=1
		if j[2] in rel[i]:
			rel_docs_encounter+=1
			ap+=(rel_docs_encounter/total_doc_encounter)
			# print(rel_docs_encounter,total_doc_encounter,ap)
	ap=ap/total_rel_docs
	average_precision.append(ap)
mean_average_precision=0.0
for i in range(301,304):
	print "average_precision for ",i," is :",average_precision[i%3]
	mean_average_precision+=average_precision[i%3]
mean_average_precision/=3
print "mean_average_precision is : ",mean_average_precision