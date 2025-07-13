# Empty Tuple
T=()
print(type(T))#<class 'tuple'>  
t=()
t=tuple()#<class 'tuple'>

#2. Accessing Tuple Elements
#a. Indexing
t=(1,2,3,'shivani')
print(t[2])#3
#b. Negative Indexing
t=(1,2,3,4,5,6)#5
print(t[-2])
#c. Slicing
x=(1,2,3,4,5,6,77,8,0)#(2, 3, 4)
print(x[1:4])
print(x[::-1])#(0, 8, 77, 6, 5, 4, 3, 2, 1)
print(x[0:6])#(1, 2, 3, 4, 5, 6)

#3. Operations on Tuples
#a. Concatenation
x=(1,2,3,4)
y=(5,6,7,8)#(1, 2, 3, 4, 5, 6, 7, 8)
z=x+y
print(z)
names=('shivani','nani','junnu')
names2=('nani','raju','soni')
names3=names+names2#('shivani', 'nani', 'junnu', 'nani', 'raju', 'soni')
print(names3)
#b. Repetition
a=(1,2)#(1, 2, 1, 2, 1, 2, 1, 2)
print(a*4)
#c. Membership Testing
a=(1,2,3,4,5)
print(2 in a)#True
print(6 not in a)#True
#d. Tuple Unpacking
x=(1,2,34,6,7,8)
a,b,c,d,e,f=x
print(a,b,c,d,e,f)#1 2 34 6 7 8

#4. Tuple Methods
#count(x)
x=(1,2,3,4,3,4,5,67,7,7)
print(x.count(3))#2
#index(x)
print(x.index(5))#6

#5. Built-in Functions for Tuples
#len(tuple)
print(len(x))#10
print(max(x))#67
print(min(x))#1
print(sum(x))#103
x=(1,2,3)
y=(tuple([1,2,3]))#(1, 2, 3)
print(y)

#6. Immutability and Tuple Behavior
tuple=(1,[2,3])
tuple[1][0]=90#(1, [90, 3])
print(tuple)



