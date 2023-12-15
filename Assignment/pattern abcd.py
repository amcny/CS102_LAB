# Initialize the number of rows
rows = 7

# Initialize the ASCII value of 'A'
ascii_value = 65

# Pattern
for i in range(rows):
    pattern = ''
    for j in range(i+1):
        pattern += chr(ascii_value) + ' '
        ascii_value += 1
    print(pattern)
