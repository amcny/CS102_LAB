def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_month_days(year, month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and is_leap_year(year):
        return 29
    else:
        return days_in_month[month - 1]

def display_calendar(year, month, first_day):
    days_in_month = get_month_days(year, month)

    print(f"{month} {year}")
    print("Sun Mon Tue Wed Thu Fri Sat")

    day = 1
    for _ in range(first_day):
        print("    ", end=" ")

    for _ in range(1, days_in_month + 1):
        print(f"{day:2}", end=" ")
        if (day + first_day) % 7 == 0:
            print()
        day += 1

year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))
first_day = int(input("Enter the first day of the month (0-6, where 0 is Sunday): "))

display_calendar(year, month, first_day)