# -*- coding: utf-8 -*-


import pygal
import numpy as np
import matplotlib.pyplot as plt


import numpy as np
import matplotlib.pyplot as plt
import matplotlib


matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
labels = np.array(['EI', 'ECI', 'SI', 'FBI'])
nAttr = 4
before = np.array([0.358715649, 0.297369167, 0.237138567, 0.329713323])
after = np.array([0.33229556, 0.370293758, 0.500051171, 0.361631087])
angles = np.linspace(0, 2*np.pi, nAttr, endpoint=False)
before = np.concatenate((before, [before[0]]))
after = np.concatenate((after, [after[0]]))
angles = np.concatenate((angles, [angles[0]]))
labels = np.concatenate((labels, [labels[0]]))
fig = plt.figure(facecolor="white")
plt.subplot(111, polar=True)
plt.plot(angles, before, color='g', linewidth=2)
plt.fill(angles, before, facecolor='g', alpha=0.25)
plt.plot(angles, after, color='r', linewidth=2)
plt.fill(angles, after, facecolor='r', alpha=0.25)
plt.thetagrids(angles*180/np.pi, labels, fontsize=12)
plt.grid(True)
plt.ylim(0, 1)
plt.legend(['before', 'after'])
plt.show()

