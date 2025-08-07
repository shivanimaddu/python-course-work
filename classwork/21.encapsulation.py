class Details:
    def __init__(self,name,mail,psw):
        self.name=name
        self._mail=mail
        self.__psw=psw
    def getpassord(self):
        return self.__psw
    def setpassword(self,psw):
        self.__psw=psw
## Accessing class variable  
shiv=Details("shiv",'shiv@mail.com','shiv@123') 
print(shiv.name)
shiv.name='nani'  
print(shiv.name)
print(shiv._mail) 
shiv._mail='nani@mail.com'
print(shiv._mail)
print(shiv.getpassord())  # Accessing private variable through method
shiv.setpassword('nani@123')  # Setting new password
print(shiv.getpassord())  # Accessing updated private variable

#bank details
class bank:
    def __init__(self):
        self.name='shivani'
        self._balance=0
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, amount):
        self._balance+= amount
b=bank()  
print(b.balance)# Accessing balance using property
b.balance = 1000  # Setting balance using setter
print(b.balance)  # Accessing updated balance
print(b.name)
b.name='nani'
print(b.name)
class login:
    def __init__(self):
        self.name='shivani'
        self._pin=1234
    @property
    def pin(self):
        return self._pin
    @pin.setter
    def pin(self, new_pin):
        self._pin=new_pin
l=login()
print(l.name)  # Accessing name
l.name='nani'  # Setting new name
print(l.name)  # Accessing updated name
print(l.pin)  # Accessing pin using property
l.pin = 5678  # Setting new pin using setter
print(l.pin)  # Accessing updated pin
class instagram:
    def __init__(self,username,bio,status):
        self.username=username
        self._bio=bio
        self.__status=status
    def get_status(self):
        return self.__status
    def set_status(self, status):
        self.__status = status
    @property
    def bio(self):
        return self._bio
    @bio.setter
    def bio(self, new_bio):
        self._bio = new_bio
insta=instagram("shivani","Hello World!","active")
print(insta.username)  # Accessing username.
print(insta.bio)  # Accessing bio using property
insta.bio = "Updated Bio"  # Setting new bio using setter
print(insta.bio)  # Accessing updated bio
print(insta.get_status())  # Accessing status using method
print(insta.get_status())  # Accessing status using method
insta.set_status("inactive")  # Setting new status using method
print(insta.get_status())  # Accessing updated status using method   

