# Эта программа управляет контактами.

import contact
import pickle

# Глобальные константы для пунктов меню.
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

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
