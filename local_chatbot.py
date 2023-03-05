
    # Cделать локальный чат-бот с хранилищем данных в формате JSON, 
    # как объясняли в приложенной записи буткемпа

import json

filmets = {'name': '', 'age': '', 'genre': '', 'country': ''}
file = 'chatbot.json'

with open(file) as film_save:
    films = json.load(film_save)


def save():
    with open(file, 'w') as file_save:
        json.dump(films, file_save)

def all_print():
    if len(films) == 0:
        print('\nСписок фильмов пуст! \n')
        return

    else:
        for film in films:
            film_print(film)

def film_print(film):
    print(f'\nНазвание - {film["name"]}\nГод - {film["age"]}\nЖанр - {film["genre"]}\nСтрана - {film["country"]}\n')

def search_one(key, message):
    search_film = input(f'Введите {message} фильма! \n')
    for film in films:
        if film[key] == search_film:
            film_print(film)
            return film
    print('\nТакого фильма нет в списке! \nПопробуйте ввести заново: \n')
    search_one(key, message)

def film_delete(key, message):
    film = search_one(key, message)
    command_del_one = input(f'Удалить фильм {film["name"]}? \n Yes - y\n No - n\n')
    if command_del_one == 'y':
        i = films.index(film)
        films.pop(i)
        print(f'Фильм {film["name"]} успешно удалён! \n')
        save()
        return
    elif command_del_one == 'n': return
    else: print('Введите команду правильно! \n')

def film_edit(key, message):
    film = search_one(key, message)
    command_edit_one = input(f'Редактировать фильм {film["name"]}? \n')
    if command_edit_one == 'y':
        film_add(film)
        save()
        print(f'Фильм {film["name"]} успешно изменён! \n')
        return
    elif command_edit_one == 'n': return
    else: print('Введите команду правильно! \n')

def film_add(film):
    film['name'] = input('Введите название фильма! \n')
    film['age'] = input('Введите год фильма! \n')
    film['genre'] = input('Введите жанр фильма! \n')
    film['country'] = input('Введите страну! \n')
    print(f'Фильм {film["name"]} успешно добавлен! \n')
    return film

def glob_search(function):
    if len(films) == 0:
        print('\nСписок фильмов пуст! \n')
        return
    
    else:
        command_search = input('Искать будем по: \n названию фильма - n\n году - a \n жанру - g \n стране - c \n')

        if command_search == 'n':
            key = 'name'
            message = 'название'
            function(key, message)

        elif command_search == 'a':
            key = 'age'
            message = 'год'
            function(key, message)

        elif command_search == 'g':
            key = 'genre'
            message = 'жанр'
            function(key, message)

        elif command_search == 'c':
            key = 'country'
            message = 'страну'
            function(key, message)

        else: 
            print('Введите команду правильно! \n')
            glob_search(function)


while True:
    command = input('Что будем делать?\n Просмотреть фильмы - see \n Добавить фильм - add \n Удалить фильм - del \n Редактировать фильм - edit \n Завершить работу - q\n')

    if command == 'see':
        command_see = input('Показать все фильмы, или один? all / one \n')

        if command_see == 'all':
            all_print()
        elif command_see == 'one':
            glob_search(search_one)

    elif command == 'add':
        film = film_add(filmets)
        films.append(film)
        save()

    elif command == 'del':
        glob_search(film_delete)

    elif command == 'edit':
        glob_search(film_edit)

    elif command == 'q':
        break

