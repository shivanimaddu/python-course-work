#POSITIONAL ARGUMENTS
def display(name,pwd,email):
    print(name,email,pwd)
name,email,pwd='nani','nani@gmail.com','nani@1020'
display(name,pwd,email)
#keywords arguments:
def display(name,email,pwd):
    print(name,email,pwd)
name,email,pwd='nani','nani@gmail.com','nani@1020'
display(name='nani',email='nani@gmail.com',pwd='nani@1020')
#variable-length
def display(*var):
    print(var)
name,email,pwd='nani','nani@gmail.com','nani@1020'
display(name,email,pwd)
#keyarguments
def display(**var):
    print(var)
name,email,pwd='nani','nani@gmail.com','nani@1020'
display(name='nani',email='nani@gmail.com',pwd='nani@1020')
#default
def display(name,pwd,email,status='absent'):
    print(name,email,pwd,status)
name,email,pwd='nani','nani@gmail.com','nani@1020'
display(name,pwd,email)

'''
1=1
2=1*2
3=1*2*3
4=1*2*3*4
'''
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact    
n=int(input("Enetr the number:"))
for i in range(1,n+1):
    print(f"{i}!={factorial(i)}")

