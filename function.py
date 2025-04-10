def sum(a, b):
    return a+b

def returString():
    return "Hello, Guest!"

def multiply(a,b):
    return a*b

def sumAndMultiplyAndSubstractResult(a,b):
    sumResult = sum(a, b)
    multiplyResult = multiply(a, b)
    return multiplyResult - sumResult


def findNumberInArr(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i

def linear_search(arr, target):
    number = findNumberInArr(arr, target)
    if(number):
        return number
    else:   
        return -1


