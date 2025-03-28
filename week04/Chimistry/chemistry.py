from formula import parse_formula
from os import system, name
from enum import Enum
import os
import csv

class Utilities:
    def clear_screen():
        system("cls" if name == "nt" else "clear")

    def yes_no_prompt(prompt):
        print(prompt)
        return input().strip().lower() == 'y'
    
    def get_current_directory():
        return os.path.dirname(os.path.realpath(__file__))

class PeriodicTableItem(Enum):
    AtomicNumber=0
    Name=1
    Symbol=2
    AtomicMass=3
    NumberofNeutrons=4
    NumberofProtons=5
    NumberofElectrons=6

class Element:
    def __init__(self, symbol, name, atomic_mass, atomic_number=0, number_of_electrons=0, number_of_neutrons=0, number_of_protons=0):
                
        self._name = name
        self._symbol = symbol
        self._atomic_mass = atomic_mass

        self._atomic_number = atomic_number
        self._number_of_electrons = number_of_electrons
        self._number_of_neutrons = number_of_neutrons
        self._number_of_protons = number_of_protons

    @property
    def atomic_number(self):
        return self._atomic_number
    
    @property
    def name(self):
        return self._name
    
    @property
    def symbol(self):
        return self._symbol
    
    @property
    def atomic_mass(self):
        return self._atomic_mass
    
    @property
    def number_of_electrons(self):
        return self._number_of_electrons    

    @property
    def number_of_neutrons(self):
        return self._number_of_neutrons

    @property
    def number_of_protons(self):
        return self._number_of_protons
    
    def update(self, atomic_number=0, number_of_electrons=0, number_of_neutrons=0, number_of_protons=0 ):
        
        self._atomic_number = atomic_number
        self._number_of_electrons = number_of_electrons
        self._number_of_neutrons = number_of_neutrons
        self._number_of_protons = number_of_protons

    def to_list_item(self):
        return [self._symbol, self._name, self._atomic_mass]
    
    def to_list_item_extended(self):
        return [self._name, self._atomic_mass, self._symbol, self._atomic_number, self._number_of_electrons, self._number_of_neutrons, self._number_of_protons]


class PeriodicTable:
    def __init__(self, element_file="ElementInfo.csv", extended_element_file="ExtendedElementInfo.csv"):
        self._Initialize(element_file, extended_element_file)

    def _Initialize(self, element_file, extended_element_file):
        
        self._elements = {}

        element_info_path = F"{Utilities.get_current_directory()}\\{element_file}"

        with open(element_info_path, 'r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            element_data = list(csv_reader)

            for element in element_data:

                symbol = element[0].strip()
                name = element[1].strip()
                atomic_mass = float(element[2].strip())

                self.add_element(Element(symbol, name, atomic_mass))


        extended_element_info = F"{Utilities.get_current_directory()}\\{extended_element_file}"

        with open(extended_element_info, 'r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            extended_element_data = list(csv_reader)

            for element in extended_element_data:
                
                symbol = element[PeriodicTableItem.Symbol.value].strip()

                if not self.has_key(symbol):
                    continue

                atomic_number = int(element[PeriodicTableItem.AtomicNumber.value].strip())
                electrons = int(element[PeriodicTableItem.NumberofElectrons.value].strip())
                neutrons = int(element[PeriodicTableItem.NumberofNeutrons.value].strip())
                protons = int(element[PeriodicTableItem.NumberofProtons.value].strip())

                self.get_element(symbol).update(atomic_number, electrons, neutrons, protons)


    def add_element(self, element):
        
        if element.symbol not in self._elements:
            self._elements[element.symbol] = element

    def has_key(self, symbol):
        return symbol in self._elements

    def get_element(self, symbol):
        return self._elements[symbol]

    def to_list(self):
        
        elements = []
        
        for element in self._elements.values():
            elements.append(element.to_list_item())

        return elements

    def to_dictionary(self):

        elements = {}

        for element in self._elements.values():
            elements[element.symbol] = element.to_list_item_extended()

        return elements
    
    def to_advanced_dictionary(self):
        return self._elements

def make_periodic_table():
    
    global periodic_table

    if periodic_table is None:
        periodic_table = PeriodicTable()

    # return periodic_table.to_list()
    return periodic_table.to_dictionary()
    
    
def molecules_library():
    return {
        "Al2O3": "aluminum oxide",
        "CH3OH": "methanol",
        "C2H6O": "ethanol",
        "C2H5OH": "ethanol",
        "C3H8O": "isopropyl alcohol",
        "C3H8": "propane",
        "C4H10": "butane",
        "C6H6": "benzene",
        "C6H14": "hexane",
        "C8H18": "octane",
        "CH3(CH2)6CH3": "octane",
        "C13H18O2": "ibuprofen",
        "C13H16N2O2": "melatonin",
        "Fe2O3": "iron oxide",
        "FeS2": "iron pyrite",
        "H2O": "water"}


NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

SYMBOL_INDEX = 0
QUANTITY_INDEX = 1

def compute_molar_mass(symbol_quantity_list, periodic_table):
    
    total_molar_mass = 0

    for element in symbol_quantity_list:
        symbol = element[SYMBOL_INDEX]
        quantity = element[QUANTITY_INDEX]

        e = periodic_table[symbol]
        atomic_mass = e[ATOMIC_MASS_INDEX]

        total_molar_mass += atomic_mass * quantity   

    return total_molar_mass

# Advanced

def get_formula_name(formula, known_molecules_dict):
    if formula in known_molecules_dict:
        return known_molecules_dict[formula]
    else:
        return "unknown compound"

ATOMIC_NUMBER = 3
ELECTRONS = 4
NEUTRONS = 5
PROTONS = 6

def sum_electrons(symbol_quantity_list, periodic_table_dict):

    electron_sum = 0

    for element in symbol_quantity_list:
        chemical_symbol = element[NAME_INDEX]
        electron_count = periodic_table_dict[chemical_symbol].number_of_electrons * element[QUANTITY_INDEX]
    
        electron_sum += electron_count

    return electron_sum

def sum_neutrons(symbol_quantity_list, periodic_table_dict):
    
    neutron_sum = 0

    for element in symbol_quantity_list:
        chemical_symbol = element[NAME_INDEX]
        neutron_count = periodic_table_dict[chemical_symbol].number_of_neutrons * element[QUANTITY_INDEX]
    
        neutron_sum += neutron_count

    return neutron_sum

def sum_protons(symbol_quantity_list, periodic_table_dict):

    proton_sum = 0

    for element in symbol_quantity_list:
        chemical_symbol = element[NAME_INDEX]
        
        proton_count = periodic_table_dict[chemical_symbol].number_of_protons * element[QUANTITY_INDEX]
    
        proton_sum += proton_count

    return proton_sum

periodic_table = None

def main():

    global periodic_table

    if periodic_table is None:
        periodic_table = PeriodicTable()
      
    Utilities.clear_screen()

    while(True):

        Utilities.clear_screen()

        print("Enter formula:")
        response = input().upper()

        print("Enter the mass:")
        mass = float(input().upper())

        symbol_quantity_list = parse_formula(response.upper(), periodic_table.to_dictionary())

        data = compute_molar_mass(symbol_quantity_list, periodic_table.to_dictionary())    
        moles =  mass / data

        formula_name = get_formula_name(response, molecules_library())

        electron_count = sum_electrons(symbol_quantity_list, periodic_table.to_advanced_dictionary())
        neutron_count = sum_neutrons(symbol_quantity_list, periodic_table.to_advanced_dictionary())
        proton_count = sum_protons(symbol_quantity_list, periodic_table.to_advanced_dictionary())

        Utilities.clear_screen()

        print(F"Formula Name: {formula_name.title()}")
        print()
        print(F"{F"Formula:".ljust(25,'.')}{F"{response}".rjust(25,'.')}")
        print(F"{F"Mass:".ljust(25,'.')}{F"{mass} grams".rjust(25,'.')}")
        print(F"{F"grams/mole:".ljust(25,'.')}{F"{data:,.5f}".rjust(25,'.')}")
        print(F"{F"moles:".ljust(25,'.')}{F"{moles:,.5f}".rjust(25,'.')}")
        print(F"{F"Electrons:".ljust(25,'.')}{F"{electron_count}".rjust(25,'.')}")
        print(F"{F"Neutrons:".ljust(25,'.')}{F"{neutron_count}".rjust(25,'.')}")
        print(F"{F"Protons:".ljust(25,'.')}{F"{proton_count}".rjust(25,'.')}")
        print()
        
        if input("Enter another formula?").lower() != 'y':
            break
    
    print()
    print()
    print("Have a blessed day!")
    print()
    print()



if __name__ == "__main__":
    main()