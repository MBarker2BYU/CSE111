from formula import parse_formula
from os import system, name
import sys

class Utilities:
    def clear_screen():
        system("cls" if name == "nt" else "clear")

    def yes_no_prompt(prompt):
        print(prompt)
        return input().strip().lower() == 'y'
    
# Element Class
class Element:

    def __init__(self, symbol, name, atomic_mass, atomic_number = 0):
        
        self._name = name
        self._symbol = symbol
        self._atomic_mass = atomic_mass
        self._atomic_number = atomic_number
        

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
    
    # @property
    # def to_list_item(self):
    #     return [self._symbol, self._name, self._atomic_mass]

    @property
    def to_list_item(self):
        return [self._name, self._atomic_mass]

# Elements Class to hold the list of elements
class Elements:    
    def __init__(self):
        self._elements = {}

    @property
    def get_elements(self):
        return self._elements

def make_periodic_table_dictionary():

    elements = Elements().get_elements
    
    elements["Ac"] = Element("Ac", "Actinium", 227)
    elements["Ag"] = Element("Ag", "Silver", 107.8682)
    elements["Al"] = Element("Al", "Aluminum", 26.9815386)
    elements["Ar"] = Element("Ar", "Argon", 39.948)
    elements["As"] = Element("As", "Arsenic", 74.9216)
    elements["At"] = Element("At", "Astatine", 210)
    elements["Au"] = Element("Au", "Gold",	196.966569)
    elements["B"] = Element("B", "Boron", 10.811)
    elements["Ba"] = Element("Ba", "Barium", 137.327)
    elements["Be"] = Element("Be", "Beryllium", 9.012182)
    elements["Bi"] = Element("Bi", "Bismuth", 208.9804)
    elements["Br"] = Element("Br", "Bromine", 79.904)
    elements["C"] = Element("C", "Carbon", 12.0107)
    elements["Ca"] = Element("Ca", "Calcium", 40.078) 
    elements["Cd"] = Element("Cd", "Cadmium", 112.411) 
    elements["Ce"] = Element("Ce", "Cerium", 140.116)
    elements["Cl"] = Element("Cl", "Chlorine", 35.453)
    elements["Co"] = Element("Co", "Cobalt", 58.933195)
    elements["Cr"] = Element("Cr", "Chromium", 51.9961)
    elements["Cs"] = Element("Cs", "Cesium", 132.9054519)
    elements["Cu"] = Element("Cu", "Copper", 63.546)
    elements["Dy"] = Element("Dy", "Dysprosium", 162.5)
    elements["Er"] = Element("Er", "Erbium", 167.259)
    elements["Eu"] = Element("Eu", "Europium", 151.964)
    elements["F"] = Element("F", "Fluorine", 18.9984032)
    elements["Fe"] = Element("Fe", "Iron",	55.845)
    elements["Fr"] = Element("Fr", "Francium",	223)
    elements["Ga"] = Element("Ga", "Gallium", 69.723)
    elements["Gd"] = Element("Gd", "Gadolinium", 157.25)
    elements["Ge"] = Element("Ge", "Germanium", 72.64)
    elements["H"] = Element("H", "Hydrogen", 1.00794)
    elements["He"] = Element("He", "Helium", 4.002602)
    elements["Hf"] = Element("Hf", "Hafnium", 178.49)
    elements["Hg"] = Element("Hg", "Mercury", 200.59)
    elements["Ho"] = Element("Ho", "Holmium", 164.93032)
    elements["I"] = Element("I", "Iodine", 126.90447)
    elements["In"] = Element("In", "Indium", 114.818)
    elements["Ir"] = Element("Ir", "Iridium", 192.217)
    elements["K"] = Element("K", "Potassium", 39.0983)
    elements["Kr"] = Element("Kr", "Krypton", 83.798)
    elements["La"] = Element("La", "Lanthanum", 138.90547)
    elements["Li"] = Element("Li", "Lithium", 6.941)
    elements["Lu"] = Element("Lu", "Lutetium", 174.9668)
    elements["Mg"] = Element("Mg", "Magnesium", 24.305)
    elements["Mn"] = Element("Mn", "Manganese", 54.938045)
    elements["Mo"] = Element("Mo", "Molybdenum", 95.96)
    elements["N"] = Element("N", "Nitrogen", 14.0067)
    elements["Na"] = Element("Na", "Sodium", 22.98976928)
    elements["Nb"] = Element("Nb", "Niobium", 92.90638)
    elements["Nd"] = Element("Nd", "Neodymium", 144.242)
    elements["Ne"] = Element("Ne", "Neon",	20.1797)
    elements["Ni"] = Element("Ni", "Nickel", 58.6934)
    elements["Np"] = Element("Np", "Neptunium", 237)
    elements["O"] = Element("O", "Oxygen", 15.9994)
    elements["Os"] = Element("Os", "Osmium", 190.23)
    elements["P"] = Element("P", "Phosphorus", 30.973762)
    elements["Pa"] = Element("Pa", "Protactinium", 231.03588)
    elements["Pb"] = Element("Pb", "Lead",	207.2)
    elements["Pd"] = Element("Pd", "Palladium", 106.42)
    elements["Pm"] = Element("Pm", "Promethium", 145)
    elements["Po"] = Element("Po", "Polonium",	209)
    elements["Pr"] = Element("Pr", "Praseodymium",	140.90765)
    elements["Pt"] = Element("Pt", "Platinum", 195.084)
    elements["Pu"] = Element("Pu", "Plutonium", 244)
    elements["Ra"] = Element("Ra", "Radium", 226)
    elements["Rb"] = Element("Rb", "Rubidium", 85.4678)
    elements["Re"] = Element("Re", "Rhenium", 186.207)
    elements["Rh"] = Element("Rh", "Rhodium", 102.9055)
    elements["Rn"] = Element("Rn", "Radon", 222)
    elements["Ru"] = Element("Ru", "Ruthenium", 101.07)
    elements["S"] = Element("S", "Sulfur", 32.065)
    elements["Sb"] = Element("Sb", "Antimony", 121.76)
    elements["Sc"] = Element("Sc", "Scandium", 44.955912)
    elements["Se"] = Element("Se", "Selenium", 78.96)
    elements["Si"] = Element("Si", "Silicon", 28.0855)
    elements["Sm"] = Element("Sm", "Samarium", 150.36)
    elements["Sn"] = Element("Sn", "Tin", 118.71)
    elements["Sr"] = Element("Sr", "Strontium", 87.62)
    elements["Ta"] = Element("Ta", "Tantalum", 180.94788)
    elements["Tb"] = Element("Tb", "Terbium", 158.92535)
    elements["Tc"] = Element("Tc", "Technetium", 98)
    elements["Te"] = Element("Te", "Tellurium", 127.6)
    elements["Th"] = Element("Th", "Thorium", 232.03806)
    elements["Ti"] = Element("Ti", "Titanium", 47.867)
    elements["Tl"] = Element("Tl", "Thallium", 204.3833)
    elements["Tm"] = Element("Tm", "Thulium", 168.93421)
    elements["U"] = Element("U", "Uranium", 238.02891)
    elements["V"] = Element("V", "Vanadium",	50.9415)
    elements["W"] = Element("W", "Tungsten", 183.84)
    elements["Xe"] = Element("Xe", "Xenon", 131.293)
    elements["Y"] = Element("Y", "Yttrium", 88.90585)
    elements["Yb"] = Element("Yb", "Ytterbium", 173.054)
    elements["Zn"] = Element("Zn", "Zinc",	65.38)
    elements["Zr"] = Element("Zr", "Zirconium", 91.224)

    return elements

def make_periodic_table():
    
    elements = {}

    for element in make_periodic_table_dictionary().items():
        elements[element[0]] = element[1].to_list_item

    return elements

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
    """Try to find formula in the known_molecules_dict.
    If formula is in the known_molecules_dict, return
    the name of the chemical formula; otherwise return
    "unknown compound".
    Parameters
        formula is a string that contains a chemical formula
        known_molecules_dict is a dictionary that contains
            known chemical formulas and their names
    Return: the name of a chemical formula
    """ 
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

# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1
# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.
    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total molar mass of all the elements in
        symbol_quantity_list.
    For example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """
    # Do the following for each inner list in the
    # compound symbol_quantity_list:
        # Separate the inner list into symbol and quantity.
        # Get the atomic mass for the symbol from the dictionary.
        # Multiply the atomic mass by the quantity.
        # Add the product into the total molar mass.
    # Return the total molar mass.

    total_molar_mass = 0

    for element in symbol_quantity_list:
        symbol = element[SYMBOL_INDEX]
        quantity = element[QUANTITY_INDEX]

        atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]

        total_molar_mass += atomic_mass * quantity   

    return total_molar_mass

def main():

    # elements = make_periodic_table()
               
    # print(F"{len(elements)} Elements loaded.")

    # data = parse_formula("C6H12O6", elements)

    # molar_mass = compute_molar_mass(data, elements)

    # moles = 12.37 / molar_mass

    # a = 1
   
    Utilities.clear_screen()

    print("Enter formula:")
    response = input().upper()

    print("Enter the mass:")
    mass = float(input().upper())

    data = compute_molar_mass(parse_formula(response, make_periodic_table()), make_periodic_table())    
    moles =  mass / data

    print(F"The molar mass of {response} is {data} g/mol.")
    print(F"The number of moles in {mass} grams of {response} is {moles} moles.")

if __name__ == "__main__":
    main()