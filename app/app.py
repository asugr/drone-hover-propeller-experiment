import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Drone Propeller Lab", page_icon="🚁", layout="wide")

st.title("🚁 Why Does Propeller Size Matter for Drones?")
st.caption("An educational hover-physics experiment using a simplified ideal rotor model.")

g = 9.81

mass = st.slider("Drone mass (kg)", 0.5, 10.0, 2.0, 0.1)
rotors = st.slider("Number of rotors", 2, 8, 4, 1)
diameter_cm = st.slider("Propeller diameter (cm)", 10, 50, 25, 1)
rho = st.slider("Air density (kg/m³)", 1.0, 1.3, 1.225, 0.005)

diameter = diameter_cm / 100
total_area = rotors * np.pi * (diameter / 2) ** 2
weight = mass * g
induced_velocity = np.sqrt(weight / (2 * rho * total_area))
ideal_power = weight * induced_velocity

c1, c2, c3 = st.columns(3)
c1.metric("Required hover thrust", f"{weight:.1f} N")
c2.metric("Total rotor disk area", f"{total_area:.3f} m²")
c3.metric("Ideal hover power", f"{ideal_power:.1f} W")

st.divider()

st.markdown("### What happens when propellers get larger?")

diameters = np.linspace(0.10, 0.50, 100)
areas = rotors * np.pi * (diameters / 2) ** 2
powers = weight * np.sqrt(weight / (2 * rho * areas))

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(diameters * 100, powers)
ax.axvline(diameter_cm, linestyle="--")
ax.set_xlabel("Propeller diameter (cm)")
ax.set_ylabel("Ideal induced hover power (W)")
ax.set_title("Propeller diameter vs. ideal hover power")
st.pyplot(fig)

st.info(
    "This is an idealized momentum-theory model. Real drone power is higher because of "
    "blade profile drag, motor/ESC losses, rotor interactions, turbulence and other effects."
)
