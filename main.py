def main():
    book_path = "books/frankenstein.txt"
    text = book_text(book_path)
    word_count = count_words(text)
    print(f"{word_count} found in the doc.")

def count_words(text):
    words = text.split()
    return len(words)

def book_text(book):
    with open(book) as f:
        return f.read()

main()
