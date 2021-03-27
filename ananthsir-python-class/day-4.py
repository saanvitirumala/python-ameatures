
actual_pin = "1106"
max_attempt = 5


attempt_counter = 0

while attempt_counter < 5 and actual_pin != input("Please enter pin - ") :  #Exit condition
    print("invaild pin... Please re enter")
    attempt_counter = attempt_counter + 1

if attempt_counter <5 :
    print("Welcome to Python world")
else :
    print(" Better Luck next time! Locked for 10 min")







num = int(input("Enter any number : "))

counter = 1 

while counter < 100 :
    product = num*counter
    print(num," x ", counter, " = ", product)    
    counter = counter +1