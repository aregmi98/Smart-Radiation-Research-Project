I along with my superviser were studying a paper titled "Spacecraft smart radiation device with variable emission and low absorption based on phase change material VO2" (DOI: https://doi.org/10.1016/j.ijthermalsci.2022.108039). 

This paper proposes and analyzes a vanadium dioxide (VO2)-based multilayer films structure for thermal control devices in spacecraft. It addresses the challenge posed by the miniaturization of satellites by reducing spacecraft load and size while adapting to changing thermal environments in space. The study investigates the influence of film thicknesses on emission and solar absorption, considering two optical dielectric layers: silicon oxide (SiO2) and aluminum oxide (Al2O3). 

![layers](https://github.com/aregmi98/Smart-Radiation-Research-Project/assets/151678499/8cbcb78a-aafb-4be6-9f6d-1eaf8dddcf75)

The paper proposes a smart radiation device that comprises a VO2 film, a dielectric layer (SiO2/Al2O3), and a metallic Ag substrate as in the figure above. In its low-temperature state, VO2 behaves as a transparent semiconductor, allowing the absorption of infrared (IR) wavelength light, which is then reflected by the metal. This configuration functions as an IR reflector with low emission. Conversely, in its high-temperature state, VO2 becomes translucent and semi-metallic.

A detailed calculation for emmissivity of the film, in different temperatures (phase changing for VO2) has been conducted in the paper. We wanted to run calculations for the permittivity of SiO2 and Al2O3 and generated the permittivity graph for the materials and compare them with the graphs presented in the paper. The goal was to see if the calculations and their approaches in the paper were viable. This project was aimed to determined the correct methodoly to calculate the permittivity of the materials for future research purposes. 

I wrote some python codes to calculates the permittivity of the materials and the graphs were generated. Following were the graphs that we obtained from the codes:

![image](https://github.com/aregmi98/Smart-Radiation-Research-Project/assets/151678499/bd22ac08-a1e3-4d09-b939-8f046fd50cc2)

![image](https://github.com/aregmi98/Smart-Radiation-Research-Project/assets/151678499/077978bc-7546-417a-9490-ee2c279f0958)

In comparison with the permittivity graphs in the paper, the graphs that we were able to generate were identical. The peaks in our graphs were observed at the same wavelengths as in the paper, along with similar magnitudes of permittivity. This calculation and its methodology can be used for future research works with similar studies as in the paper.

