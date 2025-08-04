from stats import *
import sys

def sort_on(items):
    return items["num"]

def main():
    
    if len(sys.argv)> 1:
        bookpath = sys.argv[1]
        print(bookpath)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    word_count = get_num_words(bookpath)
    all_chars = get_num_char_appearance(bookpath)
    
    sort_list = []
    
    for k, v in all_chars.items():
        sort_list.append({"char":k, "num":v})
        
        
    sort_list.sort(reverse=True, key=sort_on)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}...")
    print("----------- Word Count ----------")
    print( f"Found {word_count} total words")
    print("--------- Character Count -------")
    for ele in sort_list:
        if ele["char"].isalpha():
            print(f"{ele["char"]}: {ele["num"]}")
        else:
            continue
    
    print("============= END ===============")
    
    

    
main()






