"""
Instrumentation Amplifier (INA) Gain & CMRR Analysis
Course: Sensors Laboratory (Experiment - 1)
Institution: Indian Institute of Technology Madras (IIT Madras)
Author: Arpit Katiyar (Roll No: 24F1100064)

Description:
Derives and calculates differential gain (Ad), resistor values (Rg),
common-mode gain (Ac), and CMRR for the 3-opamp INA.
Formula:
  Ad = 1 + (2 * R / Rg)   [where R1 = R2 = Rf = R]
"""

import math

def calculate_rg(ad, r=10000.0):
    """
    Computes required Rg for desired differential gain Ad
    when R1 = R2 = Rf = R
    """
    if ad <= 1.0:
        raise ValueError("Differential gain Ad must be strictly greater than 1.")
    return (2.0 * r) / (ad - 1.0)

def calculate_cmrr(ad, ac):
    """
    Computes CMRR in dB: CMRR = 20 * log10(|Ad / Ac|)
    """
    if ac == 0:
        return float('inf')
    return 20.0 * math.log10(abs(ad / ac))

if __name__ == '__main__':
    print("3-OpAmp Instrumentation Amplifier (INA) Design Calculations")
    print("=" * 60)
    r_val = 10000.0  # 10 kOhm
    gains = [3, 5, 10, 20, 50, 100]

    print(f"Base Resistors (R1 = R2 = Rf = R): {r_val/1000:.1f} kΩ\n")
    print("Desired Gain (Ad) | Calculated Rg (Ω) | Nearest Standard Value")
    print("-" * 60)
    for g in gains:
        rg = calculate_rg(g, r=r_val)
        print(f"{g:16d} | {rg:16.1f} | ~{rg:.0f} Ω")

    print("\nCMRR Example Calculation:")
    ad_test = 20.0
    ac_test = 0.002
    cmrr_db = calculate_cmrr(ad_test, ac_test)
    print(f"For Ad = {ad_test} and Ac = {ac_test}: CMRR = {cmrr_db:.2f} dB")
    print("=" * 60)
