# TODO
# Plot for multiple timesteps, clean up plotting
# Rewrite for loop in given form
# Rewrite as function
# Integrate

# Garrett F. Jepson
# Through assignment 36 by next Tuesday (9/20)

# Sept 2022

# Assignment 33: Euler's Method

import numpy as np
from matplotlib import pyplot as plt

dt = 0.1 # Timestep
lim = 10
# Initial conditions
x0 = 0
p0 = 1

t = np.arange(0, lim+dt, dt) # Numerical grid

# Euler Method Implementation (explicit)
x = np.zeros(len(t))
p = np.zeros(len(t))

x[0] = x0
p[0] = p0

for i in range(0,len(t) - 1):
	x[i + 1] = x[i] + dt * p[i]
	p[i + 1] = p[i] - dt * x[i]

H = 0.5 * x + 0.5 * p

# Plot Position vs Momentum
plt.plot(x,p)
plt.xlabel('Position')
plt.ylabel('Momentum')
plt.show()


# Plot total energy
plt.plot(t,H)
plt.xlabel('Time')
plt.ylabel('Total Energy')
plt.show()











