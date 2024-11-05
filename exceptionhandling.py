
try:
    number = 23
    print(number)

except:
    print("An error has occurred")


try:
    num1 = 39
    num2 = 13
    print(num1 / num2)
except:
    print("A ZerDivisionerror has occurred")
finally:
    print("Success")