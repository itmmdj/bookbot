def main():
    book_path = "books/frankenstein.txt"
    text = get_file_path(book_path)
    count = count_words(text)
    print(count)
    print(sort_and_count_letters)

def get_file_path(path):
    with open(path) as f:
        return f.read()

def count_words(book):
    words = book.split()
    return len(words)

def sort_and_count_letters(text):
    lowercase_string = text.lower()
    letter_dict = {}
    for letter in lowercase_string:
       if letter in letter_dict:
           letter_dict[letter] += 1
       else:
           letter_dict[letter] = 1
    return letter_dict 
    
main()