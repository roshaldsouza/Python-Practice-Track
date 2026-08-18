def mini_calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation  == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    elif operation == "//":
        return num1 // num2
    else:
        print("invalid operation")

num1 = int(input("enter num1 "))
num2 = int(input("enter num2 "))
operation = input("enter operator ")
res = mini_calculator(num1,num2,operation)
print(f"{num1} {operation} {num2} = {res}")