# Author: Matthew D. Barker
# Date: Mar 06, 2025
# Description: Milestone: Water Pressure

DENSITY = 998.2
GRAVITY = 9.80665

def water_column_height(tower_height, tank_height):
    
    return tower_height + 3 * tank_height / 4
 
def pressure_gain_from_water_height(height):

    return DENSITY * GRAVITY * height / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):

    if pipe_diameter == 0:
        return 0.0
    
    result = -(friction_factor * pipe_length * DENSITY * fluid_velocity**2) / (2000 * pipe_diameter)
    
    #do not return a -0.0
    return result if abs(result) else 0.0    