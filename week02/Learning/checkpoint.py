# Author: Matthew D. Barker
# Date: Mar 05, 2025
# Class: Learning

# Description: Learning Functions week 2

from os import system, name, path

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

class Learning:
  
  @staticmethod
  def miles_per_gallon(odometer_start, odometer_end, gallons):
      
      return (odometer_end - odometer_start) / gallons
  
  @staticmethod  
  def lp_100K_mpg(mpg):
      
      return 235.215 / mpg

# Included to meet assignment requirements only
def main():
    
    Utilities.clear_screen()

    Utilities.spacing(2)

    odometer_start = Utilities.input_number("What was the starting odometer value? ", "odometer reading", True)
    odometer_end = Utilities.input_number("What was the ending odometer value? ", "odometer reading", True)
    gallons_used = Utilities.input_number("How many gallons were used? ", "gallons", True)

    mpg = miles_per_gallon(odometer_start, odometer_end, gallons_used)
    liters_per_100_km = lp100k_from_mpg(mpg)

    Utilities.spacing(2)

    Utilities.input_plus(F"{odometer_end - odometer_start:,.1f} miles were traveled using {gallons_used} gallons of fuel for an average of {mpg:,.1f} miles per gallon ({liters_per_100_km:,.2f} liters per one hundred kilometers).", True)

    Utilities.spacing(2)

# Included to meet assignment requirements only
def miles_per_gallon(start_miles, end_miles, amount_gallons):
    return Learning.miles_per_gallon(start_miles, end_miles, amount_gallons)

# Included to meet assignment requirements only
def lp100k_from_mpg(mpg):
    return Learning.lp_100K_mpg(mpg)
    

if __name__=="__main__":

    main()