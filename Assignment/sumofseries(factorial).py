sum = 0
n = int(input())
pro = 1
for i in range(1, n + 1):
    sum += 1 / pro
    pro *= i
print(sum)