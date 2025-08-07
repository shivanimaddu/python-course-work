class shopping:
    discount=10
    def product(self,price,name):
        self.price=price
        self.name=name
user1=shopping()
user2=shopping()
user1.product(1000,"shoes")
user2.product(2000,"shirt")
print(user1.price)
print(user2.price)        




class shopping:
    discount=10
    @classmethod
    def update(cls,new_discount):
        cls.discount = new_discount
        print("Discount updated to", cls.discount)
   
    def product(self,price,name):
        self.price=price
        self.name=name
user1=shopping()
user2=shopping()
shopping.update(20)  # Update discount to 20%
user1.product(1000,"shoes")
user2.product(2000,"shirt")
print(user1.price)
print(user2.price)        