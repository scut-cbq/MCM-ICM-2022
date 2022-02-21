# -*- coding: utf-8 -*-


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {'gd': [0.439830016, 0.552958633, 0.503944845, 0.7,
               0.555947277, 0.197816111, 0.8923562, 0.355969275,
               0.377321262, 0.636620192, 0.2116846, 0.453234457],
        'ln': [-0.329713323, -0.237138567, -0.249518089, -0.2,
               -0.297369167, -0.354343694, -0.4236895, -0.149344251,
               -0.358715649, -0.850493638, -0.12069414, -0.254032671],
        'index': ['FBI', 'SI', '$\mathregular{SI_2}$', '$\mathregular{SI_1}$', 'ECI', '$\mathregular{ECI_3}$',
                  '$\mathregular{ECI_2}$', '$\mathregular{ECI_1}$', 'EI', '$\mathregular{EI_3}$',
                  '$\mathregular{EI_2}$', '$\mathregular{EI_1}$'],
        }
Pyramid_Data = pd.DataFrame(data)
bar_plot = sns.barplot(y='index', x="gd", color="red", data=Pyramid_Data,
                       order=['FBI', 'SI', '$\mathregular{SI_2}$', '$\mathregular{SI_1}$', 'ECI', '$\mathregular{ECI_3}$',
                  '$\mathregular{ECI_2}$', '$\mathregular{ECI_1}$', 'EI', '$\mathregular{EI_3}$',
                  '$\mathregular{EI_2}$', '$\mathregular{EI_1}$'],
                       label='Guangdong Province')
bar_plot = sns.barplot(y='index', x="ln", color="g", data=Pyramid_Data,
                       order=['FBI', 'SI', '$\mathregular{SI_2}$', '$\mathregular{SI_1}$', 'ECI', '$\mathregular{ECI_3}$',
                  '$\mathregular{ECI_2}$', '$\mathregular{ECI_1}$', 'EI', '$\mathregular{EI_3}$',
                  '$\mathregular{EI_2}$', '$\mathregular{EI_1}$'],
                       label='Liaoning Province')
plt.xticks([-1, -0.5, 0, 0.5, 1], [1, 0.5, 0, 0.5, 1, ])
# sns is seaborn alias

plt.xlabel('Score', fontsize=12)
plt.ylabel('Indicator', fontsize=12)
plt.legend(loc='upper left')
plt.show()
