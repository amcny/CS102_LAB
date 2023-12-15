import random

def generator(l):
    x = random.randint(100000, 200000)
    if x not in l:
        l.append(x)

def search(l, k):
    low, high = 0, len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] < k:
            low = mid + 1
        elif l[mid] > k:
            high = mid - 1
        else:
            return mid
    return -1

l = []
for i in range(10000):
    generator(l)

l.sort()

k = int(input("Enter which number are you looking for: "))
index = search(l, k)

if index == -1:
    print("The number is not there.")
else:
    print(f"The number {k} is at index {index} in the sorted list.")