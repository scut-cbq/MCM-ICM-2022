# -*- coding: utf-8 -*-
# file_name: product_graphy.py
# function: draw the graphy of the product


from matplotlib import pyplot as plt
import numpy as np
import math
from scipy.interpolate import make_interp_spline


V = 1
D = 1
SB = 1
BT = 1
TD = 1
Cc = np.array([0.3, 0.4, 0.45, 0.3, 0.2, 0.1])
csf = (V*D*SB*BT*(1+TD))*Cc

paper = []
transportation = []
plywood = []
n1 = 0
n2 = 0
n3 = 0
cur1 = 0
cur2 = 0
cur3 = 0

for i in range(80):
    if i == 0:
        continue
    n1 += 1
    n2 += 1
    n3 += 1
    n1 = min(n1, 5)
    n2 = min(n2, 5)
    n3 = min(n3, 5)
    if i % 5 == 0:
        n1 = 0
        cur1 -= 2
    cur1 += csf[n1]
    paper.append(cur1)
    if i % 12 == 0:
        n2 = 0
        cur2 -= 0.1
    cur2 += csf[n2]
    transportation.append(cur2)
    if i % 8 == 0:
        n3 = 0
        cur3 -= 1
    cur3 += csf[n3]
    plywood.append(cur3)


print(paper[0])
print(transportation[0])
print(plywood[0])
x = np.array(range(79))
plt.plot(x, np.array(paper))
plt.plot(x, np.array(transportation))
plt.plot(x, np.array(plywood))

plt.xlabel('Month', fontsize=12)
plt.ylabel('TAFP (Tg)', fontsize=12)
plt.legend(['Paper', 'Transportation', 'Plywood'])
plt.show()