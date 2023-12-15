def find_factors(n):
    factors = []
    for i in range(1, int(n/2) + 1):
        if n % i == 0:
            factors.append(i)
    factors.append(n)
    return factors
n = int(input("Enter an integer: "))
print("The factors of", n, "are:", find_factors(n))