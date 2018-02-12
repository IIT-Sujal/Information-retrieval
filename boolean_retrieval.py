import porter
import pickle
posting_list = pickle.load(open("posting_list.dict", "rb"))
documents = sorted(pickle.load(open("documents.dict", "rb")))

print('Posting List of term "Art":')
print(posting_list['art'])
print('Posting List of term "Watch":')
print(posting_list['watch'])
print('Posting List of term "Normal":')
print(posting_list['normal'])
query=input("Enter query: ")
query=query.lower()

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
	operator=stack_op.pop()
	list1=stack_list.pop()
	if operator=='not':
		result_list=not_operation(list1)
	elif operator=='and':
		list2=stack_list.pop()
		result_list=and_operation(list1,list2)
	elif operator=='or':
		list2=stack_list.pop()
		result_list=or_operation(list1,list2)
	return result_list

for word in query.split():
	if word=='(':
		stack_op.append('(')
	elif word=='not':
		stack_op.append(word)
	elif word=='and' or word=='or':
		while len(stack_op)!=0 and stack_op[len(stack_op)-1]=='not':
			result_list=operate()
			stack_list.append(result_list)
		stack_op.append(word)
	elif word==')':
		while stack_op[len(stack_op)-1]!='(':
			result_list=operate()
			stack_list.append(result_list)
		stack_op.pop()
	else:
		stack_list.append(sorted(posting_list[porter.stem(word)]))

while len(stack_op):
	result_list=operate()
	stack_list.append(result_list)

print("Resultant list")
print(stack_list[0])