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
    
    students = read_dictionary("students.csv")

    while(True):

        Utilities.clear_screen()
        
        print()
        response = input("What I-Number(xx-xxx-xxxx) do you want to lookup?")

        response = response.replace("-", "")

        if not response.isdigit():
            print("Invalid I-Number")
        else:
            if len(response) < 9:
                print("Invalid I-Number: too few digits")
            elif len(response) > 9:
                print("Invalid I-Number: too many digits")
            else:
                if response in students:
                    student = students[response]
                    print(student[1])                    
                else:
                    print("No such student")
            
        if not Utilities.yes_no_prompt("Would you like to lookup another I-Number? (y/n)"):
            break

    Utilities.clear_screen()

    print()
    print()
    print("Have a blessed day!")
    print()
    print()

if __name__ == "__main__":
    main()