import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

with open("Numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]
file.close()

R = random.randint(1, 100)
for i in range(4, len(numbers), 5):
    a = gcd(numbers[i], R)
    if a == 1:
        numbers[i] = 1
    else:
        numbers[i] = 0

with open("Numbers.txt", "w") as file:
    for num in numbers:
        file.write(f"{num}\n")
file.close()

print("File 'Numbers.txt' has been updated.")
