from address import extract_city, extract_state, extract_zipcode
import pytest

class Address:
    def __init__(self, street, city, state, zip_code):
        
        self._street = street
        self._city = city
        self._state = state
        self._zip_code = zip_code

    @property
    def street(self):
        return self._street

    @property
    def city(self):
        return self._city
    
    @property
    def state(self):
        return self._state
    
    @property
    def zip_code(self):
        return self._zip_code

    @property
    def full_address(self):
        return F"{self._street}, {self._city}, {self._state} {self._zip_code}"

test_data = []

test_data.append(Address("29051 Fruitvale LN", "Valley Center", "CA", "92082"))
test_data.append(Address("9040 Twin Trails CT", "San Diego", "CA", "92129"))
test_data.append(Address("2973 Krista Key Cir", "Orlando", "FL", "32817"))
test_data.append(Address("816 NW 3rd Ave", "Cape Coral", "FL", "33993"))

def test_extract_city():
    for address in test_data:
        assert extract_city(address.full_address) == address.city

def test_extract_state():
    for address in test_data:
        assert extract_state(address.full_address) == address.state

def test_extract_zip_code():
    for address in test_data:
        assert extract_zipcode(address.full_address) == address.zip_code


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])