SQL_1 = '''SELECT DISTINCT employer_name, COUNT(*) AS count_vacancies
    FROM employers
    GROUP BY employer_name
    ORDER BY count_vacancies DESC'''


SQL_2 = '''SELECT employer_name, vacancy_name, salary_from, salary_to, currency, url
    FROM employers
    ORDER BY employer_name'''

SQL_3 = '''SELECT ROUND(AVG(salary_to + salary_from / 2)) AS avg_salary
    FROM employers
    WHERE salary_from IS NOT NULL AND salary_to IS NOT NULL'''

SQL_4 = '''SELECT vacancy_name
    FROM employers
    WHERE (salary_to + salary_from) / 2 > (SELECT AVG(salary_to + salary_from / 2) FROM employers WHERE salary_from IS NOT NULL AND salary_to IS NOT NULL)'''


SQL_5 = '''SELECT vacancy_name, url
    FROM employers
    WHERE vacancy_name ILIKE '%{keyword}%
    '''