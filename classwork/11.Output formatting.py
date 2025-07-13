#Basic Examples of print()
#a) Printing Text
print("hello everyone")
print("good morning")
print("what are you doing")

#b) Printing Multiple Items
name='shivani'
age=21
print("name:",name,"age:",age)
x=(1,2,3)
y=(3,4,5)
print("x:",x,"y:",y)#x: (1, 2, 3) y: (3, 4, 5)

#c) Using sep to Change the Separator
print("nani","soni","junnu",sep='-')#nani-soni-junnu
print("2025","8","07",sep=('/'))#2025/8/07

#d) Using end to Control Line Endings
print("x,",end=" ")
print("y")#x, y

#Printing Special Characters
print("line1\nline2")
print("name:\tshivani")

#Output Formatting
#1️⃣Using Commas (Simple Print Method)
name='shivani'
age=12
score=23
print("name:",name,"age:",age,"score:",score)

#2️⃣Using Modulo Operator (% Formatting)
name='shivani'
age=12
score=23.0
print("name:%s,age:%d,score:%.2f"%(name,age,score))#name:shivani,age:12,score:23.00

#3️⃣Using f-strings (Formatted String Literals) — Python 3.6+
name='shivani'
age=12
score=23.0
print(f"name:{name}|age:{age}|score:{score}")

#4️⃣Using str.format() Method
name='shivani'
age=12
score=23.0
print("name:{},age:{},score:{}".format(name,age,score))