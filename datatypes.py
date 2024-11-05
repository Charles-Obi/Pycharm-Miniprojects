from variables import number

number = 67 #integer
second = 45.67 #float
greeting = "goodmorning" #string
isPythonInterestng = True #Boolean

#datastructures - Multiple values stored in a single variable
cars = ["toyota", "nissan", "mercedes", "vw"] #lists - Ordered and changeable
fruits = ("apple", "mango", "orange", "grape") #Tuple - Ordered but unchangeable
countries = {"Kenya", "India", "Mexico"} #set - elements are unordered and also unchangeable
students = {
    "firstname" : "Jane",
    "age" : 23,
    "course" : "Web development",
    "gender" : "Female",
}

print(cars)
print(fruits)
print(countries)
print(students)
print(students["gender"])

print(number)
print(second)
print(isPythonInterestng)


#deemining a data type
print(type(countries))
print(type(students))



print(number, second, greeting, isPythonInterestng)
print(number)
print(second)
print(greeting)
print(isPythonInterestng)

#typecasting - onverting from onr datatype to another
print(float(number))
print(int(second))
