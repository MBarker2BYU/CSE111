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

    csv_list = []

    for index in range(len(csv_row)):
        csv_list.append(csv_row[index])
    
    return csv_list


def read_dictionary(filename, key_column_index=0):

    file_path = F"{Utilities.get_current_directory()}\{filename}"

    if not os.path.isfile(file_path):
        return None

    csv_file = {}

    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        csv_data = list(csv_reader)

        for csv_row in csv_data:
            csv_file[csv_row[key_column_index]] = to_list(csv_row)

    return csv_file  

def main():
    
    products = read_dictionary("products.csv")
    
    

if __name__ == "__main__":
    main()