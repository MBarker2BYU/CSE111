# Author: Matthew D. Barker
# Date: Mar 06, 2025
# Description: Milestone: Water Pressure

from pytest import approx
import pytest

from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe

class TestData:
    def __init__ (self, method_name, *parameters):
        
        self._method_name = method_name
        self._parameters = parameters

    @property
    def method_name(self):
        return self._method_name

    def test_parameter(self, index):

        try:
            value = self._parameters[index] 
        except Exception as e:
            a = e.args

        return value
    
tests = []

water_column_height 
tests.append(TestData('water_column_height', 0.0, 0.0, 0.0))
tests.append(TestData('water_column_height', 0.0, 10.0, 7.5))
tests.append(TestData('water_column_height', 25.0, 0.0, 25.0))
tests.append(TestData('water_column_height', 48.3, 12.8, 57.9))

pressure_gain_from_water_height
tests.append(TestData('pressure_gain_from_water_height', 0.0, 0.000, 0.001))
tests.append(TestData('pressure_gain_from_water_height', 30.2, 295.628, 0.001))
tests.append(TestData('pressure_gain_from_water_height', 50.0, 489.450, 0.001))

pressure_loss_from_pipe
tests.append(TestData('pressure_loss_from_pipe', 0.048692, 0.00, 0.018, 1.75, 0.000, 0.001))
tests.append(TestData('pressure_loss_from_pipe', 0.048692,	200.00,	0.000, 1.75, 0.000,	0.001))
tests.append(TestData('pressure_loss_from_pipe', 0.048692,	200.00,	0.018, 0.00, 0.000,	0.001))
tests.append(TestData('pressure_loss_from_pipe', 0.048692,	200.00,	0.018, 1.75, -113.008, 0.001))
tests.append(TestData('pressure_loss_from_pipe', 0.048692,	200.00,	0.018, 1.65, -100.462, 0.001))
tests.append(TestData('pressure_loss_from_pipe', 0.286870,	1000.00, 0.013,	1.65, -61.576, 0.001))
tests.append(TestData('pressure_loss_from_pipe', 0.286870,	1800.75, 0.013,	1.65, -110.884,	0.001))

def test_water_column_height():
    
    result = water_column_height(0.0, 0.0)
    assert isinstance(result, float), F"{water_column_height} function must return a float"

    for test_data in tests:
        if not test_data.method_name == 'water_column_height':
            continue
        
        assert water_column_height(test_data.test_parameter(0), test_data.test_parameter(1)) == test_data.test_parameter(2)

def test_pressure_gain_from_water_height():
    
    result = pressure_gain_from_water_height(0.0)
    assert isinstance(result, float), F"{test_pressure_gain_from_water_height} function must return a float"

    for test_data in tests:
        if not test_data.method_name == 'pressure_gain_from_water_height':
            continue
        
        assert pressure_gain_from_water_height(test_data.test_parameter(0)) == approx(test_data.test_parameter(1), abs=test_data.test_parameter(2))


def test_pressure_loss_from_pipe():
    
    result = pressure_loss_from_pipe(0.0, 0.0, 0.0, 0.0)
    assert isinstance(result, float), F"{test_pressure_gain_from_water_height} function must return a float"

    for test_data in tests:
        if not test_data.method_name == 'pressure_loss_from_pipe':
            continue
        
        assert pressure_loss_from_pipe(test_data.test_parameter(0),test_data.test_parameter(1),test_data.test_parameter(2),test_data.test_parameter(3)) == approx(test_data.test_parameter(4), test_data.test_parameter(5))

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])