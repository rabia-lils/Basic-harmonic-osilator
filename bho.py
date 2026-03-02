# Basic-harmonic-osilator
import numpy as np
import matplotlib.pyplot as plt

# Parametreler
m = 1.0
k = 1.0
dt = 0.01
T = 20

# diziler
t = np.arange(0, T, dt)
x = np.zeros(len(t))
v = np.zeros(len(t))

# Başlangıç değerleri
x[0] = 1.0
v[0] = 0.0

# Euler Yöntemi
for i in range(len(t) - 1):
    a = -(k / m) * x[i]
    v[i+1] = v[i] + a * dt
    x[i+1] = x[i] + v[i+1] * dt # Euler-Cromer için v[i+1] kullanıldı

# Grafik
plt.figure(figsize=(10, 5))
plt.plot(t, x, label='Konum (x)')
plt.xlabel("Zaman (s)")
plt.ylabel("Konum (m)")
plt.title("Basit Harmonik Osilatör Simülasyonu")
plt.grid(True)
plt.legend()
plt.show()
