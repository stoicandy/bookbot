def main():
    book_path = "books/frankenstein.txt"
    
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = number_of_chars(text)

    # print(f"\nNumber of words: {num_words}")
    # print(f"\nNumber of chars: {chars_dict}")

    final_report(book_path, num_words, chars_dict)

def final_report(book_path, num_words, chars_dict):
    print(f"\n***Report of book {book_path}!***")
    print(f"Number of words in this doucument: {num_words}")

    sorted_chars_dict = {}
    for key in sorted(chars_dict, key = chars_dict.get, reverse = True):
        sorted_chars_dict[key] = chars_dict[key]
        
    for key, value in sorted_chars_dict.items():
        if key.isalpha():
            print(f"The '{key}' character was found '{value}' times")
        else:
            continue

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()


def number_of_chars(text):
    c = {}
    text_lower = text.lower()

    for char in text_lower:
        if char in c:
            c[char]+= 1
        else:
            c[char] = 1

    return c






main()
