# name={1:"dinesh",2:"gopal",3:"shivani",4:"prasanth"}
# for i in name.keys():
#     print(f'{i}- {name[i].title()}')

# num={'1':1,'2':4,'3':9,'4':16,'5':25,'6':36,'7':49,'8':64,'9':81,'10':100}
# for i in num.keys():
#     print(f'{i}-{num[i]}')#1-1
'''2-4
3-9
4-16
5-25
6-36
7-49
8-64
9-81
10-100'''
# 
#            
# email,pwd='shivani@gmail.com','shivani@123'
# max_attempt=5
# cur_attempt=1

# while cur_attempt <=max_attempt:
#     e=input("Enter the email: ")
#     p=input("Enter password: ")
#     if e==email and p==pwd:
#         print("Login Successful")
#         break
#     else:
#         print("Invalid email or pwd.try again!!")
#     cur_attempt+=1
# else:
#         print("Max attemts are done.try after 5 min")

# ##for loop        
# l=['laptop','shoe','watch','airpods']
# for i in l:
#     if i=='watch':
#         break
#     print(i.center(20,'-'))
# else:
#     print("End of the items")    

# l=['laptop','shoe','watch','airpods']
# for i in l:
#     if i=='watch':
#         continue
#     print(i.center(20,'-'))
# else:
#     print("End of the items")    

# ##while with else

# bullets=10
# while bullets>0:
#     if bullets==5:
#         print("dead")
#         break
#     print("shoot()")
#     bullets-=1
# else:
#     print("Game Over")    

# bullets=10
# while bullets>0:    
#     print("shoot()")
#     bullets-=1
# else:
#     print("Game Over")    


# ##PRIME NUMBER
# n=int(input("Enter the num:"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

# fact=0
# n=int(input("Enter the num:"))
# for i in range(1,n+1):
#     if n%i==0:
#         fact+=1
# if fact==2: 
#     print(f"{n} is a prime number\nFcators count={fact}") 
# else:
#     print(f"{n} is not a prime number\nFcators count={fact}")          


# fact=0
# n=int(input("Enter the num:"))
# for i in range(2,(n//2)+1):
#     if n%i==0:
#         fact+=1
# if fact==0: 
#     print(f"{n} is a prime number\nFcators count={fact}") 
# else:
#     print(f"{n} is not a prime number\nFcators count={fact}") 

# photos=['beach.png','sunset.png','mountain.png']
# for i in range(len(photos)):
#     print(f"{i+1}.{photos[i]}")
# s=set(map(int,input("enter the pic ids: ").split(',')))    
# for i in s:
#     print(photos[i-1])

# data={1:{'name':'shivani','exam_status':True,'python':100,'sql':80,'html':95},
#       2:{'name':'junnu','exam_status':True,'python':80,'sql':90,'html':95}}
# for i in data.keys():
#     print(f'{i}.{data[i]["name"]}')
# stuid=int(input("Enter the student id:")) 
# if stuid in data:
#     if data[stuid]["exam_status"]:
#         total=(data[stuid]["python"]+data[stuid]["html"]+data[stuid]["sql"])/3
#         if total>90:
#             print(f'congrats!!\n{data[stuid]["name"]} got "A" grade')
#         elif total>75:
#             print(f'Good!!\n{data[stuid]["name"]} got "B" garde')
#         elif total>50:
#             print(f'Butter luck next time!!\n{data[stuid]["name"]}failed')

#grocery store

lists='''
Rice        qty  price          20/kg
wheat flour qty  price          30/kg
sugar       qty  price          40/kg
milk        qty  price          60/lit
eggs(12 pcs)qty  price          70/dozen
cooking oil qty  price          130/packet
tea powder  qty  price          30/packet
salt        qty  price          20/kg
bread       qty  price          30/packet
soap        qty  price          20 each
'''
print(lists)
data={
1:{'prodcut':'Rice','price':20},
2:{'prodcut':'wheat flour','price':30},
3:{'prodcut':'sugar','price':40},
4:{'prodcut':'milk','price':60},
5:{'prodcut':'eggs','price':70},
6:{'prodcut':'cooking oil','price':130},
7:{'prodcut':'tea powder','price':20},
8:{'prodcut':'salt','price':20}}
print(data)
for i in range(1,9):
    print(f'{i}.{(data[i]["prodcut"]).ljust(15," ")}:{data[i]["price"]}')
items=list(map(int,input("Enter the iem indexes: ").split(',')))   
print(items) 
total=0
ids=set()
for i in items:
    if i not in ids:
        cost=items.count(i)
        total+=(data[i]["price"]*cost)
        print(f'{data[i]["prodcut"]}-{cost}*{data[i]["price"]}={data[i]["price"]}+{data[i]["prodcut"]}')
        ids.add(i)
print("Total Bill: ",total)        







    

      

