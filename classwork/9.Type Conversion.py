a=10
print(float(a))#10.0
a_str=str(a)
print(a_str)#10
print(bool(a))#True

b=10.90
print(int(b))#10
b1=str(b)
print(b1)#10.91
print(bool(b))#True

c='shivani'
print(bool(c))#True
print(list(c))#['s', 'h', 'i', 'v', 'a', 'n', 'i']
print(tuple(c))#('s', 'h', 'i', 'v', 'a', 'n', 'i')
print(set(c))#{'i', 's', 'h', 'v', 'n', 'a'}  

d=[1,2,56,890]
d1=str(d)
print(d1)#[1, 2, 56, 890]
print(bool(d))#True
print(tuple(d))#(1, 2, 56, 890)
print(set(d))#{56, 1, 2, 890}

e=(2,4,6,8)
print(str(e))
print(bool(e))#True
print(list(e))#[2, 4, 6, 8]
print(set(e))#{8, 2, 4, 6}

f={8,9,10}
print(str(f))
print(list(f))#[8, 9, 10]
print(bool(f))#True
print(tuple(f))#(8, 9, 10)

dict_g={1:2,2:2,3:3}
print(list(dict_g))#[1, 2, 3]
print(tuple(dict_g))#(1, 2, 3)
print(set(dict_g))#{1, 2, 3}
print(bool(dict_g))#True

#9. Dictionary Conversion
d=[('name','nani'),('btach','22'),('sub','python')]
print(dict(d)){'name': 'nani', 'btach': '22', 'sub': 'python'}