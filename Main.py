import Reciepe

profit = 0
resources = {
    "water": 1000,
    "milk": 2000,
    "coffee": 2000,
}


def enough_things(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Not Enough {item}")
            return False
    return True


def coins():
    print("Make Payment: Insert Coins\n")
    total = int(input("Quarters: "))*0.25
    total += int(input("Dimes: "))*0.1
    total += int(input("Nickles: "))*0.05
    total += int(input("Pennies: "))*0.01
    return total


def transaction(given, coffee_price):
    if given >= coffee_price:
        print("Transaction Successful!")
        global profit
        profit += coffee_price
        if given > coffee_price:
            print("Here is your Change: $" + str(round((given-coffee_price), 2)))
        return True
    else:
        print("Transaction Failed! Not Sufficient Money, Try Again!")
        return False


def make_coffee(name, ingredients):
    for items in ingredients:
        resources[items] -= ingredients[items]
    print(f"Enjoy your {name}! Have a great day, Visit us again!")


is_on = True
while is_on:
    choice = (input("What coffee do you like to order? Expresso / Latte / Cappuccino:\n")).lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}gm")
        print(f"${profit}")
    else:
        drink = Reciepe.MENU[choice]
        if enough_things(drink["ingredients"]):
            payment = coins()
            if transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
