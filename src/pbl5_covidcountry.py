# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.stats.api as sm
import matplotlib.pyplot as plt
import math
from scipy import stats

df = pd.read_csv(r'Coviddata.csv')
df2 = pd.read_csv(r'CovidVacdata.csv')
###########################################
Us = df['UsCpM']
Kor = df['KorCpM']
Jap = df['JapCpM']
Isr = df['IsrCpM']
Eu = df['EuCpM']

UsVac = df2['UsTotalVac']
KorVac = df2['KorTotalVac']
JapVac = df2['JapTotalVac']
IsrVac = df2['IsrTotalVac']
EuVac = df2['EuTotalVac']

##############################################
###    Graph of New Cases per millions    ####
##############################################
x = np.arange(1,len(df)+1)
y1 = np.array(Us)
y2 = np.array(Kor)
y3 = np.array(Jap)
y4 = np.array(Isr)
y5 =  np.array(Eu)

f = plt.figure()
f.set_figwidth(20)
f.set_figheight(5)

plt.title("New cases per million")
plt.plot(x,y1,label="US")
plt.plot(x,y2,label="Korea")
plt.plot(x,y3,label="Japan")
plt.plot(x,y4,label="Israel")
plt.plot(x,y5,label="EU")
plt.legend()

##############################################
### Graph of Total Vaccination per hundred ###
##############################################

x2 = np.arange(1,len(df2)+1)
z1 = np.array(UsVac)
z2 = np.array(KorVac)
z3 = np.array(JapVac)
z4 = np.array(IsrVac)
z5 =  np.array(EuVac)

f = plt.figure()
f.set_figwidth(20)
f.set_figheight(5)

plt.title("Total Vac per hundred")
plt.plot(x2,z1,label="US")
plt.plot(x2,z2,label="Korea")
plt.plot(x2,z3,label="Japan")
plt.plot(x2,z4,label="Israel")
plt.plot(x2,z5,label="EU")
plt.legend()

################################################
###        SIR model of each country        ####
################################################










