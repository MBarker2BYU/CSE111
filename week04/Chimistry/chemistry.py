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

def element_list():

    elements = []

    elements.append(["H","Hydrogen",1.008,1])
    elements.append(["He","Helium",4.003,2])
    elements.append(["Li","Lithium",6.94,3])
    elements.append(["Be","Beryllium",9.012,4])
    elements.append(["B","Boron",10.81,5])
    elements.append(["C","Carbon",12.011,6])
    elements.append(["N","Nitrogen",14.007,7])
    elements.append(["O","Oxygen",15.999,8])
    elements.append(["F","Fluorine",18.998,9])
    elements.append(["Ne","Neon",20.18,10])
    elements.append(["Na","Sodium",22.99,11])
    elements.append(["Mg","Magnesium",24.305,12])
    elements.append(["Al","Aluminium",26.982,13])
    elements.append(["Si","Silicon",28.085,14])
    elements.append(["P","Phosphorus",30.974,15])
    elements.append(["S","Sulfur",32.06,16])
    elements.append(["Cl","Chlorine",35.45,17])
    elements.append(["Ar","Argon",39.948,18])
    elements.append(["K","Potassium",39.098,19])
    elements.append(["Ca","Calcium",40.078,20])
    elements.append(["Sc","Scandium",44.956,21])
    elements.append(["Ti","Titanium",47.867,22])
    elements.append(["V","Vanadium",50.942,23])
    elements.append(["Cr","Chromium",51.996,24])
    elements.append(["Mn","Manganese",54.938,25])
    elements.append(["Fe","Iron",55.845,26])
    elements.append(["Co","Cobalt",58.933,27])
    elements.append(["Ni","Nickel",58.693,28])
    elements.append(["Cu","Copper",63.546,29])
    elements.append(["Zn","Zinc",65.38,30])
    elements.append(["Ga","Gallium",69.723,31])
    elements.append(["Ge","Germanium",72.63,32])
    elements.append(["As","Arsenic",74.922,33])
    elements.append(["Se","Selenium",78.971,34])
    elements.append(["Br","Bromine",79.904,35])
    elements.append(["Kr","Krypton",83.798,36])
    elements.append(["Rb","Rubidium",85.468,37])
    elements.append(["Sr","Strontium",87.62,38])
    elements.append(["Y","Yttrium",88.906,39])
    elements.append(["Zr","Zirconium",91.224,40])
    elements.append(["Nb","Niobium",92.906,41])
    elements.append(["Mo","Molybdenum",95.95,42])
    elements.append(["Tc","Technetium",98,43])
    elements.append(["Ru","Ruthenium",101.07,44])
    elements.append(["Rh","Rhodium",102.906,45])
    elements.append(["Pd","Palladium",106.42,46])
    elements.append(["Ag","Silver",107.868,47])
    elements.append(["Cd","Cadmium",112.414,48])
    elements.append(["In","Indium",114.818,49])
    elements.append(["Sn","Tin",118.71,50])
    elements.append(["Sb","Antimony",121.76,51])
    elements.append(["Te","Tellurium",127.6,52])
    elements.append(["I","Iodine",126.904,53])
    elements.append(["Xe","Xenon",131.293,54])
    elements.append(["Cs","Caesium",132.905,55])
    elements.append(["Ba","Barium",137.327,56])
    elements.append(["La","Lanthanum",138.905,57])
    elements.append(["Ce","Cerium",140.116,58])
    elements.append(["Pr","Praseodymium",140.908,59])
    elements.append(["Nd","Neodymium",144.242,60])
    elements.append(["Pm","Promethium",145,61])
    elements.append(["Sm","Samarium",150.36,62])
    elements.append(["Eu","Europium",151.964,63])
    elements.append(["Gd","Gadolinium",157.25,64])
    elements.append(["Tb","Terbium",158.925,65])
    elements.append(["Dy","Dysprosium",162.5,66])
    elements.append(["Ho","Holmium",164.93,67])
    elements.append(["Er","Erbium",167.259,68])
    elements.append(["Tm","Thulium",168.934,69])
    elements.append(["Yb","Ytterbium",173.045,70])
    elements.append(["Lu","Lutetium",174.967,71])
    elements.append(["Hf","Hafnium",178.49,72])
    elements.append(["Ta","Tantalum",180.948,73])
    elements.append(["W","Tungsten",183.84,74])
    elements.append(["Re","Rhenium",186.207,75])
    elements.append(["Os","Osmium",190.23,76])
    elements.append(["Ir","Iridium",192.217,77])
    elements.append(["Pt","Platinum",195.084,78])
    elements.append(["Au","Gold",196.967,79])
    elements.append(["Hg","Mercury",200.592,80])
    elements.append(["Tl","Thallium",204.38,81])
    elements.append(["Pb","Lead",207.2,82])
    elements.append(["Bi","Bismuth",208.98,83])
    elements.append(["Po","Polonium",209,84])
    elements.append(["At","Astatine",210,85])
    elements.append(["Rn","Radon",222,86])
    elements.append(["Fr","Francium",223,87])
    elements.append(["Ra","Radium",226,88])
    elements.append(["Ac","Actinium",227,89])
    elements.append(["Th","Thorium",232.038,90])
    elements.append(["Pa","Protactinium",231.036,91])
    elements.append(["U","Uranium",238.029,92])
    elements.append(["Np","Neptunium",237,93])
    elements.append(["Pu","Plutonium",244,94])
    elements.append(["Am","Americium",243,95])
    elements.append(["Cm","Curium",247,96])
    elements.append(["Bk","Berkelium",247,97])
    elements.append(["Cf","Californium",251,98])
    elements.append(["Es","Einsteinium",252,99])
    elements.append(["Fm","Fermium",257,100])
    elements.append(["Md","Mendelevium",258,101])
    elements.append(["No","Nobelium",259,102])
    elements.append(["Lr","Lawrencium",266,103])
    elements.append(["Rf","Rutherfordium",267,104])
    elements.append(["Db","Dubnium",268,105])
    elements.append(["Sg","Seaborgium",269,106])
    elements.append(["Bh","Bohrium",270,107])
    elements.append(["Hs","Hassium",277,108])
    elements.append(["Mt","Meitnerium",278,109])
    elements.append(["Ds","Darmstadtium",281,110])
    elements.append(["Rg","Roentgenium",282,111])
    elements.append(["Cn","Copernicium",285,112])
    elements.append(["Nh","Nihonium",286,113])
    elements.append(["Fl","Flerovium",289,114])
    elements.append(["Mc","Moscovium",290,115])
    elements.append(["Lv","Livermorium",293,116])
    elements.append(["Ts","Tennessine",294,117])
    elements.append(["Og","Oganesson",294,118])

    return elements

CHEMICAL_SYMBOL = 0
ELEMENT_NAME = 1
ATOMIC_WEIGHT = 2
ATOMIC_NUMBER = 3

def make_periodic_table_dictionary():

    elements = Elements().get_elements
    
    for element in element_list():
        elements[element[CHEMICAL_SYMBOL]] = Element(element[CHEMICAL_SYMBOL], element[ELEMENT_NAME], element[ATOMIC_WEIGHT], element[ATOMIC_NUMBER])

    # elements["Ac"] = Element("Ac", "Actinium", 227)
    # elements["Ag"] = Element("Ag", "Silver", 107.8682)
    # elements["Al"] = Element("Al", "Aluminum", 26.9815386)
    # elements["Ar"] = Element("Ar", "Argon", 39.948)
    # elements["As"] = Element("As", "Arsenic", 74.9216)
    # elements["At"] = Element("At", "Astatine", 210)
    # elements["Au"] = Element("Au", "Gold",	196.966569)
    # elements["B"] = Element("B", "Boron", 10.811)
    # elements["Ba"] = Element("Ba", "Barium", 137.327)
    # elements["Be"] = Element("Be", "Beryllium", 9.012182)
    # elements["Bi"] = Element("Bi", "Bismuth", 208.9804)
    # elements["Br"] = Element("Br", "Bromine", 79.904)
    # elements["C"] = Element("C", "Carbon", 12.0107)
    # elements["Ca"] = Element("Ca", "Calcium", 40.078) 
    # elements["Cd"] = Element("Cd", "Cadmium", 112.411) 
    # elements["Ce"] = Element("Ce", "Cerium", 140.116)
    # elements["Cl"] = Element("Cl", "Chlorine", 35.453)
    # elements["Co"] = Element("Co", "Cobalt", 58.933195)
    # elements["Cr"] = Element("Cr", "Chromium", 51.9961)
    # elements["Cs"] = Element("Cs", "Cesium", 132.9054519)
    # elements["Cu"] = Element("Cu", "Copper", 63.546)
    # elements["Dy"] = Element("Dy", "Dysprosium", 162.5)
    # elements["Er"] = Element("Er", "Erbium", 167.259)
    # elements["Eu"] = Element("Eu", "Europium", 151.964)
    # elements["F"] = Element("F", "Fluorine", 18.9984032)
    # elements["Fe"] = Element("Fe", "Iron",	55.845)
    # elements["Fr"] = Element("Fr", "Francium",	223)
    # elements["Ga"] = Element("Ga", "Gallium", 69.723)
    # elements["Gd"] = Element("Gd", "Gadolinium", 157.25)
    # elements["Ge"] = Element("Ge", "Germanium", 72.64)
    # elements["H"] = Element("H", "Hydrogen", 1.00794)
    # elements["He"] = Element("He", "Helium", 4.002602)
    # elements["Hf"] = Element("Hf", "Hafnium", 178.49)
    # elements["Hg"] = Element("Hg", "Mercury", 200.59)
    # elements["Ho"] = Element("Ho", "Holmium", 164.93032)
    # elements["I"] = Element("I", "Iodine", 126.90447)
    # elements["In"] = Element("In", "Indium", 114.818)
    # elements["Ir"] = Element("Ir", "Iridium", 192.217)
    # elements["K"] = Element("K", "Potassium", 39.0983)
    # elements["Kr"] = Element("Kr", "Krypton", 83.798)
    # elements["La"] = Element("La", "Lanthanum", 138.90547)
    # elements["Li"] = Element("Li", "Lithium", 6.941)
    # elements["Lu"] = Element("Lu", "Lutetium", 174.9668)
    # elements["Mg"] = Element("Mg", "Magnesium", 24.305)
    # elements["Mn"] = Element("Mn", "Manganese", 54.938045)
    # elements["Mo"] = Element("Mo", "Molybdenum", 95.96)
    # elements["N"] = Element("N", "Nitrogen", 14.0067)
    # elements["Na"] = Element("Na", "Sodium", 22.98976928)
    # elements["Nb"] = Element("Nb", "Niobium", 92.90638)
    # elements["Nd"] = Element("Nd", "Neodymium", 144.242)
    # elements["Ne"] = Element("Ne", "Neon",	20.1797)
    # elements["Ni"] = Element("Ni", "Nickel", 58.6934)
    # elements["Np"] = Element("Np", "Neptunium", 237)
    # elements["O"] = Element("O", "Oxygen", 15.9994)
    # elements["Os"] = Element("Os", "Osmium", 190.23)
    # elements["P"] = Element("P", "Phosphorus", 30.973762)
    # elements["Pa"] = Element("Pa", "Protactinium", 231.03588)
    # elements["Pb"] = Element("Pb", "Lead",	207.2)
    # elements["Pd"] = Element("Pd", "Palladium", 106.42)
    # elements["Pm"] = Element("Pm", "Promethium", 145)
    # elements["Po"] = Element("Po", "Polonium",	209)
    # elements["Pr"] = Element("Pr", "Praseodymium",	140.90765)
    # elements["Pt"] = Element("Pt", "Platinum", 195.084)
    # elements["Pu"] = Element("Pu", "Plutonium", 244)
    # elements["Ra"] = Element("Ra", "Radium", 226)
    # elements["Rb"] = Element("Rb", "Rubidium", 85.4678)
    # elements["Re"] = Element("Re", "Rhenium", 186.207)
    # elements["Rh"] = Element("Rh", "Rhodium", 102.9055)
    # elements["Rn"] = Element("Rn", "Radon", 222)
    # elements["Ru"] = Element("Ru", "Ruthenium", 101.07)
    # elements["S"] = Element("S", "Sulfur", 32.065)
    # elements["Sb"] = Element("Sb", "Antimony", 121.76)
    # elements["Sc"] = Element("Sc", "Scandium", 44.955912)
    # elements["Se"] = Element("Se", "Selenium", 78.96)
    # elements["Si"] = Element("Si", "Silicon", 28.0855)
    # elements["Sm"] = Element("Sm", "Samarium", 150.36)
    # elements["Sn"] = Element("Sn", "Tin", 118.71)
    # elements["Sr"] = Element("Sr", "Strontium", 87.62)
    # elements["Ta"] = Element("Ta", "Tantalum", 180.94788)
    # elements["Tb"] = Element("Tb", "Terbium", 158.92535)
    # elements["Tc"] = Element("Tc", "Technetium", 98)
    # elements["Te"] = Element("Te", "Tellurium", 127.6)
    # elements["Th"] = Element("Th", "Thorium", 232.03806)
    # elements["Ti"] = Element("Ti", "Titanium", 47.867)
    # elements["Tl"] = Element("Tl", "Thallium", 204.3833)
    # elements["Tm"] = Element("Tm", "Thulium", 168.93421)
    # elements["U"] = Element("U", "Uranium", 238.02891)
    # elements["V"] = Element("V", "Vanadium",	50.9415)
    # elements["W"] = Element("W", "Tungsten", 183.84)
    # elements["Xe"] = Element("Xe", "Xenon", 131.293)
    # elements["Y"] = Element("Y", "Yttrium", 88.90585)
    # elements["Yb"] = Element("Yb", "Ytterbium", 173.054)
    # elements["Zn"] = Element("Zn", "Zinc",	65.38)
    # elements["Zr"] = Element("Zr", "Zirconium", 91.224)

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


# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1
# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    
    total_molar_mass = 0

    for element in symbol_quantity_list:
        symbol = element[SYMBOL_INDEX]
        quantity = element[QUANTITY_INDEX]

        atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]

        total_molar_mass += atomic_mass * quantity   

    return total_molar_mass

def main():

    while(True):

        Utilities.clear_screen()

        print("Enter formula:")
        response = input().upper()

        print("Enter the mass:")
        mass = float(input().upper())

        symbol_quantity_list = parse_formula(response.upper(), make_periodic_table_dictionary())

        data = compute_molar_mass(symbol_quantity_list, make_periodic_table())    
        moles =  mass / data

        formula_name = get_formula_name(response, molecules_library())

        proton_count = sum_protons(symbol_quantity_list, make_periodic_table_dictionary())

        Utilities.clear_screen()

        print(F"Formula Name: {formula_name.title()}")
        print()
        print(F"{F"Formula:".ljust(25,'.')}{F"{response}".rjust(25,'.')}")
        print(F"{F"Mass:".ljust(25,'.')}{F"{mass} grams".rjust(25,'.')}")
        print(F"{F"grams/mole:".ljust(25,'.')}{F"{data:,.5f}".rjust(25,'.')}")
        print(F"{F"moles:".ljust(25,'.')}{F"{moles:,.5f}".rjust(25,'.')}")
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