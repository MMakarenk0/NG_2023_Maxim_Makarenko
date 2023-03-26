from math import sqrt

firstNum = float(input("Enter first number: "))
secondNum = float(input("Enter second number: "))
choosedOper = input("Choose the operation(+,-,*,/,**,sqrt): ")

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

