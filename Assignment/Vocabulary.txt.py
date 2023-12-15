def is_valid_word(word, language_sets):
    word_set = set(word)
    return word_set in language_sets

def is_valid_sentence(sentence, language_sets):
    words = sentence.split()

    for word in words:
        if not is_valid_word(word, language_sets):
            return False

    return True

def count_valid_sentences(filename):
    language_set_1 = set('abcdefghijklm')
    language_set_2 = set('NOPQRSTUVWXYZ')
    language_sets = [language_set_1, language_set_2]

    valid_sentence_count = 0

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

            for line in lines:
                if is_valid_sentence(line.strip(), language_sets):
                    valid_sentence_count += 1

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return 0

    return valid_sentence_count

file_name = input("Enter the filename (e.g., Vocabulary.txt): ")

result = count_valid_sentences(file_name)
print("Number of valid sentences:", result)