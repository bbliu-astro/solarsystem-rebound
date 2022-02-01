#!/usr/bin/env python
### AMD and RMC plots in the parameter study
### Figure 3 & Extended data Figure 3,4,5 of Liu_etal_2022

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

ftype = 'MC'
wdir = '../sim/fiducial/'
savedir = '../figure/'
pydir  = '../python/'
cdir = os.getcwd()

opt_FILE = False # read data into simulation_file 
opt_READ = True # False:to generate AMD and RMC data ;True: read data
opt_WRITE = False # to write AMD and RMC data into file 
FIGURE_PARA = False # plot three-panel parameter comparision figure
FIGURE_4 =  False
FIGURE_5 =  True
FIGURE_6 =  False
filenum0 = 0 # starting  name list
nvar = 1000 # number of variation for the parameter, eg, Vr
filenum = nvar # end  name list



tau0 =5e+5 # duration before the disk dispersal 
### if needed, we can have the information about sysmassP,syssemiP,syseccP,Np
#sysmassP,syssemiP,syseccP,sysincP,NP,TIMEP = data_MC(nump, nvar,filenum0, wdir,pydir,fcase,ftype,opt_REBOUND,opt_FILE)
#namdP, rmcP, NP,TIMEP = calculate_AMD_RMC(nump, nvar,filenum0, wdir,fcase,ftype,opt_REBOUND,opt_FILE)

if opt_READ == False:
    fcase = 'B'
    opt_REBOUND = True
    nump = 5
    namdA_R, rmcA_R, NA_R, TA_R = calculate_AMD_RMC(nump,nvar,filenum0,wdir,pydir,fcase,ftype,opt_REBOUND,opt_FILE)
    fcase = 'C'
    opt_REBOUND = True
    nump = 5
    namdB_R, rmcB_R, NB_R, TB_R = calculate_AMD_RMC(nump,nvar,filenum0,wdir,pydir, fcase,ftype,opt_REBOUND,opt_FILE)
    fcase = 'B'
    opt_REBOUND = False
    nump = 5
    namdA_N, rmcA_N, NA_N,TA_N = calculate_AMD_RMC(nump,nvar,filenum0,wdir,pydir, fcase,ftype,opt_REBOUND,opt_FILE)
    fcase = 'C'
    opt_REBOUND = False
    nump = 5
    namdB_N, rmcB_N, NB_N,TB_N = calculate_AMD_RMC(nump,nvar,filenum0,wdir,pydir,fcase,ftype,opt_REBOUND,opt_FILE)

    if opt_WRITE == True:
        os.chdir(pydir)
        fil = open('../data/fiducial/sim_B5MCR.csv','w')
        writer = csv.writer(fil)
        for i in range(len(namdA_R)):
            writer.writerow([namdA_R[i], rmcA_R[i], NA_R[i], TA_R[i]])
        fil.close()


if opt_READ == True:
        namdA_R = []; rmcA_R = []; NA_R = []; TA_R = []
        fil = open('../data/fiducial/sim_B6MCR.csv','r')
        reader = csv.reader(fil)
        for line in reader:
            namdA_R.append(float(line[0]))
            rmcA_R.append(float(line[1]))
            NA_R.append(float(line[2]))
            TA_R.append(float(line[3]))
        fil.close()
        namdB_R = []; rmcB_R = []; NB_R = []; TB_R = []
        fil = open('../data/fiducial/sim_C6MCR.csv','r')
        reader = csv.reader(fil)
        for line in reader:
            namdB_R.append(float(line[0]))
            rmcB_R.append(float(line[1]))
            NB_R.append(float(line[2]))
            TB_R.append(float(line[3]))
        fil.close()
        namdA_N = []; rmcA_N = []; NA_N = []; TA_N = []
        fil = open('../data/fiducial/sim_B6MCR.csv','r')
        reader = csv.reader(fil)
        for line in reader:
            namdA_N.append(float(line[0]))
            rmcA_N.append(float(line[1]))
            NA_N.append(float(line[2]))
            TA_N.append(float(line[3]))
        fil.close()
        namdB_N = []; rmcB_N = []; NB_N = []; TB_N = []
        fil = open('../data/fiducial/sim_C6MCR.csv','r')
        reader = csv.reader(fil)
        for line in reader:
            namdB_N.append(float(line[0]))
            rmcB_N.append(float(line[1]))
            NB_N.append(float(line[2]))
            TB_N.append(float(line[3]))
        fil.close()


### solar system AMD and RMC ###
SSmass = [9.54e-4,2.86e-4,4.37e-5,5.15e-5]
SSsemi = [5.203,9.555,19.22,30.11]
SSecc = [0.046,0.054,0.044,0.01]
SSinc = [0.37*np.pi/180.,0.9*np.pi/180.,1.02*np.pi/180.,0.67*np.pi/180.]# rad unit

rmcSS = RMC(SSmass, SSsemi, 4)
amdSS, namdSS = AMD(SSmass,SSsemi,SSecc,SSinc,4)
### initial configuration of simulated systems 
if FIGURE_4 ==  True:
	ICmass = [9.54e-4,2.86e-4,4.37e-5,5.15e-5]
	ICsemi_A = [5.25,5.25*2.02**(2./3),5.25*2.02**(4./3),5.25*2.02**(6./3)]
	ICsemi_B = [5.25,5.25*1.51**(2./3),5.25*1.51**(4./3),5.25*1.51**(6./3)]
	ICsemi_C = [5.25,5.25*2.02**(2./3),5.25*2.02**(2./3)*1.51**(2./3),5.25*2.02**(2./3)*1.51**(4./3)]
	ICecc = [1e-2,1e-2,1e-2,1e-2]
	ICinc = [1e-2,1e-2,1e-2,1e-2]# rad unit
	rmcIC_A = RMC(ICmass, ICsemi_A, 4)
	amdIC_A, namdIC_A = AMD(ICmass,ICsemi_A,ICecc,ICinc,4)
	rmcIC_B = RMC(ICmass, ICsemi_B, 4)
	amdIC_B, namdIC_B = AMD(ICmass,ICsemi_B,ICecc,ICinc,4)
	rmcIC_C = RMC(ICmass, ICsemi_C, 4)
	amdIC_C, namdIC_C = AMD(ICmass,ICsemi_C,ICecc,ICinc,4)
if FIGURE_5 ==  True:
	ICmass = [9.54e-4,2.86e-4,4.37e-5,4.37e-5,5.15e-5]
	ICsemi_A = [5.25,5.25*2**(2./3),5.25*2**(4./3),5.25*2**(6./3),5.25*2**(8./3)]
	ICsemi_B = [5.25,5.25*1.51**(2./3),5.25*1.51**(4./3),5.25*1.51**(6./3),5.25*1.51**(8./3)]
	ICsemi_C = [5.25,5.25*2.02**(2./3),5.25*2.02**(2./3)*1.51**(2./3),5.25*2.02**(2./3)*1.51**(4./3),5.25*2.02**(2./3)*1.51**(6./3)]
	ICecc = [2e-3,2e-3,2e-3,2e-3,2e-3,2e-3]
	ICinc = [2e-3,2e-3,2e-3,2e-3,2e-3,2e-3]# rad unit
	rmcIC_A = RMC(ICmass, ICsemi_A, 5)
	amdIC_A, namdIC_A = AMD(ICmass,ICsemi_A,ICecc,ICinc,5)
	rmcIC_B = RMC(ICmass, ICsemi_B, 5)
	amdIC_B, namdIC_B = AMD(ICmass,ICsemi_B,ICecc,ICinc,5)
	rmcIC_C = RMC(ICmass, ICsemi_C, 5)
	amdIC_C, namdIC_C = AMD(ICmass,ICsemi_C,ICecc,ICinc,5)
if FIGURE_6 ==  True:
	ICmass = [9.54e-4,2.86e-4,4.37e-5,4.37e-5,5.15e-5,5.15e-5]
	ICsemi_A = [5.25,5.25*2**(2./3),5.25*2**(4./3),5.25*2**(6./3),5.25*2**(8./3),5.25*2**(10./3)]
	ICsemi_B = [5.25,5.25*1.51**(2./3),5.25*1.51**(4./3),5.25*1.51**(6./3),5.25*1.51**(8./3),5.25*1.51**(10./3)]
	ICsemi_C = [5.25,5.25*2.02**(2./3),5.25*2.02**(2./3)*1.51**(2./3),5.25*2.02**(2./3)*1.51**(4./3),5.25*2.02**(2./3)*1.51**(6./3), 5.25*2.02**(2./3)*1.51**(8./3)]
	ICecc = [2e-3,2e-3,2e-3,2e-3,2e-3,2e-3,2e-3]
	ICinc = [2e-3,2e-3,2e-3,2e-3,2e-3,2e-3,2e-3]# rad unit
	rmcIC_A = RMC(ICmass, ICsemi_A, 6)
	amdIC_A, namdIC_A = AMD(ICmass,ICsemi_A,ICecc,ICinc,5)
	rmcIC_B = RMC(ICmass, ICsemi_B, 6)
	amdIC_B, namdIC_B = AMD(ICmass,ICsemi_B,ICecc,ICinc,5)
	rmcIC_C = RMC(ICmass, ICsemi_C, 6)
	amdIC_C, namdIC_C = AMD(ICmass,ICsemi_C,ICecc,ICinc,5)
    

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


namd = [namdA_R, namdB_R, namdA_N, namdB_N]
rmc = [rmcA_R, rmcB_R, rmcA_N, rmcB_N]
N = [NA_R, NB_R, NA_N, NB_N]
T = [TA_R, TB_R, TA_N, TB_N]


# check the information of systems 
ff = 3.0
print ('N3,N4,N5,N6,NSS', checksystem(N[0], namd[0],rmc[0],namdSS,rmcSS, ff, 1/ff))
print ('N3,N4,N5,N6,NSS',checksystem(N[1], namd[1],rmc[1],namdSS,rmcSS, ff, 1/ff))
print ('N3,N4,N5,N6,NSS', checksystem(N[2], namd[2],rmc[2],namdSS,rmcSS,ff,1/ff))
print ('N3,N4,N5,N6,NSS',checksystem(N[3], namd[3],rmc[3],namdSS,rmcSS,ff,1/ff))


####  initial four planet case ####

if  FIGURE_4 == True:  
    text = ['$\\rm 3{:}2 \\ MMRs, \\  N{=}4$','$\\rm 2{:}1+3{:}2 \\ MMRs, \\  N{=}4$', '$\\rm 3{:}2 \\ MMRs, \\  N{=}4$','$\\rm 2{:}1+3{:}2 \\ MMRs, \\  N{=}4$']
    #text = ['$\\rm 2{:}1 \\ MMRs, \\  N{=}4$','$\\rm 2{:}1 \\ MMRs, \\  N{=}5$', '$\\rm 2{:}1 \\ MMRs, \\  N{=}4$','$\\rm 2{:}1 \\ MMRs, \\  N{=}5$']
    title = ['$\\rm with \\ rebound $','', '$\\rm without \\ rebound $','']
    compare_plot3D_color(namd, rmc, N, T, tau0, taud, text,title, namdSS,rmcSS, savedir, 'dynN4BC',2)
    '''
    ## plot two panels ##
    text = ['$\\rm 2{:}1{+}3{:}2 \\ MMRs, \\  N_{\\rm i}{=}4$','$\\rm 2{:}1 {+} 3{:}2\\ MMRs, \\  N_{\\rm i}{=}4$']
    title = ['$\\rm with \\ rebound $', '$\\rm without \\ rebound $']
    # include the colorbar 
    compare_plot3D_color_twopanel2(namd, rmc, N, T, tau0, taud, text,title, namdSS,rmcSS, savedir, 'dynN4C',2)
    '''

if  FIGURE_5 == True: 
    text = ['$\\rm 3{:}2\\ MMRs, \\  N{=}5$','$\\rm 2{:}1 {+} 3{:}2 \\ MMRs, \\  N{=}5$', '$\\rm 3{:}2 \\ MMRs, \\  N{=}5$','$\\rm 2{:}1 {+} 3{:}2 \\ MMRs, \\  N{=}5$']
    title = ['$\\rm with \\ rebound $','', '$\\rm without \\ rebound $','']
    compare_plot3D_color(namd, rmc, N, T, tau0, taud, text,title, namdSS,rmcSS, savedir, 'dynN5BC',2)
    '''
    ## plot two panels ##
    text = ['$\\rm 2{:}1 \\ MMRs, \\  N_{\\rm i}{=}5$','$\\rm 2{:}1 \\ MMRs, \\  N_{\\rm i}{=}5$']
    title = ['$\\rm with \\ rebound $', '$\\rm without \\ rebound $']
    # include the colorbar 
    compare_plot3D_color_twopanel2(namd, rmc, N, T, tau0, taud, text,title, namdSS,rmcSS, savedir, 'dynN5A',2)
    '''

if  FIGURE_6 == True:  
    text = ['$\\rm 3{:}2 \\ MMRs, \\  N{=}6$','$\\rm 2{:}1 {+} 3{:}2 \\ MMRs, \\  N{=}6$', '$\\rm 3{:}2 \\ MMRs, \\  N{=}6$','$\\rm 2{:}1 {+} 3{:}2 \\ MMRs, \\  N{=}6$']
    title = ['$\\rm with \\ rebound $',' $\\rm with \\ rebound $', '$\\rm with \\ rebound $','']

    compare_plot3D_color_twopanel(namd, rmc, N, T, tau0, taud, text,title, namdSS,rmcSS, savedir, 'dynN6BC',2)
    '''
    text = ['$\\rm 3{:}2 \\ MMRs, \\  N_{\\rm i}{=}6$','$\\rm 3{:}2 \\ MMRs, \\  N_{\\rm i}{=}6$']
    title = ['$\\rm with \\ rebound $', '$\\rm without \\ rebound $']
    # include the colorbar 
    compare_plot3D_color_twopanel2(namd, rmc, N, T, tau0, taud, text,title, namdSS,rmcSS, savedir, 'dynN6C',2)
    '''


