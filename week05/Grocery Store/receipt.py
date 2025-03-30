from os import system, name
from datetime import datetime, timedelta
from random import randint
import os
import csv

class Utilities:
    
    def clear_screen():
        system("cls" if name == "nt" else "clear")

    def spacing(count=1):
        for _ in range(count):
            print()

    def print_plus(values, clear_screen=False, leading_space=0, trailing_space=0):
        """
        Prints the given values to the console with optional formatting and screen clearing.
        Args:
            values (str): The content to be printed.
            clear_screen (bool, optional): If True, clears the console screen before printing. Defaults to False.
            leading_space (int, optional): The number of blank lines to add before printing the values. Defaults to 0.
            trailing_space (int, optional): The number of blank lines to add after printing the values. Defaults to 0.
        Returns:
            None
        """

        if clear_screen:
            Utilities.clear_screen()
        
        Utilities.spacing(leading_space)

        print(values)

        Utilities.spacing(trailing_space)

    def yes_no_prompt(prompt):
        print(prompt)
        return input().strip().lower() == 'y'
    
    def get_current_directory():
        return os.path.dirname(os.path.realpath(__file__))

def to_list(csv_row):
    """
    Convert a CSV row into a list.
    This function takes a row of data in CSV format (e.g., a list-like object)
    and converts it into a standard Python list by iterating through its elements.
    Parameters:
        csv_row (iterable): An iterable representing a row of CSV data.
    Returns:
        list: A list containing the elements of the input CSV row.
    """

    csv_list = []

    for index in range(len(csv_row)):
        csv_list.append(csv_row[index])
    
    return csv_list


def read_dictionary(filename, key_column_index=0):
    """
    Reads a CSV file and converts its contents into a dictionary.
    Args:
        filename (str): The name of the CSV file to read.
        key_column_index (int, optional): The index of the column to use as keys 
            for the dictionary. Defaults to 0.
    Returns:
        dict or None: A dictionary where the keys are values from the specified 
        column and the values are lists representing the rows of the CSV file. 
        Returns None if the file does not exist.
    """
    
    if not os.path.isfile(filename):
        raise FileNotFoundError(filename)

    csv_file = {}

    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        csv_data = list(csv_reader)

        for csv_row in csv_data:
            csv_file[csv_row[key_column_index]] = to_list(csv_row)

    return csv_file  
    

def read_to_list(filename):
    """
    Reads a CSV file and converts its contents into a list.
    Args:
        filename (str): The name of the CSV file to read.
    Returns:
        list: A list of lists, where each inner list represents a row of the CSV file.
    """
            
    if not os.path.isfile(filename):
        raise FileNotFoundError(filename)

    csv_file = []

    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        csv_data = list(csv_reader)

        for csv_row in csv_data:
            csv_file.append(to_list(csv_row))

    return csv_file

def days_until_new_years_sale(date):
    """
    Calculates the number of days until New Year's Sale.
    Args:
        date (datetime): The current date.
    Returns:
        int: The number of days until New Year's Sale.
    """
    
    new_years_sale = datetime(date.year + 1, 1, 1)
    return (new_years_sale - date).days if date < new_years_sale else 0
    
def return_by(date, days = 30):
    
    return_date = date + timedelta(days=days)

    return F"{return_date.replace(hour=21, minute=0, second=0, microsecond=0):%a %I:%M %p %m/%d/%y}" 
   
def product_bogo_discount(quantity, price):
    
    promotion = quantity // 2
    
    return promotion * price

def coupon_discount(product_name, discount=15):
    
    return F"{discount:.0f}% off your next purchase of {product_name}!"

def print_receipt(products, requests):
    
    """
    Prints a receipt based on the products and requests.
    Args:
        products (dict): A dictionary of products with their details.
        requests (list): A list of requests, each containing product information.
    """
    
    total_items = 0
    sub_total_price = 0.0

    bogo_item = 'D083'
    bogo_name = ""
    bogo_item_count = 0
    bogo_item_price = 0.0
    
    Utilities.clear_screen()

    Utilities.print_plus("J & S Farms".center(50, " "), leading_space=2, trailing_space=2)
       

    request_index = randint(0, len(requests) - 1)

    for request in requests:
        product_id = request[0]
        quantity = int(request[1])

        total_items += quantity
        
        if product_id in products:
            product = products[product_id]
            product_name = product[1]
            price = float(product[2])

            sub_total_price += quantity * price

            if bogo_item == product_id:
                bogo_name = product_name
                bogo_item_count += quantity
                bogo_item_price = price

            print(F"{F"{product_name}".ljust(25,".")}{F"{quantity} x ${price:.2f}".rjust(25, ".")}")

        else:
            raise KeyError(F"Product ID {product_id} not found in products.")

    print("." * 50)
    Utilities.spacing()
    print(F"Number of Items: {total_items}".center(50, " "))
    Utilities.spacing()

    tax_rate = 0.06

    Utilities.print_plus(F"BOGO discount on {product_name}s!".format(bogo_name).center(50, " "), trailing_space=2)

    print(F"{F"Subtotal: ".rjust(40, " ")}{F"${sub_total_price:.2f}".rjust(10, " ")}")

    discount = product_bogo_discount(bogo_item_count, bogo_item_price)

    print(F"{F"Discount: ".rjust(40, " ")}{F"-${discount:.2f}".rjust(10, " ")}")

    sub_total_price -= discount

    print(F"{F"Subtotal: ".rjust(40, " ")}{F"${sub_total_price:.2f}".rjust(10, " ")}")
    print(F"{F"Tax: ".rjust(40, " ")}{F"${sub_total_price * tax_rate:.2f}".rjust(10, " ")}")
    print(F"{F"Total: ".rjust(40, " ")}{F"${sub_total_price * (1 + tax_rate):.2f}".rjust(10, " ")}")
    
    Utilities.spacing(2)
    print("Thank you for shopping with us!".center(50, " "))
    Utilities.spacing()
      
    current_date_and_time = datetime.now()
    print(f"Today: {current_date_and_time:%A %I:%M %p}".center(50, " "))
    Utilities.print_plus(F"Items returnable until {return_by(current_date_and_time)}".center(50, " "), trailing_space=2)
    
    Utilities.print_plus(F"{days_until_new_years_sale(current_date_and_time)} days left until our New Years Sale!".center(50, " "))
    
    p_id = requests[request_index][0]
    p = products[p_id]

    Utilities.print_plus(F"{coupon_discount(p[1], 15)}".center(50, " "), trailing_space=2)
  
def process_application_exception(exception):
    """
    Handle and display information about an exception that occurred in the application.
    This function takes an exception as input and prints a user-friendly message
    describing the type of exception and its details. It also clears the screen
    and formats the output for better readability.
    Args:
        exception (Exception): The exception object to process.
    Behavior:
        - If the exception is a KeyError, it prints a message indicating a key error.
        - If the exception is a FileNotFoundError, it prints a message indicating a missing file.
        - If the exception is a PermissionError, it prints a message indicating a permission issue.
        - For any other exception, it prints a generic error message.
    Note:
        This function relies on the `Utilities.print_plus` method for formatted output.
    """

    Utilities.print_plus(F"The application has encountered the following exception and will shutdown.", clear_screen=True, leading_space=2, trailing_space=1)

    if isinstance(exception, KeyError):
        Utilities.print_plus(f"Key error: {exception}", trailing_space=2)
    elif isinstance(exception, FileNotFoundError):
        Utilities.print_plus(F"File not found: {exception}", trailing_space=2)
    elif isinstance(exception, PermissionError):
        Utilities.print_plus(F"Permission denied: {exception}", trailing_space=2)
    else:
        Utilities.print_plus(f"An error occurred: {exception}", trailing_space=2)

def main():
    
    try:

        file_path = F"{Utilities.get_current_directory()}\\products.csv"
        products = read_dictionary(file_path)
        
        file_path = F"{Utilities.get_current_directory()}\\request.csv"
        requests = read_to_list(file_path)

        print_receipt(products, requests)

    except Exception as exception:
        process_application_exception(exception)       

if __name__ == "__main__":
    main()