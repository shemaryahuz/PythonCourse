num=float(input("Enter a number from 1 to 1000000:"))
if num < 1 or num > 1000000:
    print("Wrong number")
elif num < 500000:
    print("small number")
elif num < 750000:
    print("Medium number")
else:
    print("large number")