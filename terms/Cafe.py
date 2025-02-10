black="Black coffee"
cap="Cappuccino"
choco="Chocolate"
way= "is on the way"
print("MANU:")
print("A:",black)
print("B:",cap)
print("C:",choco)
choice=input("Please choose a product (A/B/C):")
if choice != "A" and choice != "B" and choice != "C":
    print("Wrong input")
elif choice == "A":
    print(black,way)
elif choice == "B":
    print(cap,way)
else:
    print(choco,way)