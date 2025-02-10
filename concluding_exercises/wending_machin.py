"""Wending Machin"""

def invalid():
    print(f"⛔ invalid input ⛔\n\n")

def get_payment(price):
    print(f"Enter {price} shekel")

    while True:
        one_coins = input(f"Enter coins of ⣏⣉➊⣉⣹ ")
        if one_coins.isnumeric():
            break
        invalid()


    while True:
        two_coins = input(f"Enter coins of ⣏⣉➋⣉⣹ ")
        if two_coins.isnumeric():
            break
        invalid()


    while True:
        five_coins = input(f"Enter coins of ⣏⣉➎⣉⣹ ")
        if five_coins.isnumeric():
            break
        invalid()

    while True:
        ten_coins = input(f"Enter coins of ⣏⣉➓⣉⣹ ")
        if two_coins.isnumeric():
            break
        invalid()
    return int(one_coins) * 1 + int(two_coins) * 2 + int(five_coins) * 5 + int(ten_coins) * 10

def get_change(price):
    payment = get_payment(price)
    print("\n\n")
    return payment - price

def return_change(change):
    real_change = change
    change_str = ""
    added = False
    while change > 0:
        while change >= 10:
            change_str += "➓"
            change -= 10
            added = True
        if added:
            change_str += " + "
            added = False
        while change >= 5:
            change_str += "➎"
            change -= 5
            added = True
        if added:
            change_str += " + "
            added = False
        while change >= 2:
            change_str += "➋"
            change -= 2
            added = True
        if added:
            change_str += " + "
            added = False
        while change >= 1:
            change_str += "➊"
            change -= 1

    print(f"Your change is {real_change} Shekel ⣏⣉{change_str}⣉⣹")

def get_product(price, product):
    change = get_change(price)
    while change < 0:
        print(f"You only put in {change + price} shekel, add money.")
        price = - change
        change = get_change(price)
    if change == 0:
        print(f"Thank you! you can take the {product} ☺")
    else:
        print(f"Thank you! you can take the {product} ☺")
        return_change(change)
    print("\n\n")

def out_of_stock(product):
    print(f"Sorry, the {product} is out of stock ☹\n\n")

water = 3
apple_juice = 3
orange_juice = 3
coke = 3
sprite = 3

while True:
    print(f"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n"
          f"|||||||||||||||||  ~ WENDING MACHIN ~  |||||||||||||||||||||\n"
          f"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n"
          f"||||||||||||||||||      CHOOSE      ||||||||||||||||||||||||\n"
          f"||||||||||||||||||     A DRINK:⠀    ||||||||||||||||||||||||\n"
          f"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n"
          f"||||||||  1: ~WATER~   ~8 Shekel~   ~{water} in stock~   |||||||||\n"
          f"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n"
          f"|||||  2: ~APPLE JUICE~   ~10 Shekel~   ~{apple_juice} in stock~   |||||\n"
          f"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n"
          f"||||  3: ~ORANGE JUICE~   ~10 Shekel~   ~{orange_juice} in stock~   |||||\n"
          f"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n"
          f"|||||||  4: ~SPRITE~   ~12 Shekel~   ~{sprite} in stock~   ||||||||\n"
          f"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n"
          f"||||||||  5: ~COKE~   ~12 Shekel~   ~{coke} in stock~   |||||||||\n"
          f"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n"
          f"To exit enter 'exit' ")

    choice = input("Enter your choice here -> ")

    if choice == "1":
        if water == 0:
            out_of_stock("water")
            continue
        get_product(8, "water")
        water -= 1

    elif choice == "2":
        if apple_juice == 0:
            out_of_stock("apple juice")
            continue
        get_product(10, "apple juice")
        apple_juice -= 1

    elif choice == "3":
        if orange_juice == 0:
            out_of_stock("orange juice")
            continue
        get_product(10, "orange juice")
        orange_juice -= 1

    elif choice == "4":
        if sprite == 0:
            out_of_stock("sprite")
            continue
        get_product(12, "sprite")
        sprite -= 1

    elif choice == "5":
        if coke == 0:
            out_of_stock("coke")
            continue
        get_product(12, "coke")
        coke -= 1

    elif choice == "exit":
        break
    else:
        invalid()