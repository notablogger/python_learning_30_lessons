import art

print(art.logo)

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
while cont=="y":
    if(result==0):
        n1 = int(input("Enter first number: "))
    else:
        n1 = result
    operation=input("Enter operation \n+\n-\n*\n/\n")
    n2 = int(input("Enter second number: "))
    result=operations.get(operation)(n1,n2)

    print(f"Result:{n1} {operation} {n2} = {result} ")
    cont = input(f"Continue using the result {result}? (y/n/e)")
    if cont == "n":
        result=0.0
        cont="y"
