import tkinter as tk
from tkinter import ttk, messagebox
import math

"""This module provides a set of utility functions for creating and managing a Tkinter GUI."""
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

class BallisticCalculator:
    
    FEET_PER_METER = 3.28084  # Conversion factor from meters to feet
    GRAVITY_METERS_PER_SECOND = 9.80665  # Acceleration due to gravity (m/s^2)
    GRAVITY_FEET_PER_SECOND = round(GRAVITY_METERS_PER_SECOND * FEET_PER_METER, 3)  # Acceleration due to gravity (ft/s^2)   
    GRAINS_PER_LBS = 7000  # Grains per pound
    COEFFICIENT_OF_DRAG_FACTOR = 0.0005  # Coefficient of drag for a bullet
    WIND_SPEED_CONVERSION = 1.46667  # Conversion factor from mph to fps

    def create_window(self):
        # Create the main window
        self.window = WindowSupport.create_window("Ballistics Calculator", 300, 475, False, False)
        
        # Add input fields with labels
        y_pos = 20
        self.entries = {}
        
        # Muzzle Velocity (fps)
        WindowSupport.Add_label(self.window, "Muzzle Velocity (fps):", 20, y_pos)
        self.entries['velocity'] = WindowSupport.Add_entry(self.window, 150, y_pos)
        self.entries['velocity'].insert(0, "3000")
        y_pos += 40
        
        # Bullet Weight (grains)
        WindowSupport.Add_label(self.window, "Bullet Weight (grains):", 20, y_pos)
        self.entries['weight'] = WindowSupport.Add_entry(self.window, 150, y_pos)
        self.entries['weight'].insert(0, "150")
        y_pos += 40
        
        # Ballistic Coefficient
        WindowSupport.Add_label(self.window, "Ballistic Coefficient:", 20, y_pos)
        self.entries['bc'] = WindowSupport.Add_entry(self.window, 150, y_pos)
        self.entries['bc'].insert(0, "0.45")
        y_pos += 40
        
        # Distance (yards)
        WindowSupport.Add_label(self.window, "Distance (yards):", 20, y_pos)
        self.entries['distance'] = WindowSupport.Add_entry(self.window, 150, y_pos)
        self.entries['distance'].insert(0, "100")
        y_pos += 40
        
        # Wind Speed (mph)
        WindowSupport.Add_label(self.window, "Wind Speed (mph):", 20, y_pos)
        self.entries['wind_speed'] = WindowSupport.Add_entry(self.window, 150, y_pos)
        self.entries['wind_speed'].insert(0, "10")
        y_pos += 40
        
        # Wind Angle (degrees)
        WindowSupport.Add_label(self.window, "Wind Angle (degrees):", 20, y_pos)
        self.entries['wind_angle'] = WindowSupport.Add_entry(self.window, 150, y_pos)
        self.entries['wind_angle'].insert(0, "90")
        y_pos += 40
        
        # Sight Height (inches)
        WindowSupport.Add_label(self.window, "Sight Height (inches):", 20, y_pos)
        self.entries['sight_height'] = WindowSupport.Add_entry(self.window, 150, y_pos)
        self.entries['sight_height'].insert(0, "1.5")
        y_pos += 60
        
        # Calculate Button
        WindowSupport.Add_button(self.window, "Calculate", self.calculate, 150, y_pos)
        y_pos += 40
        
        # Results Labels
        self.drop_label = WindowSupport.Add_label(self.window, "Bullet Drop: ", 20, y_pos)
        y_pos += 20
        self.drift_label = WindowSupport.Add_label(self.window, "Wind Drift: ", 20, y_pos)
        y_pos += 20
        self.velocity_label = WindowSupport.Add_label(self.window, "Velocity at Target: ", 20, y_pos)
        y_pos += 20
        self.energy_muzzle_label = WindowSupport.Add_label(self.window, "Muzzle Energy: ", 20, y_pos)
        y_pos += 20
        self.energy_target_label = WindowSupport.Add_label(self.window, "Energy at Target: ", 20, y_pos)
        
        # Start the main loop
        self.window.mainloop()
    
    def get_distance_feet(self, distance_in_yards):
        """Convert yards to feet."""
        return distance_in_yards * 3

    def get_wind_speed_fps(self, wind_speed_mph):
        """Convert wind speed from mph to feet per second."""
        return wind_speed_mph * self.WIND_SPEED_CONVERSION

    def get_weight_lbs(self, weight_in_grains):
        """Convert weight from grains to pounds."""
        return weight_in_grains / self.GRAINS_PER_LBS

    def get_drag_factor(self, coefficient):
        """Calculate the drag factor."""
        drag_factor = self.COEFFICIENT_OF_DRAG_FACTOR / coefficient

        return drag_factor

    def get_velocity_at_target(self, velocity, distance_in_feet, drag_factor):
        """Calculate the velocity at the target."""
        return velocity * math.exp(-drag_factor * distance_in_feet)

    def get_flight_time(self, distance_in_feet, velocity, velocity_at_target):
        """Calculate the time of flight."""    
        return distance_in_feet / ((velocity + velocity_at_target) / 2)

    def get_bullet_drop(self, flight_time, sight_height):
        """Calculate the bullet drop."""
        drop_feet = 0.5 * self.GRAVITY_FEET_PER_SECOND * flight_time ** 2
        drop_inches = drop_feet * 12 - sight_height  # Convert feet to inches

        return drop_inches

    def get_wind_drift(self, wind_speed_fps, wind_angle, flight_time):
        """Calculate the wind drift."""
        wind_component = wind_speed_fps * math.sin(math.radians(wind_angle))
        drift_feet = wind_component * flight_time
        drift_inches = drift_feet * 12
        
        return drift_inches

    def get_muzzle_energy(self, velocity, weight_lbs):
        """Calculate the muzzle energy."""
        muzzle_energy = (0.5 * weight_lbs * velocity ** 2) / self.GRAVITY_FEET_PER_SECOND 

        return muzzle_energy

    def get_target_energy(self, velocity_at_target, weight_lbs):
        """Calculate the energy at the target."""

        target_energy = (0.5 * weight_lbs * velocity_at_target ** 2) / self.GRAVITY_FEET_PER_SECOND

        return target_energy

    def calculate(self):
        """Calculate the ballistic properties."""
        try:
            # Get input values from the entries
            velocity = float(self.entries['velocity'].get())
            weight = float(self.entries['weight'].get())
            bc = float(self.entries['bc'].get())
            distance = float(self.entries['distance'].get())
            wind_speed = float(self.entries['wind_speed'].get())
            wind_angle = float(self.entries['wind_angle'].get())
            sight_height = float(self.entries['sight_height'].get())

            #Perform calculations

            distance_feet = self.get_distance_feet(distance)
            wind_speed_fps = self.get_wind_speed_fps(wind_speed)
            weight_lbs = self.get_weight_lbs(weight)

            drag_factor = self.get_drag_factor(bc)
            velocity_at_target = self.get_velocity_at_target(velocity, distance_feet, drag_factor)
            flight_time = self.get_flight_time(distance_feet, velocity, velocity_at_target)
            bullet_drop = self.get_bullet_drop(flight_time, sight_height)
            wind_drift = self.get_wind_drift(wind_speed_fps, wind_angle, flight_time)
            energy_muzzle = self.get_muzzle_energy(velocity, weight_lbs)
            energy_target = self.get_target_energy(velocity_at_target, weight_lbs)

            # Update labels with results
            self.drop_label.config(text=f"Bullet Drop: {bullet_drop:.2f} ft")
            self.drift_label.config(text=f"Wind Drift: {wind_drift:.2f} ft")
            self.velocity_label.config(text=f"Velocity at Target: {velocity_at_target:.2f} fps")
            self.energy_muzzle_label.config(text=f"Muzzle Energy: {energy_muzzle:.2f} ft-lbs")
            self.energy_target_label.config(text=f"Energy at Target: {energy_target:.2f} ft-lbs")

        except ValueError:
            WindowSupport.show_message("Input Error", "Please enter valid numerical values.")

    def run(self):
        self.create_window()

if __name__ == "__main__":
    # Example usage of the BallisticCalculator class
    BallisticCalculator().run()
    
    

