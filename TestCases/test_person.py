from classes.Data import Data


class TestPerson:
    def test_person_data(self, name_to_test, age_to_test, gender_to_test, nationality_to_test):
        age = Data.get_age(name_to_test)
        gender = Data.get_gender(name_to_test)
        nationality = Data.get_national(name_to_test)
        assert age_to_test == age
        assert gender_to_test == gender
        assert nationality_to_test == nationality
