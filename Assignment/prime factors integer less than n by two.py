# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Function to find the prime factors
def prime_factors(n):
    factors = []
    for i in range(2, int(n/2) + 1):
        if n % i == 0 and is_prime(i):
            factors.append(i)
    return factors

# Test the function
num = int(input("Enter an integer: "))
print("The prime factors of", num, "are:", prime_factors(num))
