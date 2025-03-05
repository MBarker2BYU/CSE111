# Author: Matthew D. Barker
# Date: 03/02/2025
# Class: CSE111

# W01 Project: Tire Volume

from os import system, name, path
from math import pi
from datetime import datetime

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

    tire_prices = {    
        "155/65R13":"$50 - $75",
        "165/65R14":"$60 - $90",  
        "175/65R15":"$70 - $100",  
        "185/60R15":"$80 - $120",  
        "195/65R15":"$85 - $130",  
        "205/60R15":"$100 - $150", 
        "215/60R16":"$110 - $160", 
        "225/55R17":"$120 - $180", 
        "235/55R18":"$140 - $200",
        "245/40R18":"$165 - $220",
        "245/35R19":"$168 - $215", 
        "245/35R20":"$247 - $339", 
        "255/50R20":"$170 - $230", 
        "275/45R21":"$200 - $250", 
        "285/30R20":"$285 - $350",
        "285/35R19":"$297 - $362",
        "285/35R22":"$222 - $376", 
        "335/25R20":"$404"}

    def calculate_tire_volume_by_parameters(self, width, aspect_ratio, diameter_in_inches):
        
        return pi * width**2 * aspect_ratio * (2540 * diameter_in_inches + width * aspect_ratio) / 10000000000
        

    def run(self):
        
        Utilities.clear_screen()

        width = Utilities.input_number("Please enter the width value (ex. \033[04m205\033[0m/60R15): ", "Width")
        aspect_ratio = Utilities.input_number("Please enter the aspect ratio value (ex. 205/\033[04m60\033[0mR15): ", "Aspect Ratio")
        diameter = Utilities.input_number("Please enter the wheel diameter value (ex. 205/60R\033[04m15\033[0m): ", "Wheel Diameter")

        volume = self.calculate_tire_volume_by_parameters(width, aspect_ratio, diameter)

        tire_size = F"{width}/{aspect_ratio}R{diameter}"
            
        Utilities.print_plus(F"The approximate volume of a tire sized '{tire_size}' is {volume:,.2f} liters.", spacing_before=1, spacing_after=2)

        phone_number = ""

        if tire_size in self.tire_prices:
            Utilities.print_plus(F"The {tire_size} is currently running ${self.tire_prices[tire_size]} each.")
            
            if Utilities.input_plus("Are you interested in purchasing one or more? (Yes/No) ").upper() == "YES":
                phone_number = Utilities.input_plus("What phone number can we reach you at? ")    

                Utilities.print_plus(F"A sales representative will contact you at {phone_number} soon.", spacing_before=2, spacing_after=0)                
        else:
            Utilities.print_plus(F"The {tire_size} does not seem to be avalible at this time.")


        Utilities.print_plus(F"Thank you for stopping by. Have a blessed day.", spacing_before=2, spacing_after=3)


        self.write_data(width, aspect_ratio, diameter, volume, phone_number)


    def write_data(self, width, aspect_ration, diameter, volume, phone_number = ""):
                
        script_path = path.abspath(__file__)
        script_directory = path.dirname(script_path)

        file_path = F"{script_directory}\\volumes.txt"

        date = datetime.now().strftime("%Y-%m-%d")

        with open(file_path, mode="at") as volumes:
            if phone_number == "":
                volumes.write(F"{date}, {width}, {aspect_ration}, {diameter}, {volume:,.2f}\n")
            else:
                volumes.write(F"{date}, {width}, {aspect_ration}, {diameter}, {volume:,.2f}, {phone_number}\n")

if __name__=="__main__":

    TireVolumeCalculator().run()