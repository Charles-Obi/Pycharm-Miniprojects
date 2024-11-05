#Built-in library functions
y = max(34,78, 56, 10)
print(y)
x = min(34, 78, 56, 4)
print(x)
z = pow(2,3)
print("the result is", z)

#user-defined functions
def greeting():
    print("Hello there!")
greeting() #calling a function


#Parameter/variable and Argument/value
def multiply(x, y):
    print(x * y)

multiply(2,3)
multiply(20,34)
multiply(25,39)

def doctor(name):
    print(name)

doctor("Charles")
doctor("Mary")
doctor("Ken")
doctor("Judy")