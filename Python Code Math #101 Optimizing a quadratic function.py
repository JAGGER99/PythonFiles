import numpy as np
objective = np.poly1d([1.3,4.0,0.6])
print(objective)

import scipy.optimize as opt
x_ = opt.fmin(objective, 3)

x = np.linspace(-4,1, 1000)
import matplotlib.pylab as mpl
mpl.plot(x, objective(x))
mpl.plot(x_, objective(x_), 'ro')
