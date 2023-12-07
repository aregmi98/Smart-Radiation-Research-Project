import numpy as np
import matplotlib.pyplot as plt

def lorentz_dielectric(epsilon_inf, A, omega, gamma, omega_val):
    dielectric = epsilon_inf
    for Aj, omega_j, gamma_j in zip(A, omega, gamma):
        term = Aj * omega_j**2 / (omega_j**2 - omega_val**2 - 1j * gamma_j * omega_val)
        dielectric += term
    return dielectric

# Given values
epsilon_inf = 2.0014
A = [4.4767e27, 2.3584e28]  # Amplitudes for Lorentzian terms
omega = [8.6732e13, 2.0219e14]  # Resonance frequencies for Lorentzian terms
gamma = [3.3026e12, 8.3983e12]  # Damping constants for Lorentzian terms

# Convert wavelength range (micrometers) to frequency range
wavelength_values = np.linspace(2.5, 25, 1000)  # Wavelength values in micrometers
frequency_values = 3e8 / (wavelength_values * 1e-6)  # Convert to Hz

real_part_values = []
imaginary_part_values = []

for frequency_val in frequency_values:
    dielectric_val = lorentz_dielectric(epsilon_inf, A, omega, gamma, 2 * np.pi * frequency_val)
    real_part = np.real(dielectric_val)
    imaginary_part = np.imag(dielectric_val)
    real_part_values.append(real_part)
    imaginary_part_values.append(imaginary_part)

# Plot both real and imaginary parts on the same plot
plt.figure(figsize=(8, 6))

# Real Part
plt.plot(wavelength_values, real_part_values, label='Real Part', color='blue')

# Imaginary Part
plt.plot(wavelength_values, imaginary_part_values, label='Imaginary Part', color='red')

plt.xlabel('Wavelength (μm)')
plt.ylabel('Permittivity')
plt.legend()
plt.grid()
plt.title('Real and Imaginary Parts of Permittivity')
plt.show()

