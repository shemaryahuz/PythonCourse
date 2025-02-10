num=int(input("Please enter a 4 digits number:"))
unit=num%10
ten=num//10%10
hund=num//100%10
thou=num//1000
print("The conversion of the number to tow numbers is:",thou*10+hund,",",ten*10+unit)