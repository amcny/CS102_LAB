def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

# Test the function
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("The GCD of", num1, "and", num2, "is", gcd_recursive(num1, num2))
