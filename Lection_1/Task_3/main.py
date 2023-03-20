from math import sqrt

firstNum = float(input("Enter first number: "))
secondNum = float(input("Enter second number: "))
choosedOper = input("Choose the operation(+,-,*,/,**,sqrt): ")

match choosedOper:
    case "+":
        print(f"The result of addition is: {firstNum+secondNum}")
    case "-":
        print(f"The result of subtraction is: {firstNum-secondNum}")
    case "*":
        print(f"The result of multiplication is: {firstNum*secondNum}")
    case "/":
        print(f"The result of division is: {firstNum/secondNum}")
    case "**": 
        print(f"The result of elevation in degree {secondNum} is: {firstNum**secondNum}")
    case "sqrt":
        print(f"The result of finding the square root is: {sqrt(firstNum)}")
    case _:
        print("Invalid operation selected!")

