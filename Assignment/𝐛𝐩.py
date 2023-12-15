def power(base, exponent):

    result = 1

    while exponent > 0:
        if exponent % 2 == 1:
            result *= base

        base *= base
        exponent //= 2

    return result

base = int(input("Enter the base (b): "))
exponent = int(input("Enter the exponent (p): "))

if exponent < 0:
    result = 1 / power(base, -exponent)
else:
    result = power(base, exponent)

print(f"The result of {base}^{exponent} is: {result}")
