import sigplot as sp
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


matplotlib.rcParams['toolbar'] = 'None'
plt.style.use('dark_background')

fig = plt.figure()

# seed = np.linspace(3, 7, 1000)
# a = (np.sin(2 * np.pi * seed))
# b = (np.cos(2 * np.pi * seed))
# sp.correlate(fig, b, a, 300)

t = np.linspace(0, 1, 500)
b = (np.cos(2 * np.pi * t))
# x = np.concatenate([np.zeros(500), signal.sawtooth(2 * np.pi * 5 * t), np.zeros(500), np.ones(120), np.zeros(500)])
x = np.concatenate([np.zeros(500), np.ones(500), np.zeros(500)])
sp.fourier_series(fig, x, 100, 200, 200)

plt.show()

# WriteToVideo("twoPulse.mp4", anim);
