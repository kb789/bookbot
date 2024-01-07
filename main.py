import sys
def count_words(file_contents):
    words=file_contents.split()        
    return len(words)
def count_chars(file_contents):
    words=file_contents.split()  
    word_dict={}
    letters="abcdefghijklmnopqrstuvwxyz"
    for word in words:
        for c in word:
            if c in letters:
                if c in word_dict.keys():
                    word_dict[c]+=1
                else:
                    word_dict[c]=1
    return word_dict     
def main():
    with open("books/frankenstein.txt") as f:
        file_contents=f.read()
        file_contents=file_contents.lower()
        word_count=count_words(file_contents)
        char_count_dict=count_chars(file_contents)
        char_val_list=list(char_count_dict.values())
        char_val_list.sort(reverse=True)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        print()
        for c in char_val_list:
            for key, val in char_count_dict.items():
                if c==val:
                    print(f"The letter {key} was found {val} times") 
        print("--- End report ---")
if __name__== '__main__':
    sys.exit(main())