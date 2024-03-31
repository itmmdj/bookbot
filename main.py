def main():
    book_path = "books/frankenstein.txt"
    text = get_file_path(book_path)
    count = count_words(text)
    dict = char_dict(text)
    list = char_dict_to_sorted_list(dict)
    for item in list:
        if not item['char'].isalpha():
            continue
        else:
            print(f"The '{item['char']}' character was found {item['count']} times") 

    print("--- End Report ---")
        
def sort_on(d):
    return d["count"]

def char_dict_to_sorted_list(char_num_dict):
    list = []
    for entry in char_num_dict:
        list.append({"char": entry , "count": char_num_dict[entry]})
    list.sort(reverse=True, key=sort_on)
    return list
    

def get_file_path(path):
    with open(path) as f:
        return f.read()

def count_words(book):
    words = book.split()
    return len(words)

def char_dict(text):
    lowercase_string = text.lower()
    letter_dict = {}
    for letter in lowercase_string:
       if letter in letter_dict:
           letter_dict[letter] += 1
       else:
           letter_dict[letter] = 1
    return letter_dict 
    
main()