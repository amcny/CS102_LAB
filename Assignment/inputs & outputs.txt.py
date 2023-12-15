import random

def generate_random_numbers(rows, columns):
    numbers = [[random.randint(1, 100) for _ in range(columns)] for _ in range(rows)]
    return numbers

def insertion_sort_row(row):
    for i in range(1, len(row)):
        key = row[i]
        j = i - 1
        while j >= 0 and key < row[j]:
            row[j + 1] = row[j]
            j -= 1
        row[j + 1] = key

def sort_matrix_row_wise(matrix):
    for row in matrix:
        insertion_sort_row(row)

def write_matrix_to_file(matrix, filename):
    with open(filename, 'w') as file:
        for row in matrix:
            row_str = ' '.join(map(str, row))
            file.write(row_str + '\n')

random_numbers = generate_random_numbers(20, 10)

sort_matrix_row_wise(random_numbers)

write_matrix_to_file(random_numbers, 'output.txt')

print("Sorting and writing to output.txt completed.")