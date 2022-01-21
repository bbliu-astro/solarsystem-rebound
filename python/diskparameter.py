#!/usr/bin/env python
### outcome vs three disk parameters in the parameter study 
### Extended data Figure 4,5,6 of Liu_etal_2022
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







######################
### Main rountine ####
######################

nump = 5 # number of planets 
fcase = 'B' # planet resonance (A: all 2:1; B: all 3:2; C: 2:1 +3:2)
ftype = 'MC'
wdir = '..//sim/fiducial/'
datadir = '../data/fiducial/'
savedir = '../figure/'
pydir  = '../python/'
cdir = os.getcwd()

opt_FILE = False # read data into simulation_file 
opt_READ = True # False:to generate AMD and RMC data ;True: read data
opt_check =  False # to excute check SSA 
FIGURE_diskpara = True # plot disk parameters match SSA
filenum0 = 0 # starting  name list
nvar = 1000 # number of variation for the parameter, eg, Vr
filenum = nvar # end  name list

opt_REBOUND = True
if fcase=='A':
    text = '$ \\rm 2:1 MMR, \\ N ='+str(nump)+', \\ with \\ rebound$'
if fcase=='B':
    text = '$ \\rm 3:2 MMR, \\ N ='+str(nump)+', \\ with \\ rebound$'
if fcase=='C':
    text = '$ \\rm 2:1 \\ + 3:2 MMR, \\ N ='+str(nump)+', \\ with \\ rebound$'
if opt_REBOUND == True:
    data_file = datadir+'sim_'+fcase+str(nump)+ftype+'R.csv'
else:
    data_file = datadir+'sim_'+fcase+str(nump)+ftype+'N.csv'
out_file = 'disk'+fcase+str(nump)

tau0 =5e+5 # duration before the disk dispersal 
### if needed, we can have the information about sysmassP,syssemiP,syseccP,Np
#sysmassP,syssemiP,syseccP,sysincP,NP,TIMEP = data_MC(nump, nvar,filenum0, wdir,pydir,fcase,ftype,opt_REBOUND,opt_FILE)
#namdP, rmcP, NP,TIMEP = calculate_AMD_RMC(nump, nvar,filenum0, wdir,fcase,ftype,opt_REBOUND,opt_FILE)



if opt_READ == True:
        namdA_R = []; rmcA_R = []; NA_R = []; TA_R = []
        fil = open(data_file,'r')
        reader = csv.reader(fil)
        for line in reader:
            namdA_R.append(float(line[0]))
            rmcA_R.append(float(line[1]))
            NA_R.append(float(line[2]))
            TA_R.append(float(line[3]))
        fil.close()
else:
        namdA_R, rmcA_R, NA_R,TA_R = calculate_AMD_RMC(nump,nvar,filenum0,wdir,pydir,fcase,ftype,opt_REBOUND,opt_FILE)
        fil = open(data_file,'w')
        writer = csv.writer(fil)
        for i in range(len(namdA_R)):
            writer.writerow([namdA_R[i], rmcA_R[i], NA_R[i], TA_R[i]])
        fil.close()


### solar system AMD and RMC ###
SSmass = [9.54e-4,2.86e-4,4.37e-5,5.15e-5]
SSsemi = [5.20,9.54,19.19,30.07]
SSecc = [0.048,0.054,0.047,0.009]
SSinc = [1.31*np.pi/180.,2.48*np.pi/180.,0.77*np.pi/180.,1.77*np.pi/180.]# rad unit
rmcSS = RMC(SSmass, SSsemi, 4)
amdSS, namdSS = AMD(SSmass,SSsemi,SSecc,SSinc,4)


### read disk parameter data ###
fil = open('../data/fiducial/saveIC_MC.csv','r')
syspara = []
mflux = []
taud = []
vsr = []
reader = csv.reader(fil)
for line in reader:
    syspara.append([float(line[0]),float(line[1]),float(line[2])]) # [fluxt,tau, vsr]
    mflux.append(float(line[0])) # disk flux 
    taud.append(float(line[1])) # disk depletion time
    vsr.append(float(line[2])) # disk depletion time


namd = [namdA_R]
rmc = [rmcA_R]
N = [NA_R]
T = [TA_R]

### read final semimajor axes of planets information ###

#mass,semi,ecc,inc,NP,TIMEP = data_MC(nump, nvar,filenum0, wdir,pydir,fcase,ftype,opt_REBOUND,opt_FILE)
#fn = 'semi_'+fcase+str(nump)+'MCR'
#fil = open('../data/fiducial/'+fn+'.csv','w') 
#writer = csv.writer(fil)
#for i in range(len(semi)):
#    writer.writerow(semi[i])
#fil.close()

fn = 'semi_'+fcase+str(nump)+'MCR'
semi_file = '../data/fiducial/'+fn+'.csv'
semi = []
fil = open(semi_file,'r')
reader = csv.reader(fil)
with open(semi_file) as f:
    for line in csv.reader(f):
        line = list(map(float,line))
        semi.append(line)
fil.close()


# check the information of systems 
if opt_check ==True: # 
    ff = 3.0
    print ('N3,N4,N5,N6,NSS', checksystem(N[0], namd[0],rmc[0],namdSS,rmcSS, ff, 1/ff))

if FIGURE_diskpara ==True: # plot disk parameters match SSA
    diskparameter_color_new(semi,namd[0], rmc[0], N[0], mflux, vsr, tau0, taud, text, namdSS, rmcSS, savedir, out_file,nump, nvar,filenum0, wdir,pydir,fcase,ftype,opt_REBOUND,opt_FILE)

