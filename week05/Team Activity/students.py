import os
import csv
import tkinter as tk
from tkinter import ttk, messagebox


class Utilities:
    
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

def on_search():
    
    number = i_number.get()

    number = number.replace("-", "")

    if not number.isdigit():
        messagebox.showerror("Error", F"'{i_number.get()}' is an invalid I-Number.")
    else:
        if len(number) < 9:
            messagebox.showerror("Error","Invalid I-Number: too few digits")
        elif len(number) > 9:
            messagebox.showerror("Error","Invalid I-Number: too many digits")
        else:
            if number in students:
                student = students[number]
                student_name.set(F"Student Name: {student[1]}")                    
            else:
                student_name.set("Student Name: No such student")




def get_screen_size(window):
    return (window.winfo_screenwidth(), window.winfo_screenheight())

def size_and_center_window(window, width=600, height=400):
    
    window.geometry(F"{width}x{height}")

    screen_size = get_screen_size(window)
    
    x = (screen_size[0] / 2) - (width / 2)
    y = (screen_size[1] / 2) - (height / 2)

    main_window.geometry(F"+{int(x)}+{int(y)}")

def on_window_load():

    global students
    students = read_dictionary("students.csv")

    print(len(students))


students = None

main_window = tk.Tk()
main_window.title("Student Lookup")
main_window.after(1, on_window_load)
main_window.resizable(False, False)

size_and_center_window(main_window, 400, 150)

prompt_label = ttk.Label(master=main_window, text="Please enter an I-Number (xx-xxx-xxxx):", 
                         font=("Comic Sans MS", 14), anchor="w", justify="left")
prompt_label.pack()

input_frame = ttk.Frame(master=main_window)

i_number = tk.StringVar()
text_box = ttk.Entry(master=input_frame, width=30, justify="center", textvariable=i_number)
lookup_button = ttk.Button(master=input_frame, text="Search", command=on_search)

text_box.pack(side="left")
lookup_button.pack(side="left")
input_frame.pack(pady=10)

student_name = tk.StringVar()
student_label = ttk.Label(master=main_window, width=50, font=("Comic Sans MS", 14), textvariable=student_name)
student_label.pack(padx=10)

main_window.mainloop()