#opearations on special strings on slicing
c="python Full stack"
print (c[4:])
print (c[4:30]) #here 30:4 not possible
print (c[ :15])
print (c[ : ])
print (c[0:])
print (c[ : :1])
print (c[ : :-1]) #rivers string same output
print (c[16 : :-1]) #same output
print (c[16 : :1])
#examples
print (c[1:11])
print (c[1:11:1])
print (c[1:11:2])  #positive step index values
#negative step index values
print (c[11:1:-1]) #rivers string
print (c[11:1:-4])
print (c[16:2:-4])
print (c[-5:-16:-1])
print (c[-6:-16:-1]) # when n
# egative step index value   either positive or negative must be higher then exclusive value
print (c[13:5:-1])
print (c[5:13:-1]) # not possible values
print (c[-2:-5:-1])
print (c[16:-1:-1]) #not possible
print (c[16:1:-1])
print (c[13:2:-2]) #her3 one more logic exclusive value is shouldn't be negative value then when step value negative
print (c[-13:-2:2]) #rivers string
print (c[16:0:-1])







