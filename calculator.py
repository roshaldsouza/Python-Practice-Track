num1 = int(input("enter number 1 "))
num2 = int(input("enter number 2 "))
operator = input("enter operator ")
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("invalid operator")
