# Garrett F. Jepson

# Sept 2022

# Assignment 36: Numerical integration of Lotka-Volterra


# Imports
import numpy as np
from matplotlib import pyplot as plt

# Define methods

def euler(f, y0, t, dt, args=()):
	n = len(t)
	y = np.zeros((n, len(y0)))
	y[0] = y0
	for i in range(n-1):
		k1 = dt * f(y[i], t[i], *args)
		y[i+1] = y[i] + k1
	return y

def heun(f, y0, t, dt, args=()):
	n = len(t)
	y = np.zeros((n, len(y0)))
	y[0] = y0
	for i in range(n-1):
		k1 = dt * f(y[i], t[i], *args)
		k2 = dt * f(y[i] + k1, t[i] + dt, *args)
		y[i+1] = y[i] + 0.5 * (k1 + k2)
	return y

def RK(f, y0, t, dt, args=()):
	n = len(t)
	y = np.zeros((n, len(y0)))
	y[0] = y0
	for i in range(n-1):
		k1 = f(y[i], t[i], *args)
		k2 = f(y[i] + k1 * dt / 2., t[i] + dt / 2., *args)
		k3 = f(y[i] + k2 * dt / 2., t[i] + dt / 2., *args)
		k4 = f(y[i] + k3 * dt, t[i] + dt, *args)
		y[i+1] = y[i] + (dt / 6.) * (k1 + 2*k2 + 2*k3 + k4)
	return y


def RK_adaptive(f, y0, t0, tf, dt0, dt_min, dt_max, e_min, e_max, N, args=()):
	dt = dt_min
	t = np.zeros((N, 1))
	t[0] = t0
	y = np.zeros((N, len(y0)))
	y[0] = y0
	RKF4 = np.zeros((N, len(y0)))
	RKF4[0] = 0
	RKF5 = np.zeros((N, len(y0)))
	RKF5[0] = 0
	i = 0
	while np.any(i < N and t < tf):
		if dt < dt_min:
			dt = dt_min
		elif dt > dt_max:
			dt = dt_max
		#COMPUTE RKF4, RKF5 HERE
		# RKF4
		k1 = dt * f(y[i], t[i], *args)
		k2 = dt * f(y[i] + k1/4., t[i] + dt/4.)
		k3 = dt * f(y[i] + (3/32)*k1 + (9/32)*k2, t + (3/8)*dt)
		k4 = dt * f(y[i]+(1932/2197)*k1-(7200/2197)*k2+(7296/2197)*k3, t+(12/13)*dt)
		k5 = dt * f(y[i]+(439/216)*k1-8*k2+(3680/513)*k3-(845/4104)*k4, t+dt)
		RKF4[i+1] = y[i]+(2/216)*k1+(1408/2565)*k3+(2197/4104)*k4-(1/5)*k5
		# RK5
		k6 = dt * f(y[i]-(8/27)*k1+2*k2-(3544/2565)*k3+(1859/4104)*k4-(11/40)*k5)
		RKF5[i+1] = y[i]+(16/135)*k1+(6656/12825)*k3+(28561/56430)*k4-(9/50)*k5+(2/55)*k6
		e = np.abs(RKF4[i+1] - RKF5[i+1])
		if (e > e_max and h > h_min):
			dt = dt/2
		else:
			i = i + 1
			t = t + dt
			x[i] = RKF5[i]
		if e < e_min:
			h = 2*h
	return y

a = 1
b = 1
g = 1
d = 1
y0 = np.array([4, 4])
dt = 0.1
lim = 15
error = 0.0000001
t = np.arange(0, lim+dt, dt)
t0 = 0
tf = 10
dt0 = 0.1
dt_min = 0.0001
dt_max = 0.1
e_min = 0.0001
e_max = 0.01
N = 10001




# Define function
def lotka(y, t, a, b, g, d):
	return np.array([y[0]*(a-b*y[1]), y[1]*(-g+d*y[0])])


#while (t<lim):



sol = RK(lotka, y0, t, dt, args=(a, b, g, d))

print(sol)


plt.plot(sol[:,0], sol[:,1], 'g', label='Approximate')
plt.show()





















