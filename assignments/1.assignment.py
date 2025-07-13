##SWIGGY USER_ACCOUNT

#using string input 
user_name=input("Enter your full name: ")
#using integer input
contact_number=int(input("Enter your NUmber: "))
#using float input
wallet_balance=float(input("Dispaly wallet_balance: "))
#using Input as List (Space-separated)
non_veg=input("Display only NON-VEG items: ").split(',')
#list of integers
item_price=list(map(float,input("Enter price of NON-VEG items: ").split(',')))
#using tuple input
cart=tuple(map(int,input("Add items(+,-): ").split()))
#using set input
active_discounts=set(input("Enter discounts: ").strip().split(","))
#Dictionary Input using eval()
order=eval(input("Display your selected items: "))

print(f"user_name:{user_name},contact_number:{contact_number},wallet_balance:{wallet_balance},non_veg:{non_veg},item_price:{item_price},cart:{cart},active_discounts:{active_discounts},odre:{order}")
#output of fstring
#user_name:shivnia,contact_number:6304167053,wallet_balance:255.25,non_veg:['chicek briyani', 'mutton briyani', 'coca coal'],item_price:[250.0, 350.0, 20.0],cart:(2, 3, 2),active_discounts:{'welcome100', 'flat50%'}
