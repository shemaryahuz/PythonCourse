day = input("What day is it today? (1,2,...,7/Sunday,Monday,...,Shabbat):")
if day != "1" and day != "2" and day != "3" and day != "4" and day != "5" and day != "6" and day != "7" and day != "Sunday" and day != "Monday" and day != "Tuesday" and day != "Wednesday" and day != "Thursday" and day != "Friday" and day != "Shabbat" :
    print("Wrong input")
elif day == "1" or day == "2" or day == "3" or day == "4" or day == "5" or day == "6" or day == "7":
    num=int(day)
    if num < 6 :
        print("Today is a study day!")
    elif num == 6:
        print("Today we are preparing for shabbat!")
    else:
        print("Today is Shabbat!")
else:
    if day != "Friday" and day != "Shabbat":
        print("Today is a study day!")
    elif day == "Friday":
        print("Today we are preparing for shabbat!")
    else:
        print("Today is Shabbat!")

