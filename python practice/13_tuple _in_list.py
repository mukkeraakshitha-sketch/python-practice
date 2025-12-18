# list in tuple
marks=[10,20,30,(1,2,3),40]
print (marks,id(marks))
print (marks[4]) #list inner tuple we can't modify that because it is immutable
print (marks[2]) #from external case we can perform by list tuple
print (marks[3])#inner case we can't perform
print (marks[3][2])
marks.append(50)
print (marks)
print (marks.pop(0))
print (marks.pop(2))
#tuple to list
marks=(10,20,30,[1,2,3],40) #pop function not perform because its modification
print (marks)
print (marks[3]) #if we do pop 3 it can't pop
marks[3].append(4)
print (marks)
marks[3].pop(2) #inner part of list we can perform operations
print (marks)



