l = [9, 6, 15, 3, 7]
for i in range(len(l)):
    for j in range(len(l)):
        if l[i] < l[j]:
            l[i], l[j] = l[j], l[i]
    print(l)

k = 15

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
