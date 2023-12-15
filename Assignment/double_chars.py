def double_chars():
    s = input("Please enter a word: ")
    result = ''
    for i in range(len(s)):
        result += s[i]
        result += s[i]
    return result
print(double_chars())