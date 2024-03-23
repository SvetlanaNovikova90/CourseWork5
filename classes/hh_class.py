import requests


class HHParser:

    def get_request(self):
        '''
        10 интресующих компаний
        '''
        emploters = ['Тензор', 'AMS Software', 'Ярнет', 'Электроника ПСЦ', 'СИНТО', 'КРИСТА', 'Тинькофф', 'Mediascope', 'Aston', 'Арго студио']
        emploters_now = []
        for i in emploters:
            params = {
                'per_page': 1,
                'sort_by': "by_vacancies_open",
                'text': i
            }
            response = requests.get('https://api.hh.ru/employers', params)
            if response.status_code == 200:
                emploters_now.extend(response.json()['items'])
        return emploters_now

    def get_employers(self):
        '''
        Список компаний. Ключи: id и name
        :return:
        '''
        data = self.get_request()
        employers = []
        for employer in data:
            employers.append({"id": employer["id"], "name": employer["name"]})
        return employers

    def get_vacancies_from_company(self, id):
        '''
        Получение вакансий по id выбранных компаний
        :param id: id компании
        :return:
        '''
        params = {
            'per_page': 20,
            'employer_id': id
        }
        response = requests.get('https://api.hh.ru/vacancies/', params)
        if response.status_code == 200:
            return response.json()['items']

    def get_all_vacancies(self):
        '''

        :return:
        '''
        employers = self.get_employers()
        vacancies = []
        for employer in employers:
            vacancies.extend(self.get_vacancies_from_company(employer["id"]))
        return vacancies

    def filter_vacancies(self):
        vacancies = self.get_all_vacancies()
        filter_data = []
        for vacancy in vacancies:
            if not vacancy["salary"]:
                salary_from = 0
                salary_to = 0
            else:
                salary_from = vacancy["salary"]["from"] if vacancy["salary"]["from"] else 0
                salary_to = vacancy["salary"]["to"] if vacancy["salary"]["to"] else 0
            filter_data.append({
                "id": vacancy["id"],
                "name": vacancy["name"],
                "salary_from": salary_from,
                "salary_to": salary_to,
                "url": vacancy["alternate_url"],
                "area": vacancy["area"]["name"],
                "employer": vacancy["employer"]["id"]
            })
        return filter_data


vv = HHParser()
for i in vv.filter_vacancies():
    print()
