#dictionary is a collection used to store data in key value pairs keys must be unique
emp1={"empname":"xyz","age":20,"exp":3,"skill":"python","desig":"developer"}
print(emp1,type(emp1))
emp2={1:"xyz",2:20,3:3,4:"python",5:"developer"}
print(emp2,type(emp2))#here index is not possible
print (emp1["empname"])
print (emp1["age"])
print(emp1["desig"])
print(emp2[3])
print(emp2[4])
print(emp2[5])
employees={}
print(employees,type(employees))
#built in methods in dict:
emp1.clear()
print(emp1,type(emp1))
emp1={"empname":"xyz","age":20,"exp":3,"skill":"python","desig":"developer"}
print(emp1,type(emp1))
emp2=emp1.copy()
emp1.clear()
print(emp1,type(emp1))
print(emp2,type(emp2))
#fromkeys:returns a new dictionary with the specified keys and value
marks={'s1':0,'s2':0,'s3':0,'s4':0} #we don't have to create manually
students=('s1', 's2', 's3', 's4')
marks1=dict.fromkeys(students)
print(marks1,type(marks1))
marks2=dict.fromkeys(students,40)
print(marks2,type(marks2))
marks3=dict.fromkeys(students,100)
print(marks3,type(marks3))
marks4=dict.fromkeys(students,[50,60,70,100])#it's not stored in different keys
print(marks4,type(marks))
rnos=(11,22,43,54)
interested=dict.fromkeys(rnos,"singing")
print(interested,type(interested))
print (interested[11])
print (interested[22])
#get():to retrieve the value of specified key
emp={"empname":"xyz","age":20,"exp":3,"skill":"python","desig":"developer"}
print(emp)
print (emp["age"])
print(emp["empname"])
#items=returns list of tuples
print (emp.items()) #emp items it is developer has very convenient
#values:returns list of only values
print (emp.values())
#keys:returns list of only keys
print (emp.keys())
#popitem():removes the last element
print (emp.popitem())
#pop(key):removes the element specified key
print (emp.pop("age"))
#set default:inserts the key value pair
print (emp.setdefault("location","hyd"))
print(emp)
print (emp.setdefault("skill","java"))
#update():ignores the statement
print (emp.update({"age":30}))
print(emp)
print (emp.update({"location":"hyd"}))
print(emp)
























