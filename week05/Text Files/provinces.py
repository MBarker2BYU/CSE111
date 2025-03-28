from os import system, name
import os

class Utilities:
    
    def clear_screen():
        system("cls" if name == "nt" else "clear")

    def yes_no_prompt(prompt):
        print(prompt)
        return input().strip().lower() == 'y'
    
    def get_current_directory():
        return os.path.dirname(os.path.realpath(__file__))

def load_provinces():

    provinces = []

    with open(F"{Utilities.get_current_directory()}\\provinces.txt", 'r') as file:
        for line in file:
            provinces.append(line.strip())

    return provinces




def main():

    ALBERTA = 'Alberta'

    provinces = load_provinces()

    Utilities.clear_screen()

    print(provinces)

    provinces.pop(0)
    provinces.pop(len(provinces) - 1)

    for index in range(len(provinces)):
        if provinces[index] == 'AB':
            provinces[index] = ALBERTA

    print(F"{ALBERTA} occurs {provinces.count(ALBERTA)} times int the modified list.")

if __name__ == "__main__":
    main()