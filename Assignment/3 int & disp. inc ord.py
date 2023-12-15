def compare_and_swap(arr, i, j):
    if arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]

def sort_three_integers(a, b, c):
    numbers = [a, b, c]

    for i in range(2):
        for j in range(2 - i):
            compare_and_swap(numbers, j, j + 1)

    return numbers

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

sorted_numbers = sort_three_integers(num1, num2, num3)
print("Numbers in increasing order:", sorted_numbers)