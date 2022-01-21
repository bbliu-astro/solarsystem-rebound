#!/usr/bin/env python
### Jupiter eccentricity mode vs visousity Jupiter-Saturn period ratio 
### Extened Data Figure 7 of Liu_etal_2022
import matplotlib.pyplot as plt
import numpy as np
import math
import string
import os
import sys
import csv
import pylab
from mpl_toolkits.axes_grid1 import make_axes_locatable
from plotset import *
from modelfunction import *
from secularequation import *

savedir = '../figure/'
opt_rebound = True 
opt_plt = True




plt.clf()  # clear image
plt.close('all') # delete figure
fig, ax = plt.subplots(1,figsize=(8,5), num= 1 )

fig.subplots_adjust(wspace=0.15)



s_s = 25
s_s0 = 40

# solar system values 
P_JS = 2.49 
eccJ  = 0.044
ax.scatter(P_JS,eccJ,s=80, c='r',edgecolors='r', marker='*') 

ax.set_xlim(2,3.4)
ax.set_xticks([2,2.5,3])
ax.set_xticklabels(['$2$','$2.5$','$3$'],fontsize=13)
ax.set_ylim(1e-3,0.1)
ax.set_yticks([1e-3,1e-2,1e-1])
ax.set_yticklabels(['$10^{-3}$','$0.01$','$0.1$'],fontsize=13)
ax.semilogy()
ax.set_ylabel('$\\rm Jupiter \\ eccentricity \\ mode \\ |M_{55}|$',fontsize=13)
ax.set_xlabel('$\\rm Period \\ ratio \\ of  \\ Jupiter$-$\\rm Saturn$',fontsize=13)
ax.scatter(2.05,2.1e-3,s=80, c='r',edgecolors='r', marker='*') 
ax.text(2.1,1.98e-3,'Solar System',fontsize=11)
ax.scatter(2.05,1.64e-3,s=s_s, c='m',edgecolors='m', marker='^') 
ax.text(2.1,1.55e-3,'simulations without planetesimal disk' ,fontsize=11)
ax.scatter(2.05,1.28e-3,s=s_s, c='b',edgecolors='b', marker='o') 
ax.text(2.1,1.2e-3,'simulations with planetesimal disk' ,fontsize=11)




### example2 ###
### W/O plt disk ###
samplesemi_m = [4.97, 11.01]
sampleecc_m =  [0.0205, 0.09075]
samplemass = [9.54e-4,2.86e-4]
samplew_m = [4.75,4.28] # rad
g, eccM_m = cal_eccmode(samplesemi_m,samplemass,sampleecc_m,samplew_m)
P_m = (samplesemi_m[1]/samplesemi_m[0])**1.5


### with plt disk ###
### with plt disk of 5,10,20 Earth mass (resolution of N=500) ###
samplesemi_5 = [4.94814, 11.07168]
sampleecc_5 = [0.03326, 0.026672]
samplew_5 = 2*np.pi/180*np.array([115.604, 63.396]) 

samplesemi_10 = [4.92294, 11.22070]
sampleecc_10 = [ 0.012297,0.027623]
samplew_10 = 2*np.pi/180*np.array([ 94.983,  324.143]) 

samplesemi_20 = [ 4.87485, 11.41211]
sampleecc_20 = [ 0.021446, 0.025800]
samplew_20 = 2*np.pi/180*np.array([ 245.992,  141.854]) 

g, eccM_5 = cal_eccmode(samplesemi_5,samplemass,sampleecc_5,samplew_5)
P_5 = (samplesemi_5[1]/samplesemi_5[0])**1.5
g, eccM_10 = cal_eccmode(samplesemi_10,samplemass,sampleecc_10,samplew_10)
P_10 = (samplesemi_10[1]/samplesemi_10[0])**1.5
g, eccM_20 = cal_eccmode(samplesemi_20,samplemass,sampleecc_20,samplew_20)
P_20 = (samplesemi_20[1]/samplesemi_20[0])**1.5

### with plt disk of 5,10,20 Earth mass (resolution of N=1000) ###
samplesemi_20_high = [ 4.87949, 11.56563]
sampleecc_20_high = [0.02619, 0.021397 ]
samplew_20_high =  2*np.pi/180*np.array([ 59.029, 99.406])

samplesemi_10_high = [ 4.92848, 11.20751]
sampleecc_10_high = [0.001437, 0.0465 ]
samplew_10_high =   2*np.pi/180*np.array([267.302,  219.958])

samplesemi_5_high = [4.95002, 11.07764 ]
sampleecc_5_high = [0.041728, 0.062259 ]
samplew_5_high =  2*np.pi/180*np.array([ 119.268,   183.533])

g, eccM_5_high = cal_eccmode(samplesemi_5_high,samplemass,sampleecc_5_high,samplew_5_high)
P_5_high = (samplesemi_5_high[1]/samplesemi_5_high[0])**1.5
g, eccM_10_high = cal_eccmode(samplesemi_10_high,samplemass,sampleecc_10_high,samplew_10_high)
P_10_high = (samplesemi_10_high[1]/samplesemi_10_high[0])**1.5
g, eccM_20_high = cal_eccmode(samplesemi_20_high,samplemass,sampleecc_20_high,samplew_20_high)
P_20_high = (samplesemi_20_high[1]/samplesemi_20_high[0])**1.5


### W/O plt disk ###
if opt_rebound == True: 
    ax.scatter(P_m,abs(eccM_m[0][0]),s=s_s0, c='m',edgecolors='m', marker='^') 
    
if opt_plt == True: 
    ax.scatter(P_5,abs(eccM_5[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_10,abs(eccM_10[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_20,abs(eccM_20[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_5_high,abs(eccM_5_high[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_10_high,abs(eccM_10_high[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_20_high,abs(eccM_20_high[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 



### example3 ###
### W/O plt disk ###
samplesemi_m = [5.207, 9.677]
sampleecc_m =  [0.01288, 0.0738]
samplemass = [9.54e-4,2.86e-4]
samplew_m = [4.11,2.14] # rad
g, eccM_m = cal_eccmode(samplesemi_m,samplemass,sampleecc_m,samplew_m)
P_m = (samplesemi_m[1]/samplesemi_m[0])**1.5

### with plt disk ###
### with plt disk of 5,10,20 Earth mass (resolution of N=500) ###
samplesemi_5 = [ 5.17745, 9.74978]
sampleecc_5 = [ 0.012186,  0.060560]
samplew_5 = 2*np.pi/180*np.array([ 114.313, 350.176])

samplesemi_10 = [5.14447, 9.94205]
sampleecc_10 = [ 0.007848, 0.044276]
samplew_10 = 2*np.pi/180*np.array([ 45.926,  154.642])

samplesemi_20 = [ 5.07651,  10.26521]
sampleecc_20 = [ 0.010725, 0.013393]
samplew_20 = 2*np.pi/180*np.array([ 315.314, 96.743])

g, eccM_5 = cal_eccmode(samplesemi_5,samplemass,sampleecc_5,samplew_5)
P_5 = (samplesemi_5[1]/samplesemi_5[0])**1.5
g, eccM_10 = cal_eccmode(samplesemi_10,samplemass,sampleecc_10,samplew_10)
P_10 = (samplesemi_10[1]/samplesemi_10[0])**1.5
g, eccM_20 = cal_eccmode(samplesemi_20,samplemass,sampleecc_20,samplew_20)
P_20 = (samplesemi_20[1]/samplesemi_20[0])**1.5

### with plt disk of 5,10,20 Earth mass (resolution of N=1000) ###
samplesemi_20_high = [ 5.08465, 10.07701]
sampleecc_20_high = [ 0.007096, 0.012128 ]
samplew_20_high =  2*np.pi/180*np.array([ 311.820, 133.836])

samplesemi_10_high = [ 5.14983, 9.89291]
sampleecc_10_high = [ 0.009257, 0.0436 ]
samplew_10_high =   2*np.pi/180*np.array([ 43.564,  299.789])

samplesemi_5_high = [ 5.1780, 9.80281 ]
sampleecc_5_high = [ 0.032132, 0.034498 ]
samplew_5_high =  2*np.pi/180*np.array([ 346.391,  186.669])

g, eccM_5_high = cal_eccmode(samplesemi_5_high,samplemass,sampleecc_5_high,samplew_5_high)
P_5_high = (samplesemi_5_high[1]/samplesemi_5_high[0])**1.5
g, eccM_10_high = cal_eccmode(samplesemi_10_high,samplemass,sampleecc_10_high,samplew_10_high)
P_10_high = (samplesemi_10_high[1]/samplesemi_10_high[0])**1.5
g, eccM_20_high = cal_eccmode(samplesemi_20_high,samplemass,sampleecc_20_high,samplew_20_high)
P_20_high = (samplesemi_20_high[1]/samplesemi_20_high[0])**1.5


if opt_rebound == True: 
    ax.scatter(P_m,abs(eccM_m[0][0]),s=s_s0, c='m',edgecolors='m', marker='^') 
    
if opt_plt == True: 
    ax.scatter(P_5,abs(eccM_5[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_10,abs(eccM_10[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_20,abs(eccM_20[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_5_high,abs(eccM_5_high[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_10_high,abs(eccM_10_high[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_20_high,abs(eccM_20_high[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 


### example4 ###
### W/O plt disk ###
samplesemi_m = [5.029, 10.12]
sampleecc_m =  [0.01853, 0.02169]
samplemass = [9.54e-4,2.86e-4]
samplew_m = [2.64,1.52] # rad
g, eccM_m = cal_eccmode(samplesemi_m,samplemass,sampleecc_m,samplew_m)
P_m = (samplesemi_m[1]/samplesemi_m[0])**1.5


### with plt disk of 5,10,20 Earth mass (resolution of N=500) ###
samplesemi_5 = [ 5.0043, 10.2139]
sampleecc_5 = [ 0.025,  0.022]
samplew_5 = 2*np.pi/180*np.array([ 345.108, 259.863])

samplesemi_10 = [4.9839, 10.2796]
sampleecc_10 = [ 0.018, 0.013]
samplew_10 = 2*np.pi/180*np.array([ 96.432,  58.36])

samplesemi_20 = [ 4.9253,  10.6247]
sampleecc_20 = [ 0.01, 0.012]
samplew_20 = 2*np.pi/180*np.array([ 126.08, 159.626])

g, eccM_5 = cal_eccmode(samplesemi_5,samplemass,sampleecc_5,samplew_5)
P_5 = (samplesemi_5[1]/samplesemi_5[0])**1.5
g, eccM_10 = cal_eccmode(samplesemi_10,samplemass,sampleecc_10,samplew_10)
P_10 = (samplesemi_10[1]/samplesemi_10[0])**1.5
g, eccM_20 = cal_eccmode(samplesemi_20,samplemass,sampleecc_20,samplew_20)
P_20 = (samplesemi_20[1]/samplesemi_20[0])**1.5

### with plt disk of 5,10,20 Earth mass (resolution of N=1000) ###
samplesemi_20_high = [ 4.9334, 10.5251]
sampleecc_20_high = [  0.009, 0.012 ]
samplew_20_high =  2*np.pi/180*np.array([ 269.732, 156.422])

samplesemi_10_high = [ 4.9798, 10.3744]
sampleecc_10_high = [ 0.013,  0.015]
samplew_10_high =   2*np.pi/180*np.array([ 257.385,  17.387])

samplesemi_5_high = [ 5.0077, 10.1672 ]
sampleecc_5_high = [ 0.02, 0.015 ]
samplew_5_high =  2*np.pi/180*np.array([ 65.56,  6.909])

g, eccM_5_high = cal_eccmode(samplesemi_5_high,samplemass,sampleecc_5_high,samplew_5_high)
P_5_high = (samplesemi_5_high[1]/samplesemi_5_high[0])**1.5
g, eccM_10_high = cal_eccmode(samplesemi_10_high,samplemass,sampleecc_10_high,samplew_10_high)
P_10_high = (samplesemi_10_high[1]/samplesemi_10_high[0])**1.5
g, eccM_20_high = cal_eccmode(samplesemi_20_high,samplemass,sampleecc_20_high,samplew_20_high)
P_20_high = (samplesemi_20_high[1]/samplesemi_20_high[0])**1.5


if opt_rebound == True: 
    ax.scatter(P_m,abs(eccM_m[0][0]),s=s_s0, c='m',edgecolors='m', marker='^') 
    
if opt_plt == True: 
    ax.scatter(P_5,abs(eccM_5[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_10,abs(eccM_10[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_20,abs(eccM_20[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_5_high,abs(eccM_5_high[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_10_high,abs(eccM_10_high[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_20_high,abs(eccM_20_high[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 



### example5 ###
### W/O plt disk ###
samplesemi_m = [5.074, 10.83]
sampleecc_m =  [ 0.03042, 0.07266]
samplemass = [9.54e-4,2.86e-4]
samplew_m = [1.37,4.52] # rad
g, eccM_m = cal_eccmode(samplesemi_m,samplemass,sampleecc_m,samplew_m)
P_m = (samplesemi_m[1]/samplesemi_m[0])**1.5


### with plt disk ###
### with plt disk of 5,10,20 Earth mass (resolution of N=500) ###
samplesemi_5 = [ 5.0598, 10.9404]
sampleecc_5 = [0.017, 0.045]
samplew_5 = 2*np.pi/180*np.array([82.568, 282.027])

samplesemi_10 = [5.0341, 10.9487]
sampleecc_10 = [ 0.014, 0.015]
samplew_10 = 2*np.pi/180*np.array([ 290.79,  155.297])

samplesemi_20 = [ 4.9955, 11.1392]
sampleecc_20 = [ 0.004, 0.004]
samplew_20 = 2*np.pi/180*np.array([ 125.448,  121.246])

g, eccM_5 = cal_eccmode(samplesemi_5,samplemass,sampleecc_5,samplew_5)
P_5 = (samplesemi_5[1]/samplesemi_5[0])**1.5
g, eccM_10 = cal_eccmode(samplesemi_10,samplemass,sampleecc_10,samplew_10)
P_10 = (samplesemi_10[1]/samplesemi_10[0])**1.5
g, eccM_20 = cal_eccmode(samplesemi_20,samplemass,sampleecc_20,samplew_20)
P_20 = (samplesemi_20[1]/samplesemi_20[0])**1.5

### with plt disk of 5,10,20 Earth mass (resolution of N=1000) ###
samplesemi_20_high = [ 4.9916, 11.1799]
sampleecc_20_high = [0.009,  0.012]
samplew_20_high =  2*np.pi/180*np.array([ 140.519, 242.584])

samplesemi_10_high = [ 5.0359, 11.0462]
sampleecc_10_high = [0.030, 0.033 ]
samplew_10_high =   2*np.pi/180*np.array([132.101, 228.2])

samplesemi_5_high = [5.0573, 10.9199 ]
sampleecc_5_high = [ 0.022, 0.035 ]
samplew_5_high =  2*np.pi/180*np.array([ 33.952, 216.277])

g, eccM_5_high = cal_eccmode(samplesemi_5_high,samplemass,sampleecc_5_high,samplew_5_high)
P_5_high = (samplesemi_5_high[1]/samplesemi_5_high[0])**1.5
g, eccM_10_high = cal_eccmode(samplesemi_10_high,samplemass,sampleecc_10_high,samplew_10_high)
P_10_high = (samplesemi_10_high[1]/samplesemi_10_high[0])**1.5
g, eccM_20_high = cal_eccmode(samplesemi_20_high,samplemass,sampleecc_20_high,samplew_20_high)
P_20_high = (samplesemi_20_high[1]/samplesemi_20_high[0])**1.5


if opt_rebound == True: 
    ax.scatter(P_m,abs(eccM_m[0][0]),s=s_s0, c='m',edgecolors='m', marker='^') 
    
if opt_plt == True: 
    ax.scatter(P_5,abs(eccM_5[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_10,abs(eccM_10[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_20,abs(eccM_20[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_5_high,abs(eccM_5_high[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_10_high,abs(eccM_10_high[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_20_high,abs(eccM_20_high[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 




### example6 ###
### W/O plt disk ###
samplesemi_m = [5.02, 10.56]
sampleecc_m =  [ 0.01393, 0.1215]
samplemass = [9.54e-4,3.29e-4]
samplew_m = [0.05,1.05] # rad
g, eccM_m = cal_eccmode(samplesemi_m,samplemass,sampleecc_m,samplew_m)
P_m = (samplesemi_m[1]/samplesemi_m[0])**1.5

### with plt disk ###
### with plt disk of 5,10,20 Earth mass (resolution of N=500) ###
samplesemi_5 = [4.9973, 10.7201]
sampleecc_5 = [0.061, 0.039]
samplew_5 = 2*np.pi/180*np.array([178.199, 26.543])

samplesemi_10 = [4.9711, 10.8352]
sampleecc_10 = [ 0.012,0.045]
samplew_10 = 2*np.pi/180*np.array([ 164.11,  37.785])

samplesemi_20 = [ 4.929, 10.9477]
sampleecc_20 = [ 0.013, 0.037]
samplew_20 = 2*np.pi/180*np.array([ 56.022,  72.155])

g, eccM_5 = cal_eccmode(samplesemi_5,samplemass,sampleecc_5,samplew_5)
P_5 = (samplesemi_5[1]/samplesemi_5[0])**1.5
g, eccM_10 = cal_eccmode(samplesemi_10,samplemass,sampleecc_10,samplew_10)
P_10 = (samplesemi_10[1]/samplesemi_10[0])**1.5
g, eccM_20 = cal_eccmode(samplesemi_20,samplemass,sampleecc_20,samplew_20)
P_20 = (samplesemi_20[1]/samplesemi_20[0])**1.5

### with plt disk of 5,10,20 Earth mass (resolution of N=1000) ###
samplesemi_20_high = [ 4.917, 11.023]
sampleecc_20_high = [0.03, 0.012 ]
samplew_20_high =  2*np.pi/180*np.array([ 271.191, 17.141])


samplesemi_5_high = [4.9959, 10.6544 ]
sampleecc_5_high = [0.053, 0.056 ]
samplew_5_high =  2*np.pi/180*np.array([ 269.329,   136.065])

g, eccM_5_high = cal_eccmode(samplesemi_5_high,samplemass,sampleecc_5_high,samplew_5_high)
P_5_high = (samplesemi_5_high[1]/samplesemi_5_high[0])**1.5
g, eccM_20_high = cal_eccmode(samplesemi_20_high,samplemass,sampleecc_20_high,samplew_20_high)
P_20_high = (samplesemi_20_high[1]/samplesemi_20_high[0])**1.5

if opt_rebound == True: 
    ax.scatter(P_m,abs(eccM_m[0][0]),s=s_s0, c='m',edgecolors='m', marker='^') 
    
if opt_plt == True: 
    ax.scatter(P_5,abs(eccM_5[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_10,abs(eccM_10[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_20,abs(eccM_20[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_5_high,abs(eccM_5_high[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_20_high,abs(eccM_20_high[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 




### example7 ###
### W/O plt disk ###
samplesemi_m = [5.116, 10.79]
sampleecc_m =  [0.01651, 0.1052]
samplemass = [9.97e-4,2.86e-4]
samplew_m = [4.75,4.37] # rad
g, eccM_m = cal_eccmode(samplesemi_m,samplemass,sampleecc_m,samplew_m)
P_m = (samplesemi_m[1]/samplesemi_m[0])**1.5

### with plt disk ###
### with plt disk of 5,10,20 Earth mass (resolution of N=500) ###
samplesemi_5 = [5.0974, 10.79]
sampleecc_5 = [0.027, 0.049]
samplew_5 = 2*np.pi/180*np.array([114.057, 359.889])

samplesemi_10 = [5.0711, 10.9871]
sampleecc_10 = [ 0.016,0.05]
samplew_10 = 2*np.pi/180*np.array([ 38.986,  276.702])

samplesemi_20 = [ 5.0343, 11.2112]
sampleecc_20 = [ 0.005, 0.027]
samplew_20 = 2*np.pi/180*np.array([ 7.123,  91.702])

g, eccM_5 = cal_eccmode(samplesemi_5,samplemass,sampleecc_5,samplew_5)
P_5 = (samplesemi_5[1]/samplesemi_5[0])**1.5
g, eccM_10 = cal_eccmode(samplesemi_10,samplemass,sampleecc_10,samplew_10)
P_10 = (samplesemi_10[1]/samplesemi_10[0])**1.5
g, eccM_20 = cal_eccmode(samplesemi_20,samplemass,sampleecc_20,samplew_20)
P_20 = (samplesemi_20[1]/samplesemi_20[0])**1.5

### with plt disk of 5,10,20 Earth mass (resolution of N=1000) ###
samplesemi_20_high = [ 5.0375,  11.0924]
sampleecc_20_high = [0.012, 0.027 ]
samplew_20_high =  2*np.pi/180*np.array([ 109.275, 16.367])

samplesemi_10_high = [ 5.075,  10.9476]
sampleecc_10_high = [0.0019, 0.048 ]
samplew_10_high =   2*np.pi/180*np.array([ 27.81 ,  128.55])

samplesemi_5_high = [5.0961, 10.833 ]
sampleecc_5_high = [0.008, 0.073 ]
samplew_5_high =  2*np.pi/180*np.array([ 145.170,   306.513])

g, eccM_5_high = cal_eccmode(samplesemi_5_high,samplemass,sampleecc_5_high,samplew_5_high)
P_5_high = (samplesemi_5_high[1]/samplesemi_5_high[0])**1.5
g, eccM_10_high = cal_eccmode(samplesemi_10_high,samplemass,sampleecc_10_high,samplew_10_high)
P_10_high = (samplesemi_10_high[1]/samplesemi_10_high[0])**1.5
g, eccM_20_high = cal_eccmode(samplesemi_20_high,samplemass,sampleecc_20_high,samplew_20_high)
P_20_high = (samplesemi_20_high[1]/samplesemi_20_high[0])**1.5

if opt_rebound == True: 
    ax.scatter(P_m,abs(eccM_m[0][0]),s=s_s0, c='m',edgecolors='m', marker='^') 
    
if opt_plt == True: 
    ax.scatter(P_5,abs(eccM_5[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_10,abs(eccM_10[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_20,abs(eccM_20[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_5_high,abs(eccM_5_high[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_10_high,abs(eccM_10_high[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_20_high,abs(eccM_20_high[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 




### example8 ###
### W/O plt disk ###
samplesemi_m = [5.146, 8.697]
sampleecc_m =  [ 0.02678, 0.07941]
samplemass = [9.54e-4,2.86e-4]
samplew_m = [5.4,4.5] # rad
g, eccM_m = cal_eccmode(samplesemi_m,samplemass,sampleecc_m,samplew_m)
P_m = (samplesemi_m[1]/samplesemi_m[0])**1.5

### with plt disk ###
### with plt disk of 5,10,20 Earth mass (resolution of N=500) ###
samplesemi_5 = [ 5.1213, 8.7708]
sampleecc_5 = [0.03, 0.042]
samplew_5 = 2*np.pi/180*np.array([228.691, 329.86])

samplesemi_10 = [5.0909, 8.8562]
sampleecc_10 = [ 0.018,0.044]
samplew_10 = 2*np.pi/180*np.array([ 22.607,  123.197])


g, eccM_5 = cal_eccmode(samplesemi_5,samplemass,sampleecc_5,samplew_5)
P_5 = (samplesemi_5[1]/samplesemi_5[0])**1.5
g, eccM_10 = cal_eccmode(samplesemi_10,samplemass,sampleecc_10,samplew_10)
P_10 = (samplesemi_10[1]/samplesemi_10[0])**1.5

### with plt disk of 5,10,20 Earth mass (resolution of N=1000) ###
samplesemi_20_high = [ 5.0414, 9.0742]
sampleecc_20_high = [ 0.007, 0.016 ]
samplew_20_high =  2*np.pi/180*np.array([ 62.604, 268.385])

samplesemi_10_high = [ 5.09, 8.8912]
sampleecc_10_high = [0.019, 0.02 ]
samplew_10_high =   2*np.pi/180*np.array([238.019,21.903  ])

samplesemi_5_high = [5.1176, 8.7821]
sampleecc_5_high = [0.032, 0.028 ]
samplew_5_high =  2*np.pi/180*np.array([ 156.052, 294.449])

g, eccM_5_high = cal_eccmode(samplesemi_5_high,samplemass,sampleecc_5_high,samplew_5_high)
P_5_high = (samplesemi_5_high[1]/samplesemi_5_high[0])**1.5
g, eccM_10_high = cal_eccmode(samplesemi_10_high,samplemass,sampleecc_10_high,samplew_10_high)
P_10_high = (samplesemi_10_high[1]/samplesemi_10_high[0])**1.5
g, eccM_20_high = cal_eccmode(samplesemi_20_high,samplemass,sampleecc_20_high,samplew_20_high)
P_20_high = (samplesemi_20_high[1]/samplesemi_20_high[0])**1.5

if opt_rebound == True: 
    ax.scatter(P_m,abs(eccM_m[0][0]),s=s_s0, c='m',edgecolors='m', marker='^') 
    
if opt_plt == True: 
    ax.scatter(P_5,abs(eccM_5[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_10,abs(eccM_10[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_5_high,abs(eccM_5_high[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_10_high,abs(eccM_10_high[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_20_high,abs(eccM_20_high[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 


### example9 ###
### W/O plt disk ###
samplesemi_m = [5.09, 8.778]
sampleecc_m =  [ 0.01002, 0.0263]
samplemass = [9.54e-4,2.86e-4]
samplew_m = [0.74,5.06] # rad
g, eccM_m = cal_eccmode(samplesemi_m,samplemass,sampleecc_m,samplew_m)
P_m = (samplesemi_m[1]/samplesemi_m[0])**1.5

### with plt disk ###
### with plt disk of 5,10,20 Earth mass (resolution of N=500) ###
samplesemi_5 = [5.0677, 8.847]
sampleecc_5 = [0.021, 0.033]
samplew_5 = 2*np.pi/180*np.array([106.288, 62.548])

samplesemi_10 = [5.036, 8.9242]
sampleecc_10 = [ 0.006,0.016]
samplew_10 = 2*np.pi/180*np.array([ 231.625,  207.272])

samplesemi_20 = [ 4.9755, 9.0904]
sampleecc_20 = [ 0.003, 0.012]
samplew_20 = 2*np.pi/180*np.array([ 188.925,  281.415])

g, eccM_5 = cal_eccmode(samplesemi_5,samplemass,sampleecc_5,samplew_5)
P_5 = (samplesemi_5[1]/samplesemi_5[0])**1.5
g, eccM_10 = cal_eccmode(samplesemi_10,samplemass,sampleecc_10,samplew_10)
P_10 = (samplesemi_10[1]/samplesemi_10[0])**1.5
g, eccM_20 = cal_eccmode(samplesemi_20,samplemass,sampleecc_20,samplew_20)
P_20 = (samplesemi_20[1]/samplesemi_20[0])**1.5

### with plt disk of 5,10,20 Earth mass (resolution of N=1000) ###
samplesemi_20_high = [ 4.9703, 9.1789]
sampleecc_20_high = [0.002, 0.012 ]
samplew_20_high =  2*np.pi/180*np.array([ 59.264, 215.801])

samplesemi_10_high = [ 5.0340, 8.9871]
sampleecc_10_high = [0.013, 0.011 ]
samplew_10_high =   2*np.pi/180*np.array([102.544,  187.126])

samplesemi_5_high = [5.0664, 8.8561 ]
sampleecc_5_high = [0.012, 0.022 ]
samplew_5_high =  2*np.pi/180*np.array([ 79.563,   146.563])

g, eccM_5_high = cal_eccmode(samplesemi_5_high,samplemass,sampleecc_5_high,samplew_5_high)
P_5_high = (samplesemi_5_high[1]/samplesemi_5_high[0])**1.5
g, eccM_10_high = cal_eccmode(samplesemi_10_high,samplemass,sampleecc_10_high,samplew_10_high)
P_10_high = (samplesemi_10_high[1]/samplesemi_10_high[0])**1.5
g, eccM_20_high = cal_eccmode(samplesemi_20_high,samplemass,sampleecc_20_high,samplew_20_high)
P_20_high = (samplesemi_20_high[1]/samplesemi_20_high[0])**1.5

if opt_rebound == True: 
    ax.scatter(P_m,abs(eccM_m[0][0]),s=s_s0, c='m',edgecolors='m', marker='^') 
    
if opt_plt == True: 
    ax.scatter(P_5,abs(eccM_5[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_10,abs(eccM_10[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_20,abs(eccM_20[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_5_high,abs(eccM_5_high[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_10_high,abs(eccM_10_high[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_20_high,abs(eccM_20_high[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 



### example10 ###
### W/O plt disk ###
samplesemi_m = [  5.119, 8.758]
sampleecc_m =  [ 0.02336, 0.1164]
samplemass = [9.54e-4,2.86e-4]
samplew_m = [3.1,5.93] # rad
g, eccM_m = cal_eccmode(samplesemi_m,samplemass,sampleecc_m,samplew_m)
P_m = (samplesemi_m[1]/samplesemi_m[0])**1.5

### with plt disk ###
### with plt disk of 5,10,20 Earth mass (resolution of N=500) ###
samplesemi_5 = [ 5.0867, 8.8663]
sampleecc_5 = [ 0.032, 0.1]
samplew_5 = 2*np.pi/180*np.array([120.309, 278.972])

samplesemi_10 = [ 5.0647,  8.9595]
sampleecc_10 = [ 0.037, 0.071]
samplew_10 = 2*np.pi/180*np.array([ 98.799,  250.923])

samplesemi_20 = [ 5.0099,  9.1215 ]
sampleecc_20 = [ 0.01, 0.047]
samplew_20 = 2*np.pi/180*np.array([ 177.577,  346.106])

g, eccM_5 = cal_eccmode(samplesemi_5,samplemass,sampleecc_5,samplew_5)
P_5 = (samplesemi_5[1]/samplesemi_5[0])**1.5
g, eccM_10 = cal_eccmode(samplesemi_10,samplemass,sampleecc_10,samplew_10)
P_10 = (samplesemi_10[1]/samplesemi_10[0])**1.5
g, eccM_20 = cal_eccmode(samplesemi_20,samplemass,sampleecc_20,samplew_20)
P_20 = (samplesemi_20[1]/samplesemi_20[0])**1.5

### with plt disk of 5,10,20 Earth mass (resolution of N=1000) ###
samplesemi_20_high = [ 5.0086,  9.1534]
sampleecc_20_high = [0.017, 0.066 ]
samplew_20_high =  2*np.pi/180*np.array([ 339.682, 146.529])

samplesemi_10_high = [ 5.0616,  8.924]
sampleecc_10_high = [ 0.028, 0.065 ]
samplew_10_high =   2*np.pi/180*np.array([ 129.297,  309.698])

samplesemi_5_high = [5.0877, 8.8326 ]
sampleecc_5_high = [ 0.026, 0.104 ]
samplew_5_high =  2*np.pi/180*np.array([ 138.150, 304.297])

g, eccM_5_high = cal_eccmode(samplesemi_5_high,samplemass,sampleecc_5_high,samplew_5_high)
P_5_high = (samplesemi_5_high[1]/samplesemi_5_high[0])**1.5
g, eccM_10_high = cal_eccmode(samplesemi_10_high,samplemass,sampleecc_10_high,samplew_10_high)
P_10_high = (samplesemi_10_high[1]/samplesemi_10_high[0])**1.5
g, eccM_20_high = cal_eccmode(samplesemi_20_high,samplemass,sampleecc_20_high,samplew_20_high)
P_20_high = (samplesemi_20_high[1]/samplesemi_20_high[0])**1.5

if opt_rebound == True: 
    ax.scatter(P_m,abs(eccM_m[0][0]),s=s_s0, c='m',edgecolors='m', marker='^') 
    
if opt_plt == True: 
    ax.scatter(P_5,abs(eccM_5[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_10,abs(eccM_10[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_20,abs(eccM_20[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_5_high,abs(eccM_5_high[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_10_high,abs(eccM_10_high[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_20_high,abs(eccM_20_high[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 


### example11 ###
### W/O plt disk ###
samplesemi_m = [ 5.166, 9.428]
sampleecc_m =  [ 0.05082, 0.0927]
samplemass = [9.54e-4,2.86e-4]
samplew_m = [2.63,4.69] # rad
samplew_m = [0,6] # rad
g, eccM_m = cal_eccmode(samplesemi_m,samplemass,sampleecc_m,samplew_m)
P_m = (samplesemi_m[1]/samplesemi_m[0])**1.5

### with plt disk ###
### with plt disk of 5,10,20 Earth mass (resolution of N=500) ###
samplesemi_5 = [5.1402,  9.5198]
sampleecc_5 = [ 0.027,   0.054 ]
samplew_5 = 2*np.pi/180*np.array([ 171.954, 326.645])



g, eccM_5 = cal_eccmode(samplesemi_5,samplemass,sampleecc_5,samplew_5)
P_5 = (samplesemi_5[1]/samplesemi_5[0])**1.5

### with plt disk of 5,10,20 Earth mass (resolution of N=1000) ###
samplesemi_5_high = [5.1432, 9.4807 ]
sampleecc_5_high = [ 0.015,  0.024  ]
samplew_5_high =  2*np.pi/180*np.array([ 147.878,  14.833])

g, eccM_5_high = cal_eccmode(samplesemi_5_high,samplemass,sampleecc_5_high,samplew_5_high)
P_5_high = (samplesemi_5_high[1]/samplesemi_5_high[0])**1.5

if opt_rebound == True: 
    ax.scatter(P_m,abs(eccM_m[0][0]),s=s_s0, c='m',edgecolors='m', marker='^') 
    
if opt_plt == True: 
    ax.scatter(P_5,abs(eccM_5[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 
    ax.scatter(P_5_high,abs(eccM_5_high[0][0]),s=s_s, c='b',edgecolors='b', marker='o') 



fig.savefig(savedir+'emode.pdf',orientation='landscape', format='pdf',bbox_inches='tight', pad_inches=0.1)



