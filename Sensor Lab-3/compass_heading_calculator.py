"""
Electronic Compass Heading Angle Computation
Course: Sensors Laboratory (Experiment - 3)
Institution: Indian Institute of Technology Madras (IIT Madras)
Author: Arpit Katiyar (Roll No: 24F1100064)

Description:
Computes heading direction angle (theta) from orthogonally oriented
Hall Effect Sensors (SS49) after amplification by difference amplifiers.
Calculates heading: theta = atan2(Vy - Voffset_y, Vx - Voffset_x) * (180 / pi)
"""

import math
import numpy as np

def compute_heading(vx, vy, voffset_x=2.5, voffset_y=2.5):
    """
    Computes azimuth heading angle in degrees (0 deg to 360 deg)
    vx: Voltage output from X-axis Hall amplifier
    vy: Voltage output from Y-axis Hall amplifier
    voffset_x: Quiescent DC offset voltage for X channel
    voffset_y: Quiescent DC offset voltage for Y channel
    """
    delta_x = vx - voffset_x
    delta_y = vy - voffset_y

    heading_rad = math.atan2(delta_y, delta_x)
    heading_deg = math.degrees(heading_rad)
    if heading_deg < 0:
        heading_deg += 360.0

    # Determine Cardinal direction
    directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                  "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    idx = int((heading_deg + 11.25) / 22.5) % 16
    cardinal = directions[idx]

    return heading_deg, cardinal

if __name__ == '__main__':
    print("Electronic Compass Simulation Test:")
    print("--------------------------------------------------")
    print("Angle (deg) | Vx (V)   | Vy (V)   | Calculated | Cardinal")
    print("--------------------------------------------------")
    
    # Emulate rotating compass every 20 degrees
    v_ref = 2.5
    v_amp = 0.5  # Amplified magnetic swing around V_ref
    
    for true_angle in range(0, 360, 20):
        rad = math.radians(true_angle)
        vx = v_ref + v_amp * math.cos(rad)
        vy = v_ref + v_amp * math.sin(rad)
        calc_deg, card = compute_heading(vx, vy, voffset_x=v_ref, voffset_y=v_ref)
        print(f"{true_angle:10d}° | {vx:8.4f} | {vy:8.4f} | {calc_deg:9.2f}° | {card}")
    print("--------------------------------------------------")
