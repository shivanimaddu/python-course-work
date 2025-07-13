data={'shivani@mail.com':'1234@',
      'nani@mail.com':'12345678@'}
email,pwd=input("Enter the email and pwd:").split()
if data.get(email)==pwd:
    print('login successful')
else:
    print('inavalid login')#inavalid login

items=['cake','maggie','biscuits']
stocks=[10,23,0]
data=input("Enter your item:")
if data in items:
    ind=items.index(data)
    if stocks[ind]>0:
        print("Available")
    else:
        print("out of stocks")
else:
    print('not available')            

           
