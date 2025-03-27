from formula import parse_formula
from os import system, name
from enum import Enum
import sys
import csv
import os

class PeriodicTableProperties(Enum):
    AtomicNumber=0
    Element=1
    Symbol=2
    AtomicMass=3
    NumberofNeutrons=4
    NumberofProtons=5
    NumberofElectrons=6
    Period=7
    Group=8
    Phase=9
    Radioactive=10
    Natural=11
    Metal=12
    Nonmetal=13
    Metalloid=14
    Type=15
    AtomicRadius=16
    Electronegativity=17
    FirstIonization=18
    Density=19
    MeltingPoint=20
    BoilingPoint=21
    NumberOfIsotopes=22
    Discoverer=23
    Year=24
    SpecificHeat=25
    NumberofShells=26
    NumberofValence=27


class Utilities:
    def clear_screen():
        system("cls" if name == "nt" else "clear")

    def yes_no_prompt(prompt):
        print(prompt)
        return input().strip().lower() == 'y'
    
    def get_current_directory():
        return os.path.dirname(os.path.realpath(__file__))
    
# Element Class
class Element:

    def __init__(self, symbol, name, atomic_mass):
        
        self._name = name
        self._symbol = symbol
        self._atomic_mass = atomic_mass

        self._atomic_number = 0
        self._number_of_neutrons = 0
        self._number_of_protons = 0
        self._number_of_electrons = 0
        

    @property
    def symbol(self):
        return self._symbol

    @property
    def name(self):
        return self._name


    @property
    def atomic_mass(self):
        return self._atomic_mass

    @property
    def atomic_number(self):
        return self._atomic_number
    
    @property
    def to_list_item(self):
        return [self._name, self._atomic_mass]
    
    @property
    def number_of_neutrons(self):
        return self._number_of_neutrons

    @property
    def number_of_protrons(self):
        return self._number_of_protrons
    
    @property
    def number_of_electrons(self):
        return self._number_of_electrons
    
    @property
    def to_list_item(self):
        return [self._symbol, self._name, self._atomic_mass, self._atomic_number, self._number_of_neutrons, self._number_of_protons, self.number_of_electrons]

    def update_element(self, atomic_number, number_of_neutrons, number_of_protons, number_of_electrons):

        self._atomic_number = atomic_number
        self._number_of_neutrons = number_of_neutrons
        self._number_of_protons = number_of_protons
        self._number_of_electrons = number_of_electrons

# Elements Class to hold the list of elements
class Elements:
    def __init__(self):
        self._elements = {}

    def add_element(self, element):

        if element.symbol not in self._elements:
            self._elements[element.symbol] = element

    def update(file_path):
        pass

    @property
    def get_elements(self):
        return self._elements

class PeriodicTable:
    def __init__(self):
        
        self._elements = Elements()
        self._build_periodic_table()

    def _build_periodic_table(self):

        self._elements.add_element(Element("Ac", "Actinium", 227))
        self._elements.add_element(Element("Ag", "Silver", 107.8682))
        self._elements.add_element(Element("Al", "Aluminum", 26.9815386))
        self._elements.add_element(Element("Ar", "Argon", 39.948))
        self._elements.add_element(Element("As", "Arsenic", 74.9216))
        self._elements.add_element(Element("At", "Astatine", 210))
        self._elements.add_element(Element("Au", "Gold",	196.966569))
        self._elements.add_element(Element("B", "Boron", 10.811))
        self._elements.add_element(Element("Ba", "Barium", 137.327))
        self._elements.add_element(Element("Be", "Beryllium", 9.012182))
        self._elements.add_element(Element("Bi", "Bismuth", 208.9804))
        self._elements.add_element(Element("Br", "Bromine", 79.904))
        self._elements.add_element(Element("C", "Carbon", 12.0107))
        self._elements.add_element(Element("Ca", "Calcium", 40.078))
        self._elements.add_element(Element("Cd", "Cadmium", 112.411))
        self._elements.add_element(Element("Ce", "Cerium", 140.116))
        self._elements.add_element(Element("Cl", "Chlorine", 35.453))
        self._elements.add_element(Element("Co", "Cobalt", 58.933195))
        self._elements.add_element(Element("Cr", "Chromium", 51.9961))
        self._elements.add_element(Element("Cs", "Cesium", 132.9054519))
        self._elements.add_element(Element("Cu", "Copper", 63.546))
        self._elements.add_element(Element("Dy", "Dysprosium", 162.5))
        self._elements.add_element(Element("Er", "Erbium", 167.259))
        self._elements.add_element(Element("Eu", "Europium", 151.964))
        self._elements.add_element(Element("F", "Fluorine", 18.9984032))
        self._elements.add_element(Element("Fe", "Iron",	55.845))
        self._elements.add_element(Element("Fr", "Francium",	223))
        self._elements.add_element(Element("Ga", "Gallium", 69.723))
        self._elements.add_element(Element("Gd", "Gadolinium", 157.25))
        self._elements.add_element(Element("Ge", "Germanium", 72.64))
        self._elements.add_element(Element("H", "Hydrogen", 1.00794))
        self._elements.add_element(Element("He", "Helium", 4.002602))
        self._elements.add_element(Element("Hf", "Hafnium", 178.49))
        self._elements.add_element(Element("Hg", "Mercury", 200.59))
        self._elements.add_element(Element("Ho", "Holmium", 164.93032))
        self._elements.add_element(Element("I", "Iodine", 126.90447))
        self._elements.add_element(Element("In", "Indium", 114.818))
        self._elements.add_element(Element("Ir", "Iridium", 192.217))
        self._elements.add_element(Element("K", "Potassium", 39.0983))
        self._elements.add_element(Element("Kr", "Krypton", 83.798))
        self._elements.add_element(Element("La", "Lanthanum", 138.90547))
        self._elements.add_element(Element("Li", "Lithium", 6.941))
        self._elements.add_element(Element("Lu", "Lutetium", 174.9668))
        self._elements.add_element(Element("Mg", "Magnesium", 24.305))
        self._elements.add_element(Element("Mn", "Manganese", 54.938045))
        self._elements.add_element(Element("Mo", "Molybdenum", 95.96))
        self._elements.add_element(Element("N", "Nitrogen", 14.0067))
        self._elements.add_element(Element("Na", "Sodium", 22.98976928))
        self._elements.add_element(Element("Nb", "Niobium", 92.90638))
        self._elements.add_element(Element("Nd", "Neodymium", 144.242))
        self._elements.add_element(Element("Ne", "Neon",	20.1797))
        self._elements.add_element(Element("Ni", "Nickel", 58.6934))
        self._elements.add_element(Element("Np", "Neptunium", 237))
        self._elements.add_element(Element("O", "Oxygen", 15.9994))
        self._elements.add_element(Element("Os", "Osmium", 190.23))
        self._elements.add_element(Element("P", "Phosphorus", 30.973762))
        self._elements.add_element(Element("Pa", "Protactinium", 231.03588))
        self._elements.add_element(Element("Pb", "Lead",	207.2))
        self._elements.add_element(Element("Pd", "Palladium", 106.42))
        self._elements.add_element(Element("Pm", "Promethium", 145))
        self._elements.add_element(Element("Po", "Polonium",	209))
        self._elements.add_element(Element("Pr", "Praseodymium",	140.90765))
        self._elements.add_element(Element("Pt", "Platinum", 195.084))
        self._elements.add_element(Element("Pu", "Plutonium", 244))
        self._elements.add_element(Element("Ra", "Radium", 226))
        self._elements.add_element(Element("Rb", "Rubidium", 85.4678))
        self._elements.add_element(Element("Re", "Rhenium", 186.207))
        self._elements.add_element(Element("Rh", "Rhodium", 102.9055))
        self._elements.add_element(Element("Rn", "Radon", 222))
        self._elements.add_element(Element("Ru", "Ruthenium", 101.07))
        self._elements.add_element(Element("S", "Sulfur", 32.065))
        self._elements.add_element(Element("Sb", "Antimony", 121.76))
        self._elements.add_element(Element("Sc", "Scandium", 44.955912))
        self._elements.add_element(Element("Se", "Selenium", 78.96))
        self._elements.add_element(Element("Si", "Silicon", 28.0855))
        self._elements.add_element(Element("Sm", "Samarium", 150.36))
        self._elements.add_element(Element("Sn", "Tin", 118.71))
        self._elements.add_element(Element("Sr", "Strontium", 87.62))
        self._elements.add_element(Element("Ta", "Tantalum", 180.94788))
        self._elements.add_element(Element("Tb", "Terbium", 158.92535))
        self._elements.add_element(Element("Tc", "Technetium", 98))
        self._elements.add_element(Element("Te", "Tellurium", 127.6))
        self._elements.add_element(Element("Th", "Thorium", 232.03806))
        self._elements.add_element(Element("Ti", "Titanium", 47.867))
        self._elements.add_element(Element("Tl", "Thallium", 204.3833))
        self._elements.add_element(Element("Tm", "Thulium", 168.93421))
        self._elements.add_element(Element("U", "Uranium", 238.02891))
        self._elements.add_element(Element("V", "Vanadium",	50.9415))
        self._elements.add_element(Element("W", "Tungsten", 183.84))
        self._elements.add_element(Element("Xe", "Xenon", 131.293))
        self._elements.add_element(Element("Y", "Yttrium", 88.90585))
        self._elements.add_element(Element("Yb", "Ytterbium", 173.054))
        self._elements.add_element(Element("Zn", "Zinc",	65.38))
        self._elements.add_element(Element("Zr", "Zirconium", 91.224))

    def ToDictionary(self):
        return self._elements.get_elements

    def update_elements(self, file_path):
        pass
        # if file_path == None:
        #     return
    
        # if extended_elements == None:

        #     extended_elements = {}

        #     with open(file_path, 'r') as file:
        #         csv_reader = csv.reader(file)
        #         header = next(csv_reader)
        #         extended_element_data = list(csv_reader)

        #         for element in self._elements:
        #             extended_elements[element[PeriodicTableProperties.Symbol.value]] = Element()
                    

def make_periodic_table():
    return periodic_table.ToDictionary()

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

def get_formula_name(formula, known_molecules_dict):
    
    if formula in known_molecules_dict:
        return known_molecules_dict[formula]
    else:
        return "unknown compound"

def sum_protons(symbol_quantity_list, periodic_table_dict):
  """Compute and return the total number of protons in
  all the elements listed in symbol_quantity_list.
  Parameters
      symbol_quantity_list is a compound list returned
          from the parse_formula function. Each small
          list in symbol_quantity_list has this form:
          ["symbol", quantity].
      periodic_table_dict is the compound dictionary
          returned from make_periodic_table.
  Return: the total number of protons of all
      the elements in symbol_quantity_list.
  """
  proton_sum = 0

  for element in symbol_quantity_list:
    chemical_symbol = element[NAME_INDEX]
    atomic_number = periodic_table_dict[chemical_symbol].atomic_number * element[QUANTITY_INDEX]
   
    proton_sum += atomic_number

  return proton_sum;    

def compute_molar_mass(symbol_quantity_list, periodic_table):
    
    total_molar_mass = 0

    for element in symbol_quantity_list:
        symbol = element[SYMBOL_INDEX]
        quantity = element[QUANTITY_INDEX]

        e = periodic_table[symbol]
        atomic_mass = e.atomic_mass

        # atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]

        total_molar_mass += atomic_mass * quantity   

    return total_molar_mass

periodic_table = PeriodicTable()

def main():

    # file_path = F"{Utilities.get_current_directory()}\\Periodic Table of Elements.csv"

    # elements = Elements()
    # elements.update(file_path)


               
    # print(F"{len(elements)} Elements loaded.")


    # Utilities.clear_screen()

    # file_path = F"{Utilities.get_current_directory()}\\Periodic Table of Elements.csv"

    # elements = Elements(file_path)
    
    # periodic_table = elements.periodic_table

    # while(True):

    #     Utilities.clear_screen()

    #     print("Enter formula:")
    #     response = input().upper()

    #     print("Enter the mass:")
    #     mass = float(input().upper())

    #     symbol_quantity_list = parse_formula(response.upper(), periodic_table)

    #     data = compute_molar_mass(symbol_quantity_list, periodic_table)    
    #     moles =  mass / data

    #     formula_name = get_formula_name(response, molecules_library())

    #     proton_count = sum_protons(symbol_quantity_list, periodic_table)

    #     Utilities.clear_screen()

    #     print(F"Formula Name: {formula_name.title()}")
    #     print()
    #     print(F"{F"Formula:".ljust(25,'.')}{F"{response}".rjust(25,'.')}")
    #     print(F"{F"Mass:".ljust(25,'.')}{F"{mass} grams".rjust(25,'.')}")
    #     print(F"{F"grams/mole:".ljust(25,'.')}{F"{data:,.5f}".rjust(25,'.')}")
    #     print(F"{F"moles:".ljust(25,'.')}{F"{moles:,.5f}".rjust(25,'.')}")
    #     print(F"{F"Protons:".ljust(25,'.')}{F"{proton_count}".rjust(25,'.')}")
    #     print()
        
    #     if input("Enter another formula?").lower() != 'y':
    #         break
    
    # print()
    # print()
    # print("Have a blessed day!")
    # print()
    # print()

if __name__ == "__main__":
    main()