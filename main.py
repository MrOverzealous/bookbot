
def main():
    frank_path = "./books/frankenstein.txt"
    text = get_book_text(frank_path)
    print(text)
    word_count = count_words(text)
    print(f"{word_count} words found in the document")
    letter_count = count_letters(text)
    print(letter_count)
    chars_sorted_list = chars_dict_to_sorted_list(letter_count)

    print(f"--- Begin report of {frank_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_book_text(text):
    with open(text) as f:
        return f.read()

def count_words(text):
    words = text.split(None)
    return len(words)
    
def count_letters(text):
    letters = {}
    for i in range(len(text)):
        lower_letter = text[i].lower()
        if (lower_letter in letters):
            letters[lower_letter] += 1
        else:
            letters[lower_letter] = 1

    return letters

def sort_on(item):
    return item["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()

