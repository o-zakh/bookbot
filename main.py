output_dict = {}
dict_list = []
book_path = "books/frankenstein.txt"

def main():
    print(f"--- Begin report of {book_path} ---")
    lowered_letters_text = lower_letters(read_text()) # Взяли текст и сделали все буквы маленькими
    char_num(lowered_letters_text) # Посчитали все буквы и добавили их в словарь output_dict
    print(f"{count_words(read_text())} words found in the document")
    print()
    dict_to_list()
    dict_list.sort(reverse=True, key=sort_on)
    for listed_dict in dict_list:
        print(f"The '{listed_dict['letter']}' character was found {listed_dict['number']} times")
    print("--- End report ---")


# Функция открытия книги и возврата текста:
def read_text():
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

# Функция подсчета слов в книге:
def count_words(file_contents):
    word_num = len(file_contents.split())
    return word_num

# Функция уменьшения регистра букв:
def lower_letters(file_contents):
    lowered_string = file_contents.lower()
    return lowered_string

#Функция подсчета каждого символа в тексте:
def char_num(text_to_process):
    for char in text_to_process:
        if char in output_dict:
            output_dict[char] += 1 
        if char not in output_dict:
            output_dict[char] = 1
    # print(output_dict)

# Для начала надо создать новый лист •
# Потом нужно найти способ вытащить значения из output_dict и запихнуть их в новый dict
# Потом каждый такой dict запихнуть в лист

def dict_to_list():
    temp_dict = {}
    for key, value in output_dict.items():
        if key.isalpha():
            temp_dict['letter'] = key
            temp_dict['number'] = value
            dict_list.append(temp_dict)
            temp_dict = {}

# Добавляю функцию сортировки словарей по второму индексу:
def sort_on(dict):
    return dict["number"]

main()