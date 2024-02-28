import fileinput

studentGrade = {}

for line in fileinput.input():
    values = line.split(',')  #This is going to grab Ben,92 and turn it into a list ["Ben", "92"]

studentGrades.update ({ values[0] : values[1]} ) #Ben is 0 and 92 is 1

print(studentGrades)