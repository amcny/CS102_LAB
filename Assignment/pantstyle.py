n = 8
for i in range(n):
    for j in range(n-i):
        print("*", end="")
    for j in range(2*i):
        if j == 2*i-1 or j == 0:
            print("_", end="")
        else:
            print(" ", end="")
    for j in range(n-i):
        print("*", end="")
    print()