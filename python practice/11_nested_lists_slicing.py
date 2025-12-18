import copy

scores=[3,7,2,44,12,11,[[13,17],[22,34]]]
print (scores)
print (scores[1])
print (scores[4])
print (scores[6])
print (scores[6][0][1]) #del is a operator it's not function
scores=[3,7,2,44,12,11,[[13,17],[22,34]]]
del scores[1:5:2]
print (scores)
scores=[3,7,2,44,12,11,[[13,17],[22,34]]]
print (scores[0:6])
print (scores[0:7])
print (scores[6][0:1])
scores.clear()
print (scores)
print (scores.append(4))
print (scores)
#shallow copy vs deep copy
books=[2,4,6,3,5]
import copy
print (books,id(books))
shallowbooks=copy.copy(books)
print (shallowbooks,id(shallowbooks))
deepbooks=copy.deepcopy(books) #shallow copy they are imported in different memory location
print (deepbooks,id(deepbooks))
books=[[2,3],[4,5]]
print (books,id(books))
for i in books:
    print (i,id(i))
#Here when to use when data doesn't have nested(inside) structure
shallowbooks=copy.copy(books)#here  same memory address
print (shallowbooks,id(shallowbooks))
for i in shallowbooks:
    print (i,id(i))
#use deepcopy having nestedlist,dict,object and more independence if we want we can use deepcopy
deepbooks=copy.deepcopy(books)
print (deepbooks,id(deepbooks)) #its stores completely in different locations
for i in deepbooks:
    print (i,id(i))






















