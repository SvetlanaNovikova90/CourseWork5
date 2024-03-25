import psycopg2

from classes.hh_class import HHParser
from utils.config import config


def create_database(db_name):
    '''
    Создание Базы Данных
    :param db_name: название БД
    :return:
    '''
    conn = psycopg2.connect(dbname="postgres", **config())
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(f"DROP DATABASE IF EXISTS {db_name}")
    cur.execute(f"CREATE DATABASE {db_name}")

    cur.close()
    conn.close()


def create_table(db_name):
    '''
    Создание таблиц Компании и Вакансии
    :param db_name: Название БД
    :return:
    '''
    conn = psycopg2.connect(dbname=db_name, **config())
    with conn:
        with conn.cursor() as cur:
            cur.execute('CREATE TABLE employers'
                        '('
                        'id int PRIMARY KEY,'
                        'name varchar(255) UNIQUE NOT NULL)')
            cur.execute('CREATE TABLE vacancies'
                        '('
                        'id int PRIMARY KEY,'
                        'name varchar(255) NOT NULL,'
                        'salary_from int,'
                        'salary_to int,'
                        'url varchar(255),'
                        'area varchar (255),'
                        'employer int REFERENCES employers(id) NOT NULL)')
    conn.close()


def insert_data_into_tables(db_name):
    '''
    Заполнение таблиц данными
    :param db_name: название БД
    :return:
    '''
    hh = HHParser()
    employers = hh.get_employers()
    vacancies = hh.filter_vacancies()
    conn = psycopg2.connect(dbname=db_name, **config())
    with conn:
        with conn.cursor() as cur:
            for employer in employers:
                cur.execute("""
                                INSERT INTO employers VALUES (%s, %s)
                            """, (employer["id"], employer["name"]))
            for vacancy in vacancies:
                cur.execute("""INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s, %s, %s)
                                    """, (vacancy["id"], vacancy["name"],
                                          vacancy["salary_from"], vacancy["salary_to"],
                                          vacancy["url"], vacancy["area"], vacancy["employer"]))
    conn.close()


def working_with_databases():
    create_database("course5")
    create_table("course5")
    insert_data_into_tables("course5")
