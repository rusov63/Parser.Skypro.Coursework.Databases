from function import get_hh_vacanc, convert_sql, create_database, save_data_to_database
from config import config
from classes import DBManager


# id работодателей
id = 2733062, 701365, 864086, 598471, 1519234, 5971349, 9261916, 3361389, 5202841, 67611

def main():
    #приветствие. начало
    print(f'Добрый день. Программа для сбора данных по вакансиям {len(id)} компаний')

    params = config()

    #парсинг всех вакансий от работодателей по id
    data_requests = get_hh_vacanc(id)

    #создание БД
    create_database('HH_Database', params)

    #сохранение данных в созданную таблицу в БД
    save_data_to_database(data_requests, 'HH_Database', params)

    #ковертируем sql файл для извлечения вопросов
    convert_sql()

    #вывод меню для пользователя
    print('Выберите действия с полученной информацией. Выберите и нажмите ENTER:\n'
          'a - список всех компаний и количество вакансий у каждой компании\n'
          'b - список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию\n'
          'c - средняя зарплата по вакансиям\n'
          'd - список всех вакансий, у которых зарплата выше средней по всем вакансиям\n'
          'e - список всех вакансий, в названии которых указанное Вами слово)\n'
          'q - завершение')


    #выбор пользователем варианта из меню
    user_choice = input()

    db = DBManager()

    while user_choice != 'q':
        if user_choice == 'a':
            #вывод списка всех компаний и количества вакансий у каждой компании
            db.get_companies_and_vacancies_count('HH_Database', params)
            user_choice = input('Выберите следующую команду ')
        if user_choice == 'b':
            #вывод списка всех вакансий с указанием названия компании,
            #названия вакансии, зарплаты и ссылки на вакансию
            db.get_all_vacancies('HH_Database', params)
            user_choice = input('Выберите следующую команду ')
        if user_choice == 'c':
            #вывод средней зарплаты по вакансиям
            db.get_avg_salary('HH_Database', params)
            user_choice = input('Выберите следующую команду ')
        if user_choice == 'd':
            #вывод списка всех вакансий, у которых зарплата выше средней по всем вакансиям
            db.get_vacancies_with_higher_salary('HH_Database', params)
            user_choice = input('Выберите следующую команду ')
        if user_choice == 'e':
            db.get_vacancies_with_keyword('HH_Database', params)
            user_choice = input('Выберите следующую команду ')
        else:
            #обработка неверного значения, введенного пользователем
            print('Команда не распознана. Попробуйте еще раз или нажмите q для завершения')
            user_choice = input()

    print('Завершение программы')


if __name__ == "__main__":
    main()