#!/usr/bin/env python
### an example of 5-planet system with gas and plt dis
### Figure 3b of Liu_etal_2021 
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

#wdir = '../sim/fiducial/C5MCR/output590' old data
wdir = '../sim/example/'
savedir = '../figure/'
outname = 'example_plt2'

filenum0 = 590 # file number list 
iplot = filenum0 
nump = 5     # number of planets

### x-y-limit setting ###
tmin = 1e+5
tmax = 9.5e6
amin = 4.
amax = 70
xlog = True  # choose log x-axis 
ylog = True  # choose log y-axis 
tau0 = 5e+5 # initial cavity-fixed time  
fixcavity = False # choose fix cavity 



def readdata(filename):
    data = np.loadtxt(filename)
    if data.ndim != 1:
        time = data[:,0] # in unit of year
        count = len(time) # total line of time array; or np.size(time)
        mass = data[:,1]
        semi = data[:,2]
        ecc = data[:,3]
        inc = data[:,4]*np.pi/180 # in rad 
        apo = semi*(1. + ecc)
        peri = semi*(1. - ecc)
    else :
        time = data[0] # in unit of year
        count = 1 # total line of time array; or np.size(time)
        mass = data[1]
        semi = data[2]
        ecc = data[3]
        inc = data[4]*np.pi/180
        apo = semi*(1. + ecc)
        peri = semi*(1. - ecc)
    return time, semi, ecc, inc, apo, peri, mass


plt.clf()  # clear image
plt.close('all') # delete figure
plt.close() # delete figure
filename = wdir+'output'+str(iplot)


samplemass_0 = [] 
samplemass_m = [] 
samplemass_f = [] 
samplesemi_0 = [] 
samplesemi_m = [] 
samplesemi_f = [] 
sampleecc_0 = [] 
sampleecc_m = [] 
sampleecc_f = [] 
sampleinc_0 = [] 
sampleinc_m = [] 
sampleinc_f = [] 


for i in range(1,nump+1):
	outlist = 'Sd'+str(i)
	stri = str(i)
	if (i < 10):
		os.system("cat "+filename+" | grep 'ORBIT  NAM I TIME MASS ECC R A I S   "+stri+" ' |awk '{print $13,$14,$15,$16,$17,$18}' > "+outlist+"  ")
	else:
		os.system("cat "+filename+" | grep 'ORBIT  NAM I TIME MASS ECC R A I S   "+stri+" ' |awk '{print $13,$14,$15,$16,$17,$18}' > "+outlist+"  ")
	os.system("cat "+filename+" | grep 'YEAR  RMAG' |awk '{print $3,$4}' > Sd98  ")
	data = np.loadtxt(outlist)
	if data.ndim != 1:
		if fixcavity == True:
			time = data[:,0] - tau0*np.ones(len(data[:,0]))
		else:
			time = data[:,0]
		count = len(time) # total line of time array; or np.size(time)
		mass = data[:,1]
		ecc = data[:,2]
		radii = data[:,3]
		semi = data[:,4]
		inc = data[:,5] # in degree
		apo = semi*(1. + ecc)
		peri = semi*(1. - ecc)
		lasttime = time[count-1]
		lastmass = mass[count-1]
		lastsemi = semi[count-1]
		lastecc = ecc[count-1]
		lastinc = inc[count-1]
	else:
		if fixcavity == True:
			time = data[0] - tau0*np.ones(len(data[0]))
		else:
			time = data[0]
		mass = data[1]
		ecc = data[2]
		radii = data[3]
		semi = data[4]
		inc = data[5] # in degree
		apo = semi*(1. + ecc)
		peri = semi*(1. - ecc)
		lasttime = time
		lastmass = mass
		lastsemi = semi
		lastecc = ecc
		lastinc = inc
	if (i == 1):
		time1 = time
		mass1 = mass
		ecc1 = ecc
		radii1 = radii
		semi1 = semi
		inc1 = inc
		apo1 =  apo
		peri1 = peri 
		lastmass1 = lastmass
		samplemass_0.append(mass[0])
		samplemass_m.append(lastmass)
		samplesemi_0.append(semi[0])
		samplesemi_m.append(semi[-1])
		sampleecc_0.append(ecc[0])
		sampleecc_m.append(ecc[-1])
		sampleinc_0.append(inc[0]*np.pi/180)
		sampleinc_m.append(inc[-1]*np.pi/180)
	if (i == 2):
		time2 = time
		mass2 = mass
		ecc2 = ecc
		radii2 = radii
		semi2 = semi
		inc2 = inc
		apo2 =  apo
		peri2 = peri 
		lastmass2 = lastmass
		samplemass_0.append(mass[0])
		samplemass_m.append(lastmass)
		samplesemi_0.append(semi[0])
		samplesemi_m.append(semi[-1])
		sampleecc_0.append(ecc[0])
		sampleecc_m.append(ecc[-1])
		sampleinc_0.append(inc[0]*np.pi/180)
		sampleinc_m.append(inc[-1]*np.pi/180)
	if (i == 3):
		time3 = time
		mass3 = mass
		ecc3 = ecc
		radii3 = radii
		semi3 = semi
		inc3 = inc
		apo3 =  apo
		peri3 = peri 
		lastmass3 = lastmass
		samplemass_0.append(mass[0])
		samplemass_m.append(lastmass)
		samplesemi_0.append(semi[0])
		samplesemi_m.append(semi[-1])
		sampleecc_0.append(ecc[0])
		sampleecc_m.append(ecc[-1])
		sampleinc_0.append(inc[0]*np.pi/180)
		sampleinc_m.append(inc[-1]*np.pi/180)
	if (i == 4):
		time4 = time
		mass4 = mass
		ecc4 = ecc
		semi4 = semi
		radii4 = radii
		inc4 = inc
		apo4 =  apo
		peri4 = peri 
		lastmass4 = lastmass
		samplemass_0.append(mass[0])
		samplemass_m.append(lastmass)
		samplesemi_0.append(semi[0])
		samplesemi_m.append(semi[-1])
		sampleecc_0.append(ecc[0])
		sampleecc_m.append(ecc[-1])
		sampleinc_0.append(inc[0]*np.pi/180)
		sampleinc_m.append(inc[-1]*np.pi/180)
	if (i == 5):
		time5 = time
		mass5 = mass
		ecc5 = ecc
		radii5 = radii
		semi5 = semi
		inc5 = inc
		apo5 =  apo
		peri5 = peri 
		lastmass5 = lastmass
		samplemass_0.append(mass[0])
		samplemass_m.append(lastmass)
		samplesemi_0.append(semi[0])
		samplesemi_m.append(semi[-1])
		sampleecc_0.append(ecc[0])
		sampleecc_m.append(ecc[-1])
		sampleinc_0.append(inc[0]*np.pi/180)
		sampleinc_m.append(inc[-1]*np.pi/180)

	data98 = np.loadtxt('Sd98')
	if fixcavity == True:
		x98 = data98[:,0] - tau0*np.ones(len(data[:,0]))
	else:
		x98 = data98[:,0]
	y98 = data98[:,1]


### system AMD and RMC ###
rmc_0 = RMC(samplemass_0, samplesemi_0, 5)
amd_0, namd_0 = AMD(samplemass_0,samplesemi_0,sampleecc_0,sampleinc_0,4)
rmc_m = RMC(samplemass_m, samplesemi_m, 4)
amd_m, namd_m = AMD(samplemass_m,samplesemi_m,sampleecc_m,sampleinc_m,4)


### make plots ###     
fig, [ax1,ax2] = plt.subplots(1,2,figsize=(13,4),   gridspec_kw={'width_ratios':[3,1]}, num= 0 )
fig.subplots_adjust(wspace=0.18)
ax1.plot(time1[::4],semi1[::4],'m',linewidth=3)
ax1.plot(time2[::4],semi2[::4],'darkorange',linewidth= 3)
ax1.plot(time3[::4],semi3[::4],'forestgreen',linewidth= 3,alpha=0.8)
ax1.plot(time4[::4],semi4[::4],'blue',linewidth= 3,alpha=0.7)
ax1.plot(time5[::2],semi5[::2],'grey',linewidth= 3)
ax1.legend(('Jupiter','Saturn','Neptune','Uranus','Ice giant'),frameon=True,loc='upper left', bbox_to_anchor=(0.001,0.94), fontsize=10)
ax1.plot(x98[1:],y98[1:],'k',linewidth=1.5,linestyle='dashed')
ax1.plot(time1[::4],apo1[::4],'m',linewidth= 0.5,alpha=0.6 )
ax1.plot(time1[::4],peri1[::4],'m',linewidth= 0.5,alpha=0.6 )
ax1.plot(time2[::4],apo2[::4],'darkorange',linewidth= 0.5,alpha=0.6)
ax1.plot(time2[::4],peri2[::4],'darkorange',linewidth= 0.5,alpha=0.6 )
ax1.plot(time3[::4],apo3[::4],'forestgreen',linewidth= 0.5,alpha=0.6 )
ax1.plot(time3[::4],peri3[::4],'forestgreen',linewidth= 0.5,alpha=0.6 )
ax1.plot(time4[::4],apo4[::4],'blue',linewidth= 0.5,alpha=0.6 )
ax1.plot(time4[::4],peri4[::4],'blue',linewidth= 0.5,alpha=0.6 )
ax1.plot(time5[::4],apo5[::4],'grey',linewidth= 0.5,alpha=0.6)
ax1.plot(time5[::4],peri5[::4],'grey',linewidth= 0.5,alpha=0.6 )

ax1.text(1.02e+5,60,'(c)',fontsize=12)
ax1.set_ylabel('$ {\\rm Semimajor \\ axis \\ [AU]}$',fontsize=fs1)
ax1.set_xlim(tmin,tmax)
ax1.set_ylim(amin,amax)
ax1.semilogy()
ax1.set_yticks([5,10,20,40])
ax1.set_yticklabels(['$5$','$10$','$20$','$40$'],fontsize=fs1)
if xlog == True:
  ax1.semilogx()




ax1.set_xscale('log')
ax1.set_xlim(1e+5,1e+7)
ax1.spines['right'].set_visible(False)
divider = make_axes_locatable(ax1)
ax11 = divider.append_axes("right",size=3,pad=0,sharey=ax1)
ax11.set_xscale('linear')
ax11.set_xlim((1e+7,1.15e+8))
ax11.spines['right'].set_visible(True)
ax1.spines['left'].set_visible(True)
ax11.yaxis.set_ticks_position('right')
ax11.xaxis.set_ticks_position('bottom')
plt.setp(ax11.get_xticklabels(), visible=True)
plt.setp(ax1.get_xticklabels(), visible=True)
plt.setp(ax11.get_yticklabels(), visible=False)
plt.setp(ax1.get_yticklabels(), visible=True)



cdir = os.getcwd()#+'/' #current dir
pydir = cdir # python dir
workdir = cdir+'/../figure/'
# old source = 'sim/plt/example3/run41'
source = 'example2'
nplanet = 4 # number of planets in plt disk phase 

#sourcedir = cdir+'/../sim/plt/'+source+'/'
sourcedir = cdir+'/../data/plt/'+source+'/'
## in source direction, generating the aei output file
os.chdir(sourcedir)
os.system('rm  -rf Planet*')
os.system('rm  -rf *.aei')
os.system('./element')
os.system('awk "NR>=5" P1.aei > Planet1')
os.system('awk "NR>=5" P2.aei > Planet2')
os.system('awk "NR>=5" P3.aei > Planet3')
os.system('awk "NR>=5" P4.aei > Planet4')
os.chdir(workdir)

colors = ['m','darkorange','forestgreen','blue','r', 'darkblue','indigo','brown','khaki',
    'lime','pink','#8c564b', '#e377c2', '#bcbd22', '#17becf',]
    ## make the filled region 
for i in range(nplanet):
    filename = sourcedir+ 'Planet'+ str(i+1)
    time, semi, ecc, inc, apo, peri, mass = readdata(filename)
    time = time + 1e+7
    samplemass_f.append(mass[-1])
    samplesemi_f.append(semi[-1])
    sampleecc_f.append(ecc[-1])
    sampleinc_f.append(inc[-1])
    if colors[i] == 'blue': 
        alpha0 = 0.7
    if colors[i] == 'forestgreen': 
        alpha0 = 0.8
    else:
        alpha0=1
    ax11.plot(time,semi,color=colors[i],linewidth=3,alpha=alpha0)
    ax11.plot(time,apo,color=colors[i],linewidth= 0.5,alpha=0.6)
    ax11.plot(time,peri,color=colors[i],linewidth= 0.5,alpha=0.6 )

rmc_f = RMC(samplemass_f, samplesemi_f, 4)
amd_f, namd_f = AMD(samplemass_f,samplesemi_f,sampleecc_f,sampleinc_f,4)

ax11.tick_params(axis='both',which='both', top = True, right =True, labelright=False,labeltop= False)

   ### current solar system ###
ax11.errorbar(1.13e+8, 5.2, yerr= [5.2*0.048], ms =4, mfc='m', mec='m',ecolor='m',fmt='s',capthick =2.,capsize = 1. )
ax11.errorbar(1.13e+8, 9.6, yerr= [9.6*0.057], ms =4, mfc='darkorange', mec='darkorange',ecolor='darkorange',fmt='s',capthick =2.,capsize = 1. )
ax11.errorbar(1.13e+8, 19.2, yerr= [19.2*0.046], ms = 4, mfc='blue', mec='blue',ecolor='blue',fmt='s',capthick =2.,capsize = 1.,alpha=0.7 )
ax11.errorbar(1.13e+8, 30.1, yerr= [30.1*0.009], ms =  4, mfc='forestgreen', mec='forestgreen',ecolor='forestgreen',fmt='s',capthick =2.,capsize = 1. )
ax1.text(1.31e+5,4.3,'$disk \\ inner \\ edge$',fontsize =10,rotation=0)




ax1.set_xticks([1e+5,3e+5,1e+6,3e+6,1e+7])
ax1.set_xticklabels(['$0.1$','$0.3$','$1$','$3$','$10$'],fontsize=fs1)
ax11.set_xticks([3.e+7,5e+7,7e+7,9e+7,1.1e+8])
ax11.set_xticklabels(['$30$','$50$','$70$','$90$','$110$'],fontsize=fs1)
ax1.tick_params(axis='both',        
        which='both',     
        bottom=True,
        top=True,
        left = True,
        right=False, 
        labelbottom=True)
ax11.tick_params(axis='both',        
        which='both',     
        bottom=True,
        top=True,
        right=True, 
        labelbottom=True)

ax11.text(1.1e+7,60,'$\\bf planetesimal \\  disk $', fontsize=11)
ax11.text(1.1e+7,52,'$M_{\\rm plt}=5 \\ M_{\\oplus}$', fontsize=11)
ax1.text(5.1e+5,60,'$\\bf gas \\  disk \\ dispersal $', fontsize=11)

fig.text(0.38,0.0, '$\\rm Time \\ [Myr]$', ha = 'center', fontsize=fs1)




### AMD and RMC plots  ###
### solar system AMD and RMC ###
SSmass = [9.54e-4,2.86e-4,4.37e-5,5.15e-5]
SSsemi = [5.203,9.555,19.22,30.11]
SSecc = [0.046,0.054,0.044,0.01]
SSinc = [0.37*np.pi/180.,0.9*np.pi/180.,1.02*np.pi/180.,0.67*np.pi/180.]# rad unit
rmcSS = RMC(SSmass, SSsemi, 4)
amdSS, namdSS = AMD(SSmass,SSsemi,SSecc,SSinc,4)
ax2.scatter(namdSS, rmcSS, s=150, c='r', edgecolors='none', marker='*')
ax2.scatter(namd_0, rmc_0, s=100, c='grey', edgecolors='none', marker='^',alpha=0.5)
ax2.scatter(namd_m, rmc_m, s=100, c='grey', edgecolors='none', marker='^')

### with different plt disk mass ###
namd_f_20 = 0.00028940901816438235
rmc_f_20 = 20.88784782082189
namd_f_10 = 0.0004198477227403589
rmc_f_10 = 22.904356207974143
namd_f_5 = 0.0017079434495530915
rmc_f_5 = 23.95594932010335
ax2.scatter(namd_f_5, rmc_f_5, s=100, c='pink', edgecolors='none', marker='^',alpha=0.8)
ax2.scatter(namd_f_10, rmc_f_10, s=100, c='brown', edgecolors='none', marker='^',alpha=0.7)
ax2.scatter(namd_f_20, rmc_f_20, s=100, c='purple', edgecolors='none', marker='^',alpha=1)

ax2.semilogx()
ax2.set_xlim(3e-7,1.e-2)
ax2.set_xticks([1e-6,1e-4,1e-2])
ax2.set_xticklabels(['$10^{-6}$','$10^{-4}$','$10^{-2}$'],fontsize=13)
### add label ###
ax2.scatter(1e-6, 17, s=100, c='grey', edgecolors='none', marker='^',alpha=0.5)
ax2.scatter(1e-6, 15, s=100, c='grey', edgecolors='none', marker='^',alpha=1)
ax2.scatter(1e-6, 13, s=100, c='pink', edgecolors='none', marker='^',alpha=0.8)
ax2.scatter(1e-6, 11, s=100, c='brown', edgecolors='none', marker='^',alpha=0.7)
ax2.scatter(1e-6, 9, s=100, c='purple', edgecolors='none', marker='^',alpha=1)
ax2.text(2e-6, 16, 't=0 Myr' ,fontsize=9)
ax2.text(2e-6, 14, 't=10 Myr',fontsize=9)
ax2.text(2e-6, 12, 't=100 Myr, '+'$M_{\\rm plt} = 5 M_{\\oplus}$',fontsize=9)
ax2.text(2e-6, 10, 't=100 Myr, '+'$M_{\\rm plt} = 10 M_{\\oplus}$',fontsize=9)
ax2.text(2e-6, 8, 't=100 Myr, '+'$M_{\\rm plt} = 20 M_{\\oplus}$',fontsize=9)

ax2.set_ylabel('$\\rm RMC $',fontsize=fs1)
ax2.set_xlabel('$\\rm AMD$',fontsize=fs1)
ax2.set_ylim(7,47)
ax2.text(7e-7,45,'(d)',fontsize=12)
ax2.set_yticks([10,20,30,40])
ax2.set_yticklabels(['$10$','$20$','$30$','$40$'],fontsize=13)
fig.savefig(savedir+str(outname)+'.pdf',orientation='landscape', format='pdf',bbox_inches='tight', pad_inches=0.1)
os.system('rm ../python/Sd*')



