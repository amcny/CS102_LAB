def is_neon_number(num):
    square = num * num
    digit_sum = 0
    temp_num = square
    
    while temp_num > 0:
        digit_sum += temp_num % 10
        temp_num //= 10
    return digit_sum == num

number = int(input("Enter a number: "))

if is_neon_number(number):
    print(f"{number} is a Neon number.")
else:
    print(f"{number} is not a Neon number.")