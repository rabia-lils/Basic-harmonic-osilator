# Basic-harmonic-osilator
import numpy as np
import matplotlib.pyplot as plt
# Parameters
m=1.0
k=1.0
dt= 0.01
T= 20
# times array
t= np.arange(0, T, dt)
# arrays
x= np.zeros(len(t))
v= np.zeros(len(t))
# initial
x[0]= 1.0
v{0}= 0.0
# Eular Method
for i in range(len(t)-1)
a= -(k/m)*x[i]
v[i+1]= v[i]+ a*dt
x[i+1]= x[i]+ v[i]*dt
# grafik
plt.plot(t, x)
plt.xlabel("zaman (s)")
plt.ylabel("konum (m)")
plt.title("Basic Harmonic Oscillator")
plt.show()
