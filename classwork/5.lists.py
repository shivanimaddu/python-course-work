#Creating Lists
#2.1 Empty List
a=[]
print(type(a))#<class 'list'>

#2.2 List with Elements
x=[1,2,3,4,5]## List of integers
y=["apple","banana","cherry"]## List of strings
print(x)
print(y)

#2.3 List with Nested Lists
nested_list=[[1,2,3],['a','b','c'],[True,False]]
print(nested_list)#[[1, 2, 3], ['a', 'b', 'c'], [True, False]]       

#2.4 List using list() Constructor
list_from_tuple=list((1,2,3))
my_list=list(list_from_tuple)#[1, 2, 3]
string_to_list=list("shivani")
my_list1=list(string_to_list)#['s', 'h', 'i', 'v', 'a', 'n', 'i']
print(my_list1)
print(my_list)

x=list((1,2,3))#[1, 2, 3]
y=list(x)
print(y)

##3. Accessing Elements in a List
#3.1 Using Indexing (Positive & Negative)
x=['shivani','nani','junnu']
print(x[1])#nani
print(x[-1])#junnu
print(x[0])#shivani

#3.2 Using Slicing
a=[1,2,3,4,5,6,7]
print(a[0:5:1])#[1, 2, 3, 4, 5]
print(a[:4])#[1, 2, 3, 4]
print(a[::1])#[1, 2, 3, 4, 5, 6, 7]
print(a[-5:-1])#[3, 4, 5, 6]
print(a[:6])#[1, 2, 3, 4, 5, 6]

#4. Modifying Lists
#4.1 Changing Elements
x=[10,20,30,50,60]
x[3]=40#[10, 20, 30, 40, 60]
print(x)
#4.2 Adding Elements
x.append(50)#[10, 20, 30, 40, 60, 50]
x.insert(1,30)#[10, 30, 20, 30, 40, 60, 50]
print(x)
x.extend([70,80,90,100])#[10, 30, 20, 30, 40, 60, 50, 70, 80, 90, 100]
print(x)
#4.3 Removing Elements
x=[1,2,3,4,5]#[1, 2, 3, 5]
x.remove(4)
print(x)
x.pop(3)#[1, 2, 3]
print(x)
x.pop()#[1, 2]
print(x)
del x[0]#[2]
print(x)
x.clear()#[]
print(x)
x=[1,2,3,4,5,4,4,4,4,9,8,10]
#print(x.count(4))#5
x=[1,2,78,90,3456,34567,34556]
x.sort()#[1, 2, 78, 90, 3456, 34556, 34567]
print(x)
x.reverse()#[34567, 34556, 3456, 90, 78, 2, 1]
print(x)
x=[1,2,3,4]
y=x.copy([])#[1, 2, 3, 4]
print(x)
