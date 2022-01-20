#!/usr/bin/env python
### planet system semimajor axis vs ecc and inc including both gas and plt disk 
### Figure 4 of Liu_etal_2021
### sampleX_m is the quantity X at the end of the dispersal phase t=10 Myr 
### sampleX_5/10/20 is the quantity X at t=100 Myr with plt disk of different masses
### data obtained from solarsystem_rebound/sim/plt/ 

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

opt_rebound = True # include rebound effct for gas disk
opt_plt = True     # include plt disk 

fig, [ax1,ax2] = plt.subplots(1,2,figsize=(12,4),   gridspec_kw={'width_ratios':[1,1]}, num= 1 )

fig.subplots_adjust(wspace=0.15)



s_s = 25
s_s0 = 55
f = 180./np.pi

ax1.set_xlim(3,35)
ax1.set_xticks([5,10,15,20,25,30])
ax1.set_xticklabels(['$5$','$10$','$15$','$20$','$25$','$30$'],fontsize=13)
ax1.set_ylim(-0.01,0.24)
ax1.set_yticks([0,0.05,0.1,0.15,0.2])
ax1.set_yticklabels(['$0$','$0.05$','$0.1$','$0.15$','$0.2$',],fontsize=13)
ax1.set_ylabel('$\\rm Eccentricity$',fontsize=13)
ax1.set_xlabel('$\\rm Semimajor \\ axis \\ [AU]$',fontsize=13)
ax1.scatter(5.8,0.232,s=100, c='k',edgecolors='k', marker='*') 
ax1.text(6.4,0.228,'Solar System',fontsize=11)
ax1.scatter(5.8,0.215,s=s_s, c='k',edgecolors='k', marker='^') 
ax1.text(6.4,0.21,'simulations without planetesimal disk' ,fontsize=11)
ax1.scatter(5.8,0.194,s=s_s, c='k',edgecolors='k', marker='o') 
ax1.text(6.4,0.19,'simulations with planetesimal disk' ,fontsize=11)
ax1.text(3.3,0.225,'(a)' ,fontsize=12)


ax2.set_xlim(3,35)
ax2.set_xticks([5,10,15,20,25,30])
ax2.set_xticklabels(['$5$','$10$','$15$','$20$','$25$','$30$'],fontsize=13)
ax2.text(3.3,7.5,'(b)' ,fontsize=12)
ax2.set_ylim(-0.4,8)
ax2.set_yticks([0,3,6])
ax2.set_yticklabels(['$0$','$3$','$6$'],fontsize=13)
ax2.set_ylabel('$\\rm Inclination \\  [^{\\circ}]$',fontsize=13)
ax2.set_xlabel('$\\rm Semimajor \\ axis \\ [AU]$',fontsize=13)






### example2 ###
### W/O plt disk ###
samplesemi_m = [4.97, 11.01, 28.6, 17.61]
sampleecc_m =  [0.02205, 0.09075, 0.1822, 0.1855]
sampleinc_m = [  0.02230530784048753,
 0.04153883619746504,
 0.10180505526882923,
 0.039165188414752757]
### with plt disk ###
### with plt disk of 5,10,20 Earth mass (resolution of N=500) ###
samplesemi_5 = [4.94814, 11.07168, 28.80623, 17.85259]
sampleecc_5 = [0.03326, 0.026672, 0.07779, 0.073914]
sampleinc_5 = [0.0010035643198967395,
 0.013479177813152205,
 0.03424685058263273,
 0.18114074174748349]
samplesemi_10 = [4.92294, 11.2207, 30.31273, 17.83434]
sampleecc_10 = [0.012297, 0.027623, 0.061372, 0.008163]
sampleinc_10 = [0.0166818569905618,
 0.011517427733910582,
 0.005597270911145814,
 0.03641454951360969]
samplesemi_20 = [4.87485, 11.41211, 32.0623, 20.11376]
sampleecc_20 = [0.021446, 0.0258, 0.009385, 0.028203]
sampleinc_20 = [0.009264207669585902,
 0.000705113017805709,
 0.010135126966331072,
 0.014042919161546376]
### with plt disk of 5,10,20 Earth mass (resolution of N=1000) ###
samplesemi_20_high = [ 4.87949, 11.56563, 31.63561, 20.53]
sampleecc_20_high = [0.02619, 0.021397, 0.026598, 0.009795 ]
sampleinc_20_high = [ 0.005864306286700947, 0.007717845952318924, 
0.017730799871010394, 0.001499237827463129 ]
samplesemi_10_high = [ 4.92848, 11.20751, 29.71132, 18.23797]
sampleecc_10_high = [0.001437, 0.0465, 0.015584, 0.116379 ]
sampleinc_10_high = [ 0.00830078592248503, 0.013913764796898796,
 0.00804247719318987, 0.021607176139689 ]
samplesemi_5_high = [4.95002, 11.07764, 29.00661, 17.77292 ]
sampleecc_5_high = [0.041728, 0.062259, 0.053305, 0.077103 ]
sampleinc_5_high = [ 0.010208430794914833, 0.02372775118086291, 0.036100390248250715, 0.043244022876663506 ]


if opt_rebound == True: 
    ax1.scatter(samplesemi_m[0],sampleecc_m[0],s=s_s0, c='m',edgecolors='k', marker='^',alpha=0.7) 
    ax1.scatter(samplesemi_m[1],sampleecc_m[1],s=s_s0, c='darkorange',edgecolors='k', marker='^',alpha=0.7) 
    ax1.scatter(samplesemi_m[3],sampleecc_m[3],s=s_s0, c='b',edgecolors='k', marker='^',alpha=0.6) 
    ax1.scatter(samplesemi_m[2],sampleecc_m[2],s=s_s0, c='yellowgreen',edgecolors='k', marker='^',alpha=0.7) 
    ax2.scatter(samplesemi_m[0],f*sampleinc_m[0],s=s_s0, c='m',edgecolors='k', marker='^',alpha=0.7) 
    ax2.scatter(samplesemi_m[1],f*sampleinc_m[1],s=s_s0, c='darkorange',edgecolors='k', marker='^',alpha=0.7) 
    ax2.scatter(samplesemi_m[3],f*sampleinc_m[3],s=s_s0, c='b',edgecolors='k', marker='^',alpha=0.6) 
    ax2.scatter(samplesemi_m[2],f*sampleinc_m[2],s=s_s0, c='yellowgreen',edgecolors='k', marker='^',alpha=0.7) 
    
if opt_plt == True: 
    ax1.scatter(samplesemi_5[0],sampleecc_5[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5[1],sampleecc_5[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5[3],sampleecc_5[3],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_5[2],sampleecc_5[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5[0],f*sampleinc_5[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5[1],f*sampleinc_5[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5[3],f*sampleinc_5[3],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_5[2],f*sampleinc_5[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    
    ax1.scatter(samplesemi_10[0],sampleecc_10[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10[1],sampleecc_10[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10[3],sampleecc_10[3],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_10[2],sampleecc_10[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10[0],f*sampleinc_10[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10[1],f*sampleinc_10[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10[3],f*sampleinc_10[3],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_10[2],f*sampleinc_10[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    
    
    ax1.scatter(samplesemi_20[0],sampleecc_20[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20[1],sampleecc_20[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20[3],sampleecc_20[3],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_20[2],sampleecc_20[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20[0],f*sampleinc_20[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20[1],f*sampleinc_20[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20[3],f*sampleinc_20[3],s=s_s, c='b',edgecolors='k', marker='o' ,alpha=0.6) 
    ax2.scatter(samplesemi_20[2],f*sampleinc_20[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    
    
    ax1.scatter(samplesemi_5_high[0],sampleecc_5_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5_high[1],sampleecc_5_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5_high[3],sampleecc_5_high[3],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_5_high[2],sampleecc_5_high[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5_high[0],f*sampleinc_5_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5_high[1],f*sampleinc_5_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5_high[3],f*sampleinc_5_high[3],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_5_high[2],f*sampleinc_5_high[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o' ,alpha=0.7) 
    
    ax1.scatter(samplesemi_10_high[0],sampleecc_10_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10_high[1],sampleecc_10_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10_high[3],sampleecc_10_high[3],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_10_high[2],sampleecc_10_high[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10_high[0],f*sampleinc_10_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10_high[1],f*sampleinc_10_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10_high[3],f*sampleinc_10_high[3],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_10_high[2],f*sampleinc_10_high[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    
    
    ax1.scatter(samplesemi_20_high[0],sampleecc_20_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20_high[1],sampleecc_20_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20_high[3],sampleecc_20_high[3],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_20_high[2],sampleecc_20_high[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20_high[0],f*sampleinc_20_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20_high[1],f*sampleinc_20_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20_high[3],f*sampleinc_20_high[3],s=s_s, c='b',edgecolors='k', marker='o' ,alpha=0.6) 
    ax2.scatter(samplesemi_20_high[2],f*sampleinc_20_high[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 








### example3 ###
### W/O plt disk ###
samplesemi_m = [  5.207, 9.677, 22.95, 16.05]
sampleecc_m =  [ 0.01288, 0.0738, 0.1889, 0.01112 ]
sampleinc_m = [  0.0029129545215785357,
 0.02933898472602468,
 0.11403981332530948,
 0.03621558197888234]
### with plt disk ###
### with plt disk of 5,10,20 Earth mass (resolution of N=500)  ###
samplesemi_5 = [5.17745, 9.74978, 23.92039, 16.41192]
sampleecc_5 = [ 0.012186, 0.06056, 0.045548, 0.053485 ]
sampleinc_5 = [0.007738789903342857,
 0.020488420089161432,
 0.007705628647554965,
 0.002748893571891069]
samplesemi_10 = [5.14447, 9.94205, 25.85755, 17.11017]
sampleecc_10 = [ 0.007848, 0.044276, 0.018943, 0.02307]
sampleinc_10 = [0.005131268000863328,
 0.013922491443158765,
 0.011721631256393916,
 0.01147728516111471]
samplesemi_20 = [5.07651, 10.26521, 28.39824, 18.12664]
sampleecc_20 = [0.010725, 0.013393, 0.004189, 0.025594]
sampleinc_20 = [0.004026474584350918,
 0.012412781640183673,
 0.027015951491620227,
 0.009864600932271952 ]
### with plt disk of 5,10,20 Earth mass (resolution of N=1000)  ###
samplesemi_20_high = [5.08465, 10.07701, 29.54212, 18.24162]
sampleecc_20_high = [0.007096, 0.012128, 0.019461, 0.054507 ]
sampleinc_20_high = [ 0.00562345084992573, 0.005920156822764766, 0.01599943325303202, 0.018387043669760263 ]
samplesemi_10_high = [ 5.14983, 9.89291, 25.92234, 17.0373]
sampleecc_10_high = [ 0.009257, 0.0436, 0.008006, 0.007981 ]
sampleinc_10_high = [ 0.005213298475707063, 0.01081580537460886, 
0.012611749174911025, 0.00334405084 ]
samplesemi_5_high = [ 5.178, 9.80281, 23.76761, 16.30783]
sampleecc_5_high = [ 0.032132, 0.034498, 0.054508, 0.047712]
sampleinc_5_high = [ 0.007433357284243849, 0.018626153777283484, 0.012531464029319286, 0.011081095420911997 ]


if opt_rebound == True: 
    ax1.scatter(samplesemi_m[0],sampleecc_m[0],s=s_s0, c='m',edgecolors='k', marker='^',alpha=0.7) 
    ax1.scatter(samplesemi_m[1],sampleecc_m[1],s=s_s0, c='darkorange',edgecolors='k', marker='^',alpha=0.7) 
    ax1.scatter(samplesemi_m[3],sampleecc_m[3],s=s_s0, c='b',edgecolors='k', marker='^',alpha=0.6) 
    ax1.scatter(samplesemi_m[2],sampleecc_m[2],s=s_s0, c='yellowgreen',edgecolors='k', marker='^',alpha=0.7) 
    ax2.scatter(samplesemi_m[0],f*sampleinc_m[0],s=s_s0, c='m',edgecolors='k', marker='^',alpha=0.7) 
    ax2.scatter(samplesemi_m[1],f*sampleinc_m[1],s=s_s0, c='darkorange',edgecolors='k', marker='^',alpha=0.7) 
    ax2.scatter(samplesemi_m[3],f*sampleinc_m[3],s=s_s0, c='b',edgecolors='k', marker='^',alpha=0.6) 
    ax2.scatter(samplesemi_m[2],f*sampleinc_m[2],s=s_s0, c='yellowgreen',edgecolors='k', marker='^',alpha=0.7) 
    

if opt_plt == True: 
    ax1.scatter(samplesemi_5_high[0],sampleecc_5_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5_high[1],sampleecc_5_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5_high[3],sampleecc_5_high[3],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_5_high[2],sampleecc_5_high[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5_high[0],f*sampleinc_5_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5_high[1],f*sampleinc_5_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5_high[3],f*sampleinc_5_high[3],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_5_high[2],f*sampleinc_5_high[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    
    ax1.scatter(samplesemi_10_high[0],sampleecc_10_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10_high[1],sampleecc_10_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10_high[3],sampleecc_10_high[3],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_10_high[2],sampleecc_10_high[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10_high[0],f*sampleinc_10_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10_high[1],f*sampleinc_10_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10_high[3],f*sampleinc_10_high[3],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_10_high[2],f*sampleinc_10_high[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20_high[0],sampleecc_20_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20_high[1],sampleecc_20_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20_high[3],sampleecc_20_high[3],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_20_high[2],sampleecc_20_high[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20_high[0],f*sampleinc_20_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20_high[1],f*sampleinc_20_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20_high[3],f*sampleinc_20_high[3],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_20_high[2],f*sampleinc_20_high[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    
    
    
    
    ax1.scatter(samplesemi_5[0],sampleecc_5[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5[1],sampleecc_5[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5[3],sampleecc_5[3],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_5[2],sampleecc_5[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5[0],f*sampleinc_5[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5[1],f*sampleinc_5[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5[3],f*sampleinc_5[3],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_5[2],f*sampleinc_5[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    
    ax1.scatter(samplesemi_10[0],sampleecc_10[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10[1],sampleecc_10[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10[3],sampleecc_10[3],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_10[2],sampleecc_10[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10[0],f*sampleinc_10[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10[1],f*sampleinc_10[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10[3],f*sampleinc_10[3],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_10[2],f*sampleinc_10[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    
    
    ax1.scatter(samplesemi_20[0],sampleecc_20[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20[1],sampleecc_20[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20[3],sampleecc_20[3],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_20[2],sampleecc_20[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20[0],f*sampleinc_20[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20[1],f*sampleinc_20[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20[3],f*sampleinc_20[3],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_20[2],f*sampleinc_20[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 






### example4 ###
### W/O plt disk ###
samplesemi_m = [ 5.029, 10.12, 17.17, 26.78]
sampleecc_m =  [ 0.01853, 0.02169, 0.1551, 0.2391]
sampleinc_m = [0.019041542139258134, 0.023527038316883565, 0.11730357902653889, 0.04827580711016315]
### with plt disk ###
### with plt disk of 5,10,20 Earth mass (resolution of N=500)  ###
samplesemi_5 = [ 5.0043, 10.2139, 17.3968, 27.1077]
sampleecc_5 = [ 0.025, 0.022, 0.092, 0.106]
sampleinc_5 = [ 0.014084807063594239, 0.0045553093477052, 0.049235738198760044, 0.015428710587629874]
samplesemi_10 = [ 4.9839, 10.2796, 17.8437, 27.2305]
sampleecc_10 = [ 0.018, 0.013, 0.047, 0.014]
sampleinc_10 = [ 0.007033676885537148, 0.01949532774477666, 0.03829252378875559, 0.011466813185602744]
samplesemi_20 = [ 4.9253, 10.6247, 19.0471, 29.9245]
sampleecc_20 = [ 0.01, 0.012, 0.016, 0.008 ]
sampleinc_20 = [ 0.01661553447898602, 0.004747295565424576, 0.024294983187761066, 0.01007054978400728 ]

### with plt disk of 5,10,20 Earth mass (resolution of N=1000)  ###
samplesemi_5_high = [ 5.0077, 10.1672, 17.5089, 27.0677 ]
sampleecc_5_high = [ 0.02, 0.015, 0.108, 0.127]
sampleinc_5_high = [ 0.01223475805648025, 0.009896016858807847, 0.019128808601857852, 0.0411199571769864 ]
samplesemi_10_high = [ 4.9798, 10.3744, 18.0038, 27.4505]
sampleecc_10_high = [0.013, 0.015, 0.052, 0.002 ]
sampleinc_10_high = [ 0.011815879036001611, 0.01075122819228507, 0.015515977050229588, 0.01223475805648025 ]
samplesemi_20_high = [  4.9334, 10.5251, 19.5644, 29.9756]
sampleecc_20_high = [ 0.009, 0.012, 0.021, 0.015 ]
sampleinc_20_high = [ 0.012374384396639796, 0.00773180858633488, 0.004136430327226561, 0.016144295580947546]

if opt_rebound == True: 
    ax1.scatter(samplesemi_m[0],sampleecc_m[0],s=s_s0, c='m',edgecolors='k', marker='^',alpha=0.7) 
    ax1.scatter(samplesemi_m[1],sampleecc_m[1],s=s_s0, c='darkorange',edgecolors='k', marker='^',alpha=0.7) 
    ax1.scatter(samplesemi_m[2],sampleecc_m[2],s=s_s0, c='b',edgecolors='k', marker='^',alpha=0.6) 
    ax1.scatter(samplesemi_m[3],sampleecc_m[3],s=s_s0, c='yellowgreen',edgecolors='k', marker='^',alpha=0.7) 
    ax2.scatter(samplesemi_m[0],f*sampleinc_m[0],s=s_s0, c='m',edgecolors='k', marker='^',alpha=0.7) 
    ax2.scatter(samplesemi_m[1],f*sampleinc_m[1],s=s_s0, c='darkorange',edgecolors='k', marker='^',alpha=0.7) 
    ax2.scatter(samplesemi_m[2],f*sampleinc_m[2],s=s_s0, c='b',edgecolors='k', marker='^',alpha=0.6) 
    ax2.scatter(samplesemi_m[3],f*sampleinc_m[3],s=s_s0, c='yellowgreen',edgecolors='k', marker='^',alpha=0.7) 
    
if opt_plt == True: 
    ax1.scatter(samplesemi_5_high[0],sampleecc_5_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5_high[1],sampleecc_5_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5_high[2],sampleecc_5_high[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_5_high[3],sampleecc_5_high[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5_high[0],f*sampleinc_5_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5_high[1],f*sampleinc_5_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5_high[2],f*sampleinc_5_high[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_5_high[3],f*sampleinc_5_high[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    
    
    ax1.scatter(samplesemi_20_high[0],sampleecc_20_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20_high[1],sampleecc_20_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20_high[2],sampleecc_20_high[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_20_high[3],sampleecc_20_high[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20_high[0],f*sampleinc_20_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20_high[1],f*sampleinc_20_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20_high[2],f*sampleinc_20_high[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_20_high[3],f*sampleinc_20_high[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    
    ax1.scatter(samplesemi_5[0],sampleecc_5[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5[1],sampleecc_5[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5[2],sampleecc_5[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_5[3],sampleecc_5[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5[0],f*sampleinc_5[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5[1],f*sampleinc_5[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5[2],f*sampleinc_5[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_5[3],f*sampleinc_5[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10[0],sampleecc_10[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10[1],sampleecc_10[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10[2],sampleecc_10[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_10[3],sampleecc_10[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10[0],f*sampleinc_10[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10[1],f*sampleinc_10[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10[2],f*sampleinc_10[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_10[3],f*sampleinc_10[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20[0],sampleecc_20[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20[1],sampleecc_20[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20[2],sampleecc_20[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_20[3],sampleecc_20[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20[0],f*sampleinc_20[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20[1],f*sampleinc_20[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20[2],f*sampleinc_20[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_20[3],f*sampleinc_20[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 


### example5 ###
### W/O plt disk ###
samplesemi_m = [ 5.074, 10.83,  22.31, 28.07]
sampleecc_m =  [ 0.03042, 0.07266,  0.04358, 0.09294]
sampleinc_m = [ 0.031869712141416456, 0.08386307055832752, 0.06049311187412347, 0.13301154229448786]
### with plt disk ###
### with plt disk of 5,10,20 Earth mass (resolution of N=500)  ###
samplesemi_5 = [ 5.0598, 22.4596, 28.372, 10.9404]
sampleecc_5 = [ 0.017, 0.049, 0.051, 0.045]
sampleinc_5 = [ 0.027663468644110123, 0.06672393730374321, 0.012269664641520135, 0.06602580560294548]
samplesemi_10 = [ 5.0341, 22.1662, 30.1585, 10.9487]
sampleecc_10 =  [ 0.014, 0.077, 0.03, 0.015]
sampleinc_10 = [0.028885199120506154, 0.029112091923265415, 0.017558012275062956, 0.04782202150464464]
samplesemi_20 = [4.9955, 22.3042, 31.8184, 11.1392 ]
sampleecc_20 = [0.004, 0.051, 0.008, 0.004 ]
sampleinc_20 = [0.01059414855960558, 0.015219271077390554, 0.006876597252857658, 0.02893755899806598 ]

### with plt disk of 5,10,20 Earth mass (resolution of N=1000)  ###
samplesemi_5 = [ 5.0598, 22.4596, 28.372, 10.9404]
samplesemi_5_high = [ 5.0573, 23.0688, 27.7065, 10.9199]
sampleecc_5_high = [ 0.022, 0.048, 0.033, 0.035]
sampleinc_5_high = [   0.029880036794142924, 0.04560545335461182, 0.022113321622768155, 0.06853907972581733]
samplesemi_10_high = [ 5.0359, 22.3597, 29.6648, 11.0462 ]
sampleecc_10_high = [ 0.03, 0.041, 0.018, 0.033]
sampleinc_10_high = [ 0.027803094984269666, 0.017016960206944712, 0.02014109956801456, 0.04897393881096089 ]
samplesemi_20_high = [  4.9916, 22.5128, 32.4015, 11.1799]
sampleecc_20_high = [ 0.009, 0.039, 0.021, 0.012 ]
sampleinc_20_high = [0.01572541656046891, 0.0204378055408536, 0.02214822820780804, 0.029391344603584505 ]

if opt_rebound == True: 
    ax1.scatter(samplesemi_m[0],sampleecc_m[0],s=s_s0, c='m',edgecolors='k', marker='^',alpha=0.7) 
    ax1.scatter(samplesemi_m[1],sampleecc_m[1],s=s_s0, c='darkorange',edgecolors='k', marker='^',alpha=0.7) 
    ax1.scatter(samplesemi_m[2],sampleecc_m[2],s=s_s0, c='b',edgecolors='k', marker='^',alpha=0.6) 
    ax1.scatter(samplesemi_m[3],sampleecc_m[3],s=s_s0, c='yellowgreen',edgecolors='k', marker='^',alpha=0.7) 
    ax2.scatter(samplesemi_m[0],f*sampleinc_m[0],s=s_s0, c='m',edgecolors='k', marker='^',alpha=0.7) 
    ax2.scatter(samplesemi_m[1],f*sampleinc_m[1],s=s_s0, c='darkorange',edgecolors='k', marker='^',alpha=0.7) 
    ax2.scatter(samplesemi_m[2],f*sampleinc_m[2],s=s_s0, c='b',edgecolors='k', marker='^',alpha=0.6) 
    ax2.scatter(samplesemi_m[3],f*sampleinc_m[3],s=s_s0, c='yellowgreen',edgecolors='k', marker='^',alpha=0.7) 
    
if opt_plt == True: 
    ax1.scatter(samplesemi_5_high[0],sampleecc_5_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5_high[3],sampleecc_5_high[3],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5_high[1],sampleecc_5_high[1],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_5_high[2],sampleecc_5_high[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5_high[0],f*sampleinc_5_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5_high[3],f*sampleinc_5_high[3],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5_high[1],f*sampleinc_5_high[1],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_5_high[2],f*sampleinc_5_high[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10_high[0],sampleecc_10_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10_high[3],sampleecc_10_high[3],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10_high[1],sampleecc_10_high[1],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_10_high[2],sampleecc_10_high[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10_high[0],f*sampleinc_10_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10_high[3],f*sampleinc_10_high[3],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10_high[1],f*sampleinc_10_high[1],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_10_high[2],f*sampleinc_10_high[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    
    
    ax1.scatter(samplesemi_20_high[0],sampleecc_20_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20_high[3],sampleecc_20_high[3],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20_high[1],sampleecc_20_high[1],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_20_high[2],sampleecc_20_high[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20_high[0],f*sampleinc_20_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20_high[3],f*sampleinc_20_high[3],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20_high[1],f*sampleinc_20_high[1],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_20_high[2],f*sampleinc_20_high[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    
    ax1.scatter(samplesemi_5[0],sampleecc_5[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5[3],sampleecc_5[3],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5[1],sampleecc_5[1],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_5[2],sampleecc_5[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5[0],f*sampleinc_5[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5[3],f*sampleinc_5[3],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5[1],f*sampleinc_5[1],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_5[2],f*sampleinc_5[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10[0],sampleecc_10[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10[3],sampleecc_10[3],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10[1],sampleecc_10[1],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_10[2],sampleecc_10[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10[0],f*sampleinc_10[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10[3],f*sampleinc_10[3],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10[1],f*sampleinc_10[1],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_10[2],f*sampleinc_10[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20[0],sampleecc_20[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20[3],sampleecc_20[3],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20[1],sampleecc_20[1],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_20[2],sampleecc_20[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20[0],f*sampleinc_20[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20[3],f*sampleinc_20[3],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20[1],f*sampleinc_20[1],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_20[2],f*sampleinc_20[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 



### example6 ###
### W/O plt disk ###
samplesemi_m = [ 5.02, 10.56,  29.15, 18.78]
sampleecc_m =  [  0.01393, 0.1215,  0.134, 0.04192]
sampleinc_m = [  0.009730210579868387, 0.014041173832294382, 0.011664035391078104, 0.026214845364954827]
### with plt disk ###
### with plt disk of 5,10,20 Earth mass (resolution of N=500)  ###
samplesemi_5 = [4.9973, 29.3077, 19.1914, 10.7201 ]
sampleecc_5 = [  0.061, 0.04, 0.032, 0.039]
sampleinc_5 = [  0.008831366015091307, 0.0052010811709431014, 0.003944444109507185, 0.008569566627292158]
samplesemi_10 = [ 4.9711, 30.9078, 19.6607, 10.8352]
sampleecc_10 =  [0.012, 0.05, 0.082, 0.045]
sampleinc_10 = [ 0.0018151424220741027, 0.021467549799530253, 0.011711159280881954, 0.011903145498601327]
samplesemi_20 = [ 4.929, 32.6441, 20.9903, 10.9477]
sampleecc_20 = [0.013, 0.01, 0.012, 0.037 ]
sampleinc_20 = [ 0.0049741883681838385, 0.020245819323134222, 0.00884881930761125, 0.0035953782591083183]

### with plt disk of 5,10,20 Earth mass (resolution of N=1000)  ###
samplesemi_5_high = [ 4.9959, 29.6456, 19.2249, 10.6544]
sampleecc_5_high = [0.053, 0.045, 0.079, 0.056 ]
sampleinc_5_high = [ 0.0076270888312152205, 0.0018500490071139892, 0.021170843826691217, 0.008133234314293575 ]
samplesemi_10_high = []
sampleecc_10_high = []
sampleinc_10_high = [ ]
samplesemi_20_high = [4.917, 33.029, 21.0908, 11.023 ]
sampleecc_20_high = [  0.03, 0.015, 0.027, 0.012]
sampleinc_20_high = [0.005096361415823441, 0.023090706003884978, 0.009459684545809265, 0.006579891280018623 ]

if opt_rebound == True: 
    ax1.scatter(samplesemi_m[0],sampleecc_m[0],s=s_s0, c='m',edgecolors='k', marker='^',alpha=0.7) 
    ax1.scatter(samplesemi_m[1],sampleecc_m[1],s=s_s0, c='darkorange',edgecolors='k', marker='^',alpha=0.7) 
    ax1.scatter(samplesemi_m[3],sampleecc_m[3],s=s_s0, c='b',edgecolors='k', marker='^',alpha=0.6) 
    ax1.scatter(samplesemi_m[2],sampleecc_m[2],s=s_s0, c='yellowgreen',edgecolors='k', marker='^',alpha=0.7) 
    ax2.scatter(samplesemi_m[0],f*sampleinc_m[0],s=s_s0, c='m',edgecolors='k', marker='^',alpha=0.7) 
    ax2.scatter(samplesemi_m[1],f*sampleinc_m[1],s=s_s0, c='darkorange',edgecolors='k', marker='^',alpha=0.7) 
    ax2.scatter(samplesemi_m[3],f*sampleinc_m[3],s=s_s0, c='b',edgecolors='k', marker='^',alpha=0.6) 
    ax2.scatter(samplesemi_m[2],f*sampleinc_m[2],s=s_s0, c='yellowgreen',edgecolors='k', marker='^',alpha=0.7) 

if opt_plt == True: 
    ax1.scatter(samplesemi_5_high[0],sampleecc_5_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5_high[3],sampleecc_5_high[3],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5_high[2],sampleecc_5_high[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_5_high[1],sampleecc_5_high[1],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5_high[0],f*sampleinc_5_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5_high[3],f*sampleinc_5_high[3],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5_high[2],f*sampleinc_5_high[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_5_high[1],f*sampleinc_5_high[1],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    
    
    ax1.scatter(samplesemi_20_high[0],sampleecc_20_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20_high[3],sampleecc_20_high[3],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20_high[2],sampleecc_20_high[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_20_high[1],sampleecc_20_high[1],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20_high[0],f*sampleinc_20_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20_high[3],f*sampleinc_20_high[3],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20_high[2],f*sampleinc_20_high[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_20_high[1],f*sampleinc_20_high[1],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    
    ax1.scatter(samplesemi_5[0],sampleecc_5[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5[3],sampleecc_5[3],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5[2],sampleecc_5[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_5[1],sampleecc_5[1],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5[0],f*sampleinc_5[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5[3],f*sampleinc_5[3],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5[2],f*sampleinc_5[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_5[1],f*sampleinc_5[1],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10[0],sampleecc_10[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10[3],sampleecc_10[3],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10[2],sampleecc_10[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_10[1],sampleecc_10[1],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10[0],f*sampleinc_10[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10[3],f*sampleinc_10[3],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10[2],f*sampleinc_10[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_10[1],f*sampleinc_10[1],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20[0],sampleecc_20[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20[3],sampleecc_20[3],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20[2],sampleecc_20[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_20[1],sampleecc_20[1],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20[0],f*sampleinc_20[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20[3],f*sampleinc_20[3],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20[2],f*sampleinc_20[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_20[1],f*sampleinc_20[1],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 


### example7 ###
### W/O plt disk ###
samplesemi_m = [ 5.116, 10.79,  20.76, 32.85]
sampleecc_m =  [  0.01651, 0.1052, 0.08585, 0.2193]
sampleinc_m = [  0.009730210579868387, 0.040020399748229976, 0.10447540902438056, 0.105574966453137]
### with plt disk ###
### with plt disk of 5,10,20 Earth mass (resolution of N=500)  ###
samplesemi_5 = [ 10.79, 20.761, 33.6059, 5.0974 ]
sampleecc_5 = [ 0.049, 0.135, 0.146, 0.027]
sampleinc_5 = [ 0.017016960206944712, 0.03989822670059037, 0.026354471705114374, 0.02707005669843205]
samplesemi_10 = [ 10.9781, 21.1838, 32.2604, 5.0711]
sampleecc_10 =  [0.05, 0.041, 0.025, 0.016]
sampleinc_10 = [ 0.019984019935335072, 0.014486232791552934, 0.0079412480965742, 0.014556045961632708]
samplesemi_20 = [ 11.2112, 22.3993, 34.4274, 5.0343]
sampleecc_20 = [ 0.027, 0.024, 0.018, 0.005 ]
sampleinc_20 = [0.003787364476827695, 0.03235840433197487, 0.013439035240356337, 0.016057029118347832 ]

### with plt disk of 5,10,20 Earth mass (resolution of N=1000)  ###
samplesemi_5_high = [ 10.8335, 21.0433, 32.3339, 5.0961]
sampleecc_5_high = [0.073, 0.051, 0.142, 0.008 ]
sampleinc_5_high = [ 0.025394540616517493, 0.03508111796508602, 0.036878807094640184, 0.020734511513692634 ]
samplesemi_10_high = [ 10.9476, 21.4374, 32.1147, 5.075]
sampleecc_10_high = [0.048, 0.008, 0.043, 0.019 ]
sampleinc_10_high = [ 0.03026400922958167, 0.0054105206811824215, 0.014084807063594239, 0.009896016858807847 ]
samplesemi_20_high = [ 11.0924, 21.5368, 33.8318, 5.0375]
sampleecc_20_high = [  0.027, 0.029, 0.022, 0.012 ]
sampleinc_20_high = [ 0.01403244718603441, 0.013753194505715317, 0.02518510110627818, 0.00947713783832921]

if opt_rebound == True: 
    ax1.scatter(samplesemi_m[0],sampleecc_m[0],s=s_s0, c='m',edgecolors='k', marker='^',alpha=0.7) 
    ax1.scatter(samplesemi_m[1],sampleecc_m[1],s=s_s0, c='darkorange',edgecolors='k', marker='^',alpha=0.7) 
    ax1.scatter(samplesemi_m[2],sampleecc_m[2],s=s_s0, c='b',edgecolors='k', marker='^',alpha=0.6) 
    ax1.scatter(samplesemi_m[3],sampleecc_m[3],s=s_s0, c='yellowgreen',edgecolors='k', marker='^',alpha=0.7) 
    ax2.scatter(samplesemi_m[0],f*sampleinc_m[0],s=s_s0, c='m',edgecolors='k', marker='^',alpha=0.7) 
    ax2.scatter(samplesemi_m[1],f*sampleinc_m[1],s=s_s0, c='darkorange',edgecolors='k', marker='^',alpha=0.7) 
    ax2.scatter(samplesemi_m[2],f*sampleinc_m[2],s=s_s0, c='b',edgecolors='k', marker='^',alpha=0.6) 
    ax2.scatter(samplesemi_m[3],f*sampleinc_m[3],s=s_s0, c='yellowgreen',edgecolors='k', marker='^',alpha=0.7) 

if opt_plt == True: 
    ax1.scatter(samplesemi_5_high[3],sampleecc_5_high[3],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5_high[0],sampleecc_5_high[0],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5_high[1],sampleecc_5_high[1],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_5_high[2],sampleecc_5_high[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5_high[3],f*sampleinc_5_high[3],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5_high[0],f*sampleinc_5_high[0],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5_high[1],f*sampleinc_5_high[1],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_5_high[2],f*sampleinc_5_high[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10_high[3],sampleecc_10_high[3],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10_high[0],sampleecc_10_high[0],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10_high[1],sampleecc_10_high[1],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_10_high[2],sampleecc_10_high[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10_high[3],f*sampleinc_10_high[3],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10_high[0],f*sampleinc_10_high[0],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10_high[1],f*sampleinc_10_high[1],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_10_high[2],f*sampleinc_10_high[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    
    ax1.scatter(samplesemi_20_high[3],sampleecc_20_high[3],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20_high[0],sampleecc_20_high[0],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20_high[1],sampleecc_20_high[1],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_20_high[2],sampleecc_20_high[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20_high[3],f*sampleinc_20_high[3],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20_high[0],f*sampleinc_20_high[0],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20_high[1],f*sampleinc_20_high[1],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_20_high[2],f*sampleinc_20_high[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
 
    ax1.scatter(samplesemi_5[3],sampleecc_5[3],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5[0],sampleecc_5[0],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5[1],sampleecc_5[1],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_5[2],sampleecc_5[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5[3],f*sampleinc_5[3],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5[0],f*sampleinc_5[0],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5[1],f*sampleinc_5[1],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_5[2],f*sampleinc_5[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    
    ax1.scatter(samplesemi_10[3],sampleecc_10[3],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10[0],sampleecc_10[0],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10[1],sampleecc_10[1],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_10[2],sampleecc_10[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10[3],f*sampleinc_10[3],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10[0],f*sampleinc_10[0],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10[1],f*sampleinc_10[1],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_10[2],f*sampleinc_10[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20[3],sampleecc_20[3],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20[0],sampleecc_20[0],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20[1],sampleecc_20[1],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_20[2],sampleecc_20[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20[3],f*sampleinc_20[3],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20[0],f*sampleinc_20[0],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20[1],f*sampleinc_20[1],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_20[2],f*sampleinc_20[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 

### example8 ###
### W/O plt disk ###
samplesemi_m = [ 5.146, 8.697,  15.99, 29.27] 
sampleecc_m =  [ 0.02678, 0.07941,  0.1319, 0.06081 ]
sampleinc_m = [0.0022706733568446224, 0.007518878417591571, 0.004536110725933263, 0.008892452538911109 ]
### with plt disk ###
## with plt disk of 5,10,20 Earth mass (resolution of N=500)  ###
samplesemi_5 = [ 5.1213, 8.7708, 16.5619, 29.9953]
sampleecc_5 = [0.03, 0.042, 0.048, 0.002 ]
sampleinc_5 = [ 0.004694935687864747, 0.0015707963267948967, 0.0030368728984701333, 0.005235987755982988 ]
samplesemi_10 = [ 5.0909, 8.8562, 17.7683, 30.8658]
sampleecc_10 =  [ 0.018, 0.044, 0.01, 0.01]
sampleinc_10 = [ 0.0044156830075456534, 0.0034033920413889425, 0.008813912722571364, 0.004101523742186674 ]
samplesemi_20 = [ ]
sampleecc_20 = [  ]
sampleinc_20 = []

## with plt disk of 5,10,20 Earth mass (resolution of N=1000)  ###
samplesemi_5_high = [5.1176, 8.7821, 16.6162, 30.1914 ]
sampleecc_5_high = [ 0.032, 0.028, 0.059, 0.004 ]
sampleinc_5_high = [  0.001500983156715123, 0.006440264939859076, 0.0045204027626653135, 0.0026354471705114374 ]
samplesemi_10_high = [ 5.09, 8.8912, 17.4349, 31.5474]
sampleecc_10_high = [ 0.019, 0.02, 0.009, 0.003  ]
sampleinc_10_high = [ 0.003106686068549906, 0.003961897402027128, 0.00905825881785057, 0.0023387411976724015 ]
samplesemi_20_high = [ 5.0414, 9.0742, 19.3837, 32.4399 ]
sampleecc_20_high = [ 0.007, 0.016, 0.012, 0.005 ]
sampleinc_20_high = [0.0038571776469074684, 0.0011519173063162574, 0.010192722831646883, 0.012932889757277981 ]


if opt_rebound == True: 
    ax1.scatter(samplesemi_m[0],sampleecc_m[0],s=s_s0, c='m',edgecolors='k', marker='^',alpha=0.7) 
    ax1.scatter(samplesemi_m[1],sampleecc_m[1],s=s_s0, c='darkorange',edgecolors='k', marker='^',alpha=0.7) 
    ax1.scatter(samplesemi_m[2],sampleecc_m[2],s=s_s0, c='b',edgecolors='k', marker='^',alpha=0.6) 
    ax1.scatter(samplesemi_m[3],sampleecc_m[3],s=s_s0, c='yellowgreen',edgecolors='k', marker='^',alpha=0.7) 
    ax2.scatter(samplesemi_m[0],f*sampleinc_m[0],s=s_s0, c='m',edgecolors='k', marker='^',alpha=0.7) 
    ax2.scatter(samplesemi_m[1],f*sampleinc_m[1],s=s_s0, c='darkorange',edgecolors='k', marker='^',alpha=0.7) 
    ax2.scatter(samplesemi_m[2],f*sampleinc_m[2],s=s_s0, c='b',edgecolors='k', marker='^',alpha=0.6) 
    ax2.scatter(samplesemi_m[3],f*sampleinc_m[3],s=s_s0, c='yellowgreen',edgecolors='k', marker='^',alpha=0.7) 

if opt_plt == True: 
    ax1.scatter(samplesemi_5_high[0],sampleecc_5_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5_high[1],sampleecc_5_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5_high[2],sampleecc_5_high[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_5_high[3],sampleecc_5_high[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5_high[0],f*sampleinc_5_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5_high[1],f*sampleinc_5_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5_high[2],f*sampleinc_5_high[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_5_high[3],f*sampleinc_5_high[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10_high[0],sampleecc_10_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10_high[1],sampleecc_10_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10_high[2],sampleecc_10_high[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_10_high[3],sampleecc_10_high[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10_high[0],f*sampleinc_10_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10_high[1],f*sampleinc_10_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10_high[2],f*sampleinc_10_high[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_10_high[3],f*sampleinc_10_high[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    
    ax1.scatter(samplesemi_20_high[0],sampleecc_20_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20_high[1],sampleecc_20_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20_high[2],sampleecc_20_high[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_20_high[3],sampleecc_20_high[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20_high[0],f*sampleinc_20_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20_high[1],f*sampleinc_20_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20_high[2],f*sampleinc_20_high[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_20_high[3],f*sampleinc_20_high[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 

    ax1.scatter(samplesemi_5[0],sampleecc_5[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5[1],sampleecc_5[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5[2],sampleecc_5[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_5[3],sampleecc_5[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5[0],f*sampleinc_5[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5[1],f*sampleinc_5[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5[2],f*sampleinc_5[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_5[3],f*sampleinc_5[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    
    ax1.scatter(samplesemi_10[0],sampleecc_10[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10[1],sampleecc_10[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10[2],sampleecc_10[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_10[3],sampleecc_10[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10[0],f*sampleinc_10[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10[1],f*sampleinc_10[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10[2],f*sampleinc_10[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_10[3],f*sampleinc_10[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    '''
    ax1.scatter(samplesemi_20[0],sampleecc_20[0],s=s_s, c='m',edgecolors='k', marker='o') 
    ax1.scatter(samplesemi_20[1],sampleecc_20[1],s=s_s, c='darkorange',edgecolors='k', marker='o') 
    ax1.scatter(samplesemi_20[2],sampleecc_20[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_20[3],f*sampleecc_20[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o') 
    ax2.scatter(samplesemi_20[0],f*sampleinc_20[0],s=s_s, c='m',edgecolors='k', marker='o') 
    ax2.scatter(samplesemi_20[1],f*sampleinc_20[1],s=s_s, c='darkorange',edgecolors='k', marker='o') 
    ax2.scatter(samplesemi_20[2],f*sampleinc_20[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_20[3],f*sampleinc_20[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o') 
    '''

### example9 ###
### W/O plt disk ###
samplesemi_m = [ 5.09, 8.778, 15.03, 22.16]
sampleecc_m =  [ 0.01002, 0.0263, 0.03935, 0.2424 ]
sampleinc_m = [ 0.015652112731885146, 0.06778858814745975, 0.08946557745722933,  0.09960594041131637 ]
### with plt disk ###
### with plt disk of 5,10,20 Earth mass (resolution of N=500)  ###
samplesemi_5 = [ 5.0677, 8.847, 15.142, 23.2846]
sampleecc_5 = [0.021, 0.033, 0.044, 0.065 ]
sampleinc_5 = [ 0.0226543736908864, 0.05534439058074018, 0.03799581781591655, 0.026040312439755395 ]
samplesemi_10 = [ 5.036, 8.9242, 16.2642, 24.7789 ]
sampleecc_10 =  [ 0.006, 0.016, 0.03, 0.002 ]
sampleinc_10 = [ 0.016528268016386297, 0.05382595413150512, 0.008342673824532893, 0.0055152404363020815 ]
samplesemi_20 = [ 4.9755, 9.0904, 17.6132, 29.389 ]
sampleecc_20 = [  0.003, 0.012, 0.042, 0.003 ]
sampleinc_20 =  [ 0.01754055898254301, 0.0366868208769208, 0.006876597252857658, 0.023247785636564468 ]

### with plt disk of 5,10,20 Earth mass (resolution of N=1000)  ###
samplesemi_5 = [ 5.0677, 8.847, 15.142, 23.2846]
samplesemi_5_high = [ 5.0664, 8.8561, 15.2398, 22.8991 ]
sampleecc_5_high = [ 0.012, 0.022, 0.073, 0.063 ]
sampleinc_5_high = [  0.016824973989225337, 0.05733406592801373, 0.028483773392547457, 0.0010471975511965976 ]
samplesemi_10_high = [ 5.034, 8.9871, 15.9548, 24.9421  ]
sampleecc_10_high = [ 0.013, 0.011, 0.005, 0.005 ]
sampleinc_10_high = [ 0.021956241990088665, 0.04417428336797648, 0.013107422682477414, 0.008761552845011535 ]
samplesemi_20_high = [ 4.9703, 9.1789, 17.605, 29.1203  ]
sampleecc_20_high = [ 0.002, 0.012, 0.017, 0.001 ]
sampleinc_20_high = [ 0.015899949485668342, 0.031328660073298216, 0.01361356816555577, 0.019774580425095754]

if opt_rebound == True: 
    ax1.scatter(samplesemi_m[0],sampleecc_m[0],s=s_s0, c='m',edgecolors='k', marker='^',alpha=0.7) 
    ax1.scatter(samplesemi_m[1],sampleecc_m[1],s=s_s0, c='darkorange',edgecolors='k', marker='^',alpha=0.7) 
    ax1.scatter(samplesemi_m[2],sampleecc_m[2],s=s_s0, c='b',edgecolors='k', marker='^',alpha=0.6) 
    ax1.scatter(samplesemi_m[3],sampleecc_m[3],s=s_s0, c='yellowgreen',edgecolors='k', marker='^',alpha=0.7) 
    ax2.scatter(samplesemi_m[0],f*sampleinc_m[0],s=s_s0, c='m',edgecolors='k', marker='^',alpha=0.7) 
    ax2.scatter(samplesemi_m[1],f*sampleinc_m[1],s=s_s0, c='darkorange',edgecolors='k', marker='^',alpha=0.7) 
    ax2.scatter(samplesemi_m[2],f*sampleinc_m[2],s=s_s0, c='b',edgecolors='k', marker='^',alpha=0.6) 
    ax2.scatter(samplesemi_m[3],f*sampleinc_m[3],s=s_s0, c='yellowgreen',edgecolors='k', marker='^',alpha=0.7) 


if opt_plt == True: 
    ax1.scatter(samplesemi_5_high[0],sampleecc_5_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5_high[1],sampleecc_5_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5_high[2],sampleecc_5_high[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_5_high[3],sampleecc_5_high[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5_high[0],f*sampleinc_5_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5_high[1],f*sampleinc_5_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5_high[2],f*sampleinc_5_high[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_5_high[3],f*sampleinc_5_high[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10_high[0],sampleecc_10_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10_high[1],sampleecc_10_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10_high[2],sampleecc_10_high[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_10_high[3],sampleecc_10_high[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10_high[0],f*sampleinc_10_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10_high[1],f*sampleinc_10_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10_high[2],f*sampleinc_10_high[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_10_high[3],f*sampleinc_10_high[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    
    ax1.scatter(samplesemi_20_high[0],sampleecc_20_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20_high[1],sampleecc_20_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20_high[2],sampleecc_20_high[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_20_high[3],sampleecc_20_high[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20_high[0],f*sampleinc_20_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20_high[1],f*sampleinc_20_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20_high[2],f*sampleinc_20_high[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_20_high[3],f*sampleinc_20_high[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 

    ax1.scatter(samplesemi_5[0],sampleecc_5[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5[1],sampleecc_5[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5[2],sampleecc_5[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_5[3],sampleecc_5[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5[0],f*sampleinc_5[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5[1],f*sampleinc_5[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5[2],f*sampleinc_5[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_5[3],f*sampleinc_5[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    
    ax1.scatter(samplesemi_10[0],sampleecc_10[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10[1],sampleecc_10[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10[2],sampleecc_10[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_10[3],sampleecc_10[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10[0],f*sampleinc_10[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10[1],f*sampleinc_10[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10[2],f*sampleinc_10[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_10[3],f*sampleinc_10[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20[0],sampleecc_20[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20[1],sampleecc_20[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20[2],sampleecc_20[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_20[3],sampleecc_20[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20[0],f*sampleinc_20[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20[1],f*sampleinc_20[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20[2],f*sampleinc_20[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_20[3],f*sampleinc_20[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 



### example10 ###
### W/O plt disk ###
samplesemi_m = [ 5.119, 8.758, 17.77, 29.04]
sampleecc_m =  [ 0.02336, 0.1164, 0.08854, 0.05113 ]
sampleinc_m = [ 0.005996951309852516, 0.03221877799181532, 0.09442231253289324, 0.02946115777366428 ]
### with plt disk ###
### with plt disk of 5,10,20 Earth mass (resolution of N=500)  ###
samplesemi_5 = [ 5.0867, 8.8663, 18.2352, 29.9802]
sampleecc_5 = [0.032, 0.1, 0.016, 0.008 ]
sampleinc_5 = [ 0.010000736613927507, 0.020315632493213994, 0.009389871375729494, 0.010192722831646883 ]
samplesemi_10 = [5.0647, 8.9595, 18.5679, 30.8432 ]
sampleecc_10 =  [ 0.037, 0.071, 0.066, 0.006 ]
sampleinc_10 = [ 0.015166911199830723, 0.013735741213195376, 0.006003932626860492, 0.009354964790689606 ]
samplesemi_20 = [  5.0099, 9.1215, 19.8575, 33.3861]
sampleecc_20 = [  0.01, 0.047, 0.028, 0.01]
sampleinc_20 = [ 0.0034732052114687163, 0.02494075501099897, 0.011763519158441782, 0.026720990848033185]


### with plt disk of 5,10,20 Earth mass (resolution of N=1000)  ###
samplesemi_5_high = [ 5.0877, 8.8326, 18.1908, 30.092 ]
sampleecc_5_high = [ 0.026, 0.104, 0.007, 0.006 ]
sampleinc_5_high = [ 0.012775810124598492, 0.0143116998663535, 0.006352998477259359, 0.009721483933608416  ]
samplesemi_10_high = [ 5.0616, 8.924, 18.9328, 31.0013 ]
sampleecc_10_high = [ 0.028, 0.065, 0.037, 0.003 ]
sampleinc_10_high = [ 0.013369222070276564, 0.011135200627723822, 0.005864306286700947, 0.005864306286700947 ]
samplesemi_20_high = [5.0086, 9.1534, 20.1641, 32.7363  ]
sampleecc_20_high = [ 0.017, 0.066, 0.023, 0.004 ]
sampleinc_20_high = [0.0027052603405912107, 0.015673056682909078, 0.025778513051956248, 0.01864011641129944 ]

if opt_rebound == True: 
    ax1.scatter(samplesemi_m[0],sampleecc_m[0],s=s_s0, c='m',edgecolors='k', marker='^',alpha=0.7) 
    ax1.scatter(samplesemi_m[1],sampleecc_m[1],s=s_s0, c='darkorange',edgecolors='k', marker='^',alpha=0.7) 
    ax1.scatter(samplesemi_m[2],sampleecc_m[2],s=s_s0, c='b',edgecolors='k', marker='^',alpha=0.6) 
    ax1.scatter(samplesemi_m[3],sampleecc_m[3],s=s_s0, c='yellowgreen',edgecolors='k', marker='^',alpha=0.7) 
    ax2.scatter(samplesemi_m[0],f*sampleinc_m[0],s=s_s0, c='m',edgecolors='k', marker='^',alpha=0.7) 
    ax2.scatter(samplesemi_m[1],f*sampleinc_m[1],s=s_s0, c='darkorange',edgecolors='k', marker='^',alpha=0.7) 
    ax2.scatter(samplesemi_m[2],f*sampleinc_m[2],s=s_s0, c='b',edgecolors='k', marker='^',alpha=0.6) 
    ax2.scatter(samplesemi_m[3],f*sampleinc_m[3],s=s_s0, c='yellowgreen',edgecolors='k', marker='^',alpha=0.7) 

if opt_plt == True: 
    ax1.scatter(samplesemi_5_high[0],sampleecc_5_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5_high[1],sampleecc_5_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5_high[2],sampleecc_5_high[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_5_high[3],sampleecc_5_high[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5_high[0],f*sampleinc_5_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5_high[1],f*sampleinc_5_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5_high[2],f*sampleinc_5_high[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_5_high[3],f*sampleinc_5_high[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10_high[0],sampleecc_10_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10_high[1],sampleecc_10_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10_high[2],sampleecc_10_high[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_10_high[3],sampleecc_10_high[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10_high[0],f*sampleinc_10_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10_high[1],f*sampleinc_10_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10_high[2],f*sampleinc_10_high[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_10_high[3],f*sampleinc_10_high[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    
    ax1.scatter(samplesemi_20_high[0],sampleecc_20_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20_high[1],sampleecc_20_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20_high[2],sampleecc_20_high[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_20_high[3],sampleecc_20_high[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20_high[0],f*sampleinc_20_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20_high[1],f*sampleinc_20_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20_high[2],f*sampleinc_20_high[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_20_high[3],f*sampleinc_20_high[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
 
    ax1.scatter(samplesemi_5[0],sampleecc_5[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5[1],sampleecc_5[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5[2],sampleecc_5[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_5[3],sampleecc_5[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5[0],f*sampleinc_5[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5[1],f*sampleinc_5[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5[2],f*sampleinc_5[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_5[3],f*sampleinc_5[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    
    ax1.scatter(samplesemi_10[0],sampleecc_10[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10[1],sampleecc_10[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_10[2],sampleecc_10[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_10[3],sampleecc_10[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10[0],f*sampleinc_10[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10[1],f*sampleinc_10[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_10[2],f*sampleinc_10[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_10[3],f*sampleinc_10[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20[0],sampleecc_20[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20[1],sampleecc_20[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_20[2],sampleecc_20[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_20[3],sampleecc_20[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20[0],f*sampleinc_20[0],s=s_s, c='m',edgecolors='None', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20[1],f*sampleinc_20[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_20[2],f*sampleinc_20[2],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_20[3],f*sampleinc_20[3],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 


### example11 ###
### W/O plt disk ###
samplesemi_m = [ 5.166, 9.428, 34.08, 19.63]
sampleecc_m =  [ 0.05082, 0.0927, 0.1936, 0.1082 ]
sampleinc_m = [  0.021327923459370707, 0.05536184387326013, 0.009862855603019957, 0.13372712728780553]
### with plt disk ###
### with plt disk of 5,10,20 Earth mass (resolution of N=500)  ###
samplesemi_5 = [5.1402, 9.5198, 33.9995, 20.0437 ]
sampleecc_5 = [0.027, 0.054, 0.05, 0.228 ]
sampleinc_5 = [ 0.02516764781375823, 0.04190535534038385, 0.007260569688296411, 0.02881538595042638 ]
samplesemi_10 = []
sampleecc_10 =  []
sampleinc_10 = []
samplesemi_20 = [ ]
sampleecc_20 = [  ]
sampleinc_20 = []

### with plt disk of 5,10,20 Earth mass (resolution of N=1000)  ###
samplesemi_5_high = [5.1432, 9.4807, 33.3781, 20.2144 ]
sampleecc_5_high = [ 0.015, 0.024, 0.056, 0.251 ]
sampleinc_5_high = [  0.010943214410004447, 0.032655110304813904, 0.007539822368615503, 0.009965830028887622 ]
samplesemi_10_high = [ ]
sampleecc_10_high = [ ]
sampleinc_10_high = [ ]
samplesemi_20_high = [ ]
sampleecc_20_high = [ ]
sampleinc_20_high = []

if opt_rebound == True: 
    ax1.scatter(samplesemi_m[0],sampleecc_m[0],s=s_s0, c='m',edgecolors='k', marker='^',alpha=0.7) 
    ax1.scatter(samplesemi_m[1],sampleecc_m[1],s=s_s0, c='darkorange',edgecolors='k', marker='^',alpha=0.7) 
    ax1.scatter(samplesemi_m[3],sampleecc_m[3],s=s_s0, c='b',edgecolors='k', marker='^',alpha=0.6) 
    ax1.scatter(samplesemi_m[2],sampleecc_m[2],s=s_s0, c='yellowgreen',edgecolors='k', marker='^',alpha=0.7) 
    ax2.scatter(samplesemi_m[0],f*sampleinc_m[0],s=s_s0, c='m',edgecolors='k', marker='^',alpha=0.7) 
    ax2.scatter(samplesemi_m[1],f*sampleinc_m[1],s=s_s0, c='darkorange',edgecolors='k', marker='^',alpha=0.7) 
    ax2.scatter(samplesemi_m[3],f*sampleinc_m[3],s=s_s0, c='b',edgecolors='k', marker='^',alpha=0.6) 
    ax2.scatter(samplesemi_m[2],f*sampleinc_m[2],s=s_s0, c='yellowgreen',edgecolors='k', marker='^',alpha=0.7) 

if opt_plt == True: 
    ax1.scatter(samplesemi_5_high[0],sampleecc_5_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5_high[1],sampleecc_5_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5_high[3],sampleecc_5_high[3],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_5_high[2],sampleecc_5_high[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5_high[0],f*sampleinc_5_high[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5_high[1],f*sampleinc_5_high[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5_high[3],f*sampleinc_5_high[3],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_5_high[2],f*sampleinc_5_high[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 

    ax1.scatter(samplesemi_5[0],sampleecc_5[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5[1],sampleecc_5[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax1.scatter(samplesemi_5[3],sampleecc_5[3],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax1.scatter(samplesemi_5[2],sampleecc_5[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5[0],f*sampleinc_5[0],s=s_s, c='m',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5[1],f*sampleinc_5[1],s=s_s, c='darkorange',edgecolors='k', marker='o',alpha=0.7) 
    ax2.scatter(samplesemi_5[3],f*sampleinc_5[3],s=s_s, c='b',edgecolors='k', marker='o',alpha=0.6) 
    ax2.scatter(samplesemi_5[2],f*sampleinc_5[2],s=s_s, c='yellowgreen',edgecolors='k', marker='o',alpha=0.7) 





### plot Solar system ###
### AMD and RMC plots  ###
### solar system AMD and RMC ###
SSmass = [9.54e-4,2.86e-4,4.37e-5,5.15e-5]
SSsemi = [5.203,9.555,19.22,30.11]
SSecc = [0.046,0.054,0.044,0.01]
SSinc = [0.37*np.pi/180.,0.9*np.pi/180.,1.02*np.pi/180.,0.67*np.pi/180.]# rad unit
SS0 = 200
ax1.scatter(SSsemi[0],SSecc[0],s=SS0, c='m',edgecolors='k', marker='*') 
ax1.scatter(SSsemi[1],SSecc[1],s=SS0, c='darkorange',edgecolors='k', marker='*') 
ax1.scatter(SSsemi[2],SSecc[2],s=SS0, c='b',edgecolors='k', marker='*',alpha=0.6) 
ax1.scatter(SSsemi[3],SSecc[3],s=SS0, c='yellowgreen',edgecolors='k', marker='*') 
ax2.scatter(SSsemi[0],180/np.pi*SSinc[0],s=SS0, c='m',edgecolors='k', marker='*') 
ax2.scatter(SSsemi[1],180/np.pi*SSinc[1],s=SS0, c='darkorange',edgecolors='k', marker='*') 
ax2.scatter(SSsemi[2],180/np.pi*SSinc[2],s=SS0, c='b',edgecolors='k', marker='*',alpha=0.6) 
ax2.scatter(SSsemi[3],180/np.pi*SSinc[3],s=SS0, c='yellowgreen',edgecolors='k', marker='*') 

fig.savefig('../figure/aei.pdf',orientation='landscape', format='pdf',bbox_inches='tight', pad_inches=0.1)



