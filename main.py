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

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        file_words = count_words(file_contents)
        character_counts = char_counts(file_contents)
        print(file_words)
        print(character_counts)

if __name__ == "__main__":
    main()
