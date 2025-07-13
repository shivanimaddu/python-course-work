#1.Arithmetic Operators

a=110
b=10
print("Addition(+):",a+b)#Addition(+): 120
print("Subsraction(-):",a-b)#Subsraction(-): 100
print("Multiplication(*):",a*b)#Multiplication(*): 1100
print("Division(/):",a/b)#Division(/): 11.0
print("Floor Divison(//):",a//b)#Floor Divison(//): 11
print("Modulus(%):",a%b)#Modulus(%): 0
print("Exponential(**):",a**b)#259374246010000000000

#2.Comparison Operators
a=10
b=12
print("Equal to(==):",a==b)#False
print("Not Equal to(!=):",a!=b)#True
print("Greater than(>):",a>b)#False
print("less than(<):",a<b)#True
print("Greater than or Equal to(>=):",a>=b)#False
print("Less than or Equal to(<=):",a<=b)#True

#3. Assignment Operators
x=10
x+=5#Add & Assign(+=): 15
print("Add & Assign(+=):",x)
x-=10#Subtract & Assign(-=): 5
print("Subtract & Assign(-=):",x)
x*=3#Multiply & Assign(*=): 15
print("Multiply & Assign(*=):",x)
x/=2#Divide & Assign(/=): 7.5
print("Divide & Assign(/=):",x)
x//=2#Floor Divide & Assign(//=): 3.0
print("Floor Divide & Assign(//=):",x)
x%=4#Modulus & Assign(%=): 3.0
print("Modulus & Assign(%=):",x)
x**=2#Exponentiate & Assign(**=): 9.0
print("Exponentiate & Assign(**=):",x)

#4. Logical Operators (Using Logic Gates)

'''***AND***
A   B  A and B(T=TRUE,F=FALSE)
T   T     T
F   T     F
T   F     F
F   F     F
 ***OR***
A   B   A or B
T   T    T
F   T    T
F   F    F
T   F    T
 ***NOT***
A   not A
T    F
F    T'''

x=10
y=26
print(x>5 and y<30)#True
print(x>15 or y<30)#True
print(not(x>18))#True

#5. Membership Operators

fruits=["apple","banana","orange"]
print("apple" in fruits)#True
print("mango" not in fruits)#True

#6. Identity Operators

a=[1,2,3]
b=a
c=[1,2,3]
print(a is b)#True
print(a is c)#False
print(a is not c)#True

#7. Bitwise Operators (With Binary Representation)
'''Logic Gates Truth Table (for bits 0 and 1)
A   B  A and B  A OR B A XOR B  NOT A 
0   0     0       0       0     1
0   1     0       1       1     1
1   0     0       1       1     0 
1   1     1       1       0     0'''
x=10
y=20

print("AND(&):",x&y)#AND(&): 0
print("OR(|):",x|y)#OR(|): 30
print("XOR(^):",x^y)#XOR(^): 30
print("NOT(~):",~x)#NOT(~): -11
print("Left Shift(<<):",x<<y)#Left Shift(<<): 10485760
print("Right Shift(>>):",x>>y)#Right Shift(>>): 0





