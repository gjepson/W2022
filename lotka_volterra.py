# Garrett F. Jepson

# Sept 2022

# Assignment 36: Numerical integration of Lotka-Volterra equation

# Imports
import numpy as np
from matplotlib import pyplot as plt


# Define initial conditions
a = 1
b = 1
g = 1
d = 1

dt = 0.1 # Timestep
lim = 10

t = np.arange(0, lim+dt, dt) # Numerical grid

x1_0 = 2
x2_0 = 4
x1_dot = -4
x2_dot = -2

'''
def lotka(y, t, a, b, g, d):
	return np.array([y[1], -])

'''
# Euler method implementation (explicit)
x1 = np.zeros(len(t))
x2  = np.zeros(len(t))

x1[0] = x1_0
x2[0] = x2_0

for i in range(0, len(t) -1):
	x1[i + 1] = x1[i] + dt * x1[i]*(a - b*x2[i])
	x2[i + 1] = x2[i] + dt * x2[i]*(-g + d*x1[i])


# Plot in (x1, x2) plane
plt.plot(x1, x2)
plt.grid()
plt.show()

# Plot change in energy as a function of time
E = d*x1 + b*x2 - g * np.log(x1) - a * np.log(x2)

plt.plot(t, E)
plt.show()


y0 = np.array

def lotka(y, t, a, b, g, d):
	return np.array([x[0] * (a - b*x[1]), x[1] * (-g + d*x[0])])


# Integrate over five cycles using Heun's method
def heun(f, y0, t, args=()):
	n = len(t)


## Plot trajectory in (x,p) plane

## Plot change in energy as a function of time



# Integrate over five cycles using Runge-Kutta

## Plot trajectory in (x,p) plane

## Plot change in energy as a function of time


# Integrate over five cycles using Runge-Kutta w/ adaptive step

## Plot trajectory in (x,p) plane

## Plot change in energy as a function of time




