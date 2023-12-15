def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]

    if n == 0:
        return 0
    elif n == 1:
        return 1

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

def demonstrate_fibonacci(n):
    global function_calls
    function_calls = 0

    def fibonacci_count_calls(k):
        global function_calls
        function_calls += 1
        return fibonacci(k)

    result = fibonacci_count_calls(n)

    print(f"The {n}th Fibonacci number is: {result}")
    print(f"Number of function calls: {function_calls}")

# Demonstrate for input value 9
demonstrate_fibonacci(9)