#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 21:12:28 2021

@author: Chokeunhee
"""
# Covid19 Korea SIR model

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv(r'ISRSIRMODEL.csv')

#Pop = 50000000
#Pop = 126000000
Pop = 8600000
#Pop = 330000000

Con = df["Confirmed"]
Dea = df["Death"]
Rec = df["Recovered"]
Vac = df["Full_Vac"]
#Tim = df["Day"]

S = (Pop - Con - Vac) / Pop
I = (Con - Rec - Dea) / Pop
R = (Rec + Dea) / Pop
V = Vac / Pop

Sprime = S.diff()
Iprime = I.diff()
Rprime = R.diff()

#Beta = -(S * I) / Sprime / Pop
#mu = I / Rprime
#print(Beta)


plt.ticklabel_format(style = 'plain')

plt.plot (S,label="Susceptible")
#plt.plot (I,label="Infected")
#plt.plot (R,label="Recovered")
#plt.plot (V,label="Vaccinated")

#plt.plot (Con/Pop,label="confirmed")
#plt.plot (Dea/Pop,label="fatal")
#plt.plot (Rec/Pop,label="Recovered")

#plt.plot (Vac)

#plt.plot(Beta)

plt.legend()
plt.show()
