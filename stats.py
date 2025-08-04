# Stats for books of bookbot

def get_num_words(filepath):
    with open(filepath) as book:
        contents = book.read()
        words = contents.split()
        return len(words)
        
def get_num_char_appearance(filepath):
    all_text = ""
    char_dict = {}
    with open(filepath) as book:
        all_text = book.read()
        all_text = all_text.lower() # no caps
        #all_text = sorted(all_text) # sort all chars : probably dont need to do.
        make_dict = set(all_text)
        
        # make a dict of each char from list
        for each in sorted(make_dict):
            char_dict[each] = 0
        # get count of each char from list. then add value to dict
        for each in char_dict:
            char_dict[each] = all_text.count(each)
        
        return char_dict
    
def get_char_frequency(filepath):
    all_text = get_num_char_appearance(filepath)
    sort_list = []
    for k, v in all_chars.items():
        sort_list.append({"char":k, "num":v})
        
        
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list
    
    