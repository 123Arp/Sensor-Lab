%% Human Activity Recognition Using Smartphone Accelerometer
% Course: Sensors Laboratory (Experiment - 4)
% Institution: Indian Institute of Technology Madras (IIT Madras)
% Author: Arpit Katiyar (Roll No: 24F1100064)
%
% Description:
% Analyzes 3-axis accelerometer data recorded via Physics Toolbox Sensor Suite Pro
% to detect steps and classify human activity (Walking vs. Stair Climbing).

clc; clear; close all;

%% ---------------- STEP 1: SELECT & IMPORT DATA ----------------
% Options: 'Walking_on_Floor.csv', 'Climbing_up.csv', 'Climbing_down.csv'
dataFile = 'Climbing_up.csv'; 

fprintf('Loading data from: %s\n', dataFile);
data = readtable(dataFile);

time = data.time;
x = data.x;
y = data.y;
z = data.z;

%% ---------------- STEP 2: COMPUTE MAGNITUDE ----------------
mag = sqrt(x.^2 + y.^2 + z.^2);

%% ---------------- STEP 3: SMOOTHING (MOVING AVERAGE FILTER) ----------------
windowSize = 5;   % Moving average window length
smoothMag = movmean(mag, windowSize);

%% ---------------- STEP 4: PLOT RAW vs SMOOTHED ACCELERATION ----------------
figure('Name', 'Raw vs Smoothed Acceleration', 'NumberTitle', 'off');
plot(time, mag, 'Color', [0.7 0.7 0.7], 'DisplayName', 'Raw Magnitude'); 
hold on;
plot(time, smoothMag, 'b', 'LineWidth', 1.5, 'DisplayName', 'Smoothed Magnitude (SMA)');
title(sprintf('Raw vs Smoothed Acceleration Magnitude (%s)', dataFile), 'Interpreter', 'none');
xlabel('Time (s)');
ylabel('Acceleration (g)');
legend('show', 'Location', 'northeast');
grid on;

%% ---------------- STEP 5: PEAK DETECTION (STEP COUNTING) ----------------
minPeakHeight = 1.05;     % Acceleration threshold in g (~1 baseline gravity)
minPeakDistance = 20;     % Minimum sample distance between consecutive steps

[peaks, locs] = findpeaks(smoothMag, ...
    'MinPeakHeight', minPeakHeight, ...
    'MinPeakDistance', minPeakDistance);

step_count = length(peaks);

%% ---------------- STEP 6: PLOT DETECTED STEPS ----------------
figure('Name', 'Step Detection', 'NumberTitle', 'off');
plot(time, smoothMag, 'b', 'LineWidth', 1.2, 'DisplayName', 'Smoothed Signal'); 
hold on;
plot(time(locs), peaks, 'ro', 'MarkerFaceColor', 'r', 'MarkerSize', 6, 'DisplayName', 'Detected Steps');
title(sprintf('Step Detection: %s | Total Steps = %d', dataFile, step_count), 'Interpreter', 'none');
xlabel('Time (s)');
ylabel('Acceleration (g)');
legend('show', 'Location', 'northeast');
grid on;

%% ---------------- STEP 7: CADENCE & STEP FREQUENCY ----------------
if step_count > 1
    time_diff = diff(time(locs));   % Time between consecutive footfalls
    avg_step_time = mean(time_diff);
    step_frequency = 1 / avg_step_time;   % Steps per second (Hz)
else
    avg_step_time = 0;
    step_frequency = 0;
end

%% ---------------- STEP 8: ACTIVITY CLASSIFICATION ----------------
if step_frequency > 2.0
    activity = 'Running';
elseif step_frequency > 1.5
    activity = 'Climbing Stairs';
elseif step_frequency > 0.8
    activity = 'Walking';
else
    activity = 'Slow Movement / Standing';
end

%% ---------------- STEP 9: DISPLAY SUMMARY RESULTS ----------------
fprintf('\n==========================================\n');
fprintf('Activity Recognition Summary (%s)\n', dataFile);
fprintf('------------------------------------------\n');
fprintf('Duration               : %.2f s\n', time(end) - time(1));
fprintf('Total Steps Detected   : %d\n', step_count);
fprintf('Average Step Time      : %.3f s\n', avg_step_time);
fprintf('Step Frequency (Cadence): %.2f steps/sec\n', step_frequency);
fprintf('Classified Activity    : %s\n', activity);
fprintf('==========================================\n\n');

%% ---------------- STEP 10: TRI-AXIAL ACCELEROMETER SIGNALS ----------------
figure('Name', 'Tri-axial Accelerometer Signals', 'NumberTitle', 'off');
plot(time, x, 'r', 'LineWidth', 1, 'DisplayName', 'X-axis (Lateral)'); hold on;
plot(time, y, 'g', 'LineWidth', 1, 'DisplayName', 'Y-axis (Longitudinal)');
plot(time, z, 'b', 'LineWidth', 1, 'DisplayName', 'Z-axis (Vertical)');
title(sprintf('Tri-axial Accelerometer Data (%s)', dataFile), 'Interpreter', 'none');
xlabel('Time (s)');
ylabel('Acceleration (g)');
legend('show', 'Location', 'northeast');
grid on;
