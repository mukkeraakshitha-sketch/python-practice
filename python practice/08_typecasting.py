# type casting conversions of one datatype to another datatype possible types
a=10
b=20   #normal example
print(a+b)
#concatination with string
a="10"
b="20"
print(a+b)
#Type casting examples
a=int("10")
b=int("20")
print(a+b)
#int examples with all datatypes
a=3.2
print (a,id(a),type(a)) #yes here float converted into integer
b=int(a)
print (b,id(b),type(b))
a=True
print (a,id(a),type(a)) #bool is accepted to int
b=int(a)
print (b,id(b),type(b))
a=2+3j
print (a,id(a),type(a)) #complex datatype is not converted to int
a="10"
print (a,id(a),type(a)) #only here string with integer only possible and no other datatypes converted into strings
b=int(a)
print (b,id(b),type(b)) #string with integer value accepted and it converted into string
a="10.2"
print (a,id(a),type(a)) #string with float not accepted
#string with bool not accepted and string with complex also not accepted
#float conversions
a=10
print (a,id(a),type(a)) #int with float accepted
b=float(a)
print (b,id(b),type(b))
a=True
print (a,id(a),type(a)) #bool with float accepted
b=float(a)
print (b,id(b),type(b))
#complex not converted into float because it has imaginary part
a="10"
print (a,id(a),type(a))
b=float(a)
print (b,id(b),type(b))
a="10.2"
print (a,id(a),type(a))
b=float(a)
print (b,id(b),type(b))
#string with bool and string with text format not possible float conversion
#Boolean conversions
a=1
print (a,id(a),type(a)) #boolean accepted all datatypes
b=bool(a)
print (b,id(b),type(b))
a=3.2
print (a,id(a),type(a))
b=bool(a)
print (b,id(b),type(b))
a=2+3j
print (a,id(a),type(a))
b=bool(a)
print (b,id(b),type(b))
a="10"
print (a,id(a),type(a))
b=bool(a)
print (b,id(b),type(b))
a="10.2"
print (a,id(a),type(a))
b=bool(a)
print (b,id(b),type(b))
a="twg"
print (a,id(a),type(a))
b=bool(a)
print (b,id(b),type(b))
#complex conversions with all data types only errors are string with bool and string with text not conv to complex
a=10
print (a,id(a),type(a)) #int value accepted complex
b=complex(a)
print (b,id(b),type(b))
a=10.3
print (a,id(a),type(a)) #float converted into complex
b=complex(a)
print (b,id(b),type(b))
a=True
print (a,id(a),type(a)) #bool converted to complex
b=complex(a)
print (b,id(b),type(b))
a="10"
print (a,id(a),type(a)) #string with int value converted into complex
b=complex(a)
print (b,id(b),type(b))
a="10.3"
print (a,id(a),type(a)) #string with float value converted into complex
b=complex(a)
print (b,id(b),type(b))
#string with bool value not converted to complex
#string with text value not converted to complex
a="2+3j"
print (a,id(a),type(a))
b=complex(a)
print (b,id(b),type(b))
#string conversions
a=10
print (a,id(a),type(a))
b=str(a)
print (b,id(b),type(b))
a=10.4
b=str(a)
print (b,id(b),type(b))
a=True
b=str(a)
print (b,id(b),type(b))
a=2+3j
b=str(a)
print (b,id(b),type(b))
a="10"
b=str(a)
print (b,id(b),type(b))
a="10.2"
b=str(a)
print (b,id(b),type(b))
a="TWG"
b=str(a)
print (b,id(b),type(b)) #string datatypes all are accepted









