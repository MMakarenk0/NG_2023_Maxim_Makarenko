from math import sqrt
 
def summa(firstNum, secondNum):
    return firstNum + secondNum

def diff(firstNum, secondNum):
    return firstNum - secondNum
    
def mult(firstNum, secondNum):
    return firstNum * secondNum

def div(firstNum, secondNum):
    return firstNum / secondNum

def pow(firstNum, secondNum):
    return firstNum ** secondNum


def operation(firstNum, secondNum, choosedOper):
    match choosedOper:
        case "+":
            print(summa(firstNum, secondNum))
        case "-":
            print(diff(firstNum, secondNum))
        case "*":
            print(mult(firstNum, secondNum))
        case "/":
            print(div(firstNum, secondNum))
        case "**": 
            print(pow(firstNum, secondNum))
        case "sqrt":
            print(sqrt(firstNum))
        case _:
            print("Invalid operation selected!")

firstNum, secondNum = float(input("Enter first number: ")), float(input("Enter second number: "))
choosedOper = input("Choose the operation(+,-,*,/,**,sqrt): ")

operation(firstNum, secondNum, choosedOper)