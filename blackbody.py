import numpy as np
import matplotlib.pyplot as plt



#planck constant

h = 6.62e-34 #Js

#speed of light

c = 3.0e+10 #cm/s

#Boltzmann constant

k = 1.38e-23 #J/K

#FUV  effective wavelength

lfuv = 1.516e-5 #cm

#NUV effective  wavelength

lnuv = 2.267e-5 #cm

#temperature range

t = np.array([5000.0, 5500.0, 6000.0, 6500.0, 7000.0, 7500.0, 8000.0, 8500.0, 9000.0, 9500.0, 10000.0, 15000.0])

#planks equation FUV

a= 2.0*h*c**2

b = h*c/(lfuv*k*t)

blackbodyf = a/((lfuv**5) * (np.exp(b) -1.0))

#planks equation NUV

a2= 2.0*h*c**2

b2 = h*c/(lnuv*k*t)

blackbodyn = a2/((lnuv**5) * (np.exp(b2) -1.0))

#FUV/NUV ratio

ratio = blackbodyf/blackbodyn

print(ratio)

plt.plot(t, ratio)
plt.ylabel('FUV/NUV')
plt.xlabel('Temperature (K)')
plt.title('FUV/NUV flux ratio vs. Tempterature (K)')
plt.ylim(0.0, 1.0)
plt.xlim(5000.0, 15000.0)
plt.yticks(np.arange(0.0, 1.0, 0.05))
plt.xticks(np.arange(5000.0, 15000.0, 1000.0))
plt.gca().invert_xaxis()
plt.grid()
plt.show()
