#set is store collection of unique elements not allowed redundant values sets is a unordered
#does not maintain index, set is a mutable and some internal hashing will perform
s1={10,20,30}
print (s1,type(s1))
s2={"hi",20,True} #it doesn't maintain insertion order
print (s2,type(s2))
s3=set()
print (s3,type(s3))
s4={} #if we not mention  set fun it receives dictionary so must use set fun
print (s4,type(s4))
l=[10,20,30]
s=set(l)
print (s,type(s)) #list converted to set
t=(10,20,30)
s=set(t)
print (s,type(s)) #tuple converted to set
t=(10,20,30,10,20,30)
s=set(t)
print (t)
print (s,type(s))
print (t[0])
print (t[3])
print (t[-1])
s={10,20,(1,2)} #according to hash values it will generate
print (s,type(s))
#built in methods in sets
#add():to add new elements
s={44,10,33,22,67,98,45,66,87,33}
print(s,type(s))
s.add(88)
print(s,type(s))
s.add((55,66,77))
print(s,type(s))
s.clear() #to clear elements from the list
print(s,type(s))
#copy():to create a duplicate copy
s={"java","python","pHp"}
s1=s.copy()
print(s1,type(s1))
print(id(s),id(s1)) #seperate copies
#difference function:it returns difference from the set
s1={"java","python","pHp"}
s2={"pHp","HTML","CSS"}
print(s1.difference(s2)) #only it occurs s1
print(s2.difference(s1))#only it occurs s2
print(s1,s2) #orginal sets is as it is
print(s1.difference_update(s2))
print(s1,s2) #direct modification
#remove:to remove element from the set
s2.remove("CSS")
print(s2)
s1.remove("java")
print(s1)
#discard:to remove element from the set
s1={10,20,30}
s1.discard(20)
print(s1)
s1.discard(50) #existing number dont showing error
print(s1)
#intersection:returns intersection of the set
s1={"java","python","pHp"}
s2={"pHp","HTML","CSS"} #they occur common elements from the sets
print (s1.intersection(s2))
print(s1,s2)
print(s1.intersection_update(s2)) #intersection update will direct modification
print(s1,s2)
#disjoint:it returns whether two sets intersection or not
s1={"java","python","pHp"}
s2={"pHp","HTML","CSS"}
print (s1.isdisjoint(s2))
s1={1,2}
s2={3,4}
print (s1.isdisjoint(s2))
#issubset and superset
s1={1,2,3,10,20,5,6,7}
s2={10,20}
print (s1.issubset(s2))
print (s2.issubset(s1))
print (s1.issuperset(s2))
print (s2.issuperset(s1))
a={1,2,6}
b={1,2,3,4,5}
print (a.issuperset(b))
print (b.issuperset(a))
print (a.issubset(b))
print (b.issuperset(a))
#pop:it removes any arbitrary element(because unordered internal element
s1={1,2,3,5,6,7,10,20}
print (s1.pop())
print(s1,type(s1))
print (s1.pop())
print(s1,type(s1))
s1={23,11,54,34,12}
print (s1.pop())
print(s1,type(s1))
#symmentric difference:it removes the common elements and keeps the unique ones
s1={"java","python","pHp"}
s2={"pHp","HTML","CSS"}
print (s1.symmetric_difference(s2))
s1.symmetric_difference_update(s2)
print(s1,s2)
#union:combining all unique elements from both sets it removes duplicates automatically
s1={"java","python","pHp"}
s2={"pHp","HTML","CSS"}
print (s1.union(s2))
print(s1,s2)
s1.update(s2)
print(s1,s2)













