# Author: Matthew D. Barker
# Date: 03/02/2025
# Class: CSE111

# Project: Tire Volume

from sys import exit
from random import randint
from os import system
from os import name
from datetime import datetime
from math import pi

class Utilities:

    @staticmethod
    def clear_screen():

        system("cls" if name == "nt" else "clear")

    @staticmethod
    def spacing(lines = 1):

        for _ in range(lines):
            print("")    

    @staticmethod
    def print_plus(text, clear_screen_first = False, spacing_before = 0, spacing_after = 1):
        
        if clear_screen_first:
            Utilities.clear_screen()

        Utilities.spacing(spacing_before)

        print(text)

        Utilities.spacing(spacing_after)

    @staticmethod
    def is_digit(value):

        try:
            number = int(value)

            return True
        except:
            return False

    @staticmethod
    def is_float(value):

        try:
            number = float(value)

            return True
        except:
            return False

    @staticmethod
    def input_plus(prompt, clear_screen_first = False, new_line = False):

        if clear_screen_first:
            Utilities.clear_screen()

        if new_line > 0:
            
            print(prompt)

            return input()
        else:
            return input(prompt)

    @staticmethod
    def input_number(prompt, variable_name, as_float=False):

        while True:
            
            user_input = Utilities.input_plus(prompt)

            if as_float:

                if not Utilities.is_float(user_input):
                    Utilities.print_plus(F"'{user_input}' is not a valid {variable_name}. Please enter a valid {variable_name}.", True, 1)
                    Utilities.press_space_continue(clear_screen_after=True)

                    continue

                return float(user_input)
            
            else:

                if not Utilities.is_digit(user_input):
                    Utilities.print_plus(F"'{user_input}' is not a valid {variable_name}. Please enter a valid {variable_name}.", True, 1)
                    Utilities.press_space_continue(clear_screen_after=True)

                    continue

                return int(user_input)
    
    @staticmethod
    def press_space_continue(key = "enter", spacing_before = 0, clear_screen_after = False):

        if spacing_before > 0:
            Utilities.spacing(spacing_before)

        input(F"Press {key} to continue...")

        if clear_screen_after:
            Utilities.clear_screen()

class TireVolumeCalculator:

    padding = 25

    def run(self):
        
        center_padding = self.padding * 2
        valid_tire_size = True

        while(True):

            user_input = Utilities.input_plus("Would you like to use size wall tire size (ex. 205/60R15)? (Y/N)", True, 1).upper()

            valid_tire_size = True

            volume = 0.0
            tire_size = ""

            if user_input == "Y":
                tire_size = Utilities.input_plus("Please enter the tire size as seen on tire (ex. '205/60R15'): ", True).upper()

                tire_parameters = self.valid_tire_size(tire_size)

                if tire_parameters[0]:
                    volume = self.calculate_tire_volume_by_parameters(tire_parameters[1], tire_parameters[2], tire_parameters[3])
                else:
                    Utilities.clear_screen()
                    Utilities.input_plus(F"'{tire_size}' is an invalid tire size detected.")
                    Utilities.press_space_continue()

                    valid_tire_size = False

            else:
                Utilities.clear_screen()

                width = Utilities.input_number("Please enter the width value (ex. \033[04m205\033[0m/60R15): ", "Width")
                aspect_ratio = Utilities.input_number("Please enter the aspect ratio value (ex. 205/\033[04m60\033[0mR15): ", "Aspect Ratio")
                diameter = Utilities.input_number("Please enter the wheel diameter value (ex. 205/60R\033[04m15\033[0m): ", "Wheel Diameter")

                volume = self.calculate_tire_volume_by_parameters(width, aspect_ratio, diameter)

                tire_size = F"{width}/{aspect_ratio}R{diameter}"
            
            if valid_tire_size:
                Utilities.print_plus(F"The approximate volume of a tire sized '{tire_size}' is {volume:,.2f} liters.", True, 0, 2)

                Utilities.press_space_continue()

            user_input = Utilities.input_plus("Calculate another tire size? (Y/N)", True).upper()

            if user_input == "N":
                break

        
        Utilities.print_plus("Have a blessed day!".center(center_padding),True ,0 , 3)


    def calculate_tire_volume_by_nomenclature(self, nomenclature):
        
        result = self.valid_tire_size(nomenclature)

        if result[0]:
            return (True, self.calculate_tire_volume_by_parameters(result[1], result[2], result[3]))
        else:
            return (False, 0)

    def calculate_tire_volume_by_parameters(self, width, aspect_ratio, diameter_in_inches):
        
        volume = pi * width**2 * aspect_ratio * (2540 * diameter_in_inches + width * aspect_ratio) / 10000000000

        return volume

    def calculate_outer_radius(self, width, aspect_ratio, radius):
        return (width * aspect_ratio) + radius

    def calculate_inner_radius(self, width, aspect_ratio):
        return (width * aspect_ratio) / 2
    
    def valid_tire_size(self, tire_size):

        try:
            stage1 = tire_size.split("/")
            width = int(stage1[0])
            stage2 = stage1[1].split("R")
            aspect_ratio = int(stage2[0])
            diameter = int(stage2[1])

            return (True, width, aspect_ratio, diameter)
        except:
            return (False, 0, 0, 0)

        
    
if __name__=="__main__":

    TireVolumeCalculator().run()