#!/usr/bin/env python
### an example of 5-planet system with fiducial gas disk 
### Figure 1 of Liu_etal_2021

import matplotlib.pyplot as plt
import numpy as np
import math
import string
import os
import csv
import pylab



wdir = '../sim/example/'
savedir = '../figure/'

filenum0 = 0 # started file numnber list
filenum = filenum0  # ended file number list
nump = 5      # number of planets

### x-y-limt setting ###
tmin = 0e+5 
tmax = 2.05e+6
amin = 4.5 
amax = 200
xlog = False  # choose log x-axis 
ylog = True  # choose log y-axis 
tau0 = 5e+5 # initial cavity-fixed time  



for iplot in range(filenum0,filenum+1):
    plt.clf()  # clear image
    plt.close('all') # delete figure
    filename = wdir+'output'+str(iplot)

    for i in range(1,nump+1):
        ### read and save data ###
        outlist = 'Sd'+str(i)
        stri = str(i)
        if (i < 10):
            os.system("cat "+filename+" | grep 'ORBIT  NAM I TIME MASS ECC R A I S   "+stri+" ' |awk '{print $13,$14,$15,$16,$17,$18}' > "+outlist+"  ")
        else:
            os.system("cat "+filename+" | grep 'ORBIT  NAM I TIME MASS ECC R A I S   "+stri+" ' |awk '{print $13,$14,$15,$16,$17,$18}' > "+outlist+"  ")
        os.system("cat "+filename+" | grep 'YEAR  RMAG' |awk '{print $3,$4}' > Sd98  ")

        data = np.loadtxt(outlist)
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
        if (i == 1):
            time1 = time
            mass1 = mass
            ecc1 = ecc
            semi1 = semi
            inc1 = inc
            apo1 =  apo
            peri1 = peri 
            lastmass1 = lastmass
        if (i == 2):
            time2 = time
            mass2 = mass
            ecc2 = ecc
            semi2 = semi
            inc2 = inc
            apo2 =  apo
            peri2 = peri 
            lastmass2 = lastmass
        if (i == 3):
            time3 = time
            mass3 = mass
            ecc3 = ecc
            semi3 = semi
            inc3 = inc
            apo3 =  apo
            peri3 = peri 
            lastmass3 = lastmass
        if (i == 4):
            time4 = time
            mass4 = mass
            ecc4 = ecc
            semi4 = semi
            inc4 = inc
            apo4 =  apo
            peri4 = peri 
            lastmass4 = lastmass
        if (i == 5) :
            time5 = time
            mass5 = mass
            ecc5 = ecc
            semi5 = semi
            inc5 = inc
            apo5 =  apo
            peri5 = peri 
            lastmass5 = lastmass
        data98 = np.loadtxt('Sd98')
        x98 = data98[:,0]
        y98 = data98[:,1]

    #### make plots ###        
    plt.figure(num=1,figsize=(8,5))
    plt.plot(time1,semi1,'m',linewidth=3.) 
    plt.plot(time2,semi2,'darkorange',linewidth= 3.)
    plt.plot(time3,semi3,'grey',linewidth=3)
    plt.plot(time4,semi4,'b',linewidth= 3,alpha=0.7)
    plt.plot(time5,semi5,'forestgreen',linewidth= 3.,alpha=0.8)
    plt.legend(('Jupiter','Saturn','Ice giant','Uranus','Neptune'),frameon=True,loc='upper left',fontsize='medium' )
    plt.plot(x98[1:],y98[1:],'k',linewidth=2.5,linestyle='dashed')
    plt.plot(time1,apo1,'m',linewidth= 0.5,alpha=1 )
    plt.plot(time1,peri1,'m',linewidth= 0.5,alpha=1 )
    plt.plot(time2,apo2,'darkorange',linewidth= 0.5,alpha=1 )
    plt.plot(time2,peri2,'darkorange',linewidth= 0.5,alpha=1 )
    plt.plot(time3,apo3,'grey',linewidth= 0.5,alpha=1)
    plt.plot(time3,peri3,'grey',linewidth= 0.5,alpha=1 )
    plt.plot(time5,apo5,'forestgreen',linewidth= 0.5,alpha=1 )
    plt.plot(time5,peri5,'forestgreen',linewidth= 0.5,alpha=1 )
    plt.plot(time4,apo4,'b',linewidth= 0.5, alpha=0.6 )
    plt.plot(time4,peri4,'b',linewidth= 0.5, alpha=0.6 )
    ### current solar system ###
    plt.errorbar(2.03e+6, 5.2, yerr= [5.2*0.048], ms =4, mfc='m', mec='m',ecolor='m',fmt='s',capthick =2.,capsize = 1. )
    plt.errorbar(2.03e+6, 9.6, yerr= [9.6*0.057], ms =4, mfc='darkorange', mec='darkorange',ecolor='darkorange',fmt='s',capthick =2.,capsize = 1. )
    plt.errorbar(2.03e+6, 19.2, yerr= [19.2*0.046], ms = 4, mfc='b', mec='b',ecolor='b',fmt='s',capthick =2.,capsize = 1. )
    plt.errorbar(2.03e+6, 30.1, yerr= [30.1*0.009], ms =  4, mfc='forestgreen', mec='forestgreen',ecolor='forestgreen',fmt='s',capthick =2.,capsize = 1. )
    plt.text(1.71e+6,52,'$disk \\ inner \\ edge$',fontsize =9,rotation=10)
    plt.xlabel('${\\rm Time \\ [Myr]}$',fontsize=12)
    plt.ylabel('$ {\\rm Semimajor \\ axis \\ [AU]}$',fontsize=12)
    plt.xlim(tmin,tmax)
    plt.ylim(amin,amax)
    if ylog == True:
      plt.semilogy()
    plt.yticks([5,10,20,40,100],['$5$','$10$','$20$','$40$','$100$'],fontsize=12)
    if xlog == True:
      plt.semilogx()
    plt.xticks([5e+5,1e+6,1.5e+6,2e+6],['$0.5$','$1$','$1.5$','$2$'],fontsize=12)
    plt.tick_params(axis='both',        
    which='both',      
    top=True,
    right=True, 
    )
    plt.savefig(savedir+'example_fiducial.pdf',orientation='landscape', format='pdf',bbox_inches='tight', pad_inches=0.1)
os.system('rm ../python/Sd*')

