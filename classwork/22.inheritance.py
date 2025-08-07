class status:
    def __init__(self,caption,image,video):
        self.caption = caption
        self.image = image
        self.video = video
    def display_status(self):
        if self.video:
            print("Status with video:")
        else:    
            print("Status with image:")
class statusv1(status):
    def likes(self,likes):
        self.likes=likes
        print(f"Status liked by {self.likes} users.")   
    def addmusic(self,music):
        self.music = music
        print(f"Music '{self.music}' added to the status.")
shivani=status("My first status","image1.jpg","video1.mp4")
shivani.display_status()
nani=statusv1("my second status","image2.jpg","video2.mp4")
nani.display_status()
nani.likes(100)
nani.addmusic("Song Title")
####################-------SINGLE INHERITANCE-------##########################
class status:
    def upload(self,image):
        self.image=image
        print(f"Image '{self.image}' uploaded successfully.")
class statusv1(status):
    def addcaption(self,caption):
        self.caption=caption
        print(f"Caption '{self.caption}' added to the status.")  
#######################-------####---Hierarchical inheritance---####------#######################        
class statusv2(status):
    def like(self,likes):
        self.likes=likes   
        print(f"Status liked by {self.likes} users.") 
########################-------####---Multiple inheritance---####------#######################        
class statusv3(statusv1,statusv2):
    def share(self,shares):
        self.shares=shares
        print(f"Status shared {self.shares} times.")
#########################-------####---Multilevel inheritance---####------#######################
class statusv4(status):
    def upload(self,image):
        self.image=image
        print(f"Image '{self.image}' uploaded successfully.")
    def addcaption(self,caption):
        self.caption=caption
        print(f"Caption '{self.caption}' added to the status.")        
shivani=status()
shivani.upload("image.png")
nani=statusv1()
nani.upload("image2.png")
nani.addcaption("My second status")
junnu=statusv2()
junnu.upload("image3.png")
junnu.like(50)
soni=statusv3()
soni.upload("image4.png")
soni.addcaption("My third status")
soni.like(75)
soni.share(10)
daddy=statusv4()
daddy.upload("image5.png")
daddy.addcaption("My fourth status")

