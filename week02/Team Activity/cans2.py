from math import pi as PI
from os import system, name

#Clears the screen on multiple operating systems
def clear_screen():

    system("cls" if name == "nt" else "clear")

#Prints multiple blank line
def spacing(lines = 1):

    for _ in range(lines):
        print("")    

#Prints the text with a blank line before and after
def print_plus(text, clear_screen_first = False, spacing_before = 0, spacing_after = 1):
    
    if clear_screen_first:
        clear_screen()

    spacing(spacing_before)

    print(text)

    spacing(spacing_after)

#Class to hold the information about the can
class CanInfo:

    super_script = str.maketrans('23', '\u00b2\u00b3')
    
    def __init__(self, name, radius, height, cost_per_can, unit_of_measurement = "cm", currency = "$"):

        self._name = name
        self._radius = radius
        self._height = height
        self._cost_per_can = cost_per_can
        self._unit_of_measurement = unit_of_measurement
        self._currency = currency

    @property
    def name(self):
        return self._name
    
    @property
    def radius(self):
        return self._radius
    
    @property
    def height(self):
        return self._height
    
    @property
    def cost_per_can(self):
        return self._cost_per_can
    
    @property
    def unit_of_measurement(self):
        return self._unit_of_measurement
    
    @property
    def currency(self):
        return self._currency
    
    @staticmethod
    def format_data( title, value, padding=25, padding_character='.'):
        return F"{F"{title}".ljust(padding, padding_character)}{F"{value}".rjust(padding, padding_character)}"

    

    #end of Can_Info

#Core Requirements

#Volume is the area of the circle times the height
def compute_volume(radius, height):
    return PI * radius**2 * height

#Surface area is the sum of the two circles and the rectangle
def compute_surface_area(radius, height):
    return 2 * PI * radius * (radius + height)

#End Core Requirements

#Stretch Challenges

#Storage efficiency is the volume divided by the surface area
def compute_storage_efficiency(volume, surface_area):

    if surface_area == 0:
        return 0

    return volume / surface_area

#Cost efficiency is the volume divided by the cost per can
def compute_cost_efficiency(volume, cost_per_can):

    if cost_per_can == 0:
        return 0

    return volume / cost_per_can    

#End Stretch Challenges

def display_information(volume, surface_area, storage_efficiency, cost_efficiency, name, volume_unit_of_measurement = "cm\u00b3", surface_area_unit_of_measurement = "cm\u00b2"):

        print_plus(F"Can '{name}' information:", spacing_after=0)
        print_plus(CanInfo.format_data('Volume', F"{volume:,.2f} {volume_unit_of_measurement}"), spacing_after=0)
        print_plus(CanInfo.format_data('Surface Area', F"{surface_area:,.2f} {surface_area_unit_of_measurement}"), spacing_after=0)
        print_plus(CanInfo.format_data('Storage Efficiency', F"{storage_efficiency:,.2f}"), spacing_after=0)
        print_plus(CanInfo.format_data('Cost Efficiency', f"{cost_efficiency:,.0f}"), spacing_after=1)

def main():

    cans = []
    cans.append(CanInfo("#1 Picnic", 6.83, 10.16, 0.28))
    cans.append(CanInfo("#1 Tall", 7.78, 11.91, 0.43))
    cans.append(CanInfo("#2", 8.73, 11.59, 0.45))
    cans.append(CanInfo("#2.5", 10.32, 11.91, 0.61))
    cans.append(CanInfo("#3 Cylinder", 10.79, 17.78, 0.86))
    cans.append(CanInfo("#5", 13.02, 14.29, 0.83))
    cans.append(CanInfo("#6Z", 5.4, 8.89, 0.22))
    cans.append(CanInfo("#8Z short", 6.83, 7.62, 0.26))
    cans.append(CanInfo("#10", 15.72, 17.78, 1.53))
    cans.append(CanInfo("#211", 6.83, 12.38, 0.34))
    cans.append(CanInfo("#300", 7.62, 11.27, 0.38))
    cans.append(CanInfo("#303", 8.10, 11.11, 0.42))

    #For the storage efficiency
    best_storage_efficiency = cans[0] 
    best_storage_efficiency_value = 0

    #For the cost efficiency
    best_cost_efficiency = cans[0]
    best_cost_efficiency_value = 0

    clear_screen()

    for can_info in cans:

        #Compute the volume and surface area
        volume = compute_volume(can_info.radius, can_info.height)
        surface_area = compute_surface_area(can_info.radius, can_info.height)

        #Compute the storage and cost efficiency
        computed_storage_efficiency_value = compute_storage_efficiency(volume, surface_area)
        computed_cost_efficiency_value = compute_cost_efficiency(volume, can_info.cost_per_can)

        #Display the information
        display_information(volume, surface_area, computed_storage_efficiency_value, computed_cost_efficiency_value, can_info.name)

        #Determine the best storage efficiency
        if best_storage_efficiency_value < computed_storage_efficiency_value:
            best_storage_efficiency = can_info
            best_storage_efficiency_value = computed_storage_efficiency_value

        #Determine the best cost efficiency
        if best_cost_efficiency_value < computed_cost_efficiency_value:
            best_cost_efficiency = can_info
            best_cost_efficiency_value = computed_cost_efficiency_value

    #Display the best storage and cost efficiency
    print_plus(F"The {best_storage_efficiency.name} can has the best storage efficiency.", spacing_after=0)
    print_plus(CanInfo.format_data('Storage Efficiency', F"{best_storage_efficiency_value:,.2f}"))

    #Display the best cost efficiency
    print_plus(F"The {best_cost_efficiency.name} can has the best cost efficiency.", spacing_after=0)
    print_plus(CanInfo.format_data('Cost Efficiency', F"{best_cost_efficiency_value:,.0f}"))    

    # Core Requirements
    # volume = compute_volume(radius, height)
    # surface_area = compute_surface_area(radius, height)

    # compute_storage_efficiency = compute_storage_efficiency(volume, surface_area)
    # compute_cost_efficiency = compute_cost_efficiency(volume, 0.50)

    # print(f'Volume: {volume:.2f}')
    # print(f'Surface Area: {surface_area:.2f}')
    # print(f'Storage Efficiency: {compute_storage_efficiency:.2f}')
    # print(f'Cost Efficiency: {compute_cost_efficiency:.2f}')

#Run the main function
if __name__ == "__main__":
    main()