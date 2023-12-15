a = 0
b = 1
n = int(input("Num of terms= "))
print(a, b, end=" ")

for i in range(2, n):
    t = a + b
    a = b
    b = t
    print(t, end=" ")