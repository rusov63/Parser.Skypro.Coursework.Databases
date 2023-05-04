import psycopg2
from queries import SQL_1, SQL_2, SQL_3, SQL_4, SQL_5
from config import config

#параметры подключения к БД
params = config()

class DBManager:
    '''Подключается к БД Postgres'''

    def __init__(self):
        pass

    def __repr__(self):
        pass

    def get_companies_and_vacancies_count(self, database_name: str, params: dict):
        '''получает список всех компаний'''
        conn = psycopg2.connect(dbname=database_name, **params)

        with conn.cursor() as cur:
            cur.execute(SQL_1)
            rows = cur.fetchall()
            for row in rows:
                print(row)

        conn.commit()
        conn.close()


    def get_all_vacancies(self, database_name: str, params: dict):
        '''получает список всех вакансий с указанием названия компании,
        зарплаты и ссылки на вакансию'''
        conn = psycopg2.connect(dbname=database_name, **params)

        with conn.cursor() as cur:
            cur.execute(SQL_2)
            rows = cur.fetchall()
            for row in rows:
                print(row)

        conn.commit()
        conn.close()

    def get_avg_salary(self, database_name: str, params: dict):
        '''получает среднюю зарплату по вакансиям.'''
        conn = psycopg2.connect(dbname=database_name, **params)

        with conn.cursor() as cur:
            cur.execute(SQL_3)
            rows = cur.fetchall()
            for row in rows:
                print(row)

        conn.commit()
        conn.close()


    def get_vacancies_with_higher_salary(self, database_name: str, params: dict):
        '''получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.'''
        conn = psycopg2.connect(dbname=database_name, **params)

        with conn.cursor() as cur:
            cur.execute(SQL_4)
            rows = cur.fetchall()
            for row in rows:
                print(row)

        conn.commit()
        conn.close()


    def get_vacancies_with_keyword(self, database_name: str, params: dict):
        '''получает список всех вакансий, в названии которых содержатся переданные в метод слова'''
        keyword = input("Слово для поиска - ")
        conn = psycopg2.connect(dbname=database_name, **params)
        with conn.cursor() as cur:
            cur.execute(SQL_5)
            rows = cur.fetchall()
            for row in rows:
                print(row)

        conn.commit()
        conn.close()