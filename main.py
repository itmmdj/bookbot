def main():
    book_path = "books/frankenstein.txt"
    text = get_file_path(book_path)
    count = count_words(text)
    print(count)
    
def get_file_path(path):
    with open(path) as f:
        return f.read()

def count_words(book):
    words = book.split()
    return len(words)

main()