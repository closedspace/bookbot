from collections import Counter


def main():
    with open("./books/frankenstein.txt") as f:
        content = f.read()
        word_count = len(content.split())
        countah = Counter(content.lower())
        print("--- Begin Report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document\n")
        for char, num in countah.most_common():
            if char.isalpha():
                print(f"The '{char}' character was found {num} times'")
        print("--- End Report ---")


if __name__ == "__main__":
    main()
