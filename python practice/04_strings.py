#strings examples
course="python programming"
platform='twg'
print (course,type(course))
print (platform,type(platform))
address="""Telangana,
hyderabad,
india"""
print(address)
course='''software
engineering 
mathematics '''
print(course)
#operations on string collection of char or set of elements storing in order
c="python Full stack"
print (c[4])
print(c[8]) # we can retrieve all elements by indexing numbers
print(c[11])
print (len(c))
#here (c[len(c)]) c len c index is 17 there is no value 17 index (interview question
print(c[len(c)-1])
#negative indexing
print (c[-1]) # like this we can access negative index by values
print(c[-5])
print  (c[-len(c)])
print (-len(c))
#print c of 20 value index is not available
#slicing  accessing range of multiple elements
c="python Full stack"
print (c[4:8])
print (c[0:4]) #slicing positive values direction should be in forward
print (c[5:10]) # and must be inclusive value should be smaller then exclusive
print (c[10:15])  # it dont print 15:10 is gives empty
#negative slicing indexing
print (c[-15:-9]) # here -9:-15 not possible negative or either positive there should be must be inclusive value lesser
print (c[4:-2])
print (c[-17:4]) # 4:-17 it won't perform backward direction











