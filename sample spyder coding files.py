# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 20:37:20 2022

@author: krishnappa
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sandeep = pd.read_csv('CSCO Historical Data.csv,uscols= [0,1,2,3,4]')


POHL_avg = sandeep[['Price', 'Open', 'High', 'Low']].mean(axis = 1)



obs = np.arange(1,len(sandeep)+1,1)


plt.plot(obs,POHL_avg,'r',label = 'MY FIRST PLOT')