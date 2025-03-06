"""Verify that the prefix and suffix functions work correctly."""

from words import prefix, suffix
import pytest


def test_prefix():
    """Verify that the prefix function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the prefix function and verify that it returns a string.
    pre = prefix("upbeat", "upgrade")
    assert isinstance(pre, str), "prefix function must return a string"

    # Call the prefix function ten times and use an assert
    # statement to verify that the string returned by the
    # prefix function is correct each time.
    assert prefix("cat", "catalog") == "cat"
    assert prefix("", "") == ""
    assert prefix("", "correct") == ""
    assert prefix("clear", "") == ""
    assert prefix("happy", "funny") == ""
    assert prefix("cat", "catalog") == "cat"
    assert prefix("dogmatic", "dog") == "dog"
    assert prefix("jump", "joyous") == "j"
    assert prefix("upbeat", "upgrade") == "up"
    assert prefix("Disable", "dIstasteful") == "dis"


class Test():
    
    def __init__(self, parameter1, parameter2, expected_result):
        
        self._parameter1 = parameter1
        self._parameter2 = parameter2
        self._expected_result = expected_result


    @property
    def parameter1(self):
        return self._parameter1
    
    @property
    def parameter2(self):
        return self._parameter2
    
    @property
    def expected_result(self):
        return self._expected_result



#this can be read in via file.
tests = []
tests.append(Test("", "", ""))
tests.append(Test("", "correct", ""))
tests.append(Test("clear", "", ""))
tests.append(Test("angelic", "awesome", ""))
tests.append(Test("found", "profound", "found"))
tests.append(Test("ditch", "itch", "itch"))
tests.append(Test("happy", "funny", "y"))
tests.append(Test("tired", "fatigued", "ed"))
tests.append(Test("swimming", "FLYING", "ing"))


def test_Suffix():

    suf = suffix("upbeat", "upgrade")
    assert isinstance(suf, str), "suffix function must return a string"

    for test in tests:
        assert suffix(test.parameter1, test.parameter2) == test.expected_result
    


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
