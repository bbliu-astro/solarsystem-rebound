#!/usr/bin/env python
### culmulative distributions of instability time, 
### culmulative distributions of delay time between ice and gas giant planets 
### Extended Data Figure 10 of Liu_etal_2022
import matplotlib.pyplot as plt
import numpy as np
import math
import string
import os
import csv
import pylab
import time
import sys
from plotset import *
from modelfunction import *
from scipy.interpolate import griddata
import subprocess as sp


######################
### Main rountine ####
######################

plt.close("all")
fig, [ax1,ax2] = plt.subplots(1,2, figsize=(9,4), num= 10)
fig.subplots_adjust(wspace=0.1)
colors =['k','c', 'b','c','orange','c']
b_list = [-1e+4,-5e+3]+list(np.linspace(0,7.5e+4,40))

for i in range(5):
    # we choose run_P0/P2/P4 for illustration 
    if i == 0 or i == 2 or i == 4: 
        fnum = str(i)
        fil1 = open('../data/low_vis/data5_ins'+ fnum+'.csv','r')
        reader1 = csv.reader(fil1)
        data_ins1 = []
        for line in reader1:
            data_ins1.append(float(line[0]))
        fil1.close()
        fil2 = open('../data/low_vis/data5_int'+ fnum+'.csv','r')
        reader2 = csv.reader(fil2)
        data_ins2 = []
        for line in reader2:
            data_ins2.append(float(line[0]))
        fil2.close()
        
        values1, base = np.histogram(data_ins1,bins=100)
        cumulative =np.cumsum(values1)/sum(values1)
        line, = ax1.plot(base[:-1],cumulative, c=colors[i],linewidth=3,alpha=0.7,label='run_B5R_P'+str(i))
        ax1.legend()
        values2, base = np.histogram(data_ins2,bins=b_list)
        cumulative2 =np.cumsum(values2)/sum(values2)
        ax2.plot(base[:-1],cumulative2, c=colors[i],linewidth=3,alpha=0.7)

ax1.set_xlim([0,1e+7])
ax1.text(2e+4,0.94, '(a)',fontsize= 11)
ax2.text(-0.9e+4,0.94, '(b)',fontsize= 11)
ax1.set_xticks([0,2.5e+6,5e+6,7.5e+6])
ax1.set_xticklabels(['$0$','$2.5$','$5$','$7.5$'],fontsize=fs1)
ax1.set_yticks([0.25,0.5,0.75])
ax1.set_yticklabels(['$0.25$','$0.5$','$0.75$'],fontsize=fs1)
ax1.set_ylabel('Cumulative distribution',fontsize =fs1)
ax1.set_ylim([0,1])
ax1.set_ylabel('Cumulative distribution',fontsize =fs1)
ax1.set_xlabel('$t_{\\rm ins} \\  \\rm [Myr]$',fontsize =fs1)
ax1.tick_params(axis='both',        
                which='both',     
                bottom=True,
                labelbottom=True,
                top=True,
                left= True,
                right=True) 
        
ax2.set_ylim([0,1])
ax2.set_xlim([-1e+4,7.e+4])
ax2.set_yticks([0.25,0.5,0.75])
ax2.set_yticklabels(['$0.25$','$0.5$','$0.75$'],fontsize=fs1)
ax2.set_xticks([-1e+4,0,2.5e+4,5e+4])
ax2.set_xticklabels(['$-10$','$0$','$25$','$50$'],fontsize=fs1)
ax2.set_xlabel('$t_{\\rm ins, gas} -t_{\\rm ins, ice} \\ \\rm [kyr]$',fontsize =fs1)
ax2.tick_params(axis='both',         
                which='both',     
                bottom=True,
                labelbottom=True,
                labelleft =False,
                top=True,
                left= True,
                right=True,
                labelright=False) 

plt.savefig('../figure/cul.pdf',orientation='landscape', format='pdf',bbox_inches='tight', pad_inches=0.01)
        
