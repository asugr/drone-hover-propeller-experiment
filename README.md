# 🚁 Why Does Propeller Size Matter for Drones?

### A simple computational experiment in rotor physics and drone design

> **How does propeller diameter affect the ideal power required for a drone to hover?**

**Engineering portfolio project | Drones • Mechanical Engineering • Aerospace Engineering • Python**

---

## 🔬 Research Question

A drone must generate enough upward thrust to balance its weight.

But how does the **size of its propellers** affect the energy required to hover?

This project uses a simplified rotor model to investigate the relationship between:

**drone mass → required thrust → rotor disk area → induced velocity → ideal hover power**

---

## 📐 The Physics

A hovering drone must produce approximately its own weight in thrust:

$$T = mg$$

A simplified momentum-theory relationship for rotor-induced velocity is:

$$v_i = \\sqrt{\\frac{T}{2\\rho A}}$$

where:

- **T** = required thrust
- **m** = drone mass
- **g** = gravitational acceleration
- **ρ** = air density
- **A** = total rotor disk area

The corresponding ideal induced power is:

$$P_i = T v_i$$

This model predicts that increasing total rotor disk area reduces the induced velocity required to generate the same thrust.

---

## 🧪 The Experiment

The interactive model allows the user to change:

- Drone mass
- Number of rotors
- Propeller diameter
- Air density

The model then calculates:

- Required hover thrust
- Total rotor disk area
- Ideal induced air velocity
- Ideal induced hover power

### Key idea

For the same drone weight:

> **Larger rotor disk area can reduce ideal induced hover power.**

This helps explain why propeller size is an important part of drone design.

---

## 📊 What the Model Shows

The simplified model demonstrates that:

- A heavier drone requires more thrust.
- More rotor disk area can reduce the ideal induced velocity.
- Larger propellers can therefore reduce ideal induced hover power.
- The relationship is a trade-off rather than a simple "bigger is always better" rule.

Larger propellers also affect:

- vehicle size
- mass
- packaging
- maneuverability
- response characteristics
- operating speed

---

## 💻 Interactive Experiment

**[🚁 Launch the Drone Propeller Lab](https://drone-hover-propeller-experiment-sk3dphswikqw634fulua7z.streamlit.app/)**

Change the drone mass and propeller diameter and observe how the estimated ideal hover power changes.

---

## ⚠️ Model Limitations

This is an **idealized educational model**, not a real drone performance calculator.

It does not include:

- blade profile drag
- motor efficiency
- ESC losses
- battery losses
- rotor-rotor aerodynamic interactions
- turbulence
- detailed propeller geometry
- forward flight

Therefore, the calculated power should not be interpreted as the actual electrical power required by a real drone.

---

## 🧠 Engineering Interpretation

The interesting part is not simply that "bigger propellers are better."

The real engineering question is:

> **How should rotor size be balanced against the other requirements of a drone?**

A designer must balance efficiency with vehicle size, weight, responsiveness, packaging, and mission requirements.

---

## 🛠️ Technical Workflow

```text
Drone mass
    ↓
Required hover thrust
    ↓
Total rotor disk area
    ↓
Induced velocity
    ↓
Ideal hover power
    ↓
Sensitivity experiment
    ↓
Engineering interpretation
```

---

## 📁 Repository Structure

```text
drone-hover-propeller-experiment/
│
├── app/
│   └── app.py
│
├── data/
│   └── processed/
│       └── hover_power_comparison.csv
│
├── images/
│   ├── power_vs_mass.png
│   ├── power_vs_diameter.png
│   └── disk_area_vs_diameter.png
│
├── notebooks/
│   └── drone_hover_propeller_experiment.ipynb
│
├── src/
│
├── README.md
└── requirements.txt
```

---

## 🚀 Future Work

A possible future extension would be to compare the simplified model with published propeller-performance data.

Other extensions could investigate:

- different numbers of rotors
- different air densities
- propeller diameter vs. drone mass
- ideal hover efficiency
- a simple battery-endurance estimate

---

## 🎓 Why This Project Matters to Me

This project connects my interest in **drones, Mechanical Engineering, and Aerospace Engineering** with mathematical modeling and programming.

Instead of only learning equations, I used them to build an interactive experiment:

**Physics → Model → Simulation → Visualization → Engineering interpretation**

---

## 👩‍💻 Part of ScienceBehindIt Engineering Lab

This project is part of my **ScienceBehindIt Engineering Lab**, where I explore the science and engineering behind real-world machines through computational experiments and science communication.
