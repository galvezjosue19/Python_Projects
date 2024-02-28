import time

def GreetUser():
    if time.localtime().tm_hour < 12:
     print("Good Morning Josue!")
    else:
       print ("Good Afternoon Josue") 

GreetUser()
GreetUser()
