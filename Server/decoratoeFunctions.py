# decorator functions

#example 1
def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

def calculation(calculate,n1,n2):
    print(f"the calculation is :", calculate(n1,n2))

calculation(divide,10,5)

#example 2
def out():
    print("outer function")
    def inner():
        print("Inner function")
    inner()
out()