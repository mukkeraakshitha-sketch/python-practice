#lists are  collection of multiple values stored in single variable and sequence related datatype
marks=[] #empty list
print (marks,id(marks),type(marks))
marks=list()
print (marks,id(marks),type(marks))
marks=[45,49,"twg",3.2,2+3j,True]
print (marks,id(marks),type(marks)) #list can accept any datatype
marks=[49,48,44,46,47,48,35,39,50] #non empty list accessing values
print (marks[5])
print (marks[-6])
print (marks[-3])
print (marks[-9]) #here marks 9 index number value can't retrieve because there is no value positive index 9
#slicing examples
print (marks[4:8])
print (marks[8:4])
print (marks[-6:-2])
print (marks[2:8])
print (marks[2:8:2])
print (marks[8:2:-2])
print (marks[-6:-2:1]) #step index value -1 if we give it will happen empty list
print (marks[-2:-6:-1])  #if we want to give step index value -negative inclusive value must be higher value
print(marks[-6:-2:-1])
#special operations
marks=[49,48,44,46,47,48,35,39,50]
print (marks[1:])
print (marks[ :7])
print (marks[:])
print (marks[::-1]) #rivers string
print (marks[-5: ])
print (len(marks))
print (len(marks)-1)
print (-len(marks))
 #list index out of range value interview question print (marks[len(marks)])
 


