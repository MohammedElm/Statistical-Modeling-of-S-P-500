# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:26:01 2020

@author: Mohammed EL MENDILI
"""

from MHP import MHP


m = np.array([0.2, 0.0, 0.0])
a = np.array([[0.1, 0.0, 0.0], 
              [0.9, 0.0, 0.0],
              [0.0, 0.9, 0.0]])
w = 3.1

P = MHP(mu=m, alpha=a, omega=w)
P.generate_seq(60)
print(P.get_integral())
P.plot_rates()