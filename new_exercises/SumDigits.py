num=int(input("Please enter a 4 digits number:"))
unit=num%10
ten=num//10%10
hund=num//100%10
thou=num//1000
print("The sum of the number's digits is",thou,"+",hund,"+",ten,"+",unit,"=",unit+ten+hund+thou)
