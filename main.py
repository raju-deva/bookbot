def main():
    path_to_file="books/frankenstein.txt"
    # text=get_book_text(path_to_file)
    totalcount=count_words(path_to_file)
    chars_dict=char_count(path_to_file)
    # print(text)
    # print(totalcount)
    # print(totalchar)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{totalcount} words found in the document")
    print()
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
def get_book_text(path):    
    with open(path) as f:
       return f.read()

def count_words(path):
    words=get_book_text(path).split()
    return len(words)

def char_count(path):
    text=get_book_text(path).lower()
    char_count_dict={}
    for char in text:
        char_count_dict[char]=char_count_dict.get(char,0)+1
    return char_count_dict

def sorn_on(d):
    return d["num"]
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list=[]
    for ch in num_chars_dict:
        sorted_list.append({"char":ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sorn_on)
    return sorted_list

main()