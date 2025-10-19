# solid3d_start.py

from math import pi
import ti_plotlib as plt
import ti_system

# Function definition (replace this with Y1 later)
def f(x):
    return x**2  # You can replace this with eval("Y1") later

# Integration bounds
a = 0
b = 2
n = 100  # Number of slices
dx = (b - a) / n

# Volume calculation (Disk method)
volume = 0
for i in range(n):
    x = a + i * dx
    volume += pi * f(x)**2 * dx

# Show volume on screen
ti_system.cls()
print("Solid3D - v0.1")
print("----------------------")
print("f(x) = x^2")
print("Volume =", round(volume, 4))
print()
print("Press any key to view 2D plot")

ti_system.wait_key()

# 2D Plot
plt.cls()
plt.set_window(a, b, 0, f(b))  # xmin, xmax, ymin, ymax

x_vals = [a + i * dx for i in range(n+1)]
y_vals = [f(x) for x in x_vals]

for i in range(n):
    plt.line(x_vals[i], y_vals[i], x_vals[i+1], y_vals[i+1])

plt.show()
