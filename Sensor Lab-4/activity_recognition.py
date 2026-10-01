"""
Human Activity Recognition & Step Detection
Course: Sensors Laboratory (Experiment - 4)
Institution: IIT Madras
Author: Arpit Katiyar (Roll No: 24F1100064)

Description:
Processes 3-axis accelerometer data (Walking_on_Floor.csv, Climbing_up.csv, Climbing_down.csv)
using Physics Toolbox Sensor Suite Pro recordings.
Steps:
  1. Computes total acceleration magnitude: mag = sqrt(x^2 + y^2 + z^2)
  2. Applies a Moving Average (SMA) smoothing filter
  3. Detects peaks representing individual foot strikes (steps)
  4. Computes step frequency (cadence) and classifies the activity
"""

import os
import numpy as np
import pandas as pd
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

def analyze_activity(csv_path, min_peak_height=1.05, min_peak_distance=20, window_size=5, plot=False):
    filename = os.path.basename(csv_path)
    data = pd.read_csv(csv_path)
    time = data['time'].values
    x = data['x'].values
    y = data['y'].values
    z = data['z'].values

    # Step 1: Compute Acceleration Magnitude
    mag = np.sqrt(x**2 + y**2 + z**2)

    # Step 2: Smoothing with Moving Average Filter
    smooth_mag = np.convolve(mag, np.ones(window_size)/window_size, mode='same')

    # Step 3: Peak Detection
    peaks, properties = find_peaks(smooth_mag, height=min_peak_height, distance=min_peak_distance)
    step_count = len(peaks)

    # Step 4: Cadence & Step Frequency
    if step_count > 1:
        time_diff = np.diff(time[peaks])
        avg_step_time = np.mean(time_diff)
        step_frequency = 1.0 / avg_step_time if avg_step_time > 0 else 0.0
    else:
        avg_step_time = 0.0
        step_frequency = 0.0

    # Step 5: Activity Classification
    if step_frequency > 2.0:
        detected_activity = "Running"
    elif step_frequency > 1.5:
        detected_activity = "Climbing Stairs"
    elif step_frequency > 0.8:
        detected_activity = "Walking"
    else:
        detected_activity = "Slow Movement / Standing"

    print("=" * 60)
    print(f"File: {filename}")
    print(f"Total Duration: {time[-1] - time[0]:.2f} s")
    print(f"Step Count: {step_count}")
    print(f"Step Frequency: {step_frequency:.2f} steps/sec")
    print(f"Detected Activity: {detected_activity}")
    print("=" * 60)

    if plot:
        fig, axs = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
        
        # Plot Raw vs Smoothed
        axs[0].plot(time, mag, color='lightgray', label='Raw Magnitude')
        axs[0].plot(time, smooth_mag, color='blue', linewidth=1.5, label='Smoothed (SMA)')
        axs[0].plot(time[peaks], smooth_mag[peaks], 'ro', markersize=6, label=f'Steps ({step_count})')
        axs[0].set_ylabel('Acceleration (g)')
        axs[0].set_title(f'Step Detection: {filename} | {detected_activity} ({step_count} steps)')
        axs[0].legend(loc='upper right')
        axs[0].grid(True)

        # Plot 3-axis acceleration
        axs[1].plot(time, x, 'r', alpha=0.7, label='X-axis')
        axs[1].plot(time, y, 'g', alpha=0.7, label='Y-axis')
        axs[1].plot(time, z, 'b', alpha=0.7, label='Z-axis')
        axs[1].set_xlabel('Time (s)')
        axs[1].set_ylabel('Acceleration (g)')
        axs[1].set_title('Tri-axial Accelerometer Signals')
        axs[1].legend(loc='upper right')
        axs[1].grid(True)

        plt.tight_layout()
        plt.show()

    return {
        'file': filename,
        'step_count': step_count,
        'step_frequency': step_frequency,
        'activity': detected_activity
    }

if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    datasets = ['Walking_on_Floor.csv', 'Climbing_up.csv', 'Climbing_down.csv']

    print("Running Human Activity Recognition Analysis...\n")
    for ds in datasets:
        path = os.path.join(script_dir, ds)
        if os.path.exists(path):
            analyze_activity(path, plot=False)
