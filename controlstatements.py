temperature = int(input("Enter temperature: "))

if temperature > 35:
    print("It is too hot")
else:
    print("It is too cold")

#python programme that checks three numbers and returns smallest number
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 < num2 and num1 < num3:
    print(num1, "is the smallest number")
elif num2 < num1 and num2 < num3:
    print(num2, "is the smallest number")
else:
    print(num3, "is the smallest number")

#proggram to check whether a number is even or odd
number = 67

if number % 2 == 0:
    print(number, "is an even number")
else:
    print(number, "is an odd number")