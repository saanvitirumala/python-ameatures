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


def my_function5(**Kid):
  print("Her Last name is :" + lstname)

my_function5(fname = "Saanvi",lastname = "Tirumala")

def my_function6(country = "Russia"):
    print("The biggest country is:",country)

my_function6("India")
my_function6("USA")
my_function6("Brazil")
my_function6("China")


def my_function7(food):
    for y in food:
        print(y)

Food = ["Bacon","Chicken nuggets","Brownies"]

my_function7(Food)

def my_function8():
    pass


