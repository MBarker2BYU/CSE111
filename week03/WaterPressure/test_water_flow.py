# Author: Matthew D. Barker
# Date: Mar 07, 2025
# Description: Milestone: Water Pressure

from pytest import approx
import pytest
import inspect

from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe
from water_flow import pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction
from water_flow import kpa_to_psi

# Begin Real World External

class Tests:
    # Flag as not to be tested    
    __test__ = False

    def __init__(self):
        
        self._tests = {}

    def append(self, test_data):
        
        if not self._tests.__contains__(test_data.method_name):
            self._tests[test_data.method_name] = []
        
        self._tests[test_data.method_name].append(test_data)

    def get_tests(self, name):
        
        return self._tests[name]

class TestData:
    # Flag as not to be tested    
    __test__ = False

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
    
tests = Tests()

# water_column_height 
tests.append(TestData('water_column_height', 0.0, 0.0, 0.0))
tests.append(TestData('water_column_height', 0.0, 10.0, 7.5))
tests.append(TestData('water_column_height', 25.0, 0.0, 25.0))
tests.append(TestData('water_column_height', 48.3, 12.8, 57.9))

# pressure_gain_from_water_height
tests.append(TestData('pressure_gain_from_water_height', 0.0, 0.000, 0.001))
tests.append(TestData('pressure_gain_from_water_height', 30.2, 295.628, 0.001))
tests.append(TestData('pressure_gain_from_water_height', 50.0, 489.450, 0.001))

# pressure_loss_from_pipe
tests.append(TestData('pressure_loss_from_pipe', 0.048692, 0.00, 0.018, 1.75, 0.000, 0.001))
tests.append(TestData('pressure_loss_from_pipe', 0.048692,	200.00,	0.000, 1.75, 0.000,	0.001))
tests.append(TestData('pressure_loss_from_pipe', 0.048692,	200.00,	0.018, 0.00, 0.000,	0.001))
tests.append(TestData('pressure_loss_from_pipe', 0.048692,	200.00,	0.018, 1.75, -113.008, 0.001))
tests.append(TestData('pressure_loss_from_pipe', 0.048692,	200.00,	0.018, 1.65, -100.462, 0.001))
tests.append(TestData('pressure_loss_from_pipe', 0.286870,	1000.00, 0.013,	1.65, -61.576, 0.001))
tests.append(TestData('pressure_loss_from_pipe', 0.286870,	1800.75, 0.013,	1.65, -110.884,	0.001))

# test_pressure_loss_from_fittings
tests.append(TestData('pressure_loss_from_fittings', 0.00,	3, 0.000, 0.001))
tests.append(TestData('pressure_loss_from_fittings', 1.65,	0, 0.000, 0.001))
tests.append(TestData('pressure_loss_from_fittings', 1.65,	2, -0.109, 0.001))
tests.append(TestData('pressure_loss_from_fittings', 1.75,	2, -0.122, 0.001))
tests.append(TestData('pressure_loss_from_fittings', 1.75,	5, -0.306, 0.001))

# test_reynolds_number
tests.append(TestData('reynolds_number', 0.048692,	0.00, 0, 1))
tests.append(TestData('reynolds_number', 0.048692,	1.65, 80069, 1))
tests.append(TestData('reynolds_number', 0.048692,	1.75, 84922, 1))
tests.append(TestData('reynolds_number', 0.286870,	1.65, 471729, 1))
tests.append(TestData('reynolds_number', 0.286870, 1.75, 500318, 1))

# test_pressure_loss_from_pipe_reduction
tests.append(TestData('pressure_loss_from_pipe_reduction', 0.28687, 0.00, 1, 0.048692, 0.000, 0.001))
tests.append(TestData('pressure_loss_from_pipe_reduction', 0.28687,	1.65, 471729, 0.048692, -163.744, 0.001))
tests.append(TestData('pressure_loss_from_pipe_reduction', 0.28687,	1.75, 500318, 0.048692, -184.182, 0.001))

# test_kpa_to_psi
tests.append(TestData('kpa_to_psi', 1, 0.145038, 0.01))
tests.append(TestData('kpa_to_psi', 5, 0.725189, 0.01))
tests.append(TestData('kpa_to_psi', 13, 1.88549, 0.01))
tests.append(TestData('kpa_to_psi', 27, 3.91602, 0.01))
tests.append(TestData('kpa_to_psi', 71, 10.2977, 0.01))
tests.append(TestData('kpa_to_psi', 1701, 246.7092, 0.01))
tests.append(TestData('kpa_to_psi', 1776, 257.587, 0.01))


# End Real world External 


def validate_float_type(name, result):

    assert isinstance(result, float), F"{name} function must return a float"

def method_name():
    return inspect.stack()[1][3].replace('test_', '')


def test_water_column_height():

    # Get the method name from the stack and remover 'test_' to get the method being tested    
    name = method_name()

    validate_float_type(name, water_column_height(0.0, 0.0))

    # Get the tests for the the give menthod
    for test_data in tests.get_tests(name):
                
        assert water_column_height(test_data.test_parameter(0), test_data.test_parameter(1)) == test_data.test_parameter(2)

def test_pressure_gain_from_water_height():

    # Get the method name from the stack and remover 'test_' to get the method being tested    
    name = method_name() 

    validate_float_type(name, pressure_gain_from_water_height(0.0))

    for test_data in tests.get_tests(name):
                
        assert pressure_gain_from_water_height(test_data.test_parameter(0)) == approx(test_data.test_parameter(1), abs=test_data.test_parameter(2))


def test_pressure_loss_from_pipe():

    # Get the method name from the stack and remover 'test_' to get the method being tested    
    name = method_name()

    validate_float_type(name, pressure_loss_from_pipe(0.0, 0.0, 0.0, 0.0))

    for test_data in tests.get_tests(name):
        # if not test_data.method_name == 'pressure_loss_from_pipe':
        #     continue
        
        assert pressure_loss_from_pipe(test_data.test_parameter(0),test_data.test_parameter(1),test_data.test_parameter(2),test_data.test_parameter(3)) == approx(test_data.test_parameter(4), abs=test_data.test_parameter(5))

def test_pressure_loss_from_fittings():
    
    # Get the method name from the stack and remover 'test_' to get the method being tested    
    name = method_name()

    validate_float_type(name, pressure_loss_from_fittings(0.0, 0.0))

    for test_data in tests.get_tests(name):
        
        assert pressure_loss_from_fittings(test_data.test_parameter(0),test_data.test_parameter(1)) == approx(test_data.test_parameter(2), abs=test_data.test_parameter(3))

def test_reynolds_number():

    # Get the method name from the stack and remover 'test_' to get the method being tested    
    name = method_name()

    validate_float_type(name, reynolds_number(0.0, 0.0))

    for test_data in tests.get_tests(name):
        
        assert reynolds_number(test_data.test_parameter(0),test_data.test_parameter(1)) == approx(test_data.test_parameter(2), abs=test_data.test_parameter(3))

def test_pressure_loss_from_pipe_reduction():

    # Get the method name from the stack and remover 'test_' to get the method being tested    
    name = method_name()

    validate_float_type(name, pressure_loss_from_pipe_reduction(0.0, 0.0, 0.0, 0.0))

    for test_data in tests.get_tests(name):

        assert pressure_loss_from_pipe_reduction(test_data.test_parameter(0), test_data.test_parameter(1), test_data.test_parameter(2), test_data.test_parameter(3)) == approx(test_data.test_parameter(4), abs=test_data.test_parameter(5))

def test_kpa_to_psi():

    # Get the method name from the stack and remover 'test_' to get the method being tested    
    name = method_name()

    validate_float_type(name, kpa_to_psi(0.0))

    for test_data in tests.get_tests(name):
        
        assert kpa_to_psi(test_data.test_parameter(0)) == approx(test_data.test_parameter(1), abs=test_data.test_parameter(2))



# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])