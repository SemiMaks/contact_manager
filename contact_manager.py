# Эта программа управляет контактами.

import contact
import pickle

# Глобальные константы для пунктов меню.
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
line = '-' * 30

# Глобальная константа для имени файла.
FILENAME = 'contacts.dat'


def main():
    # Загрузить существующий словарь контактов
    # и присвоить его пременной mycontacts.
    mycontacts = load_contacts()

    # Инициализация переменной для выбора пользователя.
    choice = 0

    # Обрабатывать варианты выбора пунктов меню до тех пор,
    # пока пользователь не пожелает выйти из программы.
    while choice != QUIT:
        # Получить выбранный пользователем пункт меню.
        choice = get_menu_choice()

        # Обработать выбранный вариант действий.
        if choice == LOOK_UP:
            look_up(mycontacts)
        elif choice == ADD:
            add(mycontacts)
        elif choice == CHANGE:
            change(mycontacts)
        elif choice == DELETE:
            delete(mycontacts)

    # Сохранить словарь mycontacts в файл.
    save_contacts(mycontacts)


def load_contacts():
    try:
        # Попробовать открыть файл contacts.dat.
        input_file = open(FILENAME, 'rb')

        # Расконсервировать словарь.
        contact_dct = pickle.load(input_file)

        # Закрыть файл phone_inventory.dat.
        input_file.close()
    except IOError:
        # Ошибка открытия файла,
        # создание пустого словаря.
        contact_dct = {}

    # Вернуть словарь.
    return contact_dct

# Функция выводит меню и получает
# проверенный на допустимость выбранный пользователем пункт.
def get_menu_choice():
    print(line)
    print('Меню')
    print(line)
    print('1 - Найти контактное лицо.')
    print('2 - Добавить новое контактное лицо.')
    print('3 - Изменить существующий контакт.')
    print('4 - Удалить контактное лицо.')
    print('5 - Выйти из программы.')
    print(line)

    # Получить выбранный пользователем пункт.
    choice = int(input('Введите выбранный пункт: '))

    # Проверка на допустимость.
    while choice < 1 or choice > 5:
        choice = int(input('Введите выбранный пункт: '))

    # Возвращаем выбранный пользователем пункт.
    return choice

# Функция look_up отыскивает элемент
# в заданном словаре.

def look_up(mycontacts):
    # Получить искомое имя.
    name = input('Введите имя: ')

    # Отыскать его в словаре.
