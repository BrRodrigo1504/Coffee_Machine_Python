MENU = {
    "espresso": {
        "Ingredients": {
            "Water": 50,
            "Coffee": 18,
        },
        "Cost": 1.5,
    },
    "latte": {
        "Ingredients": {
            "Water": 200,
            "Milk": 150,
            "Coffee": 24,
        },
        "Cost": 2.5,
    },
    "cappuccino": {
        "Ingredients": {
            "Water": 250,
            "Milk": 100,
            "Coffee": 24,
        },
        "Cost": 3.0,
    }
}

resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
}

profit = 0

is_on = True


def resource_calc(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def make_drink(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️.")


def money():
    print("Please, insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that´s not enough money. Money refunded")
        return False


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): \n")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['Water']}ml")
        print(f"Milk: {resources['Milk']}ml")
        print(f"Coffee: {resources['Coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if resource_calc(drink["Ingredients"]):
            payment = money()
            if is_successful(payment, drink["Cost"]):
                make_drink(choice, drink["Ingredients"])
