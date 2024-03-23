from classes.DBManager import DBManager


def user_interaction():
    print('''Привет!
Выберите команду:
1 - Список всех компаний и количество их вакансий
2 - Список всех вакансий с информацией по каждой
3 - Узнать среднюю зарплату
4 - Список вакансий, у которых зарплата выше средней
5 - Поискать по ключевому слову''')
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
    while True:
        user_interaction()
        user_choice = input("Продолжить? (да/нет): ")
        if user_choice.lower() != "да":
            break
