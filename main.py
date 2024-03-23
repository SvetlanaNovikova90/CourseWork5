from classes.DBManager import DBManager
from utils.utils import create_database, create_table, insert_data_into_tables


# employer = ['67611', '52510', '3177', '3529',
#                 '154', '26877', '1949248', '27611',
#                 '920774', '634253']
def user_interaction():
    print(" Привет!\n"
          " Выберите команду:\n"
          " 1 - Список всех компаний и количесво их вакансий\n 2 - Список всех вакансий с информацией по каждой\n 3 - "
          "Узнать среднюю зарплату \n 4 - Списсок вакансий, у которых зарплата выше средней\n 5 - Поискать по ключевому "
          "слову\n")
    all = DBManager("course_work5")

    while True:
        user_input = input()
        if user_input in ["1", "2", "3", "4", "5"]:
            break
        else:
            print("Попробуйте еще раз")

    if user_input == "1":
        all_companies = all.get_companies_and_vacancies_count()
        for i in all_companies:
            print(i)
    elif user_input == "2":
        all_vacancies = all.get_all_vacancies()
        for i in all_vacancies:
            print(i)

    elif user_input == "3":
        avg_salary = all.get_avg_salary()
        for i in avg_salary:
            print(i)

    elif user_input == "4":
        high_salary = all.get_vacancies_with_higher_salary()
        for i in high_salary:
            print(i)
    elif user_input == "5":
        keyword_input = input("Введите ключевое слово ")
        vacancy_with_keyword = all.get_vacancies_with_keyword(keyword_input)
        if len(vacancy_with_keyword) <= 0:
            print('Ключевое слово не найдено')
        else:
            for i in vacancy_with_keyword:
                print(i)


if __name__ == '__main__':
    # create_database("course_work5")
    # create_table("course_work5")
    # insert_data_into_tables("course_work5")
    while True:
        user_interaction()
        user_choice = input("Продолжить? (да/нет): ")
        if user_choice.lower() != "да":
            break