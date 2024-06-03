def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero is not allowed."

# Example usage
result = add(5, 3)
print(result)  # Output: 8

result = subtract(10, 4)
print(result)  # Output: 6

result = multiply(2, 6)
print(result)  # Output: 12

result = divide(10, 2)
print(result)  # Output: 5

result = divide(10, 0)
print(result)  # Output: Error: Division by zero is not allowed.