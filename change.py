changeAmt = 84

numQtrs = changeAmt // 25 #Figure out the number of quarters
changeAmt = changeAmt - (numQtrs * 25)

numDimes = changeAmt // 10 #figure out the number of dimes
changeAmt -= (numDimes * 10)

numNickels = changeAmt // 5 #Figure out the number of nickels
changeAmt -= (numNickels * 5)

numPennies = changeAmt // 1 #Figure out the number of pennies
changeAmt -= (numPennies * 1)

print ("Quarters:", numQtrs)
print ("Dimes: %s" % numDimes)
print (f"Nickels:{numNickels}")
print (f"Pennies: {numPennies}")
print (f"Final Change Amount: {changeAmt}")