from os import system, name
import os
import csv

class Utilities:
    
    def clear_screen():
        system("cls" if name == "nt" else "clear")

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

    # file_path = F"{Utilities.get_current_directory()}\{filename}"

    if not os.path.isfile(filename):
        return None

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
        return None

    csv_file = []

    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        csv_data = list(csv_reader)

        for csv_row in csv_data:
            csv_file.append(to_list(csv_row))

    return csv_file

def main():
    
    file_path = F"{Utilities.get_current_directory()}\\products.csv"
    
    products = read_dictionary(file_path)
    
    file_path = F"{Utilities.get_current_directory()}\\request.csv"

    requests = read_to_list(file_path)

    Utilities.clear_screen()
    print()
    print()
    print(products)
    print()
    print()

    for request in requests:
        product_id = request[0]
        quantity = int(request[1])

        if product_id in products:
            product_name = products[product_id][1]
            price = products[product_id][2]

            print(f"Product: {product_name}, Quantity: {quantity}, Price: {price}")

        else:
            print(f"Product ID {product_id} not found.")



if __name__ == "__main__":
    main()