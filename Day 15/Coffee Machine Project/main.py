MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

balance = 0
def print_report():
    print(f"\nwater - {resources['water']}\nmilk - {resources['milk']}\ncoffee - {resources['coffee']}\nbalance - "
          f"{round(balance,2)}\n")

def collect_money(money_to_collect):
    print(f"You need to pay {money_to_collect} dollars.")
    quater=int(input("Number of quater: "))
    dimes = int(input("Number of dimes: "))
    nickel = int(input("Number of nickel: "))
    pennies = int(input("Number of pennies: "))

    collected_money= (0.25*quater) + (0.1*dimes) + (0.05*nickel) + (0.01*pennies)
    global balance
    if collected_money>money_to_collect:
        print(f"Thank you for paying {round(collected_money,2)}, Refunding you extra "
              f"{round(collected_money-money_to_collect,2)} dollars")
        balance=round(balance + money_to_collect,2)
        return True
    if collected_money==money_to_collect:
        print(f"Thank you for paying {collected_money}")
        balance=round(balance + money_to_collect,2)
        return True
    print(f"Not enough money, refunding you {collected_money} dollars")
    return False

def enough_resources(drink_name, ingredients):
    for item in ingredients:
        if resources[item]<ingredients[item]:
            print(f"Not enough resources for a {drink_name}.")
            return False
    return True

def make_drink(ingredients):
    for item in ingredients:
        resources[item]-=ingredients[item]

def order_latte():
    drink_name="latte"
    drink=MENU[drink_name]
    ingredients = drink["ingredients"]
    if enough_resources(drink_name, ingredients):
        if collect_money(drink["cost"]):
            print("Here is your drink")
        make_drink(ingredients)

def order_expresso():
    drink_name = "espresso"
    drink=MENU[drink_name]
    ingridients = drink["ingredients"]
    if enough_resources(drink_name, ingridients):
        if collect_money(drink["cost"]):
            print("Here is your drink")
        make_drink(ingridients)


def order_cappuccino():
    drink_name = "cappuccino"
    drink = MENU[drink_name]
    ingridients = drink["ingredients"]
    if enough_resources(drink_name, ingridients):
        if collect_money(drink["cost"]):
            print("Here is your drink")
        make_drink(ingridients)

while True:
    user_input=input("What do you want Expresso (e) / Latte (l) / Caappuccino (c)?")

    if user_input == "e":
        order_expresso()
    elif user_input == "l":
        order_latte()
    elif user_input == "c":
        order_cappuccino()
    else:
        print_report()


