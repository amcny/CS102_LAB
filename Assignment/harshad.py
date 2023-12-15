def is_harshad_number(num):
    digit_sum = 0
    temp_num = num
    
    while temp_num > 0:
        digit_sum += temp_num % 10
        temp_num //= 10
    return num % digit_sum == 0

number = int(input("Enter a number: "))

if is_harshad_number(number):
    print(f"{number} is a Harshad number.")
else:
    print(f"{number} is not a Harshad number.")