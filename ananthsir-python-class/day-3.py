import random

randomVal = random.randint(0,20);

input("Take any random number\n")

input("Borrow same from your friend\n")

print("I can give you - ",randomVal," add it" )

input("\nDivide the the resulting value by 2\n")

input("Return the borrow number to  your friend\n")

input("Once your ready press enter I will guess the number ..... ")

print("\nRemaining number with you is - ",randomVal/2)


principalVal = int(input("Enter principal in $ - "))

timeVal = float(input("Enter no. of years - "))

rateVal = float(input("Enter rate of interest % - "))
# SI = PTR/100 
simpleInterestVal = (principalVal* timeVal * rateVal)/100

print("Simple interest would be - $",simpleInterestVal )

amount = principalVal + simpleInterestVal

print("Final amount would be  - $",amount )