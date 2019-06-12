import numpy as np
import matplotlib.pyplot as plt



#planck constant

h = 6.62e-34 #kg*m**2/s

#speed of light

c = 3.0e+08 #m/s

#Boltzmann constant

k = 1.38e-23 #kg*m**2/K*s**2

#FUV  effective wavelength

lfuv = 1.516e-7 #m


#NUV effective  wavelength

lnuv = 2.267e-7 #m


#temperature range

x = int(input("Enter lower tempture limit: "))
y = int(input("Enter upper tempture limit: "))
z = int(input("Enter number of points: "))

t = np.linspace( x, y, num=z , endpoint=True)
#t = np.array([5000.0, 5500.0, 6000.0, 6500.0, 7000.0, 7500.0, 8000.0, 8500.0, 9000.0, 9500.0, 10000.0])

#planks equation FUV

a= 2.0*h*c

b = h*c/(lfuv*k*t)

blackbodyf = a/((lfuv**3) * (np.exp(b) -1.0))

#planks equation NUV

a2= 2.0*h*c

b2 = h*c/(lnuv*k*t)

blackbodyn = a2/((lnuv**3) * (np.exp(b2) -1.0))

#FUV/NUV ratio

ratio = blackbodyf/blackbodyn

print(ratio)
print(blackbodyf)
print(blackbodyn)

plt.plot(t, ratio)
plt.ylabel('FUV/NUV')
plt.xlabel('Temperature (K)')
plt.title('FUV/NUV flux ratio vs. Temperature (K)')
plt.ylim(0, max(ratio))
plt.xlim(x , y)
plt.yticks(np.arange(0.0, max(ratio), 0.05))
plt.xticks(np.arange(x  , y, 1000.0))
plt.gca().invert_xaxis()
plt.grid()
plt.show()
