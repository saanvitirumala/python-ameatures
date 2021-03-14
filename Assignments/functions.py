def my_function1():
    print(" HELLO WORLD!")
    
my_function1()


def my_function2(firstname):
    print(firstname +" "+ lstname )

lstname = "Tirumala"

my_function2("Saanvi")
my_function2("Saharsh")

def my_function3(*Item):
    print("The cheapest item is:"+Item[1])

milk = 1.99
banana = 3.00
chips = 9.00

my_function3("banana","milk","chips")


def my_function4(*Fruits):
  print("The smallest fruit is:"+ Fruits[1])

my_function4("apples","grape","Pinneapple")