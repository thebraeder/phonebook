from fileinput import filename
import os
def check_directory(filename: str):
    if filename not in os.listdir():
        with open(filename, 'w', encoding = 'utf-8') as data:
            data.write("")

def add_new_user(name: str, phone: str, filename: str):
    with open(filename, 'r+t', encoding='utf-8') as wrtbl:
#l = wrtbl.readlines()
        lins_count = len(wrtbl.readlines())
        wrtbl.write(f"{lins_count + 1};{name};{phone}\n")


def read_all(filename: str) -> str:
    with open(filename, 'r', encoding = 'utf-8') as data:
        resolt = data.read()
    return resolt


def search_user(data: str) -> str:

    with open(filename, 'r', encoding = 'UTF-8') as content:
        text = content.readlines()
        res = ([item for item in text if data.lower() in item.lower()])
    return (''.join(res)).replace(';', ' ') if res else 'Вхождений не найдено'

def transfer_user(data: str) -> str:

    with open(filename, 'r', encoding = 'UTF-8') as content:
        text = content.readlines()
        res = ([item for item in text if data.lower() in item.lower()])
    return (''.join(res)).replace(';', ' ') if res else 'Вхождений не найдено'

INFO_STRING = """
Выберите режим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск
4 - перенос контакта
"""

DATASOURCE = 'phone.txt'

check_directory(DATASOURCE)

while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        print(read_all(DATASOURCE))
    elif mode == 2:
        user = input()

        phone = input()
        add_new_user(name=user, phone=phone, filename=DATASOURCE)

    elif mode == 3:
        search = input('Введите строку для поиска: ')
        print(search_user(search, DATASOURCE))
        exit()
    elif mode == 4:
        pass