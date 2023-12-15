def is_happy_number(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit)**2 for digit in str(num))
    return num == 1

def print_happy_numbers():
    for i in range(1, 101):
        if is_happy_number(i):
            print(i)

print("Happy Numbers from 1 to 100:")
print_happy_numbers()