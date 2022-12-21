import os
def menu_():
    os.system('clear') 
    print('1 - Просмотр всех контактов')
    print('2 - Найти контакт')
    print('3 - Добавить контакт')
    print('4 - Изменить контакт')
    print('5 - Удалить контакт')
    print('6 - Завершить работу')
    print('_____________________')
    m = int(input('Введите номер строки функции: '))
    return m


def set_():
    os.system('clear') 
    print('Укажите расширение файла контактов:')
    print('1 - расширение файла: .txt')
    print('2 - расширение файла: .csv')    
    file_extension = int(input('Введите номер строки: '))
    return file_extension

def view_all(dict):
    for (k,v) in dict.items():
        print(f'{k} {v[0]} {v[1]} {v[2]}')

def contact_for_search():
    s = input('Для поиска введите часть имени или фамилии: ')
    return s

def new_contact():
    s = input('Введите через пробел Имя, Фамилию и номер (ххх-хх-хх-ххх): ')
    return s

def groupe_for_update_or_delete():
    print('Для изменения или удаления контакта сначала найдите контакт.')
    s = contact_for_search()
    return(s)

def contact_for_update():
    s = input('Введите через пробел измененную строку контакта, начиная с номера строки: ')
    return(s)
def contact_for_delete():
    s = input('Введите номер строки для удаления контакта:' ) 
    return s       