from datetime import datetime

def start_selection():
    print("\n" + "=" * 30)
    print('выберите пункт меню')
    print('1 - создать заметку ')
    print('2 - поиск заметки по ID ')
    print('3 - фильтровать по дате ')
    print('4 - редактировать заметку по ID ')
    print('5 - удалить заметку по ID ')
    print('6 - показать все заметки ')
    print('7 - выход ')
    command = int(input(": "))
    if 0 < command < 7:
        return command
    elif command == 7:
        return False
    else:
        print('ошибка ввода')


def confirm():
    print('успешно')


def create_note():
    title = input('введите заголовок: ')
    data = input('введите данные: ')
    date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
    note = {'title' : title, 'data': data, 'date': date}
    return note


def print_note(note):
    print(note['ID'])
    print(note['title'].center(20))
    print(note['data'])
    print(note['date'])
    print('-------------------')


def get_id():
    id = int(input('введите ID: '))
    return id


def get_date():
    date = input('Введите дату в формате dd.mm.yyyy: ')
    return date


def not_find():
    print('не нашлось')

