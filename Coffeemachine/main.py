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
    "income": 0,
}
is_on = True
process = False


def check_resource(ingredient, resource, ingredient_needed):
    """Checks if the ingredient in the resource is more than that needed."""
    if resource[ingredient] < ingredient_needed[ingredient]:
        return True


def calculate(quarters, dimes, nickels, pennies):
    """Takes the number of coins each and calculate it's value."""
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return total


def purchase(input, menu, resource, price):
    """Removes the spent resources."""
    ingredient_used = menu[input]["ingredients"]
    for ingredient in ingredient_used:
        resource[ingredient] -= ingredient_used[ingredient]
    resources["income"] += price
    if user_money > price:
        change = round((user_money - price), 2)
        print(f"Here is ${change} in change.")
    print(f"Here is your {input} ☕, Enjoy.")


# TODO 1. Prompt user what they like.
# Check user input and keep repeating after completing an action.
while is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

# TODO 2. Turn off coffee machine.
    if user_input == "off":
        is_on = False
        continue

# TODO 3. Print report.
    elif user_input == "report":
        water_qty = resources["water"]
        milk_qty = resources["milk"]
        coffee_qty = resources["coffee"]
        income = resources["income"]
        print(f"Water: {water_qty}ml")
        print(f"Milk: {milk_qty}ml")
        print(f"Coffee: {coffee_qty}g")
        print(f"Money: ${income}")
        continue

# TODO 4. Check resources sufficient?
    else:
        ingredients = MENU[user_input]["ingredients"]
        for ingredient in ingredients:
            check_result = check_resource(ingredient=ingredient, resource=resources, ingredient_needed=ingredients)
            if check_result:
                process = check_result
                print(f"Sorry, there is no enough {ingredient}.")
                continue

# TODO 5. Process coins.
    if not process:
        print("Please insert coins.")
        quater = int(input("How many quarters? "))
        dime = int(input("How many dimes? "))
        nickel = int(input("How many nickels? "))
        penny = int(input("How many pennies? "))
        user_money = calculate(quarters=quater, dimes=dime, nickels=nickel, pennies=penny)

        # TODO 6. Check transaction successful?
        cost = MENU[user_input]["cost"]
        if user_money < cost:
            print("Sorry, that's not enough money. Money refunded.")
            continue
        else:
            # TODO 7. Make coffee.
            purchase(input=user_input, menu=MENU, resource=resources, price=cost)