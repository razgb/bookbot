def read_file(book_path):
    with open(book_path) as f:
        output = f.read()

    return output

def count_words(text):
    arr = text.split()
    count = 0

    for text in arr:
        count += 1

    print(f"{count} words found in the document")

    return count

def count_characters(text):
    char_dict = {}

    # remember, the entire book can be treated as a single large str.
    for character in text:
        character_lowered = character.lower()

        if character_lowered in char_dict:
            char_dict[character_lowered] += 1
        else:
            char_dict[character_lowered] = 1

    # filtering out the non-alphabetical chars out.
    alphabet_dict = {}

    for ch in char_dict:
        if ch.isalpha():
            alphabet_dict[ch] = char_dict[ch]
            # print(f"The '{ch}' character was found {char_dict[ch]} times")

    # turning the alphabetical chars into a list of dicts in the form of {char: "a", count: 5}
    alpha_dict_list = []
    for ch in alphabet_dict:
        alpha_dict_list.append({"char": ch, "count": alphabet_dict[ch]})

    # accepts a dictionary
    def sort_on(d):
        return d["count"]
    
    # the .sort() method sorts the list in place. key can also be a callback fn
    alpha_dict_list.sort(key=sort_on, reverse=True)

    for d in alpha_dict_list:
        print(f"The '{d["char"]}' character was found {d["count"]} times")

    return char_dict 

def main():
    print("--- Begin report of books/frankenstein.txt ---\n")

    book_path = "./books/frankenstein.txt"
    text = read_file(book_path)
    word_count = count_words(text)
    char_count = count_characters(text)

    print("\n--- End report ---")
    return 

main()
