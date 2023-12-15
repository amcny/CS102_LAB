def F(n, r):
    if n == r or r == 0:
        return 1
    else:
        return F(n - 1, r) + F(n - 1, r - 1)

n_value = int(input("Enter the value of n: "))
r_value = int(input("Enter the value of r: "))

result = F(n_value, r_value)
print(f"F({n_value}, {r_value}) =", result)