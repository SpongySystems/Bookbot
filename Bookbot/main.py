def main():
    book_name = "Frankenstein"
    book_path = f"books/{book_name.lower()}.txt"
    book_content = get_book_text(book_path)
    word_count = count_words(book_content)
    letters = letter_count(book_content)
    generate_report(book_name, word_count, letters)


def get_book_text(bookpath):
    with open(bookpath) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def letter_count(text):
    letter_dict = {}
    for letter in text:
        if not letter.isalpha():
            continue
        if letter.lower() not in letter_dict:
            letter_dict[letter.lower()] = 0
        letter_dict[letter.lower()] += 1
    return letter_dict

def generate_report(book_name, word_count, letters):
    letter_list = sort_dict(letters)

    print(f"---Report of {book_name} ---")
    print(f"This document has {word_count} words in total\n")

    for letter in letter_list:
        print(f"The '{letter["char"]}' character was found {letter["count"]} times.")

    print("---End report---")

def sort_on(dict):
    return dict["count"]

def sort_dict(dict):
    letter_list = []
    for char in dict:
        letter_list.append({"char": char, "count": dict[char]})

    letter_list.sort(reverse=True, key=sort_on)
    return letter_list

main()