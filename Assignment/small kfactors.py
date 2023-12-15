def find_smallest_factors(n, k):
    factors = []
    count = 0
    current_number = 1

    while count < k:
        if n % current_number == 0:
            factors.append(current_number)
            count += 1
        current_number += 1

    return factors

number = int(input("Enter the integer (n): "))
K = int(input("Enter the value of K: "))

result = find_smallest_factors(number, K)

if len(result) == K:
    print("Smallest", K, "factors of", number, "are:", result)
else:
    print(f"Required number of factors are not possible for {number}.")