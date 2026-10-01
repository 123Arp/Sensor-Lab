# Sensors Laboratory — Comprehensive Experiments & Design Projects

[![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Institution](https://img.shields.io/badge/Institution-IIT%20Madras-brown.svg)](https://www.iitm.ac.in/)
[![Course](https://img.shields.io/badge/Course-Sensors%20Laboratory-orange.svg)]()
[![LTspice](https://img.shields.io/badge/Simulation-LTspice%20XVII%20%2F%2024-brightgreen.svg)](https://www.analog.com/en/resources/design-tools-and-calculators/ltspice-simulator.html)
[![MATLAB](https://img.shields.io/badge/Signal%20Processing-MATLAB%20%2F%20Python-red.svg)]()

This repository contains the complete laboratory documentation, circuit design files, simulation models (LTspice `.asc`), empirical datasets, and analysis scripts (MATLAB & Python) for the **Sensors Laboratory** course at the **Indian Institute of Technology Madras (IIT Madras)**.

---

## 👨‍🎓 Author & Course Information

* **Student Name:** Arpit Katiyar
* **Roll Number:** 24F1100064
* **Institution:** Indian Institute of Technology Madras (IIT Madras)
* **Course:** Sensors Laboratory
* **GitHub Profile:** [@123Arp](https://github.com/123Arp)
* **YouTube Channel:** [@arpit_iit.madras](https://youtube.com/@arpit_iit.madras?si=c5lhNswLiiwFaNUQ)

---

## 📑 Official Question Documents & Manuals

The original problem statements, laboratory instructions, and design procedures are linked below:

| Experiment | Title | Official Google Docs Manual |
|---|---|---|
| **Exp 1** | Design and Analysis of an Instrumentation Amplifier (INA) | [Official Question Doc 1](https://docs.google.com/document/d/e/2PACX-1vQZ6yvSooSk2wcbf7ih-PbY_zUxr5EYFcOAeWYrGGrZFLyhk1_YjvWNDRcnUxpZ6S6N7yuICrA3nXe6/pub) |
| **Exp 2** | Temperature Sensor Unit Using NTC Thermistor | [Official Question Doc 2](https://docs.google.com/document/d/e/2PACX-1vSJZhI_ipR0aQipFK6FxZrW8xWF20821vpt0Iu7RgeS4iAynx9cVJnla32_6Z9xBswweOYktoGEJKj-/pub) |
| **Exp 3** | An Electronic Compass Using Hall Effect Sensors | [Official Question Doc 3](https://docs.google.com/document/d/e/2PACX-1vQ9WbEi3lt_ZwVqCAiIy_EU_iiv4igbohsibmFP3EK7OrpKi4WCdAlVtIwGq7XllOGuBgSWeegXFyyE/pub) |
| **Exp 4** | Human Activity Recognition Using Smartphone Accelerometer | [Official Question Doc 4](https://docs.google.com/document/d/e/2PACX-1vSd3v58Wmn3waq888Fmgt4PR1l1-R7BwLMJYIFKtGSex5_4f3UHirY8mEhFW440izDew7CaluD9Q1Gq/pub) |

---

## 📂 Repository Directory Tree

```plaintext
Sensor-Lab/
├── .gitignore                                      # Git configuration for ignored files
├── LICENSE                                         # MIT License
├── README.md                                       # Master repository documentation
│
├── Sensor Lab-1/                                   # Experiment 1: Instrumentation Amplifier
│   ├── Sensors Laboratory Experiment -1.pdf        # Comprehensive Laboratory Report
│   ├── Sensor_LAB_1.asc                            # LTspice Schematic (3-OpAmp INA)
│   └── ina_gain_analysis.py                        # Gain, resistor & CMRR calculation script
│
├── Sensor Lab-2/                                   # Experiment 2: NTC Thermistor Temperature Unit
│   ├── Sensors Laboratory Experiment -2.pdf        # Comprehensive Laboratory Report
│   ├── Sensors_LAB_2.asc                           # LTspice Schematic (Wheatstone/Difference Amp)
│   └── temperature_calibration_linearization.py    # Thermistor Steinhart-Hart / Beta model script
│
├── Sensor Lab-3/                                   # Experiment 3: 2-Axis Electronic Compass
│   ├── 24F1100064_Week 3.pdf                       # Comprehensive Laboratory Report
│   ├── 24F1100064_Week 3.asc                       # LTspice Schematic (Dual-channel INA for SS49)
│   └── compass_heading_calculator.py               # Heading angle & azimuth direction script
│
└── Sensor Lab-4/                                   # Experiment 4: Human Activity Recognition
    ├── 24F1100064_Week 4.pdf                       # Comprehensive Laboratory Report
    ├── Walking_on_Floor.csv                        # Accelerometer dataset: walking on flat floor
    ├── Climbing_up.csv                             # Accelerometer dataset: ascending staircase
    ├── Climbing_down.csv                           # Accelerometer dataset: descending staircase
    ├── step_detection_activity_recognition.m       # Structured MATLAB script for step detection
    ├── untitled2.m                                 # Original MATLAB analysis script
    └── activity_recognition.py                     # Python step detection & classification pipeline
```

---

## 🔬 Experiment Summaries & Technical Details

### [Experiment 1: Design and Analysis of an Instrumentation Amplifier (INA)](Sensor%20Lab-1/)

* **Reference:** [Question Document 1](https://docs.google.com/document/d/e/2PACX-1vQZ6yvSooSk2wcbf7ih-PbY_zUxr5EYFcOAeWYrGGrZFLyhk1_YjvWNDRcnUxpZ6S6N7yuICrA3nXe6/pub)
* **Objective:** Design, simulate in LTspice, and assemble a 3-operational-amplifier instrumentation amplifier (INA) to amplify weak sensor differential signals while rejecting common-mode noise.
* **Circuit Topology:**
  * **Input Buffer Stage:** Two non-inverting op-amps cross-coupled via gain-setting resistor $R_G$ and feedback resistors $R_F$. Provides extremely high input impedance and differential amplification.
  * **Difference Amplifier Stage:** Four matched resistors ($R_1 = R_2 = R$) providing high common-mode rejection.
* **Governing Mathematical Equations:**
  $$\begin{aligned}
  V_{out} &= \left(1 + \frac{2 R_F}{R_G}\right)\left(\frac{R_2}{R_1}\right)(V_{IN+} - V_{IN-}) + V_{REF} \\
  \text{For } R_F = R_1 = R_2 = R \text{ and } V_{REF} = 0\text{ V}: \quad A_d &= 1 + \frac{2R}{R_G}
  \end{aligned}$$
* **Design Calculations:**
  * Base resistance: $R = 10\text{ k}\Omega$
  * **For Differential Gain $A_d = 3$:**
    $$3 = 1 + \frac{2(10\text{ k}\Omega)}{R_G} \implies R_G = \frac{20\text{ k}\Omega}{2} = 10\text{ k}\Omega$$
  * **For Differential Gain $A_d = 20$:**
    $$20 = 1 + \frac{2(10\text{ k}\Omega)}{R_G} \implies R_G = \frac{20\text{ k}\Omega}{19} \approx 1.053\text{ k}\Omega$$
* **Key Performance Metrics:**
  * **Common-Mode Rejection Ratio (CMRR):**
    $$\text{CMRR} = 20 \log_{10}\left|\frac{A_d}{A_c}\right| \text{ dB}$$
    Evaluated with $V_{IN+} = V_{IN-} = 1.5\text{ V}$.
  * **Offset Voltage Validation:** Tested with $V_{IN+} = V_{IN-} = 0\text{ V}$ and $V_{REF} = 2.5\text{ V}$, confirming $V_{out} = 2.5\text{ V}$.
  * **Frequency Response:** Evaluated with $V_d = 0.5\sin(2\pi f t)\text{ V}$ from $1\text{ kHz}$ upwards.
* **Hardware Setup:** Implemented on breadboard using **MCP6004** / AD8648 rail-to-rail quad op-amp, potentiometers, and ADALM1000 instrumentation unit.

---

### [Experiment 2: Temperature Sensor Unit Using NTC Thermistor](Sensor%20Lab-2/)

* **Reference:** [Question Document 2](https://docs.google.com/document/d/e/2PACX-1vSJZhI_ipR0aQipFK6FxZrW8xWF20821vpt0Iu7RgeS4iAynx9cVJnla32_6Z9xBswweOYktoGEJKj-/pub)
* **Objective:** Design, simulate, and experimentally validate a temperature sensing unit using an NTC (Negative Temperature Coefficient) thermistor with active linearization and signal conditioning.
* **Mathematical Modeling:**
  * **Steinhart-Hart / Beta Equation:**
    $$R(T) = R_0 \cdot \exp\left[\beta \left(\frac{1}{T} - \frac{1}{T_0}\right)\right]$$
    where $R_0 = 10\text{ k}\Omega$ at $T_0 = 298.15\text{ K}$ ($25^\circ\text{C}$), and $\beta \approx 3950\text{ K}$.
* **Signal Conditioning & Linearization:**
  * Supply voltage: $V_{DD} = 5.0\text{ V}$.
  * Target output voltage: $0.1\text{ V}$ at $30^\circ\text{C}$ to $4.5\text{ V}$ at $60^\circ\text{C}$.
  * Bridge network converts exponential resistance drop into a near-linear voltage variation.
  * **Active Low-Pass Filtering:** A parallel capacitor $C_f$ across the op-amp feedback resistor limits the cut-off frequency $f_c \le 50\text{ Hz}$, eliminating 50 Hz power-line interference:
    $$f_c = \frac{1}{2\pi R_f C_f} \le 50\text{ Hz}$$
* **Simulation & Experimental Testing:**
  * **LTspice Simulation (`Sensors_LAB_2.asc`):** Parametric sweep using `.step param Rtherm 1.7662k 7.5562k 0.1k` with `.op` analysis.
  * **Emulation:** Potentiometer resistance stepped in $5^\circ\text{C}$ equivalent intervals from $30^\circ\text{C}$ to $60^\circ\text{C}$.
  * **Water Bath Testing:** Real NTC thermistor immersed in water, heated gradually, and cross-checked against a standard digital reference thermometer.
  * **Long-Term Monitoring:** Continuous 24-hour room temperature logging at 30-minute intervals using the ADALM1000 data acquisition module.

---

### [Experiment 3: An Electronic Compass Using Hall Effect Sensors](Sensor%20Lab-3/)

* **Reference:** [Question Document 3](https://docs.google.com/document/d/e/2PACX-1vQ9WbEi3lt_ZwVqCAiIy_EU_iiv4igbohsibmFP3EK7OrpKi4WCdAlVtIwGq7XllOGuBgSWeegXFyyE/pub)
* **Objective:** Design and assemble a 2-axis electronic compass using two orthogonally mounted Hall Effect ICs (SS49 series) and dual signal conditioning difference amplifiers to detect Earth's geomagnetic field components.
* **Sensor Operating Principle:**
  * Linear Hall Effect sensor generates a voltage proportional to magnetic flux density ($B$):
    $$V_{hall} = \frac{V_{DD}}{2} \pm S \cdot B$$
  * Earth's magnetic field ($30\text{--}60\ \mu\text{T}$) induces tiny millivolt-level variations around the $V_{DD}/2 = 2.5\text{ V}$ quiescent level.
* **Signal Conditioning Architecture:**
  * Two identical 3-opamp instrumentation amplifier channels for X-axis and Y-axis sensor signals.
  * DC offset trimming to shift the amplified voltage within the readable $0\text{--}5\text{ V}$ input range of the ADALM1000 ADC.
  * Feedback capacitor limits amplifier bandwidth to $f_c < 10\text{ Hz}$ to eliminate high-frequency electromagnetic noise.
* **Heading Angle Determination:**
  $$\theta = \text{atan2}\left(V_{out\_y} - V_{offset\_y},\, V_{out\_x} - V_{offset\_x}\right) \times \frac{180^\circ}{\pi}$$
* **Simulation & Hardware Results:**
  * **LTspice Simulation (`24F1100064_Week 3.asc`):** Modeled Hall sensor outputs with dual parametric voltage sweeps:
    `.step param X 2.4986 2.5014 0.00014` and `.step param Y 2.5014 2.4986 -0.00014`.
  * **Physical Assembly:** Hall sensors mounted strictly at $90^\circ$ on a rigid, non-magnetic ruler/strip.
  * **Validation:** Sensor assembly rotated through full $360^\circ$ circle in $20^\circ$ increments; recorded X and Y channel voltages via ADALM1000 and verified computed azimuth against reference compass bearings.

---

### [Experiment 4: Human Activity Recognition Using Smartphone Accelerometer](Sensor%20Lab-4/)

* **Reference:** [Question Document 4](https://docs.google.com/document/d/e/2PACX-1vSd3v58Wmn3waq888Fmgt4PR1l1-R7BwLMJYIFKtGSex5_4f3UHirY8mEhFW440izDew7CaluD9Q1Gq/pub)
* **Objective:** Collect real-world tri-axial acceleration data ($a_x, a_y, a_z$) during human movement using a smartphone, design an automated step detection algorithm, and classify human activities (Walking vs. Stair Climbing).
* **Data Acquisition:**
  * **App Used:** *Physics Toolbox Sensor Suite Pro* on an Android device.
  * **Sampling Rate:** ~100 Hz ($\Delta t \approx 0.01\text{ s}$).
  * **Logged Datasets:**
    1. [`Walking_on_Floor.csv`](Sensor%20Lab-4/Walking_on_Floor.csv) (31.76 s, flat surface walking)
    2. [`Climbing_up.csv`](Sensor%20Lab-4/Climbing_up.csv) (25.35 s, ascending staircase)
    3. [`Climbing_down.csv`](Sensor%20Lab-4/Climbing_down.csv) (26.04 s, descending staircase)
* **Signal Processing Pipeline:**
  1. **Acceleration Magnitude Computation:**
     $$a_{mag}(t) = \sqrt{a_x^2(t) + a_y^2(t) + a_z^2(t)}$$
  2. **Noise Reduction:** Simple Moving Average (SMA) filter ($W = 5$) to suppress sensor jitter:
     $$a_{smooth}[k] = \frac{1}{W} \sum_{i=0}^{W-1} a_{mag}[k - i]$$
  3. **Peak Detection:** Evaluated using MATLAB `findpeaks` and SciPy `signal.find_peaks`:
     * Peak threshold: $h_{min} \ge 1.05\text{ g}$
     * Minimum distance: $d_{min} \ge 20\text{ samples}$ (refractory footfall period)
  4. **Cadence & Step Frequency:**
     $$\Delta t_{step} = \text{mean}\left(\text{diff}(t_{peaks})\right), \quad f_{step} = \frac{1}{\Delta t_{step}} \text{ (steps/s)}$$
  5. **Activity Classification:**
     * $f_{step} > 2.0\text{ Hz} \implies$ **Running**
     * $1.5\text{ Hz} < f_{step} \le 2.0\text{ Hz} \implies$ **Climbing Stairs**
     * $0.8\text{ Hz} \le f_{step} \le 1.5\text{ Hz} \implies$ **Walking**
     * $f_{step} < 0.8\text{ Hz} \implies$ **Slow Movement / Standing**

---

## 🛠️ Tools, Hardware & Software Stack

| Category | Tools / ICs / Software |
|---|---|
| **Active ICs** | MCP6004 (Quad Rail-to-Rail Op-Amp), AD8648 (Precision Op-Amp), SS49 (Linear Hall Effect IC) |
| **Passive Sensors** | 10 kΩ NTC Thermistor ($\beta \approx 3950\text{ K}$) |
| **Measurement & DAQ** | Analog Devices ADALM1000 (Active Learning Module), Digital Thermometer |
| **Mobile Application** | Physics Toolbox Sensor Suite Pro (Tri-axial Accelerometer logging at 100 Hz) |
| **Simulation Platform** | LTspice XVII / 24 |
| **Programming & Analysis**| MATLAB R2024 / Python 3 (NumPy, SciPy, Pandas, Matplotlib) |

---

## 🚀 How to Run & Reproduce

### 1. LTspice Circuit Simulations
1. Install [LTspice](https://www.analog.com/en/resources/design-tools-and-calculators/ltspice-simulator.html).
2. Open any `.asc` file:
   * **Lab 1:** `Sensor Lab-1/Sensor_LAB_1.asc`
   * **Lab 2:** `Sensor Lab-2/Sensors_LAB_2.asc`
   * **Lab 3:** `Sensor Lab-3/24F1100064_Week 3.asc`
3. Click the **Run** button to simulate DC sweeps, AC frequency sweeps, or transient responses.

### 2. Activity Recognition Analysis (Experiment 4)

#### Using MATLAB:
1. Open MATLAB and navigate to `Sensor Lab-4/`.
2. Run the script:
   ```matlab
   step_detection_activity_recognition
   ```
3. Change `dataFile` variable to evaluate `Walking_on_Floor.csv`, `Climbing_up.csv`, or `Climbing_down.csv`.

#### Using Python:
1. Install dependencies:
   ```bash
   pip install numpy scipy pandas matplotlib
   ```
2. Run the automated multi-dataset analysis script:
   ```bash
   python "Sensor Lab-4/activity_recognition.py"
   ```

### 3. Auxiliary Analysis Scripts
* **Lab 1 Gain & CMRR:**
  ```bash
  python "Sensor Lab-1/ina_gain_analysis.py"
  ```
* **Lab 2 Thermistor Linearization:**
  ```bash
  python "Sensor Lab-2/temperature_calibration_linearization.py"
  ```
* **Lab 3 Electronic Compass Azimuth:**
  ```bash
  python "Sensor Lab-3/compass_heading_calculator.py"
  ```

---

## 📜 License

This repository is licensed under the [MIT License](LICENSE).
