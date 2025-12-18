#mutable and immutable datatypes examples
a=2
print (a,id(a))
a=30
print (a,id(a)) #int is immutable
a=3.4
print (a,id(a))  #float is also an immutable
a=5.6
print (a,id(a))
a=True
print (a,id(a)) #float is also an immutable
a=False
print (a,id(a))
a=2+3j
print (a,id(a)) #complex is also an immutable
a=4+5j
print (a,id(a))
a="python"
print(a,id(a)) # string is immutable
a="twg"
print(a,id(a))
a=[10,20,30] # list is mutable
print(a,type(a),id(a))
a.append (40)
print(a,type(a),id(a))
marks=[50,60,70] # it is also a mutable
print(marks,type(a),id(a))
marks[1]=80
print(marks,type(a),id(a))
fruits=["apple","banana","orange"] #this is also a mutables
print(fruits,type(fruits),id(fruits))
fruits[0]="mango"
print(fruits,type(fruits),id(fruits))




