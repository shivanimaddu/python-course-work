#1.Numeric type
a=10                         #<class 'int'>
b=100.99                     #<class 'float'>
z=5+2j                       #<class 'complex'>
print(type(a),type(b),type(z))

#2.Sequence type
names="Shivani,Nani,junnu"#<class 'str'>
print(type(names))
items=["Apple","Banana","Cat"]#<class 'list'>
print(type(items))
t=(20,'jessa',35.75,[30,90,90])#<class 'tuple'>
print(type(t))

#3.Set
set1={1,2,3,4,5,5}#<class 'set'>
print(type(set1))
print(set1)#{1, 2, 3, 4, 5}
h={1,2,34,4,4,5}
print(type(h))#<class 'set'>
d=frozenset(h)#frozenset({1, 2, 34, 4, 5})
print(d)

#4.Mapping
py_dict={1:'apple',2:'banana'}#<class 'dict'>
print(type(py_dict))

#5.Boolean type
a=True#<class 'bool'>
print(type(a))

#6.NONE
a=None#<class 'NoneType'>
print(type(a))