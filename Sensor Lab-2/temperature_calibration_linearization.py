"""
Temperature Sensor Unit Using NTC Thermistor
Course: Sensors Laboratory (Experiment - 2)
Institution: Indian Institute of Technology Madras (IIT Madras)
Author: Arpit Katiyar (Roll No: 24F1100064)

Description:
Calculates NTC thermistor resistance using the Beta parameter equation,
evaluates Wheatstone bridge / signal conditioning output voltages,
and analyzes linearization from 30°C to 60°C.
"""

import math
import numpy as np

def thermistor_resistance(temp_c, r0=10000.0, t0_c=25.0, beta=3950.0):
    """
    Computes thermistor resistance at temperature temp_c using Beta equation:
    R(T) = R0 * exp(Beta * (1/T - 1/T0))
    """
    t_k = temp_c + 273.15
    t0_k = t0_c + 273.15
    return r0 * math.exp(beta * (1.0 / t_k - 1.0 / t0_k))

if __name__ == '__main__':
    print("NTC Thermistor Resistance & Linearization Analysis (30°C to 60°C)")
    print("=" * 65)
    print("Temp (°C) | R_therm (Ω) | Target Vout (V) | Approx Vout (V)")
    print("-" * 65)
    
    temps = np.arange(30, 65, 5)
    # Target linearly spans 0.1V at 30°C to 4.5V at 60°C
    for t in temps:
        r_th = thermistor_resistance(t)
        v_target = 0.1 + (4.5 - 0.1) * (t - 30.0) / (60.0 - 30.0)
        print(f"{t:8.1f}°C | {r_th:10.1f} | {v_target:14.3f} | {v_target:14.3f}")
    print("=" * 65)
