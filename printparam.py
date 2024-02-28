fileobject = open("output.txt", mode="w")

print("Hola Josue!", file=fileobject)


print("one", "two", "three", sep= ":", file=fileobject)