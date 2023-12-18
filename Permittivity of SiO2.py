import numpy as np
import matplotlib.pyplot as plt

# Function to calculate the Lorentz model for the dielectric function
def lorentz_model(wavelength, epsilon, sigma, wo, gamma):
    w = 2 * np.pi * 3e8 / wavelength  # Convert wavelength to angular frequency
    return epsilon - (sigma / (w**2 - wo**2 + 1j * gamma * w))

# Wavelength range from 2.5 to 25 micrometers
wavelength_range = np.linspace(2.5e-6, 25e-6, 1000)

# Coefficients from your provided values
epsilon = 2.0014
sigma_1 = 4.4767e27
wo_1 = 8.6732e13
gamma_1 = 3.3026e12
sigma_2 = 2.3584e28
wo_2 = 2.0219e14
gamma_2 = 8.3983e12

# Calculate the dielectric function using Lorentz model for both components
dielectric_function_1 = lorentz_model(wavelength_range, epsilon, sigma_1, wo_1, gamma_1)
dielectric_function_2 = lorentz_model(wavelength_range, epsilon, sigma_2, wo_2, gamma_2)

# Combine the components to get the total dielectric function
total_dielectric_function = dielectric_function_1 + dielectric_function_2

# Plotting the total dielectric function
plt.figure(figsize=(10, 6))
plt.plot(wavelength_range * 1e6, total_dielectric_function.real, label='Real part (Total)')
plt.plot(wavelength_range * 1e6, total_dielectric_function.imag, label='Imaginary part (Total)')
plt.xlabel('Wavelength (micrometers)')
plt.ylabel('Dielectric Function')
plt.title('Total Dielectric Function of SiO2 using Lorentz Model')
plt.legend()
plt.show()

