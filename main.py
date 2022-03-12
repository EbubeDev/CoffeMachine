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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def sufficient_resource(order_ingredients):
    """Returns true if there's enough ingredient to process order"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("Sorry, there's not enough {item}")
            return False
        return True

def transaction(money_recieved, cost_of_drink):
    """Checks to see the transaction can be completed or not"""
    if money_recieved >= cost_of_drink:
        change = round(money_recieved - cost_of_drink, 2)
        print(f"Here's your change: ${change}")
        global profit
        profit += cost_of_drink
        return True
    else:
        print("Sorry, that's not enough money")
        return False

def process_coins():
    """This function processes the total amount of money inserted"""
    print("Please insert your coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickle? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

def make_coffee (drink_name, order_ingredients):
    """Deduct used ingredients from the resource"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your {drink_name}☕ Enjoy")


is_on = True

while is_on:
    customer_choice = input("What would you like?(espresso, latte, cappuccino: \n")
    if customer_choice == "off":
        is_on = False
    elif customer_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources ['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[customer_choice]
        if sufficient_resource(drink["ingredients"]):
            pay = process_coins()
            if transaction(pay, drink["cost"]):
                make_coffee(customer_choice, drink["ingredients"])



