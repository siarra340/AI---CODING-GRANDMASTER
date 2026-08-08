def add(x,y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y

num1 = int(input("Enter Number1"))
num2 = int(input("Enter Number2"))

print("Sum: ", add(num1, num2))
print("Differnce: ", sub(num1, num2) )
print("Product: ", mult(num1, num2))
print("Quotient: ", div(num1, num2))