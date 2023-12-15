def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def compare_circles(x1, y1, r1, x2, y2, r2):
    distance_centers = calculate_distance(x1, y1, x2, y2)

    if distance_centers + r2 < r1:
        return "Circle 2 is inside Circle 1"
    elif distance_centers > r1 + r2:
        return "Circle 2 is away from Circle 1"
    else:
        return "Circle 1 and Circle 2 overlap"

x1 = float(input("Enter the x-coordinate of Circle 1 center: "))
y1 = float(input("Enter the y-coordinate of Circle 1 center: "))
r1 = float(input("Enter the radius of Circle 1: "))

x2 = float(input("Enter the x-coordinate of Circle 2 center: "))
y2 = float(input("Enter the y-coordinate of Circle 2 center: "))
r2 = float(input("Enter the radius of Circle 2: "))

result = compare_circles(x1, y1, r1, x2, y2, r2)
print(result)