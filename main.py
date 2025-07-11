import sys
from stats import get_num_words, num_of_characters, sorted_characters

def get_book_text(file_path):
    with open(file_path) as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]



    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    book_text = get_book_text(book_path)
   
    print("----------- Word Count ----------")
    word_count = get_num_words(book_text)
    print(f"Found {word_count} total words")
    
    print("--------- Character Count -------")
    char_counts = num_of_characters(book_text)

    char_list = []
    for char, count in char_counts.items():
        char_list.append({"char": char, "count": count})

    char_list.sort(reverse=True, key=sorted_characters)
    for dictionary in char_list:
        char = dictionary["char"]
        if char.isalpha():
            print(f"{char}: {dictionary['count']}")
    print("============= END ===============")
main()