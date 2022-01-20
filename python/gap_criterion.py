#!/usr/bin/env python
### gap opening mass vs visousity and disk aspect ratio 
### Extened Data Figure 8 of Liu_etal_2021
import matplotlib.pyplot as plt
import numpy as np
import math
import string
import os
import csv
import pylab
from plotset import *
import subprocess as sp




# gap-opening planet-to-star mass ratio based on Crida+2006
def q_gap (q,alpha, h):  # q is given by an array 
    P1 = 0.75*h/(q/3.0)**(1./3)
    P2 = 1.0 - 50*alpha*h**2/q
    nlist = np.argmin(abs(P1-P2))
    q1 = q[nlist]
    q2 = 3*h**3
    res = min(q1,q2)
    return res 

k1 = 1000
k2 = 100
alpha = np.linspace(5e-5,1e-2,k1)
h = np.linspace(1.5e-2,8e-2,k2)
mgap  = np.zeros((k2,k1))
M_Jupiter = 317.8*np.ones(k1)
M_Saturn = 95.2*np.ones(k1)
M_Uranus = 14.5*np.ones(k1)
M_Neptune = 17.2*np.ones(k1)
q_sun_Earth = 3.33e+5


q_tmp = np.logspace(-5,-2.5,1000)
for i in range(k2):
    for j in range(k1):
        mgap[i][j] = q_gap (q_tmp,alpha[j], h[i])*q_sun_Earth  


plt.clf()
plt.close("all")
plt.figure(num = 2, figsize=(6,5))
cmap = 'viridis'
levels = np.linspace(0.5,2.8,100)
CS = plt.contourf(alpha, h, np.log10(mgap), levels, cmap =cmap)
plt.contour(alpha, h, np.log10(mgap),  [np.log10(10), np.log10(14.5),  np.log10(17.2), np.log10(95.2), np.log10(317.8)], colors=['grey','grey','grey', 'grey','grey'],linestyles=['--','-','-','-','-'], linewidths= [1.2, 1.8,1.8,2.7,4])


plt.scatter(5e-3,0.06,s=100,marker ='o',c='r',alpha=0.6)
plt.text(4.7e-3,0.055,'P0',c='k',fontsize=8)
plt.scatter(1e-3,0.058,s=100,marker ='s',c='r',alpha=0.6)
plt.text(0.96e-3,0.053,'P1',c='k',fontsize=8)
plt.scatter(5e-4,0.03,s=100,marker ='v',c='m',alpha=0.6)
plt.text(4.6e-4,0.025,'P2',c='k',fontsize=8)
plt.scatter(1e-4,0.04,s=100,marker ='d',c='m',alpha=0.6)
plt.text(0.95e-4,0.035,'P4',c='k',fontsize=8)
plt.scatter(2e-4,0.05,s=100,marker ='^',c='m',alpha=0.6)
plt.text(1.8e-4,0.044,'P3',c='k',fontsize=9)
plt.scatter(1e-4,0.027,s=100,marker ='p',c='darkorange',alpha=0.6)
plt.text(0.95e-4,0.023,'P5',c='k',fontsize=9)
plt.text(8e-3,0.07,'$\\rm J$', color='grey', fontsize=14)
plt.text(8e-3,0.04,'$\\rm S$', color='grey', fontsize=14)
plt.text(6e-5,0.033,'$\\rm N$', color='grey', fontsize=12)
plt.text(6e-5,0.027,'$\\rm U$', color='grey', fontsize=12)
plt.text(6.8e-3,0.017,'$\\rm 8 \\ M_{\\oplus}$', color='grey', fontsize=10)
plt.semilogx()
plt.xticks([1e-4,1e-3,1e-2],['$10^{-4}$','$10^{-3}$','$10^{-2}$'],fontsize=fs1)
plt.yticks([0.03,0.05,0.07],['$0.03$','$0.05$','$0.07$'],fontsize=fs1)
plt.xlabel('$\\rm viscous \\ \\alpha_{\\rm t} $',fontsize=fs1)
plt.ylabel('$\\rm disk \\ aspect \\ ratio$',fontsize=fs1)
plt.xlim(5e-5,1e-2)
plt.ylim(0.015,0.08)
cb1 = plt.colorbar(CS, cmap=cmap, norm=levels,ticks=[1,1.5,2,2.5], orientation='horizontal')
cb1.ax.set_xlabel(' $ \\rm gap \\ opening \\ mass  \\ [M_{\\oplus}]$',fontsize=13)
cb1.ax.set_xticklabels(['$10$','$30$','$100$','$300$'],fontsize=13)


plt.savefig('../figure/gap.pdf',orientation='landscape', format='pdf',bbox_inches='tight', pad_inches=0.1)
