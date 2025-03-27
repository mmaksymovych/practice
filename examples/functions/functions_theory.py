# 1. Simple function (no arguments, no return value)
def greet():
    print("Hello, world!")

greet()  # Output: Hello, world!

# 2. Function with positional arguments
def add(x, y):
    print(f"The sum of {x} and {y} is {x + y}")

add(4, 6)  # Output: The sum of 4 and 6 is 10

# 3. Function with default arguments
def greet_user(name="Guest"):
    print(f"Hello, {name}!")

greet_user("Bob")  # Output: Hello, Bob!
greet_user()       # Output: Hello, Guest!

# 4. Function returning a value
def multiply(a, b):
    return a * b

result = multiply(3, 7)
print(f"Multiplication result: {result}")  # Output: Multiplication result: 21

# 5. Function with variable-length positional arguments (*args)
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(f"Sum is: {sum_all(1, 2, 3, 4)}")  # Output: Sum is: 10

# 6. Function with variable-length keyword arguments (**kwargs)
def print_user_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_user_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York

# 7. Lambda (anonymous) function
square = lambda x: x ** 2
print(f"Square of 5 is: {square(5)}")  # Output: Square of 5 is: 25


# A simple recursive function that counts down from a given number to 0
def countdown(n):
    if n == 0:  # Base case: stop recursion when n reaches 0
        print("Blast off!")
    else:
        print(n)
        countdown(n - 1)  # Recursive call with n-1

# Example usage:
countdown(5)

def sum(a,b):
    return a+b

def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1  # Target not found

arr = [1,3,5,7,9]
target = 5

res = linear_search(arr, target)
print(res)