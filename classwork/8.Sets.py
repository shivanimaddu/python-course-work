s=set()
s={1,2,3,4,5,6,7}#{1, 2, 3, 4, 5, 6, 7}
print(s)
s={1,2.3,"shivani",(1,2,3),3+8j}#{1, 2.3, 'shivani', (1, 2, 3), (3+8j)}
print(s)

#3. Operations on Sets
#a. Membership Testing
names={'shivani','junnu','nani','jyothi'}
print('shivani'in names)#True
print('shiva'not in names)#True
#b. Union (| or union() method)
set1={1,2,3}
set2={3,4,5}
result=set1 | set2
print(result)#{1, 2, 3, 4, 5}
result=set1&set2
print(result)#{3}
result=set1-set2
print(result)#{1, 2}
result=set1^set2
print(result)#{1, 2, 4, 5}
print(set1<=set2)#False
print(set1>=set2)#False
print(set1.isdisjoint(set2))#False

#4. Built-in Methods for Sets
x={1,2,3}
x.add(4)
print(x)##{1, 2, 3, 4}
x.remove(3)#{1, 2, 4}
print(x)
x.discard(5)#does not raise an error
print(x)
x.pop()#{2, 4}
print(x)
x.clear()
print(x)#set()
set1={1,2,3}
set2={3,4,5}
print(set1.difference(set2))#{1,2}
print(set1.symmetric_difference(set2))#{1, 2, 4, 5}
(set1.update(set2))#{1, 2, 3, 4, 5}
print(set1)
(set1.intersection_update(set2))
print(set1)
(set1.difference_update(set2))
print(set1)#set()
set1={1,2,3}
set2={3,4,5,6}
set1.symmetric_difference_update(set2)
print(set1)#1, 2, 4, 5, 6}

#set(iterable)
x=set([3,1,2,3])
print(x)#{1, 2, 3}
#frozen
f=frozenset([1,2,3])
print(f)
#frozenset({1, 2, 3})
