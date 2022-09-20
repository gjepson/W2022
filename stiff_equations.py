# TODO
# Clean up plots
# Comment code
# Plot exact, error on same axes w/ different granularity
# Plot for different timesteps
# Plot using exact relative error formula

# Garrett F. Jepson
#
# Sept 2022

# Assignment 34: Stiff equations

# Import libraries
import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint

# Define initial conditions, constants
eps = 0.01

x_0 = 2
x_dot_0 = eps - 1

dt = 1
lim = 10

t = np.arange(0, lim + dt, dt)

# 1.a Plot exact solution
f_exact = np.exp(eps*t) + np.exp(-t)

plt.plot(t, f_exact, 'b', label='Exact')
plt.title('Exact Solution')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.show()


# 1.b Plot Runge-Kutta method solution

# Define function
def stiff(y, t, b, c):
	return np.array([y[1], -b*y[1] + c*y[0]] )

eps = 0.01
b = 1 - eps
c = eps
y0 = np.array([2, eps - 1]) # initial conditions

dt = 1
lim  = 10

t = np.arange(0, lim+dt, dt)

def euler(f, y0, t, args=()):
	n = len(t)
	y = np.zeros((n, len(y0)))
	y[0] = y0
	for i in range(n - 1):
		y[i+1] = y[i] + dt * f(y[i], t[i], *args)
	return y

def RK(f, y0, t, args=()):
	n = len(t)
	y = np.zeros((n, len(y0)))
	y[0] = y0
	for i in range(n - 1):
		k1 = f(y[i], t[i], *args)
		k2 = f(y[i] + k1 * dt / 2., t[i] + dt / 2., *args)
		k3 = f(y[i] + k2 * dt / 2., t[i] + dt / 2., *args)
		k4 = f(y[i] + k3 * dt, t[i] + dt, *args)
		y[i+1] = y[i] + (dt / 6.) * (k1 + 2*k2 + 2*k3 + k4)
	return y


sol = RK(stiff, y0, t, args=(b, c))


plt.plot(t, f_exact, 'b', label='Exact')
plt.plot(t, sol[:, 0], 'g', label='Approximate Solution')
#plt.plot(t, sol[:, 1], 'g', label='y(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()

# 2. Plot relative error
error = sol[:, 0] - f_exact

plt.plot(t, error, 'r')
plt.show()













