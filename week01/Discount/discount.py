# Author: Matthew D. Barker
# Date: 03/02/2025
# Class: CSE111

# Project: Discount

from sys import exit
from random import randint
from os import system
from os import name
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

class Discount:
    
    padding = 25    

    def run(self):
        
        day_of_week = datetime.today().weekday()

        #day_of_week = 2
        
        discount_day = (day_of_week == 1 or day_of_week == 2)

        center_padding = self.padding * 2

        while(True):

            Utilities.clear_screen()

            subtotal = Utilities.input_number("Please enter the subtotal: $", "Subtotal", True)

            if subtotal == 0:
                break

            discount = 0.0
            adjusted_subtotal = subtotal
        
            if discount_day and subtotal >= 50:
                discount = subtotal * 0.1
                adjusted_subtotal *= 0.9

            tax = adjusted_subtotal * .06

            total = adjusted_subtotal + tax

            Utilities.clear_screen()
            Utilities.spacing(2)


            Utilities.print_plus(F"{'Sub Total: '.ljust(self.padding, '.')}{F" ${subtotal:,.2f}".rjust(self.padding,'.')}", spacing_after=0)

            if discount > 0:
                Utilities.print_plus(F"{'Discount: '.ljust(self.padding, '.')}{F" - ${discount:,.2f}".rjust(self.padding,'.')}", spacing_after=0)


            Utilities.print_plus(F"{'Tax: '.ljust(self.padding, '.')}{F" ${tax:,.2f}".rjust(self.padding,'.')}", spacing_after=0)

            Utilities.print_plus(F"{'Total: '.ljust(self.padding, '.')}{F" ${total:,.2f}".rjust(self.padding,'.')}")

            Utilities.print_plus("Thank you for shopping with us!".center(center_padding))

            if discount_day and subtotal < 50:
                Utilities.print_plus(F"You were ${50 - subtotal:,.2f} away from a 10% discount.".center(center_padding))
            elif discount_day and subtotal >= 50:
                Utilities.print_plus(F"Congratulations!".center(center_padding), spacing_after=0)
                Utilities.print_plus(F"You received a ${discount:,.2f} discount today!".center(center_padding))
            elif not discount_day:
                Utilities.print_plus("Enjoy a 10% discount on Tuesdays and Wednesdays".center(center_padding), spacing_after=0)
                Utilities.print_plus("with a purchase of $50 or more.".center(center_padding))

            Utilities.press_space_continue()
       
        Utilities.print_plus("Have a blessed day!".center(center_padding),True ,2, 3)

if __name__=="__main__":

    Discount().run()

