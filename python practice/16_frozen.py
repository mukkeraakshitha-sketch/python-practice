l=[10,20,30]
f=frozenset(l)#frozenset is immutable can't change after creation
print(f,type(f)) #and we cannot add or remove elements ones after we creation clear not performed
s1={"java","python","pHp"}
s2={"pHp","HTML","CSS"}
fs1=frozenset(s1)
fs2=frozenset(s2)
print (fs1.difference(fs2)) #update can't possible
print (fs1.intersection(fs2)) #update can't possible
print (fs1.isdisjoint(fs2))
print (fs1.issubset(fs2))
print (fs1.issuperset(fs2))
print (fs1.symmetric_difference(fs2)) #symmetric difference possible
print(fs1.union(fs2)) #update not possible
s1={10,20,(1,2)}
print(s1) #its only immutable can perform because frozenset is immutable
#bytes: immutable
l=[65,66,67]
b=bytes(l)
print(l)
print(b) #bytes representation
print (b[0])
print (b[1])
print (b[2])
l=[65,66,67]#bytearraY
c=bytearray(l)
print(c)
print (c[0])
c[0]=68
print(c)
#memoryview
s="ABC"
print(s,type(s))
s1=b"ABC"
print(s1,type(s1))
m=memoryview(bytearray(b"ABC"))
print (m[0]) #in bytes number adding not accept
s1=bytearray(b"ABC")
m=memoryview(bytearray(s1))
m[0]=97
print (m) #it shows memory
#range:
a=[40,41,42,.50]
b=range(40,51)
range(40,51)
print(b)
for i in b:
    print(i)
c=range(101)
print(c)
for i in c:
    print(i)
c=range(1,101,5)
print(c)
for i in c:
    print(i)
c=range(100,1,-5)
print(c)
for i in c:
    print(i)
#none:nothing is there
l=(10,20,30)
d=dict.fromkeys(l)
print(d)
print(d.update({10:'python'}))
print(d)

