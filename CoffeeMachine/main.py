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

is_on = True
profit = 0.0


# Todo: 7. Make Coffee


def make_coffee(user_drink):
    selected_drink = MENU[user_drink]
    for ingredient in selected_drink['ingredients']:
        resources[ingredient] -= selected_drink['ingredients'][ingredient]
    print(f"Here is your {user_drink}. Enjoy!")


# Todo: 6. Check if Transaction is successfully


def check_money(user_drink, user_money):
    cost_of_drink = MENU[user_drink]['cost']
    if user_money >= cost_of_drink:
        global profit
        profit += cost_of_drink
        print(f"Here is ${round(user_money - cost_of_drink, 2)} dollars in change.")
        return True
    elif user_money < cost_of_drink:
        print("Sorry that's not enough money. Money refunded.")
        return False


# Todo: 5. Process Entered coins by the User.


def calculate_coins():
    print("Please enter coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    penny = int(input("how many penny?: "))
    return (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickels) + (0.01 * penny)


# Todo: 4. Check for resources in the Machine


def check_resources(user_drink):
    selected_drink = MENU[user_drink]
    for ingredient in selected_drink['ingredients']:
        if resources[ingredient] < selected_drink['ingredients'][ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


while is_on:
    total_coins_value = 0.0
    # Todo: 1. Prompt User by asking type of coffee
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "report":
        # Todo: 3. Print report
        print(
            f"Water: {int(resources['water'])}ml\nMilk: {int(resources['milk'])}ml\nCoffee: {int(resources['coffee'])}g"
            f"\nMoney: ${profit}")
    elif choice == "off":
        # Todo: 2. Create a function for turning off the machine
        is_on = False
    else:
        if check_resources(choice):
            total_coins_value = calculate_coins()
            if check_money(choice, total_coins_value):
                make_coffee(choice)
