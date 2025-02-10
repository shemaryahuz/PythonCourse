num=int(input("Please enter a 5 digits number:"))
digit1=num//10000
digit2=num//1000%10
digit3=num//100%10
digit4=num//10%10
digit5=num%10
print("The multiplication of the number's digits is:(",digit1,"* 1 ) + (",digit2,"* 2 ) + (",digit3,"* 3 ) + (",digit4," * 4 ) + (",digit5," * 5 ) =",digit1+digit2*2+digit3*3+digit4*4+digit5*5)