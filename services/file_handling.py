import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 950

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    def chek_punkt(text: str, index: int) -> bool:
        punkt = [',', '.', '!', ':', ';', '?']

        if (index + 1) <= len(text):
            if (text[index] in punkt) and (text[index + 1] not in punkt):
                return True
            else:
                return False
        else:
            return True

    fsize = start + size
    while True:
        if chek_punkt(text, fsize) and len(text[start:fsize + 1]) <= size:
            break
        else:
            fsize -= 1

    part_text = text[start:fsize + 1]

    return (part_text, len(part_text))


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as book_file:
        text = book_file.read()
    kursor = 0
    sting_number = 1;
    while True:
        part_text = _get_part_text(text, kursor, PAGE_SIZE)
        kursor += part_text[1]
        book[sting_number] = part_text[0].strip()
        sting_number += 1
        if kursor + PAGE_SIZE >= len(text):
            book[sting_number] = text[kursor:].strip()
            break


# Вызов функции prepare_book для подготовки книги из текстового файла

prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
