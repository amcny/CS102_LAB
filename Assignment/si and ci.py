def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def calculate_compound_interest(principal, rate, time, n):
    return principal * (1 + rate / (n*100)) ** (n*time)

# Example usage:
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
n = float(input("Enter the number of times interest applied per time period: "))

simple_interest = calculate_simple_interest(principal, rate, time)
compound_interest = calculate_compound_interest(principal, rate, time, n)

print("The simple interest is: ", simple_interest)
print("The compound interest is: ", compound_interest)
