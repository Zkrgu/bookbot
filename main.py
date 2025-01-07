def count_words(str):
    return len(str.split())

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        file_words = count_words(file_contents)
        print(file_words)

if __name__ == "__main__":
    main()
