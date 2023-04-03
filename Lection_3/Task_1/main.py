from math import sqrt
 
def operation(firstNum, secondNum, choosedOper):
    match choosedOper:
        case "+":
            print(f"{firstNum} + {secondNum} = {firstNum+secondNum}")
        case "-":
            print(f"{firstNum} - {secondNum} = {firstNum-secondNum}")
        case "*":
            print(f"{firstNum} * {secondNum} = {firstNum*secondNum}")
        case "/":
            print(f"{firstNum} / {secondNum} = {firstNum/secondNum}")
        case "**": 
            print(f"{firstNum}^{secondNum} = {firstNum**secondNum}")
        case "sqrt":
            print(f"√{firstNum} = {sqrt(firstNum)}")
        case _:
            print("Invalid operation selected!")

operation(float(input("Enter first number: ")), float(input("Enter second number: ")), input("Choose the operation(+,-,*,/,**,sqrt): "))