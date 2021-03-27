import turtle 
chintu = turtle.Turtle()
#chintu.shape("turtle")


#chintu.color()

colorList = ["blue", "yellow", "green", "red",]


for x in range(15) :
  chintu.begin_fill()

  chintu.color("black",colorList[x%4])

  #chintu.stamp()


  #chintu.up()
  chintu.forward(25)
  chintu.left(25)
  #chintu.down()
  
  chintu.circle(25)
  chintu.end_fill()



greeting = "Hello "

nameStr = input("Please enter name : ")

# concatenation of string
print(greeting + nameStr)

#Extracting all chars
for charStr in nameStr:
    print(charStr)

# index starts on 0
print("4th char : ", nameStr[3])

#Sub string / slicing
print("3 to 5t char : ", nameStr[2:5])

print("Length of string ", len(nameStr))

# -
print("last char : ", nameStr[-1])

print("reverse : ", nameStr[::-1])

isItIn = "Python" not in "Hello Python"

print(isItIn)




print("---Pallendrome check---")
inputStr = input("Enter string ")

revserStr = inputStr[::-1]

if inputStr == revserStr :
  print (inputStr, "is a pallendrome!")
else :
  print (inputStr, "is not a pallendrome!")