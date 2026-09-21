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
          f"{balance}\n")

def collect_money(money_to_collect):
    print(f"You need to pay {money_to_collect} dollars.")
    quater=int(input("Number of quater: "))
    dimes = int(input("Number of dimes: "))
    nickel = int(input("Number of nickel: "))
    pennies = int(input("Number of pennies: "))

    collected_money= (0.25*quater) + (0.1*dimes) + (0.05*nickel) + (0.01*pennies)
    global balance
    if collected_money>money_to_collect:
        print(f"Thank you for paying {collected_money}, Refunding you extra {collected_money-money_to_collect} dollars")
        balance += collected_money
        return True
    if collected_money==money_to_collect:
        print(f"Thank you for paying {collected_money}")
        balance += collected_money
        return True
    print(f"Not enough money, refunding you {collected_money} dollars")
    return False

def enough_resources(drink,water, milk, coffee):
    if resources["water"]<water or resources["milk"]<milk or resources["coffee"]<coffee:
        print(f"Not enough resources for a {drink}, refunding your money.")
        return False
    return True

def consume_resources(water, milk, coffee):
    resources["water"]=resources["water"]-water
    resources["milk"]=resources["milk"]-milk
    resources["coffee"]=resources["coffee"]-coffee

def order_latte():
    drink_name="latte"
    drink=MENU[drink_name]
    ingredients = drink["ingredients"]
    if enough_resources(drink_name, ingredients["water"], ingredients["milk"],
                        ingredients["coffee"]):
        if collect_money(drink["cost"]):
            print("Here is your drink")
    consume_resources(ingredients["water"], ingredients["milk"],
                        ingredients["coffee"])

def order_expresso():
    drink_name = "espresso"
    drink=MENU[drink_name]
    ingredients = drink["ingredients"]
    if enough_resources(drink_name, ingredients["water"], 0,
                        ingredients["coffee"]):
        if collect_money(drink["cost"]):
            print("Here is your drink")
    consume_resources(ingredients["water"], 0,
                      ingredients["coffee"])


def order_cappuccino():
    drink_name = "cappuccino"
    drink = MENU[drink_name]
    ingredients = drink["ingredients"]
    if enough_resources(drink_name, ingredients["water"], ingredients["milk"],
                        ingredients["coffee"]):
        if collect_money(drink["cost"]):
            print("Here is your drink")
    consume_resources(ingredients["water"], ingredients["milk"],
                      ingredients["coffee"])

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


