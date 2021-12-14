import names
import requests
from classes.Person import Person


class Data:
    number_of_names = 5
    agify_url = "https://api.agify.io/?name="
    genderize_url = "https://api.genderize.io/?name="
    nationalize_url = "https://api.nationalize.io/?name="
    random_names = []
    persons = []

    @staticmethod
    def create_data():
        Data.set_random_names()
        for name in Data.random_names:
            age = Data.get_age(name)
            gender = Data.get_gender(name)
            nationality = Data.get_national(name)
            person = Person(name, age, gender, nationality)
            Data.persons.append(person)

    @staticmethod
    def set_random_names():
        while len(Data.random_names) < Data.number_of_names:
            Data.random_names.append(names.get_first_name())

    @staticmethod
    def get_age(name_to_search):
        url = Data.agify_url + name_to_search
        respond = requests.get(url)
        age = -1
        if respond.status_code == 200:
            data = respond.json()
            age = data["age"]
        return age

    @staticmethod
    def get_gender(name_to_search):
        url = Data.genderize_url + name_to_search
        respond = requests.get(url)
        gender = -1
        if respond.status_code == 200:
            data = respond.json()
            gender = data["gender"]
        return gender

    @staticmethod
    def get_national(name_to_search):
        url = Data.nationalize_url + name_to_search
        respond = requests.get(url)
        national_id = -1
        if respond.status_code == 200:
            data = respond.json()
            countries = data["country"]
            national_id = Data.get_max_probability_nationality(countries)
        return national_id

    @staticmethod
    def get_max_probability_nationality(countries):
        max_prob = 0
        national_id = -1
        for country in countries:
            prob = country["probability"]
            if prob > max_prob:
                max_prob = prob
                national_id = country["country_id"]
        return national_id
