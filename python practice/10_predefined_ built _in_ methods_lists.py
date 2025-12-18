#predefined methods or built in methods in list
#append():to add elements at the end of the list
marks=[49,48,44,46,47,48,35,39,50]
print (marks,id(marks),type(marks))
marks.append(49)
print (marks)
marks=[49,48,44,46,47,48,35,39,50]
marks1=[33,44,49]
print (marks,id(marks),type(marks))
print (marks.append(marks1)) #using append function list in sublist added
print (marks)
print (marks[0])
print (marks[8])
print (marks[9])
print (marks)
print (marks[9][1])
print (marks[9][2])
#copy():to create duplicate copy
marks=[49,48,44,46,47,48,35,39,50]
print (marks,id(marks),type(marks))
marks1=marks.copy()
print (marks1,id(marks1),type(marks1))
#clear function using
marks1.clear()   # as it is copy duplicate copy deleted
print (marks1,id(marks1),type(marks1))
print (marks,id(marks),type(marks)) #as it is
marks=[49,48,44,46,47,48,35,39,50]
print (marks,id(marks),type(marks))
marks2=marks
print (marks2,id(marks2),type(marks2))
marks2.clear() #here i observed without copy doing it is cleared org copy also it is affected both
print (marks2,id(marks2),type(marks2))
print (marks,id(marks),type(marks))
#count():to retrieve the element numb of times that an element occurs in list
marks=[49,48,44,46,47,48,35,39,50]
print (marks.count(44))
print (marks.count(48))
print (marks.count(35))
#one more example of append function
marks=[49,48,44,46,47,48,35,39,50]
marks1=[22,33,44]
print (marks.append(marks1)) #sublist added
print (marks)
#extend():to add the elements of a list end of the another list it will add elements independent
#but in append function it will store like sublist to overcome that extend func using
marks=[49,48,44,46,47,48,35,39,50]
print (marks,id(marks),type(marks))
marks1=[33,44,49]
print (marks.extend(marks1))
print (marks)
#index():to get the index first occurs of the element
marks=[49,48,44,46,47,48,35,39,50,22,33,44]
print (marks,id(marks),type(marks))
print (marks.index(33))
#Index from list to list
marks=[49,48,44,46,47,48,35,39,50,[22,33,44]] #sublist index
print (marks,id(marks),type(marks))
print (marks[9].index(33))
marks=[49,48,44,46,47,48,35,39,50]
print (marks,id(marks),type(marks))
print (marks.insert(-1,33))
print (marks)
print (marks.insert(-8,22))
print (marks)
#examples
marks3=[]
print (marks3.count(33)) #for example marks3.index(33) it is x is not in the list
marks3=[]
marks3.insert(0,11)
print (marks3)
marks3=[]
marks3.insert(5,11)
print (marks3)
print (marks3.index(11))
#pop():remove last element from the list
marks=[49,48,44,46,47,48,35,39,50]
marks.pop()
print (marks)
marks.pop()
print (marks)
print (marks.pop()) #here pop function will give back output it will show in extend it don't show
print (marks)
#extend():
marks=[49,48,44,46,47,48,35,39,50]
marks1=([22,33,44])
marks.extend(marks1) #here when we keep in print statement it will show us none
print (marks)
#pop index():if we want to remove particular element to remove
marks=[49,48,44,46,47,48,35,39,50]
print (marks.pop(3))
print (marks)
marks.pop(-1) #here we are removing particular element what we want with index values
print (marks)
#remove():remove first occur of an element
marks=[49,48,44,46,47,48,35,39,50]
marks.remove(48) #here we are removing values by directly an element not using index to remove
print (marks) #here observing if we keep print statement it shows none statement
marks=[49,48,44,46,47,48,35,39,50]
print (marks.pop(-4)) #keeping in print statement its showing value which value is removing
print (marks) #that's the difference to keep print statement
marks.remove(39)
print (marks)
#reverse():it rivers the list
marks=[49,48,44,46,47,48,35,39,50]
marks.reverse()  #it revers  the string
print (marks)
print (marks[ : :-1])   #here we used slicing step value method it rivers the  string
#sort():sort the elements in ascending order
marks=[49,48,44,46,47,48,35,39,50]
marks.sort()
print (marks)
print (marks[0])
print (marks[1])
marks.sort(reverse=True)
print (marks)
print (marks[0])
print (marks[1])
#del and nested lists
marks=[49,48,44,46,47,48,35,39,50] #del means  eliminating value from the list
del marks[2]
print (marks)
marks=[49,48,44,46,47,48,35,39,50]
del marks[2:6]
print (marks)
marks=[49,48,44,46,47,48,35,39,50] #just list elements cleared
marks.clear()
print (marks)
marks=[]
marks.append(10)
print (marks)
#list to list is nested list and list to sublist inside
marks=[49,48,44,46,47,48,35,39,50,[22,33,44],22,11,33,[23,43],88]
print (marks[13])
print (marks[13][0])
marks=[49,48,44,46,47,48,35,39,50,[22,33,[1,2,3],44],22,11,33,[23,43],88]
print (marks[9])
print (marks[9][2])
print (marks[9][2][1])
print (marks[9][2][2])
print (marks[9])
print (marks[0:15])
print (marks[9][2].index(2))












































