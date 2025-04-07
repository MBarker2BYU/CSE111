from math import pi as PI, sqrt as SQRT
import tkinter as tk
from tkinter import messagebox

GRAVITY = 9.81  # Acceleration due to gravity in m/s^2

class WindowSupport:

    @staticmethod
    def create_window(title, width=300, height=200, allow_resize_width=True, allow_resize_height=True, center_window=True):
        """Create a Tkinter window with the specified title and size."""
        window = tk.Tk()
        window.title(title)
        window.resizable(allow_resize_width, allow_resize_height)
        window.geometry(f"{width}x{height}")
        
        if center_window == True:
            WindowSupport.center_window(window)

        return window
    
    @staticmethod
    def Add_label(window, text, x=0, y=0):
        """Add a label to the window."""
        label = tk.Label(window, text=text)
        label.place(x=x, y=y)

        return label

    @staticmethod
    def Add_entry(window, x=0, y=0):
        """Add an entry field to the window."""
        entry = tk.Entry(window)
        entry.place(x=x, y=y)

        return entry

    @staticmethod
    def add_combobox(window, values, x=0, y=0):
        """Add a combobox to the window."""
        combobox = tk.ttk.Combobox(window, values=values)
        combobox.place(x=x, y=y)

        return combobox

    @staticmethod
    def Add_button(window, text, command, x=0, y=0):
        """Add a button to the window."""
        button = tk.Button(window, text=text, command=command)
        button.place(x=x, y=y)

        return button

    @staticmethod
    def get_widget_size(widget):
        """Get the size of a widget."""

        width = widget.winfo_width()
        height = widget.winfo_height()

        return (width, height)

    @staticmethod
    def center_window(window):
        """Center the window on the screen."""
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")

    @staticmethod
    def show_message(title, message):
        """Show a message box."""
        messagebox.showinfo(title, message)

class PendulumSwingCalculator:

    def __init__(self):
        
        """Initialize the calculator."""
        self.window = WindowSupport.create_window("Pendulum Swing Calculator", 300, 200, allow_resize_width=False, allow_resize_height=False, center_window=True)
        

        # Create input fields
        WindowSupport.Add_label(self.window, "Length (m):", 20, 20)
        self.length_entry = WindowSupport.Add_entry(self.window, 120, 20)

        WindowSupport.Add_label(self.window, "Angle (degrees):", 20, 60)
        self.angle_entry = WindowSupport.Add_entry(self.window, 120, 60)

        WindowSupport.Add_label(self.window, "Mass (kg):", 20, 100)
        self.mass_entry = WindowSupport.Add_entry(self.window, 120, 100)

        # Create buttons
        WindowSupport.Add_button(self.window, "Calculate", self.calculate_pendulum_properties, 20, 140)
        WindowSupport.Add_button(self.window, "Clear", self.clear_fields, 120, 140)

    def calculate_pendulum_properties(self):
        """Calculate the properties of the pendulum."""
        try:
            self.length = float(self.length_entry.get())
            self.angle = float(self.angle_entry.get())
            self.mass = float(self.mass_entry.get())

            period = self.calculate_period()
            energy = self.calculate_energy()
            velocity = self.calculate_velocity()
            acceleration = self.calculate_acceleration()
            kinetic_energy = self.calculate_kinetic_energy()

            # Display results
            result_message = (
                f"Period: {period:.2f} s\n"
                f"Potential Energy: {energy:.2f} J\n"
                f"Velocity: {velocity:.2f} m/s\n"
                f"Acceleration: {acceleration:.2f} m/s²\n"
                f"Kinetic Energy: {kinetic_energy:.2f} J"
            )
            WindowSupport.show_message("Pendulum Properties", result_message)

        except ValueError:
            WindowSupport.show_message("Input Error", "Please enter valid numerical values.")


    def calculate_period(self):
        """Calculate the period of the pendulum."""
        return 2 * PI * SQRT(self.length / GRAVITY)

    def calculate_energy(self):
        """Calculate the potential energy of the pendulum."""
        height = self.length * (1 - SQRT(1 - (self.angle / 180) ** 2))
        return self.mass * GRAVITY * height

    def calculate_velocity(self):
        """Calculate the velocity of the pendulum at the lowest point."""
        return SQRT(2 * GRAVITY * self.length * (1 - SQRT(1 - (self.angle / 180) ** 2)))

    def calculate_acceleration(self):
        """Calculate the acceleration of the pendulum at the lowest point."""
        return GRAVITY * SQRT(1 - (self.angle / 180) ** 2)

    def calculate_kinetic_energy(self): 
        """Calculate the kinetic energy of the pendulum at the lowest point."""
        velocity = self.calculate_velocity()
        return 0.5 * self.mass * velocity ** 2
    
    def clear_fields(self):
        """Clear the input fields."""
        self.length_entry.delete(0, 'end')
        self.angle_entry.delete(0, 'end')
        self.mass_entry.delete(0, 'end')
        self.length_entry.focus_set()

    def run(self):
        """Run the calculator."""
        self.window.mainloop()            

if __name__ == "__main__":
    calculator = PendulumSwingCalculator()
    calculator.run()
