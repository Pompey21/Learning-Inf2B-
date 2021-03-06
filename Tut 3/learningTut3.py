import numpy as np
import scipy.stats as stats
import math
import matplotlib.pyplot as plt


mu = 0
variance = 0.1
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.show()

