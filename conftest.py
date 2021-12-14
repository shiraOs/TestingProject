from classes.Data import Data


def pytest_generate_tests(metafunc):
    Data.create_data()
    persons_data = Data.persons
    persons = [(data.name, data.age, data.gender, data.nationality) for data in persons_data]
    arguments_names = "name_to_test, age_to_test, gender_to_test, nationality_to_test"
    metafunc.parametrize(arguments_names, persons)
