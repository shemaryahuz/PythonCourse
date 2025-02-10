num=int(input("Please enter the number of days:"))
if num%4 == 0:
    if num%100 == 0:
        if num%400 == 0:
            print("This is a leap year")
        else:
            print("This is not a leap year")

    else:
        print("This is a leap year")

else:
    print("This is not a leap year")