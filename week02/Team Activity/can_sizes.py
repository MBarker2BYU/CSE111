# Author: Matthew D. Barker
# Date: Mar 05, 2025
# Description: W02 Team Activity: Can Efficiency

from math import pi as PI
from os import system, name

class CanInfo:

    super_script = str.maketrans('23', '\u00b2\u00b3')
    
    def __init__(self, name, radius, height, cost_per_can, unit_of_measurement = "cm", currency = "$"):

        self._name = name
        self._radius = radius
        self._height = height
        self._cost_per_can = cost_per_can
        self._unit_of_measurement = unit_of_measurement
        self._currency = currency

        self._volume_unit_of_measurement = str.translate(F"{self.unit_of_measurement}3", self.super_script)
        self._surface_area_unit_of_measurement = str.translate(F"{self.unit_of_measurement}2", self.super_script)


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

    @property
    def volume(self):
        if not hasattr(self,'_volume'):
            self._volume = CanInfo.compute_volume(self.radius, self.height)
        
        return self._volume
    
    @property
    def surface_area(self):
        if not hasattr(self, '_surface_area'):
            self._surface_area = CanInfo.compute_surface_area(self.radius, self.height)
        
        return self._surface_area
    
    @property
    def storage_efficiency(self):
        if not hasattr(self, '_storage_efficiency'):
            self._storage_efficiency = CanInfo.compute_storage_efficiency(self.volume, self.surface_area)
        
        return self._storage_efficiency

    @property
    def cost_efficiency(self):
        if not hasattr(self, '_cost_efficiency'):
            self._cost_efficiency = CanInfo.compute_cost_efficiency(self.volume, self.cost_per_can)
        
        return self._cost_efficiency

    @property
    def volume_unit_of_measurement(self):
        return self._volume_unit_of_measurement

    @property
    def surface_area_unit_of_measurement(self):
        return self._surface_area_unit_of_measurement

    @staticmethod
    def compute_volume(radius, height):
    
        return PI * radius**2 * height
    
    @staticmethod
    def compute_surface_area(radius, height):
        
        return 2 * PI * radius * (radius + height)
    
    @staticmethod
    def compute_storage_efficiency(volume, surface_area):

        return volume / surface_area

    @staticmethod
    def compute_cost_efficiency(volume, cost):
        return volume / cost

    def display_information(self):

        print_plus(F"Can '{self.name}' information:", spacing_after=0)
        print_plus(CanInfo.format_data('Volume', F"{self.volume:,.2f} {self.volume_unit_of_measurement}"), spacing_after=0)
        print_plus(CanInfo.format_data('Surface Area', F"{self.surface_area:,.2f} {self.surface_area_unit_of_measurement}"), spacing_after=0)
        print_plus(CanInfo.format_data('Storage Efficiency', F"{self.storage_efficiency:,.2f}"), spacing_after=0)
        print_plus(CanInfo.format_data('Cost Efficiency', f"{self.cost_efficiency:,.0f}"), spacing_after=1)

    @staticmethod
    def format_data( title, value, padding=25, padding_character='.'):
        return F"{F"{title}".ljust(padding, padding_character)}{F"{value}".rjust(padding, padding_character)}"

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

    best_storage_efficiency = cans[0]    
    best_cost_efficiency = cans[0]

    clear_screen()

    for can_info in cans:
        can_info.display_information()

        if best_cost_efficiency.cost_efficiency < can_info.cost_efficiency:
            best_cost_efficiency = can_info

        if best_storage_efficiency.storage_efficiency < can_info.storage_efficiency:
            best_storage_efficiency = can_info
        

    print_plus(F"The {best_storage_efficiency.name} can has the best storage efficiency.", spacing_after=0)
    print_plus(CanInfo.format_data('Storage Efficiency', F"{best_storage_efficiency.storage_efficiency:,.2f}"))

    print_plus(F"The {best_cost_efficiency.name} can has the best cost efficiency.", spacing_after=0)
    print_plus(CanInfo.format_data('Cost Efficiency', F"{best_cost_efficiency.cost_efficiency:,.0f}"))


def clear_screen():

    system("cls" if name == "nt" else "clear")

def spacing(lines = 1):

    for _ in range(lines):
        print("")    

def print_plus(text, clear_screen_first = False, spacing_before = 0, spacing_after = 1):
    
    if clear_screen_first:
        clear_screen()

    spacing(spacing_before)

    print(text)

    spacing(spacing_after)

main()