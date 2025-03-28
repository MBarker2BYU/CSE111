from formula import parse_formula
from os import system, name
from enum import Enum
import os
# import csv

def element_info():
        
    elements = []

    elements.append(['Ac','Actinium',227.0, 89, 89, 138, 89])
    elements.append(['Ag','Silver',107.8682, 47, 47, 61, 47])
    elements.append(['Al','Aluminum',26.9815386, 13, 13, 14, 13])
    elements.append(['Ar','Argon',39.948, 18, 18, 22, 18])
    elements.append(['As','Arsenic',74.9216, 33, 33, 42, 33])
    elements.append(['At','Astatine',210.0, 85, 85, 125, 85])
    elements.append(['Au','Gold',196.966569, 79, 79, 118, 79])
    elements.append(['B','Boron',10.811, 5, 5, 6, 5])
    elements.append(['Ba','Barium',137.327, 56, 56, 81, 56])
    elements.append(['Be','Beryllium',9.012182, 4, 4, 5, 4])
    elements.append(['Bi','Bismuth',208.9804, 83, 83, 126, 83])
    elements.append(['Br','Bromine',79.904, 35, 35, 45, 35])
    elements.append(['C','Carbon',12.0107, 6, 6, 6, 6])
    elements.append(['Ca','Calcium',40.078, 20, 20, 20, 20])
    elements.append(['Cd','Cadmium',112.411, 48, 48, 64, 48])
    elements.append(['Ce','Cerium',140.116, 58, 58, 82, 58])
    elements.append(['Cl','Chlorine',35.453, 17, 17, 18, 17])
    elements.append(['Co','Cobalt',58.933195, 27, 27, 32, 27])
    elements.append(['Cr','Chromium',51.9961, 24, 24, 28, 24])
    elements.append(['Cs','Cesium',132.9054519, 55, 55, 78, 55])
    elements.append(['Cu','Copper',63.546, 29, 29, 35, 29])
    elements.append(['Dy','Dysprosium',162.5, 66, 66, 97, 66])
    elements.append(['Er','Erbium',167.259, 68, 68, 99, 68])
    elements.append(['Eu','Europium',151.964, 63, 63, 89, 63])
    elements.append(['F','Fluorine',18.9984032, 9, 9, 10, 9])
    elements.append(['Fe','Iron',55.845, 26, 26, 30, 26])
    elements.append(['Fr','Francium',223.0, 87, 87, 136, 87])
    elements.append(['Ga','Gallium',69.723, 31, 31, 39, 31])
    elements.append(['Gd','Gadolinium',157.25, 64, 64, 93, 64])
    elements.append(['Ge','Germanium',72.64, 32, 32, 41, 32])
    elements.append(['H','Hydrogen',1.00794, 1, 1, 0, 1])
    elements.append(['He','Helium',4.002602, 2, 2, 2, 2])
    elements.append(['Hf','Hafnium',178.49, 72, 72, 106, 72])
    elements.append(['Hg','Mercury',200.59, 80, 80, 121, 80])
    elements.append(['Ho','Holmium',164.93032, 67, 67, 98, 67])
    elements.append(['I','Iodine',126.90447, 53, 53, 74, 53])
    elements.append(['In','Indium',114.818, 49, 49, 66, 49])
    elements.append(['Ir','Iridium',192.217, 77, 77, 115, 77])
    elements.append(['K','Potassium',39.0983, 19, 19, 20, 19])
    elements.append(['Kr','Krypton',83.798, 36, 36, 48, 36])
    elements.append(['La','Lanthanum',138.90547, 57, 57, 82, 57])
    elements.append(['Li','Lithium',6.941, 3, 3, 4, 3])
    elements.append(['Lu','Lutetium',174.9668, 71, 71, 104, 71])
    elements.append(['Mg','Magnesium',24.305, 12, 12, 12, 12])
    elements.append(['Mn','Manganese',54.938045, 25, 25, 30, 25])
    elements.append(['Mo','Molybdenum',95.96, 42, 42, 54, 42])
    elements.append(['N','Nitrogen',14.0067, 7, 7, 7, 7])
    elements.append(['Na','Sodium',22.98976928, 11, 11, 12, 11])
    elements.append(['Nb','Niobium',92.90638, 41, 41, 52, 41])
    elements.append(['Nd','Neodymium',144.242, 60, 60, 84, 60])
    elements.append(['Ne','Neon',20.1797, 10, 10, 10, 10])
    elements.append(['Ni','Nickel',58.6934, 28, 28, 31, 28])
    elements.append(['Np','Neptunium',237.0, 93, 93, 144, 93])
    elements.append(['O','Oxygen',15.9994, 8, 8, 8, 8])
    elements.append(['Os','Osmium',190.23, 76, 76, 114, 76])
    elements.append(['P','Phosphorus',30.973762, 15, 15, 16, 15])
    elements.append(['Pa','Protactinium',231.03588, 91, 91, 140, 91])
    elements.append(['Pb','Lead',207.2, 82, 82, 125, 82])
    elements.append(['Pd','Palladium',106.42, 46, 46, 60, 46])
    elements.append(['Pm','Promethium',145.0, 61, 61, 84, 61])
    elements.append(['Po','Polonium',209.0, 84, 84, 126, 84])
    elements.append(['Pr','Praseodymium',140.90765, 59, 59, 82, 59])
    elements.append(['Pt','Platinum',195.084, 78, 78, 117, 78])
    elements.append(['Pu','Plutonium',244.0, 94, 94, 150, 94])
    elements.append(['Ra','Radium',226.0, 88, 88, 138, 88])
    elements.append(['Rb','Rubidium',85.4678, 37, 37, 48, 37])
    elements.append(['Re','Rhenium',186.207, 75, 75, 111, 75])
    elements.append(['Rh','Rhodium',102.9055, 45, 45, 58, 45])
    elements.append(['Rn','Radon',222.0, 86, 86, 136, 86])
    elements.append(['Ru','Ruthenium',101.07, 44, 44, 57, 44])
    elements.append(['S','Sulfur',32.065, 16, 16, 16, 16])
    elements.append(['Sb','Antimony',121.76, 51, 51, 71, 51])
    elements.append(['Sc','Scandium',44.955912, 21, 21, 24, 21])
    elements.append(['Se','Selenium',78.96, 34, 34, 45, 34])
    elements.append(['Si','Silicon',28.0855, 14, 14, 14, 14])
    elements.append(['Sm','Samarium',150.36, 62, 62, 88, 62])
    elements.append(['Sn','Tin',118.71, 50, 50, 69, 50])
    elements.append(['Sr','Strontium',87.62, 38, 38, 50, 38])
    elements.append(['Ta','Tantalum',180.94788, 73, 73, 108, 73])
    elements.append(['Tb','Terbium',158.92535, 65, 65, 94, 65])
    elements.append(['Tc','Technetium',98.0, 43, 43, 55, 43])
    elements.append(['Te','Tellurium',127.6, 52, 52, 76, 52])
    elements.append(['Th','Thorium',232.03806, 90, 90, 142, 90])
    elements.append(['Ti','Titanium',47.867, 22, 22, 26, 22])
    elements.append(['Tl','Thallium',204.3833, 81, 81, 123, 81])
    elements.append(['Tm','Thulium',168.93421, 69, 69, 100, 69])
    elements.append(['U','Uranium',238.02891, 92, 92, 146, 92])
    elements.append(['V','Vanadium',50.9415, 23, 23, 28, 23])
    elements.append(['W','Tungsten',183.84, 74, 74, 110, 74])
    elements.append(['Xe','Xenon',131.293, 54, 54, 77, 54])
    elements.append(['Y','Yttrium',88.90585, 39, 39, 50, 39])
    elements.append(['Yb','Ytterbium',173.054, 70, 70, 103, 70])
    elements.append(['Zn','Zinc',65.38, 30, 30, 35, 30])
    elements.append(['Zr','Zirconium',91.224, 40, 40, 51, 40])
                    
    return elements

class Utilities:
    
    def clear_screen():
        system("cls" if name == "nt" else "clear")

    def yes_no_prompt(prompt):
        print(prompt)
        return input().strip().lower() == 'y'
    
    def get_current_directory():
        return os.path.dirname(os.path.realpath(__file__))

    def translate_to_subscript(text):
        SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        return text.translate(SUB)    
    
    def translate_to_superscript(text):
        SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
        return text.translate(SUP)

class PeriodicTableItem(Enum):
    Symbol=0
    Name=1
    AtomicMass=2
    AtomicNumber=3
    NumberofElectrons=4
    NumberofNeutrons=5
    NumberofProtons=6

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
    def __init__(self):
        self._Initialize()

    def _Initialize(self):
        
        self._elements = {}

        els = element_info()

        for e in els:
            self.add_element(Element(e[PeriodicTableItem.Symbol.value],
                                     e[PeriodicTableItem.Name.value],
                                     e[PeriodicTableItem.AtomicMass.value],
                                     e[PeriodicTableItem.AtomicNumber.value],
                                     e[PeriodicTableItem.NumberofElectrons.value],
                                     e[PeriodicTableItem.NumberofNeutrons.value],
                                     e[PeriodicTableItem.NumberofProtons.value]
                                     ))

        
        # element_info_path = F"{Utilities.get_current_directory()}\\{element_file}"

        # with open(element_info_path, 'r') as file:
        #     csv_reader = csv.reader(file)
        #     header = next(csv_reader)
        #     element_data = list(csv_reader)

        #     for element in element_data:

        #         symbol = element[0].strip()
        #         name = element[1].strip()
        #         atomic_mass = float(element[2].strip())

        #         self.add_element(Element(symbol, name, atomic_mass))
            

        # extended_element_info = F"{Utilities.get_current_directory()}\\{extended_element_file}"

        # with open(extended_element_info, 'r') as file:
        #     csv_reader = csv.reader(file)
        #     header = next(csv_reader)
        #     extended_element_data = list(csv_reader)            

        #     for element in extended_element_data:
                
        #         symbol = element[PeriodicTableItem.Symbol.value].strip()

        #         if not self.has_key(symbol):
        #             continue

        #         atomic_number = int(element[PeriodicTableItem.AtomicNumber.value].strip())
        #         electrons = int(element[PeriodicTableItem.NumberofElectrons.value].strip())
        #         neutrons = int(element[PeriodicTableItem.NumberofNeutrons.value].strip())
        #         protons = int(element[PeriodicTableItem.NumberofProtons.value].strip())

        #         self.get_element(symbol).update(atomic_number, electrons, neutrons, protons)
        

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

# ATOMIC_NUMBER = 3
# ELECTRONS = 4
# NEUTRONS = 5
# PROTONS = 6

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

        print("Molecule Data:")
        print(F"{F"  Formula: ".ljust(25,'.')}{F"{Utilities.translate_to_subscript(response)}".rjust(25,'.')}")
        print(F"{F"  Name: ".ljust(25,'.')}{F"{formula_name.title()}".rjust(25,'.')}")
        print(F"{F"  Electrons: ".ljust(25,'.')}{F"{electron_count}".rjust(25,'.')}")
        print(F"{F"  Neutrons: ".ljust(25,'.')}{F"{neutron_count}".rjust(25,'.')}")
        print(F"{F"  Protons: ".ljust(25,'.')}{F"{proton_count}".rjust(25,'.')}")
        print()
        print("Sample Data:")
        print(F"{F"  Mass: ".ljust(25,'.')}{F"{mass} grams".rjust(25,'.')}")
        print(F"{F"  grams/mole: ".ljust(25,'.')}{F"{data:,.5f}".rjust(25,'.')}")
        print(F"{F"  moles: ".ljust(25,'.')}{F"{moles:,.5f}".rjust(25,'.')}")
        
        print()
        
        if input("Enter another formula? (y/n)").lower() != 'y':
            break
    
    print()
    print()
    print("Have a blessed day!")
    print()
    print()

if __name__ == "__main__":
    main()