#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

# Given values
n_values = [
    0.94, 0.90, 0.87, 0.83, 0.79, 0.74, 0.59, 0.64, 0.57, 0.49, 0.39, 0.28,
    0.18, 0.14, 0.12, 0.11, 0.10, 0.10, 0.10, 0.10, 0.11, 0.12, 0.12, 0.13,
    0.14, 0.15, 0.16, 0.16, 0.16, 0.16, 0.15, 0.15, 0.15, 0.16, 0.16, 0.17,
    0.19, 0.23, 0.29, 0.41, 0.73, 2.37, 8.50, 5.36, 3.96, 3.11, 2.45, 1.84,
    1.13, 0.34, 0.21, 0.19, 0.19, 0.20, 0.23, 0.28, 0.52, 0.89, 2.16, 11.82,
    11.36, 8.54, 7.18, 6.36, 5.82, 5.42, 5.11
]

k_values = [
    0.037, 0.039, 0.042, 0.045, 0.049, 0.054, 0.061, 0.069, 0.081, 0.098,
    0.128, 0.192, 0.312, 0.440, 0.553, 0.655, 0.750, 0.840, 0.927, 1.01, 1.09,
    1.18, 1.26, 1.34, 1.42, 1.50, 1.58, 1.66, 1.75, 1.85, 1.96, 2.08, 2.22,
    2.37, 2.55, 2.75, 3.00, 3.32, 3.74, 4.36, 5.43, 7.85, 3.27, 0.678, 0.313,
    0.206, 0.174, 0.186, 0.278, 0.932, 1.64, 2.17, 2.64, 3.10, 3.61, 4.19, 5.88,
    7.38, 10.22, 12.96, 2.26, 0.804, 0.422, 0.264, 0.182, 0.133, 0.101
]

# Wavelength range from 2.5 to 25 micrometers
wavelength_range = np.linspace(2.5, 25, len(n_values))

# Calculate corresponding frequencies
frequency_values = 3e8 / (wavelength_range * 1e-6)

# Calculate permittivity
permittivity_values = [(n + 1j * k)**2 for n, k in zip(n_values, k_values)]

# Extract real and imaginary parts
real_parts = [epsilon.real for epsilon in permittivity_values]
imaginary_parts = [epsilon.imag for epsilon in permittivity_values]

# Plot the real part without dots
plt.plot(wavelength_range, real_parts, label='Real Part', linestyle='-')

# Plot the imaginary part without dots
plt.plot(wavelength_range, imaginary_parts, label='Imaginary Part', linestyle='-')

# Adding labels and title
plt.xlabel('Wavelength (micrometers)')
plt.ylabel('Permittivity')
plt.title('Real and Imaginary Parts of Permittivity')

# Adding legend
plt.legend()

# Display the plot
plt.show()


# In[ ]:




