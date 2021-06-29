#Return statement = functions send python values/objects back to the caller.
#                   These values are known as the function's return value.

def multiply(num1, num2):
    result = num1 * num2
    return result #returns the result of num1 * num2

print(multiply(6, 8))

def divide(number1, number2):
    return number1 / number2 #returns the result of number1 / number2

x = divide(10, 5)
print(x)