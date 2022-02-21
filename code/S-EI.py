# -*- coding: utf-8 -*-


from matplotlib import pyplot as plt
import numpy as np
import math
from scipy.interpolate import make_interp_spline



x = np.array([0.2,0.25,0.35,0.4,0.45,0.5,0.55,0.6,0.7,0.8,0.9])
gd = np.array([1.0,0.999745235889684,0.919545842,0.808605713928912,0.655175196129604,0.530534395410484,0.428247675200909,0.345223804448836,0.212864210218896,0.111471906416604,0.0361936160466356])
ln = np.array([0.999512610567368,0.999617000025949,0.837805901154055,0.706780686805408,0.602803825846772,0.520129625744287,0.454400341542054,0.396481795159299,0.308115092810207,0.241302865544645,0.192253374958010])

# x_new = np.linspace(x.min(), x.max(), 300)
# gd_smooth = make_interp_spline(x, gd)(x_new)
# ln_smooth = make_interp_spline(x, ln)(x_new)
# plt.plot(x_new, gd_smooth)
# plt.plot(x_new, ln_smooth)
# plt.xlabel('The weight of EI', fontsize=12)
# plt.ylabel('Optimal value of the proportion of economic forest', fontsize=12)
# plt.legend(['Guangdong Province', 'Liaoning Province'])
# plt.show()



x = np.array()
gd_bar = [0.428247675200909,0.345223804448836,0.212864210218896,0.111471906416604,0.0361936160466356]
ln_bar = [0.454400341542054,0.396481795159299,0.308115092810207,0.241302865544645,0.192253374958010]
plt.xlabel('The weight of EI', fontsize=12)
plt.ylabel('Optimal value of the proportion of economic forest', fontsize=12)
plt.legend(['Guangdong Province', 'Liaoning Province'])
plt.show()
