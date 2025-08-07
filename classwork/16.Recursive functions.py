#pass by value:
def update(n):
    print("Before-inside of the function:",n)
    n+=10
    print("After-inside of the function:",n)
n=10
update(n)    
print("outside of the funtcion:",n)
##Recursive
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
n=int(input("Enter the value:"))
print(factorial(n))
#sum
def sum(n):
    if n==1:
        return 1
    return n+sum(n-1)
n=int(input("Enter the value:"))
print(sum(n))
#sum of digits
n=int(input("Enter the number:"))
sum=0
while n>0:
    sum=sum+ (n%10)
    n=n//10
print(sum)  

n=int(input("Enter the vaule:"))
def sum(n):
    if n==0:
        return 0
    return n%10+sum(n//10)
print(sum(n))

n=int(input("Enter the vaule:"))
a=0
b=1
if n==1:
    print(a) 
elif n>2:
    print(a)
    print(b)
    for i in range(n-2):
        c=a+b
        print(c)
        a=b
        b=c


