import matplotlib.pyplot as plt
import numpy as np
import math

# Given data
Mf = 9  # °C
Ms = 18  # °C
As = 35  # °C
Af = 49  # °C
CM = 8  # MPa/°C (slope for martensite)
CA = 14  # MPa/°C (slope for austenite)
YM = 26000
YA = 67000
TCRS = 100  # MPa (start transformation stress)
TCRF = 170  # MPa (finish transformation stress)

# Elastic region
Ta = 0
Sa = 0
Tb = TCRS
Sb = Tb / YM

stress_b = np.linspace(0, Tb, num=20, endpoint=True)
strain_b = stress_b / YM

# Plastic deformation region
Tc = TCRF
stress_c = np.linspace(Tb, Tc, num=20, endpoint=True)
shiT0 = 1
shiS0 = 0
pi = 3.14
SL = 0.07
shi_lst = []

for i in stress_c:
    shiS = ((1 - shiS0) / 2) * math.cos((pi / (TCRS - TCRF)) * (i - TCRF)) + ((1 + shiS0) / 2)
    shi_lst.append(shiS)

shi_lst = np.array(shi_lst)
strain_c = (stress_c / YM) + SL * shi_lst

# Elastic region
stress_d = np.linspace(Tc,Ta,num=20, endpoint=True)

strain_d = (stress_d / YM) + SL

# Combine both curves for a continuous plot
strain_combined = np.concatenate((strain_b, strain_c, strain_d))
stress_combined = np.concatenate((stress_b, stress_c, stress_d))

# Plot the combined curve
plt.figure(figsize=(8, 6))
plt.plot(strain_combined, stress_combined, label='Stress-Strain Curve', color='blue')
plt.xlabel('Strain')
plt.ylabel('Stress (MPa)')
plt.title('Stress-Strain Relationship')
plt.legend()
plt.grid(True)
plt.show()
