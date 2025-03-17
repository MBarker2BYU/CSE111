
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
    
    @property
    def to_list_item(self):
        return [self._symbol, self._name, self._atomic_mass]


# Elements Class to hold the list of elements
class Elements:    
    def __init__(self):
        self._elements = []

    @property
    def get_elements(self):
        return self._elements

# Better and more advanced Option
def make_periodic_table_element():

    elements = Elements().get_elements
    
    elements.append(Element("Ac", "Actinium", 227))
    elements.append(Element("Ag", "Silver", 107.8682))
    elements.append(Element("Al", "Aluminum", 26.9815386))
    elements.append(Element("Ar", "Argon", 39.948))
    elements.append(Element("As", "Arsenic", 74.9216))
    elements.append(Element("At", "Astatine", 210))
    elements.append(Element("Au", "Gold",	196.966569))
    elements.append(Element("B", "Boron", 10.811))
    elements.append(Element("Ba", "Barium", 137.327))
    elements.append(Element("Be", "Beryllium", 9.012182))
    elements.append(Element("Bi", "Bismuth", 208.9804))
    elements.append(Element("Br", "Bromine", 79.904))
    elements.append(Element("C", "Carbon", 12.0107))
    elements.append(Element("Ca", "Calcium", 40.078))
    elements.append(Element("Cd", "Cadmium", 112.411))
    elements.append(Element("Ce", "Cerium", 140.116))
    elements.append(Element("Cl", "Chlorine", 35.453))
    elements.append(Element("Co", "Cobalt", 58.933195))
    elements.append(Element("Cr", "Chromium", 51.9961))
    elements.append(Element("Cs", "Cesium", 132.9054519))
    elements.append(Element("Cu", "Copper", 63.546))
    elements.append(Element("Dy", "Dysprosium", 162.5))
    elements.append(Element("Er", "Erbium", 167.259))
    elements.append(Element("Eu", "Europium", 151.964))
    elements.append(Element("F", "Fluorine", 18.9984032))
    elements.append(Element("Fe", "Iron",	55.845))
    elements.append(Element("Fr", "Francium",	223))
    elements.append(Element("Ga", "Gallium", 69.723))
    elements.append(Element("Gd", "Gadolinium", 157.25))
    elements.append(Element("Ge", "Germanium", 72.64))
    elements.append(Element("H", "Hydrogen", 1.00794))
    elements.append(Element("He", "Helium", 4.002602))
    elements.append(Element("Hf", "Hafnium", 178.49))
    elements.append(Element("Hg", "Mercury", 200.59))
    elements.append(Element("Ho", "Holmium", 164.93032))
    elements.append(Element("I", "Iodine", 126.90447))
    elements.append(Element("In", "Indium", 114.818))
    elements.append(Element("Ir", "Iridium", 192.217))
    elements.append(Element("K", "Potassium", 39.0983))
    elements.append(Element("Kr", "Krypton", 83.798))
    elements.append(Element("La", "Lanthanum", 138.90547))
    elements.append(Element("Li", "Lithium", 6.941))
    elements.append(Element("Lu", "Lutetium", 174.9668))
    elements.append(Element("Mg", "Magnesium", 24.305))
    elements.append(Element("Mn", "Manganese", 54.938045))
    elements.append(Element("Mo", "Molybdenum", 95.96))
    elements.append(Element("N", "Nitrogen", 14.0067))
    elements.append(Element("Na", "Sodium", 22.98976928))
    elements.append(Element("Nb", "Niobium", 92.90638))
    elements.append(Element("Nd", "Neodymium", 144.242))
    elements.append(Element("Ne", "Neon",	20.1797))
    elements.append(Element("Ni", "Nickel", 58.6934))
    elements.append(Element("Np", "Neptunium", 237))
    elements.append(Element("O", "Oxygen", 15.9994))
    elements.append(Element("Os", "Osmium", 190.23))
    elements.append(Element("P", "Phosphorus", 30.973762))
    elements.append(Element("Pa", "Protactinium", 231.03588))
    elements.append(Element("Pb", "Lead",	207.2))
    elements.append(Element("Pd", "Palladium", 106.42))
    elements.append(Element("Pm", "Promethium", 145))
    elements.append(Element("Po", "Polonium",	209))
    elements.append(Element("Pr", "Praseodymium",	140.90765))
    elements.append(Element("Pt", "Platinum", 195.084))
    elements.append(Element("Pu", "Plutonium", 244))
    elements.append(Element("Ra", "Radium", 226))
    elements.append(Element("Rb", "Rubidium", 85.4678))
    elements.append(Element("Re", "Rhenium", 186.207))
    elements.append(Element("Rh", "Rhodium", 102.9055))
    elements.append(Element("Rn", "Radon", 222))
    elements.append(Element("Ru", "Ruthenium", 101.07))
    elements.append(Element("S", "Sulfur", 32.065))
    elements.append(Element("Sb", "Antimony", 121.76))
    elements.append(Element("Sc", "Scandium", 44.955912))
    elements.append(Element("Se", "Selenium", 78.96))
    elements.append(Element("Si", "Silicon", 28.0855))
    elements.append(Element("Sm", "Samarium", 150.36))
    elements.append(Element("Sn", "Tin", 118.71))
    elements.append(Element("Sr", "Strontium", 87.62))
    elements.append(Element("Ta", "Tantalum", 180.94788))
    elements.append(Element("Tb", "Terbium", 158.92535))
    elements.append(Element("Tc", "Technetium", 98))
    elements.append(Element("Te", "Tellurium", 127.6))
    elements.append(Element("Th", "Thorium", 232.03806))
    elements.append(Element("Ti", "Titanium", 47.867))
    elements.append(Element("Tl", "Thallium", 204.3833))
    elements.append(Element("Tm", "Thulium", 168.93421))
    elements.append(Element("U", "Uranium", 238.02891))
    elements.append(Element("V", "Vanadium",	50.9415))
    elements.append(Element("W", "Tungsten", 183.84))
    elements.append(Element("Xe", "Xenon", 131.293))
    elements.append(Element("Y", "Yttrium", 88.90585))
    elements.append(Element("Yb", "Ytterbium", 173.054))
    elements.append(Element("Zn", "Zinc",	65.38))
    elements.append(Element("Zr", "Zirconium", 91.224))

    return elements

# Required for class
def make_periodic_table():

    elements = []
        
    for element in make_periodic_table_element():
        elements.append(element.to_list_item)

    return elements


def main():

    elements = make_periodic_table()
               
    print(F"{len(elements)} Elements loaded.")

if __name__ == "__main__":
    main()