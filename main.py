def main():
    print(f"В книге {count_words(read_text("books/frankenstein.txt"))} слов")

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

main()