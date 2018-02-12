#from indexing import *
import porter
import pickle
posting_list = pickle.load(open("posting_list.dict", "rb"))
documents = sorted(pickle.load(open("documents.dict", "rb")))
#print (documents)
#print('Posting List of term "Made":')
#print(posting_list['made'])

#for term,docs in posting_list.items():
#	docs.sort()

#print('Posting List of term "Made":')
#print(posting_list['made'])

#query=input("Enter your query: ")
#print(sorted(posting_list.keys()))
print('Posting List of term "Art":')
print(posting_list['art'])
print('Posting List of term "Watch":')
print(posting_list['watch'])
print('Posting List of term "Normal":')
print(posting_list['normal'])
#print(type(posting_list['watch'][0]))
query=input("Enter query: ")
query=query.lower()
#query="watch and normal"

stack_list = []
stack_op = []

def and_operation(list1, list2):
	result=[]
	i=0
	j=0
	l1=len(list1)
	l2=len(list2)
	while i<l1 and j<l2:
		if list1[i]==list2[j]:
			result.append(list1[i])
			i=i+1
			j=j+1
		elif list1[i]<list2[j]:
			i=i+1
		else:
			j=j+1
	return result

def or_operation(list1, list2):
	result=[]
	i=0
	j=0
	l1=len(list1)
	l2=len(list2)
	while i<l1 and j<l2:
		if list1[i]==list2[j]:
			result.append(list1[i])
			i=i+1
			j=j+1
		elif list1[i]<list2[j]:
			result.append(list1[i])
			i=i+1
		else:
			result.append(list2[j])
			j=j+1
	while i<l1:
		result.append(list1[i])
		i=i+1
	while j<l2:
		result.append(list2[j])
		j=j+1
	return result

def not_operation(list1):
	global documents
	result=[]
	i=0
	j=0
	l1=len(documents)
	l2=len(list1)
	while j<l2:
		if documents[i]==list1[j]:
			j=j+1
		elif documents[i]<list1[j]:
			result.append(documents[i])
		i=i+1
	while i<l1:
		result.append(documents[i])
		i=i+1
	return result

def operate():
	global stack_list
	global stack_op
	#result_list=[]
	operator=stack_op.pop()
	list1=stack_list.pop()
	if operator=='not':
		result_list=not_operation(list1)
		#stack_list.append(result_list)
	elif operator=='and':
		list2=stack_list.pop()
		result_list=and_operation(list1,list2)
		#stack_list.append(result_list)
	elif operator=='or':
		list2=stack_list.pop()
		result_list=or_operation(list1,list2)
		#stack_list.append(result_list)
	return result_list


for word in query.split():
	if word=='and' or word=='or' or word=='not':
		stack_op.append(word)
	elif word=='(':
		stack_list.append('(')
	elif word==')':
		while stack_list[len(stack_list)-1]!='(':
			result_list=operate()
			if stack_list[len(stack_list)-1]!='(':
				stack_list.append(result_list)
		stack_list.pop()
		stack_list.append(result_list)
	else:
		stack_list.append(sorted(posting_list[porter.stem(word)]))

#print(stack_list)
#print(stack_op)

while len(stack_op):
	result_list=operate()
	stack_list.append(result_list)

print("Resultant list")
print(stack_list[0])
