l = [10, 5, 8, 12, 7]
for i in range(0, 5):
    min = i
    for j in range(i, 5):
        if l[min] > l[j]:
            l[min], l[j] = l[j], l[min]
    print(l)

k = int(input("Enter the number you want: "))

def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

index = binary_search(l, k)
if index != -1:
    print(f"The number {k} is at index {index} in the sorted list.")
else:
    print("The number is not in the list.")