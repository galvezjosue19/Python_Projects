#Ask a user their name and age and tell them something about themself.

userName = input ("What is your name? ")

userAge = input ("How old are you? ")
userAgeInt = int(userAge)

print ("Hola Usted" + userName)

userAgeTenTime = userAgeInt * 10
print ( "Tu edad es dies veces mas " + str(userAgeTenTime))

if (userAgeInt >= 18):
    print("Eres grande para votar")
else:
     print ("NO eres grande para votar")    