def char_counts(string):
    chars = {}
    for char in string.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


def count_words(string):
    return len(string.split())

def print_report(book, words, char_counts):
    print(
            f"--- Begin report of {book} ---\n"
            f"{words} words found in the document\n"
    )
    for char, count in sorted(char_counts.items(), key=lambda item: item[1])[::-1]:
        print(f"The '{char}' character was found {count} times")

    print('--- End report ---')

def print_report_for_book(location):
    with open(location) as f:
        file_contents = f.read()
        file_words = count_words(file_contents)
        character_counts = char_counts(file_contents)
        print_report(location, file_words, character_counts)

def main():
    print_report_for_book("books/frankenstein.txt")

if __name__ == "__main__":
    main()
