def encrypt(message):
    even_chars = ""
    odd_chars = ""
    for i in range(len(message)):
        if i % 2 == 0:
            even_chars += message[i]
        else:
            odd_chars += message[i]
    encrypted_message = even_chars + odd_chars
    return encrypted_message

def find(original, en):
    count = 1
    while en != original:
        en = encrypt(en)
        count += 1
    return count

message = input("Enter a message: ")
en = encrypt(message)
print(f"Encrypted Message: {en}")
count = find(message, en)
print(f"Number of rearrangements to get the original message: {count}")
