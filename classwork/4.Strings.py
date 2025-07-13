# Defining strings
a='shivani'
b='nani'
print(a)#shivani
print(b)#nani
print(type(a),type(b))#<class 'str'> 

#Operations on Strings
## Concatenation
a='shivani'
b='nani'
result=a +' '+ b#shivani nani
print(result)
## Repetition
print("Nani"* 3)#NaniNaniNani
## Indexing
a="hai shivani"
print(a[3])#i
print(a[-3])#a
## Slicing
print(a[0:3])#hai
print(a[ :6])#hai sh
## Membership
print('shi' in a)#True
print('no' not in a)#True

      
#Built-in String Functions     
## 1. len()
text="hello shivani"
print(len(text))#13
## 2. max() and min()
print(max("abcdXYZW"))#d by ASCII VAULE
print(min("abcdXYZW"))#W BY ASCII VAULE
## 3. sorted()
print(sorted("python"))
## 4. chr() and ord()
print(ord('A'))#65
print(chr(97))#a

#1.Complete List of Python String Methods with Examples
a="hello nani"
print("hello nani".upper())#HELLO NANI
b="HAI"
print("HAI".lower())#hai
print("hello nani".capitalize())#Hello nani
print("hello nani".title())#Hello Nani
x="PythoN","sterß"
print("PythoN".swapcase())  #pYTHOn
print("sterß".casefold())  #sterss

#2. Alignment & Formatting Methods
a="python"
b=10
print("python".center(20,"*"))#*******python*******
print("python".ljust(12,"*"))#python******
print("python".rjust(12,"*"))#******python
print("10".zfill(4))#0010
name="tom"
age="25"
print("Name:{},Age:{}".format("tom",25))#Name:tom,Age:25
print("{name} is {age}".format_map({'name':'tom','age':25}))#tom is 25

#3. Search & Find Methods
a='hello'
print("hello".find('e'))#1
print("hello".rfind('l'))#3
print("hello".index('l'))#2
print("hello".rindex('l'))#3
print("hello".count('l'))#2

#4. String Testing Methods (Boolean Results)
text='python','abc123',"  "
print('python'.startswith('py'))#True
print('python'.endswith('py'))#False
print('python'.isalpha())#True
print('abc123'.isalnum())#True
print('python'.islower())#True
print('python'.isupper())#False
print("  ".isspace())#True
print('python'.title())#Python
print('python'.isidentifier())#True

#5. Replace & Modify Methods
x='apple'
print('apple'.replace("p","a"))#aaale
print('apple'.translate('apple'.maketrans("a","x")))#xpple

#6. Splitting & Joining Methods
x='a','b','Hello\nWorld'
print('a,b'.split(" , "))#['a,b']
print('a,b'.rsplit(" , "))#['a','b']
print('Hello\nWorld'.splitlines())#['Hello', 'World']
print(" ".join(["Hello","World"]))#Hello World
print("Hello\nWorld-pie".partition("-"))#('Hello\nWorld', '-', 'pie')
print("Hello\nWorld-pie".rpartition("-"))#('Hello\nWorld', '-', 'pie')

#7. Whitespace & Trimming Methods
x="hello"
print("hello".strip())#hello
print("     hello     ".lstrip("*"))#hello
print("    hello".rstrip("-"))#hello

#8. Encoding & Decoding Methods
x="shivani"
print("hello".encode())#b'hello'
print(b'hello'.decode())#hello










      

      


