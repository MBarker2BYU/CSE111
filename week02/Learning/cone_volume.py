# Author: Matthew D. Barker
# Date: Mar 05, 2025
# Class: ConeVolume

# Description: Learning exercise 04 Checkpoint : Variable Scope

from os import system, name
from math import pi as PI

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
    def is_int(value):

        try:
            _ = int(value)

            return True
        except:
            return False

    @staticmethod
    def is_float(value):

        try:
            _ = float(value)

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

                if not Utilities.is_int(user_input):
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

class ConeVolume:
  
  #Calculate the volume of a right cone
  @staticmethod
  def cone_volume(radius, height):
      
      return PI * radius**2 * height / 3
# Included to meet assignment requirements only
def main():
            
    Utilities.print_plus("This application will calculate the volume of a right cone.", True, 2, 2)

    radius = Utilities.input_number("What is the radius of the base of the cone? ", "Radius", True)
    height = Utilities.input_number("What is the height of the cone? ", "Height", True)

    volume = cone_volume(radius, height)

    Utilities.print_plus(F"A right cone with a radius of {radius} at the base and a height of {height}, has a volume of {volume:,.1f}.", spacing_before=1)

# Included to meet assignment requirements only
def cone_volume(radius, height):

    return ConeVolume.cone_volume(radius, height)

if __name__=="__main__":

    # Included to meet assignment requirements only
    main()
    