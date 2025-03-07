# Author: Matthew D. Barker
# Date: Mar 06, 2025
# Description: Milestone: Water Pressure

from os import system, name

WATER_DENSITY = 998.2000000
EARTH_ACCELERATION_OF_GRAVITY = 9.8066500
WATER_DYNAMIC_VISCOSITY = 0.0010016

#Safe Division (Check for division by zero)
def safe_division_float(dividend, divisor):

    if(divisor == 0.0):
        return 0.0
    
    return float(dividend / divisor)


def water_column_height(tower_height, tank_height):
   
    return tower_height + (3 * safe_division_float(tank_height, 4))


def pressure_gain_from_water_height(height):

    return WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * safe_division_float(height, 1000)


def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    
    pressure = safe_division_float(-(friction_factor * pipe_length * WATER_DENSITY * fluid_velocity**2), (2000 * pipe_diameter))
    
    #do not return a -0.0
    return pressure if abs(pressure) else 0.0    


def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    
    pressure = -0.04 * WATER_DENSITY * fluid_velocity**2 * safe_division_float(quantity_fittings, 2000)

    #do not return a -0.0
    return pressure if abs(pressure) else 0.0


def reynolds_number(hydraulic_diameter, fluid_velocity):
    
    return safe_division_float(WATER_DENSITY * hydraulic_diameter * fluid_velocity,  WATER_DYNAMIC_VISCOSITY)


def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    
    k = (0.1 + safe_division_float(50 , reynolds_number)) * ( safe_division_float(larger_diameter, smaller_diameter)**4 - 1)
    
    pressure = safe_division_float(-(k * WATER_DENSITY * fluid_velocity**2), 2000)

    #do not return a -0.0
    return pressure if abs(pressure) else 0.0 

# Convert kPa to psi
def kpa_to_psi(kpa):

    return kpa / 6.895

#***********************************************************************
# -- Provided Code --
#***********************************************************************

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)

def clear_screen():

    system("cls" if name == "nt" else "clear")

def spacing(lines = 1):

        for _ in range(lines):
            print("")

def main():

    # Cleaner Look
    clear_screen()
    spacing(2)

    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    spacing()

    print(f"Pressure at house: {pressure:.1f} kilopascals ({kpa_to_psi(pressure):,.1f} psi)")

    # Cleaner Look
    spacing(2)


if __name__ == "__main__":
    main()