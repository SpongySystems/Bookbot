def main():
    book_name = "Frankenstein"
    book_path = f"books/{book_name.lower()}.txt"
    book_content = get_book_text(book_path)
    word_count = count_words(book_content)
    letters = letter_count(book_content)
    generate_report(book_name, word_count, letters)

# load the text of the file
def get_book_text(bookpath):
    with open(bookpath) as f:
        return f.read()

#count the words in the document
def count_words(text):
    words = text.split()
    return len(words)

#count only the letters in the document and store it in a dictionary
def letter_count(text):
    letter_dict = {}
    for letter in text:
        if not letter.isalpha():
            continue
        if letter.lower() not in letter_dict:
            letter_dict[letter.lower()] = 0
        letter_dict[letter.lower()] += 1
    return letter_dict

#generate a report of the book with the word- and letter count
def generate_report(book_name, word_count, letters):
    letter_list = sort_dict(letters)

    print(f"---Report of {book_name} ---")
    print(f"This document has {word_count} words in total\n")

    for letter in letter_list:
        print(f"The '{letter["char"]}' character was found {letter["count"]} times.")

    print("---End report---")

#function that handles the sorting
def sort_on(dict):
    return dict["count"]

#sort the letter count from largest to smallest count
def sort_dict(dict):
    letter_list = []
    for char in dict:
        letter_list.append({"char": char, "count": dict[char]})

    letter_list.sort(reverse=True, key=sort_on)
    return letter_list

main()