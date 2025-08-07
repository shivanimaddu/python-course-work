
# for i in range(5):
#     for j in range(5-i-1):
#         print(' ',end=' ')
#     for x  in range(i+1): 
#         print('*',end=' ') 
#     print()    ##PATTERNS:
# for j in range(5):
#     for i in range(3):
#         print(i,end=' ')
#     print()    
# ##outer loop is rows and inner loop is coloumns    
# #1. Square Pattern
# for row in range(5):
#     for column in range(5):
#         print('*',end=' ')
#     print() 
# #for rows    
# for i in range(5):
#     for j in range(5):
#         print(i,end=' ')
#     print()    
# #for columns
# for i in range(5):
#     for j in range(5):
#         print(j,end=' ')
#     print()    
   
# for i in range(5):
#     for j in range(i+1):
#         print('*',end=' ')
#     print()       

# for i in range(5):
#     for j in range(5-i):
#         print('*',end=' ')
#     print()    

        
# for i in range(5):
#     for j in range(i+1):
#         print(' ',end=' ')
#     for x  in range(5-i): 
#         print('-',end=' ') 
#     print()            

# for i in range(5):
#     for j in range(5):
#         if i==2 or j==0 or i==0 or i==5-1 or j==5-1:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')    
#     print()

# for i in range(5):
#     for j in range(5):
#         if i==0 or  i==5-1 or i+j==5-1:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')    
#     print()

# for i in range(5):
#     for j in range(5):
#         if i==j or i+j==5-1:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')    
#     print()

# for i in range(7):
#     for j in range(7):
#         if i==j or i+j==5-1:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')    
#     print()



# n=7
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or i==n//2 or (i<n//2 and j==0) or (j==n-1 and i>n//2):
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')    
#     print()        

# n=7
# for i in range(n):
#     for j in range(n):
#         if i<=n//2 and (j==0 or j==n-1):
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')    
#     print()        

# n=5
# for i in range(n):
#     for j in range(n):
#         if j==0 or j==n-i-2 or j==i-n//2+1:
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')  
#     print()          




# n=5
# for i in range(n):
#     for j in range(n):
#         if j==0 or j==n-i-2 or j==i-n//2+1:
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')  
#     print()          



n=5
for i in range(n):
    for j in range(2*n-1):
        if j==n-i-1 or j==n+i-1 or (i==n//2 and j>n-i-1 and j<n+i-1 ):
            print('*',end=' ')
        else:
            print(" ",end=' ')  
    print()          

n=5
for i in range(n):
    for j in range(2*n):
        if j==i or j==(2*n - 2 - i):
            print('*',end=' ')
        else:    
            print(" ",end=' ')  
    print()     



























