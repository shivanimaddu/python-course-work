num=int(input("Enter the number of messages: "))
messages=["Mummy: Good morning",
"Akka: Good morning mummy.",
"Me: Em chesthunaru",
"Mummy:panilu anni ayyayi ippude,ready ayipoyava nanna.",
"Akka:Tiffen chesara?",
"Me:ha ayipoyindhi nadhi,meedhi?",
"Mummy:Em tiffen?",
"Akka:idly.",
"Me:Class ki vachesanu sare bye!!",
"Mummy:bye nanna take care.",
"Akka:sare mummy cook cheyali.", 
"Me:okay!!"]
#1. Count total number of messages
total_messages=len(messages)
print(total_messages)
print(messages)
#2. Identify unique users in the chat(he)
users=set()
for msg in messages:
    user=msg.split(':')[0]
    users.add(user)
print(users)   
##output:={'Mummy', 'Me', 'Akka'} 
##3. Count total words in the chat
total_words=0
for msg in messages:
    message=msg.split(":")[1].strip()
    words=message.split()
    total_words+=len(words)
print("total_words:",total_words)   
##outp:=total_words: 36 
##4. Calculate average words per message
total_words=0
for msg in messages:
    message=msg.split(":")[1].strip()
    words=message.split()
    total_words+=len(words)
    average_msgs=total_words/total_messages
print("average words:",average_msgs)
#output:3
#5. Find the longest message sent
longest_msg=""
words=0
for msg in messages:
    message=msg.split(":")[1].strip()
    word=len(msg.split())
    if word>words:
        words=word
        longest_msg=message
print("longest_msg:",longest_msg)
#OTUPUT-longest_msg: panilu anni ayyayi ippude,ready ayipoyava nanna.
#7. Get message count for a specific user
user="Mummy"
count=0
for msg in messages:
    if msg.startswith(user+":"):
        count+=1
print("Messages sent by",user+":",count) 
#Messages sent by Mummy: 4
#9. Retrieve the first and last message sent by a user
user="Mummy"
user_message=[]
for msg in messages:
    if msg.startswith(user+":"):
        user_message.append(msg)
if user_message:
    print("First meesage by",user+":",user_message[0])
    print("last meesage by",user+":",user_message[-1])
else:
    print("No messages by",user)   
#output:=First meesage by Mummy: Mummy: Good morning!
#last meesage by Mummy: Mummy:bye nanna take care.  
#10. Check if a user is present in the chat    
to_check="Nani"
found=False
for ms in messages:
    if msg.startswith(to_check+":"):
        found=True
        break
if found:
    print(f"user {to_check} found in the messages")
else:
    print(f"user {to_check} found not in the messages")
#output=user Nani found not in the messages
#11. Find commonly repeated words
words=[]
for msg in messages:
    if ":" in msg:
        message=msg.split(":",1)[1]
        message=message.lower
        for word in msg.split():
            words.append(word)
repeated=[]
for word in words:
    if words.count(word)>1 and word not in repeated:
        repeated.append(word)
print("commonly repeated words:",set(repeated))
##13. Identify the user with the longest average message length
user='Akka'
count=0
for msg in messages:
    if user.lower() in msg.lower():
        count+=1
print(f"message {user}:",count)        
#14. Count how ma[ny messages mention a specific user
specific_user=[]
for msg in messages:
    if msg.startswith(user+":")and msg not in specific_user:
        specific_user.append(msg)
print(f"specific user by {user}:")
for msg in specific_user:
    print(msg)        
#15. Remove duplicate messages
unique_messages=set(messages)
print("unique_messages count:",len(unique_messages)) 
#16. Sort messages alphabetically
sorted_messages=sorted(messages)
for msg in sorted_messages:
    print(msg)   
'''Akka: Good morning mummy.
Akka:Tiffen chesara?
Akka:idly.
Akka:sare mummy cook cheyali.
unique_messages count: 12
Akka: Good morning mummy.
Akka:Tiffen chesara?
Akka:idly.
Akka:sare mummy cook cheyali.
Me: Em chesthunaru
Me:Class ki vachesanu sare bye!!
Me:ha ayipoyindhi nadhi,meedhi?
Me:okay!!
Mummy: Good morning
Mummy:Em tiffen?
Mummy:bye nanna take care.
Mummy:panilu anni ayyayi ippude,ready ayipoyava nanna. '''    
#17. Extract all questions asked in the chat
questions=[]
for msg in messages:
    if '?' in msg:
        questions.append(msg)
print("questions found in chat:")
for q in questions:
    print(q)   
'''questions found in chat:
Akka:Tiffen chesara?
Me:ha ayipoyindhi nadhi,meedhi?
Mummy:Em tiffen?'''   
#18. Calculate the reply ratio between two users
reply=0
for i in range(len(messages)-1):
    if messages[i].startswith("Me")and messages[i+1].startswith("Mummy:"):
        reply+=1
print("reply ratio from Mummy to Me:",reply,"replies")        
#19. Check for deleted messages
delete=0
for msg in messages:
    if msg=="This message was deleted":
        delete+=1
print("Deleted messages:",delete)        