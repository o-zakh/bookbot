def main():
    lowered_letters_text = lower_letters(read_text("books/frankenstein.txt"))
    char_num(lowered_letters_text)

# Функция открытия книги и возврата текста:
def read_text(book_path):
    print("Открываю книгу...")
    with open(book_path) as f:
        file_contents = f.read()
        print("Возвращаю текст книги...")
        return file_contents

# Функция подсчета слов в книге:
def count_words(file_contents):
    print("Начинаю подсчет слов")
    word_num = len(file_contents.split())
    return word_num

# Функция уменьшения регистра букв:
def lower_letters(file_contents):
    lowered_string = file_contents.lower()
    return lowered_string

#Функция подсчета каждого символа в тексте:
def char_num(text_to_process):
    output_dict = {}
    for char in text_to_process:
        if char in output_dict:
            output_dict[char] += 1 
        if char not in output_dict:
            output_dict[char] = 1
    print(output_dict)

main()