water = 1000
milk = 1000
coffee = 500
money = 5


def report():
    return print(f"There is: water - {water}ml, milk - {milk}ml, coffee - {coffee}g, money - £{money}.")


def off():
    return print("Thank you for using the drinks machine. Switching off.")


def drink(choice, waterf, milk_f, coffee_f, cost):

    if choice == 'espresso':
        waterf -= 25
        coffee_f -= 25
        cost = 1.25
        print(f"There is {waterf}ml water, {coffee_f}g coffee, and {milk_f}ml milk remaining.")
    elif choice == 'cappuccino':
        waterf -= 75
        coffee_f -= 50
        milk_f -= 25
        cost = 2.00
        print(f"There is {waterf}ml water, {coffee_f}g coffee, and {milk_f}ml milk remaining.")
    elif choice == 'latte':
        waterf -= 75
        coffee_f -= 25
        milk_f -= 50
        cost = 2.00
        return cost
        print(f"There is {waterf}ml water, {coffee_f}g coffee, and {milk_f}ml milk remaining.")
    elif choice == 'off':
        off()
    elif choice == 'report':
        report()


def coins():
    quarter = 0
    dime = 0
    nickle = 0
    penny = 0
    input_coins = 0

    print("Please insert your coins:")
    quarter = int(input("Quarters: "))
    dime = int(input("Dimes: "))
    nickle = int(input("Nickles: "))
    penny = int(input("Pennies: "))

    input_coins = (quarter * 0.25) + (dime * 0.1) + (nickle * 0.05) + (penny * 0.01)


drink_choice = input("What would you like? espresso/latte/cappuccino")

drink(drink_choice, water, milk, coffee, money)
