num1=float(input("Please enter number 1:"))
num2=float(input("Please enter number 2:"))
oper=input("Please enter an operator (+ or - or * or / or % or ^):")
if oper == "+":
    print("Result:",num1 + num2)
elif oper == "-":
    print("Result:",num1 - num2)
elif oper == "*":
    print("Result:",num1 * num2)
elif oper == "/":
    print("Result:",num1 / num2)
elif oper == "%":
    print("Result:",num1 % num2)
elif oper == "^":
    print("Result:",num1 ** num2)
else:
    print("Wrong operator")
