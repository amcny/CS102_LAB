def generate_series(n):
    
    series = [1, 1, 1]

    
    for i in range(3, n):
        next_term = series[i-3] + series[i-2] + series[i-1]
        series.append(next_term)

    return series
n = int(input("Enter the number of terms: "))
print("The first", n, "terms of the series are:", generate_series(n))
