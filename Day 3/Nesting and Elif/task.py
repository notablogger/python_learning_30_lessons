print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

if height >= 120:
    print("You can ride the rollercoaster")
    if age >= 18:
        print("Ticket. price is 15")
    elif age >= 15:
        print("Ticket. price is 10")
    else:
        print("Ticket is free")
else:
    print("Sorry you have to grow taller before you can ride.")
