def gcd_iterative(a, b):
    while(b):
        a, b = b, a % b
    return a

# Test the function
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("The GCD of", num1, "and", num2, "is", gcd_iterative(num1, num2))