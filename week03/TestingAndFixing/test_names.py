from names import make_full_name, extract_family_name, extract_given_name
import pytest

class Name:
    def __init__(self, given_name, family_name):
        
        self._given_name = given_name
        self._family_name = family_name
    
    @property
    def given_name(self):
        return self._given_name
    
    @property
    def family_name(self):
        return self._family_name

    @property
    def full_name(self):
        return F"{self._given_name} {self._family_name}"

    @property
    def last_name_first(self):
        return F"{self._family_name}; {self._given_name}"

test_data = []

test_data.append(Name("Wendy", "Cook"))
test_data.append(Name("Matthew", "Barker"))
test_data.append(Name("John", "Barker"))
test_data.append(Name("Sarah", "Barker"))

def test_make_full_name():
    for name in test_data:
        assert make_full_name(name.given_name, name.family_name) == name.last_name_first

def test_extract_family_name():
    for name in test_data:
        assert extract_family_name(name.last_name_first) == name.family_name

def test_extract_given_name():
    for name in test_data:
        assert extract_given_name(name.last_name_first) == name.given_name

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])