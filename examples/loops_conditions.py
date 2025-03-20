# for loop
#  Print numbers from 1 to 5
for i in [0, 1, 2, 3, 4, 5]:
    print(i)


# while loop
n = 1
while n <= 5:
    print(n)
    n += 1

# loop with break
for i in range(1, 10):
    if i == 5:
        break  # Stops when i is 5
    print(i)

# loop with continue
for i in range(1, 6):
    if i == 3:
        continue  # Skips when i is 3
    print(i)


fruits = ["apple", "banana", "cherry"]


for fruit in fruits:
    print(fruit)

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")