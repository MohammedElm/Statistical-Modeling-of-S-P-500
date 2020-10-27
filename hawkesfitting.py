# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 20:58:52 2020

@author: Mohammed EL MENDILI
"""

from MHP import MHP
import pandas as pd
import numpy as np


data=pd.read_csv("data_hawkes_20112019.csv")

data=list(data["Date"])
data=[[data[i], np.array([0])] for i in range(len(data))]

#Validation
P1 = MHP(alpha=[[0.44121204]],mu=[0.03842521],omega=0.23)
#P1.generate_seq(4000)
P1.data=data
P1.plot_events()
#P1.plot_rates()
residuals=P1.get_residuals()

import pylab 
import scipy.stats as stats

measurements = residuals  
#qq=stats.probplot(measurements, dist="expon", plot=plt)
#print("R-square is {}".format(qq[1][-1]))
#plt.savefig("QQ_hawkes2011_2019")
plt.show()

#P2 = MHP(alpha=[[0.09]],mu=[0.2],omega=0.8)
#P2.generate_seq(230)
#P2.data=data
#P2.plot_events()
#P2.plot_rates()

#P=MHP(omega=.8)
#P.data=data
mhat = np.random.uniform(0,1, size=1)
ahat = np.random.uniform(0,1, size=(1,1))
w = 0.8
#P.plot_events()

#print(P1.EM(ahat, mhat, w))

