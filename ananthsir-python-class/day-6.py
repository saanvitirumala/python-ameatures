#student_list = ["Komali", "Navin & Navya","Udeepth",  "Akshar","Adityamithran"]

# Index starts from 0

#long_name = student_list[0]

#for student_name in student_list :
#  if len(student_name) > len(long_name) :
#    long_name = student_name

#print(long_name)





import turtle 

chintu = turtle.Turtle()
#chintu.shape("turtle")

number = int(input("Enter number to be displayed - "));

if number == 1 :
  chintu.left(90)
  chintu.forward(50)
elif number == 2 :
  chintu.forward(25)
  chintu.up() # lift pen up
  chintu.backward(25) # pixels
  chintu.down()# pen down
  chintu.left(90) # 
  chintu.forward(25)
  chintu.right(90)
  chintu.forward(25)
  chintu.left(90)
  chintu.forward(25)
  chintu.left(90)
  chintu.forward(25)
elif number == 3 :
  chintu.forward(25)
  chintu.left(90)
  chintu.forward(25)
  chintu.left(90)
  chintu.forward(25)
  chintu.up()
  chintu.back(25)
  chintu.down()
  chintu.right(90)
  chintu.forward(25)
  chintu.left(90)
  chintu.forward(25)
elif number == 4 :
  chintu.left(90)
  chintu.up()
  chintu.forward(25)
  chintu.down()
  chintu.backward(25)
  chintu.right(90)
  chintu.forward(25)
  chintu.backward(13)
  chintu.left(90)
  chintu.forward(13)
  chintu.backward(39)
elif number == 5 :
  chintu.forward(25)
  chintu.left(90)
  chintu.forward(25)
  chintu.left(90)
  chintu.forward(25)
  chintu.right(90)
  chintu.forward(25)
  chintu.right(90)
  chintu.forward(25)
elif number == 6 :
  chintu.left(90)
  chintu.up()
  chintu.forward(25)
  chintu.right(90)
  chintu.down()
  chintu.forward(25)
  chintu.right(90)
  chintu.forward(25)
  chintu.right(90)
  chintu.forward(25)
  chintu.right(90)
  chintu.forward(50)
  chintu.right(90)
  chintu.forward(25)
elif number == 7 :
  chintu.up()
  chintu.forward(25)
  chintu.down()
  chintu.left(90)
  chintu.forward(50)
  chintu.left(90   )
  chintu.forward(25) 
elif number == 8 :
  chintu.forward(25)
  chintu.left(90)
  chintu.forward(50)
  chintu.left(90)
  chintu.forward(25)
  chintu.left(90)
  chintu.forward(50)
  chintu.up()
  chintu.back(25)
  chintu.down()
  chintu.left(90)
  chintu.forward(25)
elif number == 9 :
  chintu.forward(25)
  chintu.left(90)
  chintu.forward(50)
  chintu.left(90)
  chintu.forward(25)
  chintu.left(90)
  chintu.forward(25)
  chintu.left(90)
  chintu.forward(25)
elif number == 0 :
  chintu.forward(25)
  chintu.left(90)
  chintu.forward(50)
  chintu.left(90)
  chintu.forward(25)
  chintu.left(90)
  chintu.forward(50)
else :
  print(number ,"not supported ")