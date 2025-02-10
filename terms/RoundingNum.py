num=float(input("Please enter a float number:"))
print("Options:")
print("A: Round down")
print("B: Round up")
print("C: Round to the nearest")
choice=input("Select an invoice action (A/B/C):")
if choice == "A":
    print("number:",num,". Result:",num//1)
elif choice == "B":
    print("number:",num,". Result:", num // 1 + 1)
elif choice == "C":
    flo = num-(num//1)
    if flo <= 0.5:
        print("number:",num,". Result:",num//1)
    else:
        print("number:",num,". Result:", num // 1 + 1)
else:
    print("Wrong input")
# x=-3.6
# y=x%1
# if y<=0.5:
#     print(x // 1)
# else:
#     print(x // 1 + 1)


