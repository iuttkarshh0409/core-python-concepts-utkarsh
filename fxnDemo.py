name= input("Enter your name: ")
def greet(): #fxn with no parameter
    print("Hello, "+name)
greet()

def greetWithName(name):
    print("Hello, " + name + "!")

greetWithName("Utkarsh")

def add(x, y):  #fxn with return value
    return x + y

result = add(10, 20)
print("Sum is:", result)

def greet(name="Guest"):  #fxn with default parameter
    print("Hello, " + name)

greet()           # uses default
greet("Utkarsh")  # overrides default

square = lambda x: x * x
print("Square of 5:", square(5))

sum = lambda a, b: a + b
print("Sum:", sum(3, 7))
