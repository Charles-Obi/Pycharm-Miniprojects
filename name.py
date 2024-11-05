number = 67
print(float(number))
name = ''
if name == 'Sam':
    print('Hello Sam')
else:
    print('Hello dude')

text = 'Obiero'
print (text[1])

fname = "Charles"
lname = "Obiero"
print ("My name is " + fname + " " + lname)

n1 = 34
n2 = 34
print("The sum of n1 and n2 is", n1 + n2)


#data structures -Mulltiple values stored in a single variable
names = ['charles', 'william', 'obiero', 'wesonga'] #list -ordered and changeable
print(names)
fruits = ("banana", "mango", "apple")#Tuple - ordered but unchangeable
print(fruits)
student = {
    "fname": "Michael",
    "lname": "William",
    "age": 23,
    "city": "San Francisco",
}#Dictionary - Key-value pair
print(student)
countries = {"Kenya", "Uganda", "Tanzania", "Ethiopia"}
print(countries)

print(len(countries))
print(student["city"])
#determining datatypes
print(type(countries))
print(type(student))

def add():
    num1 = 67
    num2 = 34
    print(num1 + num2)
add()

def multiply(x , y):
    print(x * y)
multiply(2, 3)
multiply(23, 64)
multiply(4, 5)

def divide(x, y):
    print(x / y)
divide (2, 3)
divide (4, 5)

def doctor(name):
    print(name)

doctor("Charles")
doctor("William")
doctor("Michael")