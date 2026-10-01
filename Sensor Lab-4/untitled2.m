clc; clear; close all;

%% ---------------- STEP 1: IMPORT DATA ----------------
data = readtable('Climbing_up.csv');

time = data.time;
x = data.x;
y = data.y;
z = data.z;

%% ---------------- STEP 2: COMPUTE MAGNITUDE ----------------
mag = sqrt(x.^2 + y.^2 + z.^2);

%% ---------------- STEP 3: SMOOTHING (MOVING AVERAGE) ----------------
windowSize = 5;   % you can tune this
smoothMag = movmean(mag, windowSize);

%% ---------------- STEP 4: PLOT RAW vs SMOOTH ----------------
figure;
plot(time, mag, 'Color', [0.7 0.7 0.7]); hold on;
plot(time, smoothMag, 'b', 'LineWidth', 1.5);
title('Raw vs Smoothed Acceleration Magnitude');
xlabel('Time (s)');
ylabel('Acceleration (g)');
legend('Raw', 'Smoothed');
grid on;

%% ---------------- STEP 5: PEAK DETECTION (STEP COUNT) ----------------
% Tune these values based on your data
minPeakHeight = 1.05;     % since your data is in g (~1 baseline)
minPeakDistance = 20;     % depends on sampling rate

[peaks, locs] = findpeaks(smoothMag, ...
    'MinPeakHeight', minPeakHeight, ...
    'MinPeakDistance', minPeakDistance);

step_count = length(peaks);

%% ---------------- STEP 6: PLOT PEAKS ----------------
figure;
plot(time, smoothMag, 'b'); hold on;
plot(time(locs), peaks, 'ro', 'MarkerSize', 8);
title(['Step Detection | Steps = ', num2str(step_count)]);
xlabel('Time (s)');
ylabel('Acceleration (g)');
legend('Smoothed Signal', 'Detected Steps');
grid on;

%% ---------------- STEP 7: CADENCE (TIME BETWEEN STEPS) ----------------
time_diff = diff(time(locs));   % time between steps
avg_step_time = mean(time_diff);

step_frequency = 1 / avg_step_time;   % steps per second

%% ---------------- STEP 8: ACTIVITY CLASSIFICATION ----------------
% You can tune these thresholds after observing your data

if step_frequency > 2
    activity = 'Running';
elseif step_frequency > 1.5
    activity = 'Climbing Stairs';
elseif step_frequency > 0.8
    activity = 'Walking';
else
    activity = 'Slow Movement / Standing';
end

%% ---------------- STEP 9: DISPLAY RESULTS ----------------
disp(['Step Count: ', num2str(step_count)]);
disp(['Step Frequency (steps/sec): ', num2str(step_frequency)]);
disp(['Detected Activity: ', activity]);

%% ---------------- OPTIONAL: SHOW ALL AXES ----------------
figure;
plot(time, x, 'r'); hold on;
plot(time, y, 'g');
plot(time, z, 'b');
title('Accelerometer Data (X, Y, Z)');
xlabel('Time (s)');
ylabel('Acceleration (g)');
legend('X', 'Y', 'Z');
grid on;