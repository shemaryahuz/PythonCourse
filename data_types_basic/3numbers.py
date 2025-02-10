num1=float(input("Please enter number 1:"))
num2=float(input("Please enter number 2:"))
num3=float(input("Please enter number 3:"))
a1=num1>15 and num1<150
a2=num2>15 and num1<150
a3=num3>15 and num1<150
b=num1!=num2 and num1!=num3
c=num1==num2 or num1==num3
d=num2==num1 or num2!=num3
print("Are the numbers great then 15 and less then 150? number 1:",a1,". number 2:",a2,". number 3:",a3,".")
print("Is the first number nut equal to the second number and nut equal to the third one?",b,".")
print("Is the first number equal to the second number or to the third one?",c,".")
print("Is the second number equal to the first number or nut equal to the third one?",d,".")
