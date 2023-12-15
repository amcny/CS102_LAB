def F(x, y):
    if y <= x:
        return F(x - y, y) + 1
    else:
        return 0

x_value = int(input("Enter the value of x: "))
y_value = int(input("Enter the value of y: "))

result = F(x_value, y_value)
print(f"F({x_value}, {y_value}) =", result)