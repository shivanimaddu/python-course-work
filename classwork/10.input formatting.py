# ###Input Formatting

#1.String Input
name=input("enter your name:")
print(name)#enter your name:shivani

#2. Integer Input
num=int(input("enter your num:"))
print(num)#enter your num:2
#3. Float Input
dis=float(input("enter your dist%:"))
print(dis)#enter your dist%:2.3
##4. Input as List (Space-separated)
name=input("enter name:").split()
print(name)#['shivani', 'nani','junnu']

#List of Integers
lis1=list(map(int, input("enter list:").split()))#[1, 2, 4]
print(lis1)
##List of Floats
height=list(map(float,input("enter heights:").split()))
print(height)#[3.4, 45.9]

#Tuple Input
coordinates=tuple(map(int,input("enter your x & y:").split()))
print(coordinates)#(1, 2)

# Set Input
roll_no=set(map(int,input("enter roll num:").split()))
print(roll_no)

#Dictionary Input using eval()
login=eval(input("enter user profile as dict:"))
print(login)#{'name': 'shivani', 'psw': 1235} 

#11. Multiple Inputs with Unpacking
username,password=input("enter your username and password:")
print("username:",username)
print("password:",password)
      



