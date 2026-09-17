import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


def multiply(n1, n2):
    return n1 * n2


operations={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

result=0.0
cont = "y"
while result>=0.0:
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    result=n1*n2
    if result <10:
        break

