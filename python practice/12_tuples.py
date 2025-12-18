#tuples are the (immutable) once we created we can't modify elements they are fixed values
#data is secured then list it is immutable
marks=(10,20,30,40,50,60,70,80)
print (marks[0:8])
print (marks[0:8:2])
print (marks[0:8:4])
#append function is not allowed because it is modifying the tuple
#clear also not allowed in tuple
#copy fun is also not allowed in tuple
marks.count(80)
print (marks.count(80))#yes count is accepted tuple
marks.count(90)
print (marks.count(90))
marks.count(10)
print (marks.count(10))
marks.count(100)
print (marks.count(100))
marks.count(0)
print (marks.count(0))
#extend():is not allowed because its modifying tuple
#index:is accepted tuple
marks.index(30)
print (marks.index(30))
#insert:is not accepted because it changes the tuple
#pop is also not accepted
#remove and reverse sort not accepted #this is tuple we can't sort directly by using tuple
#we can modify by converting list and use it again convert to tuple
marks=(34,23,67,11,98,56,33) #tuple to list
print (marks,id(marks),type(marks))
l=list(marks)
print (l,id(l),type(l))#tuple converted to list and sorted the elements
l.sort()
print (l)
marks=tuple(l) #again its converted to tuple its secured now
print (marks)
#list to tuple
l=[10,20,30]
l.sort(reverse=True)
print (l)
t=tuple(l) #secured
print (t)
#string to list conversion
s="python"
l=list(s)
print (l,type(l),type(l))
#list to string
l=[1,2,3]
s=str(l)
print (s,type(s))
#string to tuple
s="python"
t=tuple(s)
print (t,type(t))
t=(1,2,3)
s=str(t)
print (s,type(s))
#nested tuples tuple inside tuple
a=(1,2,3,(10,20,30),4)
print (a,type(a))
print (a[3])
print (a[3][0])
print (a[3][2])










