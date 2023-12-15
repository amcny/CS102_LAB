x = int(input("Enter value of x: "))
n = int(input("Enter value of n: "))
sum = 0
for i in range(1, n + 1):
    sum += (x ** i) / i
print(sum)