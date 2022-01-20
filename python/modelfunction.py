import matplotlib.pyplot as plt
import numpy as np
import math
import string
import os
import csv
import pylab
import matplotlib.patches as patches

def data_MC(nump, nvar,filenum0,wdir,pydir,fcase,ftype,opt_REBOUND,opt_FILE):
    if opt_FILE == True:
        os.chdir(pydir)
        os.system('rm -rf simulation_MC.csv')
        fil = open('simulation_MC.csv','wb')
        writer = csv.writer(fil)

    massP = np.zeros((nump,nvar))
    semiP = np.zeros((nump,nvar))
    eccP = np.zeros((nump,nvar))
    incP = np.zeros((nump,nvar))
    errP = np.zeros((nump,nvar))
    time_COLL = []


    for kk in range(filenum0,filenum0+nvar):
        os.system('rm Sd*')      
        if opt_REBOUND == True:
            filename = wdir+fcase+str(nump)+ftype +'R'+'/output'+str(kk)
        else:
            filename = wdir+fcase+str(nump)+ftype+'N'+'/output'+str(kk)



        ##### mark the collision time ####
        os.system("cat "+filename+" | grep 'COLLISION    YRS'|awk '{print $8}' > "+'SdCOLL'+"  ")
        tmp1 = 0
        tmp2 = 0
        with open(filename) as f:
            for line in f:
                if 'COLLISION' in line:
                    tmp1 = float(line.strip().split()[7])
                    break
                if 'ESCAPE  TIME' in line:
                    tmp2 = float(line.strip().split()[8])
                    break
        if tmp1!=0 and tmp2!= 0:
            time_C = min(tmp1,tmp2)
        if tmp1==0 and tmp2!= 0:
            time_C = tmp2
        if tmp1!=0 and tmp2== 0:
            time_C = tmp1
        if tmp1==0 and tmp2== 0:
            time_C = 0
        time_COLL.append(time_C)



        for i in range(1,nump+1):
            outlist = 'Sd'+str(i)
            #if MMR == True:  outlist2 = 'SMMR'+str(i)
            stri = str(i)
            if (i < 10):
                os.system("cat "+filename+" | grep 'ORBIT  NAM I TIME MASS ECC R A I S   "+stri+" ' |awk '{print $13,$14,$15,$16,$17,$18}' > "+outlist+"  ")
            else:
                os.system("cat "+filename+" | grep 'ORBIT  NAM I TIME MASS ECC R A I S  "+stri+" ' |awk '{print $13,$14,$15,$16,$17,$18}' > "+outlist+"  ")
            os.system("cat "+filename+" | grep 'YEAR  RMAG' |awk '{print $5,$6}' > Sd98  ")



            data = np.loadtxt(outlist)
            if data.ndim != 1:
                time = data[:,0]
                count = len(time) # total line of time array; or np.size(time)
                mass = data[:,1]
                ecc = data[:,2]
                semi = data[:,4]
                inc = data[:,5]*np.pi/180. # rad
                apo = semi*(1. + ecc)
                peri = semi*(1. - ecc)
                lasttime = time[count-1]
                lastmass = mass[count-1]
                lastsemi = semi[count-1]
                lastecc = ecc[count-1]
                lastinc = inc[count-1]
                if time[-1] < 1e+7: # merger before the end 
                    lastmass = 0
                    lastsemi = 0
                    lastecc = -1
                    lastinc = -10
            else:
                time = data[0]
                count = 1 # total line of time array; or np.size(time)
                mass = data[1]
                ecc = data[2]
                semi = data[4]
                inc = data[5]*np.pi/180. # rad
                apo = semi*(1. + ecc)
                peri = semi*(1. - ecc)
                lasttime = 0
                lastmass = 0
                lastsemi = 0
                lastecc = -1
                lastinc = -10

            ## read data into file     
            if opt_FILE == True:
                writer.writerow([lastmass,lastsemi,lastecc])



            massP[i-1][kk] = lastmass #  varied parameter for nump planet  
            semiP[i-1][kk] = lastsemi
            eccP[i-1][kk] = lastecc
            incP[i-1][kk] = lastinc
            errP[i-1][kk] = lastecc*lastsemi

    if opt_FILE == True:
        fil.close()

    # make planet list into system 
    sysmassP_0 = []
    syssemiP_0 = []
    syseccP_0 = []
    sysincP_0 = []
    sysmassP = []
    syssemiP = []
    syseccP = []
    sysincP = []
    NP = []
    for kk in range(nvar):
        tmp_mass = []
        tmp_semi = []
        tmp_ecc = []
        tmp_inc = []
        for i in range(nump):
            tmp_mass.append( massP[i][kk])
            tmp_semi.append( semiP[i][kk])
            tmp_ecc.append( eccP[i][kk])
            tmp_inc.append( incP[i][kk])
        sysmassP_0.append(tmp_mass)
        syssemiP_0.append(tmp_semi)
        syseccP_0.append(tmp_ecc)
        sysincP_0.append(tmp_inc)

    # remove the merge planet in the list  
    for i in range(nvar):
        sysmassP.append(list(filter(lambda a: a != 0, sysmassP_0[i])) )
        syssemiP.append(list(filter(lambda a: a != 0, syssemiP_0[i])) )
        syseccP.append(list(filter(lambda a: a != -1, syseccP_0[i])) )
        sysincP.append(list(filter(lambda a: a != -10, sysincP_0[i])) )

    for i in range(nvar):
        NP.append(len(sysmassP[i]))

    print  ('n>=5',sum(i>=5 for i in NP))
    print  ('n=4',sum(i ==4 for i in NP))
    print  ('n<=3',sum(i <=3 for i in NP))


    return sysmassP,syssemiP,syseccP,sysincP,NP,time_COLL




def AMD(mass, semi, ecc, inc, N):
    res1 = 0
    tmp = 0
    for i in range(N):
        res1 = res1 + mass[i]*semi[i]**0.5*(1.0 - np.cos(inc[i])*(1. - ecc[i]**2)**0.5) # AMD
        tmp = tmp + mass[i]*semi[i]**0.5
    res2 = res1/tmp # normalized AMD
    return res1, res2

def RMC(mass, semi, N):
    a = np.logspace(0,2,500)
    S = np.zeros(500)
    tmp2 = np.zeros(500)
    for j in range(500):
        tmp1 = 0
        for i in range(N):
            tmp1 = tmp1 + mass[i]
            tmp2[j] = tmp2[j] + mass[i]*(np.log10(a[j]/semi[i]))**2
        S[j] = tmp1/tmp2[j]
    res1 = max(S)
    return res1



def calculate_AMD_RMC (nump, nvar,filenum0, wdir,pydir, fcase,ftype,opt_REBOUND,opt_FILE):
    amdP = []
    namdP = []
    rmcP = []
    sysmassP,syssemiP,syseccP,sysincP,NP, TIMEP = data_MC(nump, nvar,filenum0, wdir,pydir, fcase,ftype,opt_REBOUND,opt_FILE)
    for i in range(nvar):
        tmp1, tmp2 = AMD(sysmassP[i], syssemiP[i], syseccP[i],sysincP[i],NP[i])
        amdP.append(tmp1)
        namdP.append(tmp2)
        rmcP.append( RMC(sysmassP[i], syssemiP[i], NP[i]))
        #print (i, tmp1,tmp2,RMC(sysmassP[i], syssemiP[i],NP[i]), syssemiP[i],sysmassP[i], syseccP[i], sysincP[i],NP[i])
    return namdP, rmcP, NP,TIMEP





def selflegend(namdSS, rmcSS, ax):
    x_min =  0.5*namdSS
    x_max = 2*namdSS
    y_min = rmcSS/1.5
    y_max = 1.5*rmcSS

    rect = patches.Rectangle((x_min,y_min), x_max-x_min, y_max-y_min,linewidth=1,edgecolor='red',facecolor='none')
    ax.add_patch(rect)
    return 


def scatterplot3D(namdk, rmck, Nk, Tk, tau0, taud, atext,atitle, namdSS,rmcSS,cm,ax):
    for i in range(len(Nk)):
        if Nk[i] == 4:
            sc = ax.scatter(namdk[i], rmck[i], s=30,c='pink',edgecolors='k',linewidth=0.1,marker='o')
        if Nk[i] <= 3:
            sc = ax.scatter(namdk[i], rmck[i], s=15,c='yellowgreen',edgecolors='k',linewidth=0.1,marker='^')
        if Nk[i] == 5:
            sc = ax.scatter(namdk[i], rmck[i], s=15,c='skyblue',edgecolors='k',linewidth=0.1,marker='D')
        if Nk[i] == 6:
            sc = ax.scatter(namdk[i], rmck[i], s=15,c='orange',edgecolors='k',linewidth=0.1,marker='X')
    ax.scatter(namdSS, rmcSS, s=150, c='r', edgecolors='none', marker='*')
    ax.text(4e-6,130,atext,fontsize= 13)
    ax.set_title(atitle,fontsize= 13)
    selflegend(namdSS, rmcSS, ax)
    ax.semilogx()
    ax.semilogy()
    ax.set_xlim(3e-6,1.5e-1)
    ax.set_xticks([1e-5,1e-4,1e-3,1e-2,1e-1])
    ax.set_xticklabels(['$10^{-5}$','$10^{-4}$','$10^{-3}$','$10^{-2}$','$10^{-1}$'],fontsize=13)
    ax.set_ylim(1,200)
    ax.set_yticks([3,10,30,100])
    ax.set_yticklabels(['$3$','$10$','$30$','$100$'],fontsize=13)
    return sc


def compare_plot3D_twopanel(namd, rmc, N, T, tau0, taud, text,title, namdSS, rmcSS, savedir, filename):
    plt.clf()
    plt.close('all')
    #f,(ax1,ax2) = plt.subplots(2,sharex= True, num=71,figsize=(5,6))
    f,(ax1,ax2) = plt.subplots(2,sharex= True, num=71,figsize=(4,7))
    f.subplots_adjust(hspace=0.02)
    f.subplots_adjust(left=0.15,bottom=0.1)
    cm = plt.cm.get_cmap('RdYlBu_r')
    sc = scatterplot3D(namd[0], rmc[0], N[0], T[0], tau0, taud, text[0],title[0], namdSS,rmcSS,cm,ax1)
    sc = scatterplot3D(namd[1], rmc[1], N[1], T[1], tau0, taud, text[1],title[1], namdSS,rmcSS,cm,ax2)
    f.text(0.5,0.02,'$\\rm  Angular \\ momentum \\ deficit $' ,ha = 'center',fontsize = 13)
    f.text(0.01,0.5,'$ \\rm Radial \\  mass \\ concentration$' ,va = 'center',rotation = 'vertical',fontsize=13)

    ax2.text(9e-4,2, 'pink color = stable',fontsize=6)
    ax2.scatter(1e-3,1.65,marker= 'o',edgecolors='k',facecolors='None',s=15,linewidth=0.1)
    ax2.scatter(1e-3,1.35,marker= '^',edgecolors='k',facecolors='None',s=15,linewidth=0.1)
    ax2.text(1.5e-3,1.6,' = four surviving planets',fontsize=6)
    ax2.text(1.5e-3,1.3,' = three surviving planets',fontsize=6)
    ### colorbar ###
    f.savefig(savedir+filename+'.pdf',orientation='landscape', format='pdf',bbox_inches='tight', pad_inches=0.1)
    return





def scatterplot3D_color(namdk, rmck, Nk, Tk, tau0, taud, atext,atitle, namdSS,rmcSS,cm,ax,opt_colorbar):
    xy = []
    Nmax = max(Nk)
    for i in range(len(Nk)):
    	if opt_colorbar == 1: #color is tau_ins/taud
            if Tk[i]<= 0: # without merger
                xy.append(2)
            elif Tk[i] <= tau0: # within tau0
                xy.append(-1)
            else:
                xy.append(np.log10((Tk[i]-tau0)/taud[i])) # color range plot
        
    	if opt_colorbar == 2: #color is tau_ins
            if Tk[i]<= 0: # without merger
                xy.append(2)
            elif Tk[i] <= tau0: # within tau0
                xy.append(-1)
            else:
                xy.append(np.log10(Tk[i]-tau0)) # color range plot

    for i in range(len(Nk)):
        if Nk[i] ==4 : 
            marksymbol = 'o'
            marksize = 30
        if Nk[i] ==5 : 
            marksymbol = 'D'
            marksize = 15
        if Nk[i] ==6 : 
            marksymbol = 'p'
            marksize = 25
        if Nk[i] <=3 : 
            marksymbol = '^'
            marksize = 15
        if Nk[i] == Nmax: #no merge 
            sc = ax.scatter(namdk[i], rmck[i], s=marksize,c='pink',edgecolors='k',linewidth=0.1,marker=marksymbol)
            sc_3 = ax.scatter([1e+5],[1e+5],s=10, c=[3],marker='^',vmin=3,vmax=7) #this is the artifical one to let colorbar shown scaled 
        else: # merge case
            sc = ax.scatter([1e+5],[1e+5],s=10, c='pink',marker='^') #this is the artifical one to let colorbar shown scaled 
            if opt_colorbar == 1: #color is tau_ins/taud
                if Tk[i]>0 :
                    sc_3 = ax.scatter([namdk[i]], [rmck[i]], s=marksize,c=[xy[i]],edgecolors='k',linewidth=0.1,marker=marksymbol,vmin=-1,vmax=2)
            if opt_colorbar == 2: #color is tau_in
                if Tk[i]>0 :
                    sc_3 = ax.scatter([namdk[i]], [rmck[i]], s=marksize,c=[xy[i]],edgecolors='k',linewidth=0.1,marker=marksymbol,vmin=3,vmax=7,alpha=0.9)
    
    ax.scatter(namdSS, rmcSS, s=150, c='r', edgecolors='none', marker='*')
    ax.text(4e-6,170,atext,fontsize= 13)
    ax.set_title(atitle,fontsize= 13)
    ax.semilogx()
    ax.semilogy()
    ax.set_xlim(3e-6,5e-1)
    ax.set_xticks([1e-5,1e-4,1e-3,1e-2,1e-1])
    ax.set_xticklabels(['$10^{-5}$','$10^{-4}$','$10^{-3}$','$10^{-2}$','$10^{-1}$'],fontsize=13)
    ax.set_ylim(1,250)
    ax.set_yticks([3,10,30,100])
    ax.set_yticklabels(['$3$','$10$','$30$','$100$'],fontsize=13)
    return sc_3

def compare_plot3D_color(namd, rmc, N, T, tau0, taud, text,title, namdSS, rmcSS, savedir, filename,opt_colorbar):
    plt.close('all')
    plt.clf()
    f,((ax1,ax3),(ax2,ax4)) = plt.subplots(2,2,sharex= True, sharey=True, num=22,figsize=(8,8))
    f.subplots_adjust(hspace=0.02)
    f.subplots_adjust(wspace=0.02)
    f.subplots_adjust(left=0.11,bottom=0.14)
    cm = plt.cm.get_cmap('RdYlBu_r')
    sc_3 = scatterplot3D_color(namd[0], rmc[0], N[0], T[0], tau0, taud, text[0],title[0], namdSS,rmcSS,cm,ax1,opt_colorbar)
    sc_3 = scatterplot3D_color(namd[1], rmc[1], N[1], T[1], tau0, taud, text[1],title[1], namdSS,rmcSS,cm,ax2,opt_colorbar)
    sc_3 = scatterplot3D_color(namd[2], rmc[2], N[2], T[2], tau0, taud, text[2],title[2], namdSS,rmcSS,cm,ax3,opt_colorbar)
    sc_3 = scatterplot3D_color(namd[3], rmc[3], N[3], T[3], tau0, taud, text[3],title[3], namdSS,rmcSS,cm,ax4,opt_colorbar)
    # initial postion
    # five planet
    x =3e-6  
    #y_B = 74  #76
    #y_C = 45 # 46
    #ax1.quiver(x,y_B, 1, 0,alpha=0.5)
    #ax3.quiver(x,y_B, 1, 0,alpha=0.5)
    #ax2.quiver(x,y_C, 1, 0,alpha=0.5)
    #ax4.quiver(x,y_C, 1, 0,alpha=0.5)
    # four planet
    #y_B = 131
    #y_C = 68
    #ax1.quiver(x,y_B, 1, 0,alpha=0.5)
    #ax3.quiver(x,y_B, 1, 0,alpha=0.5)
    #ax2.quiver(x,y_C, 1, 0,alpha=0.5)
    #ax4.quiver(x,y_C, 1, 0,alpha=0.5)
    # four-five planet
    y_A1 = 45
    y_A2 = 26
    ax1.quiver(x,y_A1, 1, 0,alpha=0.5)
    ax3.quiver(x,y_A1, 1, 0,alpha=0.5)
    ax2.quiver(x,y_A2, 1, 0,alpha=0.5)
    ax4.quiver(x,y_A2, 1, 0,alpha=0.5)




    ax4.text(9e-4,2, 'pink color = stable',fontsize=6)
    ax4.scatter(1e-3,1.6,marker= 'o',edgecolors='k',facecolors='None',s=15,linewidth=0.1)
    ax4.scatter(1e-3,1.2,marker= '^',edgecolors='k',facecolors='None',s=15,linewidth=0.1)
    f.text(0.705,0.168,'= four surviving planets',fontsize=6)
    f.text(0.705,0.148,'= three surviving planets',fontsize=6)
    f.text(0.5,0.06,'$\\rm Angular \\ momentum \\ deficit $' ,ha = 'center',fontsize = 13)
    f.text(0.01,0.5,'$ \\rm Radial \\  mass \\ concentration$' ,va = 'center',rotation = 'vertical',fontsize=13)

    ### colorbar ###
    cbar_ax = f.add_axes([0.15,0.001,0.7,0.02])
    if opt_colorbar == 1:
        cbar = f.colorbar(sc_3,cax=cbar_ax,orientation='horizontal',ticks=[-1,0,1])
        cbar.ax.set_xticklabels(['$0.1$','$1$','$10$'],fontsize=13)
        cbar.ax.set_xlabel(' $\\tau_{\\rm instability}/ \\tau_{\\rm dep}$',fontsize=13)
    if opt_colorbar == 2:
        cbar = f.colorbar(sc_3,cax=cbar_ax,orientation='horizontal',ticks=[4,5,6])
        cbar.ax.set_xticklabels(['$10^{4}$','$10^{5}$','$10^{6}$'],fontsize=13)
        cbar.ax.set_xlabel(' $t_{\\rm instability} \\ \\rm  [yr]$',fontsize=13)
    f.savefig(savedir+filename+'.pdf',orientation='landscape', format='pdf',bbox_inches='tight', pad_inches=0.1)
    return


def compare_plot3D_color_twopanel(namd, rmc, N, T, tau0, taud, text,title, namdSS, rmcSS, savedir, filename,opt_colorbar):
    plt.close('all')
    f,(ax1,ax2) = plt.subplots(1,2,sharex= True, num=72,figsize=(8,4))
    f.subplots_adjust(hspace=0.02)
    f.subplots_adjust(left=0.1,bottom=0.2)
    cm = plt.cm.get_cmap('RdYlBu_r')
    sc_3 = scatterplot3D_color(namd[0], rmc[0], N[0], T[0], tau0, taud, text[0],title[0], namdSS,rmcSS,cm,ax1,opt_colorbar)
    sc_3 = scatterplot3D_color(namd[1], rmc[1], N[1], T[1], tau0, taud, text[1],title[1], namdSS,rmcSS,cm,ax2,opt_colorbar)
    f.text(0.5,0.07,'$\\rm Angular \\ momentum \\ deficit $' ,ha = 'center',fontsize = 13)
    f.text(0.01,0.55,'$ \\rm Radial \\  mass \\ concentration$' ,va = 'center',rotation = 'vertical',fontsize=13)

    # initial position    
    # six planet
    x= 3e-6
    y_B = 43
    y_C = 30
    ax1.quiver(x,y_B, 1, 0,alpha=0.5)
    ax2.quiver(x,y_C, 1, 0,alpha=0.5)

    ax1.text(9e-4,134, 'pink color = stable',fontsize=6)
    ax1.scatter(1e-3,109,marker= 'D',edgecolors='k',facecolors='None',s=12,linewidth=0.1)
    ax1.scatter(1e-3,88,marker= 'o',edgecolors='k',facecolors='None',s=15,linewidth=0.1)
    ax1.scatter(1e-3,69,marker= '^',edgecolors='k',facecolors='None',s=15,linewidth=0.1)
    ax1.text(1.25e-3,104,'= five surviving planets',fontsize=6)
    ax1.text(1.25e-3,83,'= four surviving planets',fontsize=6)
    ax1.text(1.25e-3,66,'= three surviving planets',fontsize=6)
    ### colorbar ###
    cbar_ax = f.add_axes([0.15,0.001,0.7,0.036])
    if opt_colorbar == 1:
        cbar = f.colorbar(sc_3,cax=cbar_ax,orientation='horizontal',ticks=[-1,0,1])
        cbar.ax.set_xticklabels(['$0.1$','$1$','$10$'],fontsize=13)
        cbar.ax.set_xlabel(' $\\tau_{\\rm instability}/ \\tau_{\\rm dep}$',fontsize=13)
    if opt_colorbar == 2:
        cbar = f.colorbar(sc_3,cax=cbar_ax,orientation='horizontal',ticks=[4,5,6])
        cbar.ax.set_xticklabels(['$10^{4}$','$10^{5}$','$10^{6}$'],fontsize=13)
        cbar.ax.set_xlabel(' $t_{\\rm instability} \\ \\rm  [yr]$',fontsize=13)
    f.savefig(savedir+filename+'.pdf',orientation='landscape', format='pdf',bbox_inches='tight', pad_inches=0.1)


    return




def compare_plot3D_color_twopanel2(namd, rmc, N, T, tau0, taud, text,title, namdSS, rmcSS, savedir, filename,opt_colorbar):
    plt.close('all')
    plt.clf()
    f,(ax1,ax2) = plt.subplots(1,2,sharey= True, num=72,figsize=(11,5))
    f.subplots_adjust(hspace=0.02)
    f.subplots_adjust(left=0.06,bottom=0.15)
    cm = plt.cm.get_cmap('RdYlBu_r')
    sc_3 = scatterplot3D_color(namd[0], rmc[0], N[0], T[0], tau0, taud, text[0],title[0], namdSS,rmcSS,cm,ax1,opt_colorbar)
    sc_3 = scatterplot3D_color(namd[1], rmc[1], N[1], T[1], tau0, taud, text[1],title[1], namdSS,rmcSS,cm,ax2,opt_colorbar)
    f.text(0.5,0.04,'$\\rm Angular \\ momentum \\ deficit $' ,ha = 'center',fontsize = 13)
    f.text(0.01,0.5,'$ \\rm Radial \\  mass \\ concentration$' ,va = 'center',rotation = 'vertical',fontsize=13)

    ax2.text(9e-4,2, 'pink color = stable',fontsize=6)
    ax2.scatter(1e-3,1.65,marker= 'o',edgecolors='k',facecolors='None',s=15,linewidth=0.1)
    ax2.scatter(1e-3,1.35,marker= '^',edgecolors='k',facecolors='None',s=15,linewidth=0.1)
    ax2.text(1.5e-3,1.6,' = four surviving planets',fontsize=6)
    ax2.text(1.5e-3,1.3,' = three surviving planets',fontsize=6)

    ### colorbar ###
    cbar_ax = f.add_axes([0.15,0.001,0.7,0.03])
    if opt_colorbar == 1:
        cbar = f.colorbar(sc_3,cax=cbar_ax,orientation='horizontal',ticks=[-1,0,1])
        cbar.ax.set_xticklabels(['$0.1$','$1$','$10$'],fontsize=13)
        cbar.ax.set_xlabel(' $\\tau_{\\rm instability}/ \\tau_{\\rm dep}$',fontsize=13)
    if opt_colorbar == 2:
        cbar = f.colorbar(sc_3,cax=cbar_ax,orientation='horizontal',ticks=[4,5,6])
        cbar.ax.set_xticklabels(['$10^{4}$','$10^{5}$','$10^{6}$'],fontsize=13)
        cbar.ax.set_xlabel(' $t_{\\rm instability} \\ \\rm  [yr]$',fontsize=13)
    f.savefig(savedir+filename+'.pdf',orientation='landscape', format='pdf',bbox_inches='tight', pad_inches=0.1)
    return







def diskparameter_color(namd, rmc, Naim, mflux, vsr, tau0, taud, atext, namdSS, rmcSS, savedir, filename):
    plt.close('all')
    plt.clf()
    f,(ax1,ax2,ax3) = plt.subplots(1,3, num=33,figsize=(13,4))
    f.subplots_adjust(wspace=0.33)
    cm = plt.cm.get_cmap('coolwarm')
    optSS = True
    S_max = 3.0
    S_min = 1./S_max
    i_SS = 0
    f.text(0.52,0.9,atext ,ha = 'center',fontsize = 12)


    for i in range(len(Naim)):
    	if Naim[i] ==max(Naim):
        	sc = ax1.scatter([mflux[i]], [taud[i]], s=10,c=[np.log10(namd[i])],edgecolors='k',linewidth=0.5,vmin=-6,vmax=-0.0, marker='o',cmap=cm)
    	else:
        	sc = ax1.scatter([mflux[i]], [taud[i]], s=10,c=[np.log10(namd[i])],edgecolors=None,vmin=-6,vmax=-0.0,marker='o',cmap=cm)
    	if Naim[i] ==4 and optSS == True:
        	if namd[i]< S_max*namdSS and  namd[i]>S_min*namdSS and rmc[i]< S_max*rmcSS and  rmc[i]>S_min*rmcSS:
            		sc = ax1.scatter([mflux[i]], [taud[i]], s=10,c=[np.log10(namd[i])],edgecolors='m',linewidth=1,vmin=-6,vmax=-0., marker='o',cmap=cm)
    ax1.semilogx()
    ax1.semilogy()
    ax1.set_xlim(2.8e-10,3.3e-9)
    ax1.set_xticks([3e-10,1e-9,3e-9])
    ax1.set_xticklabels(['$10^{-9.5}$','$10^{-9}$','$10^{-8.5}$'],fontsize=12)
    ax1.set_ylim(0.95e+5,1.1e+6)
    ax1.set_yticks([1e+5,3.3e+5,1e+6])
    ax1.set_yticklabels(['$10^{5}$','$ 10^{5.5}$','$10^{6}$'],fontsize=12)
    ax1.set_ylabel('$\\rm Disk \\ dispersal  \\ timescale  \\ [ yr] $',fontsize=12)
    ax1.set_xlabel('$\\rm Onest \\ mass  \\ loss  \\ rate  \\ [M_{\\odot} \\ yr^{-1}] $',fontsize=12)

    for i in range(len(Naim)):
    	if Naim[i] ==max(Naim):
        	sc = ax2.scatter([taud[i]], [vsr[i]], s=10,c=[np.log10(namd[i])],edgecolors='k',linewidth=0.5,vmin=-6,vmax=-0.0, marker='o',cmap=cm)
    	else:
        	sc = ax2.scatter([taud[i]], [vsr[i]], s=10,c=[np.log10(namd[i])],edgecolors=None,vmin=-6,vmax=-0.0,marker='o',cmap=cm)
    	if Naim[i] ==4 and optSS == True:
        	if namd[i]< S_max*namdSS and  namd[i]>S_min*namdSS and rmc[i]< S_max*rmcSS and  rmc[i]>S_min*rmcSS:
            		sc = ax2.scatter([taud[i]], [vsr[i]], s=10,c=[np.log10(namd[i])],edgecolors='m',linewidth=1,vmin=-6,vmax=-0., marker='o',cmap=cm)
    ax2.semilogx()
    ax2.semilogy()
    ax2.set_ylim(19,210)
    ax2.set_yticks([20,60,200])
    ax2.set_yticklabels(['$20$','$60$','$200$'],fontsize=12)
    ax2.set_ylabel('$\\rm Cavity \\ expansion  \\ rate  \\ [AU \\ Myr^{-1}] $',fontsize=12)
    ax2.set_xlim(0.95e+5,1.1e+6)
    ax2.set_xticks([1e+5,3.3e+5,1e+6])
    ax2.set_xticklabels(['$10^{5}$','$ 10^{5.5}$','$10^{6}$'],fontsize=12)
    ax2.set_xlabel('$\\rm Disk \\ dispersal  \\ timescale  \\ [yr] $',fontsize=12)


    for i in range(len(Naim)):
        if Naim[i] ==max(Naim):
        	sc = ax3.scatter([vsr[i]], [mflux[i]], s=10,c=[np.log10(namd[i])],edgecolors='k',linewidth=0.5,vmin=-6,vmax=-0.0, marker='o',cmap=cm)
        else:
        	sc = ax3.scatter([vsr[i]],[mflux[i]], s=10,c=[np.log10(namd[i])],edgecolors=None,vmin=-6,vmax=-0.0,marker='o',cmap=cm)
        if Naim[i] ==4 and optSS == True and namd[i]< S_max*namdSS and  namd[i]>S_min*namdSS and rmc[i]< S_max*rmcSS and  rmc[i]>S_min*rmcSS:
        	sc = ax3.scatter([vsr[i]], [mflux[i]], s=10,c=[np.log10(namd[i])],edgecolors='m',linewidth=1,vmin=-6,vmax=-0., marker='o',cmap=cm)
    ax3.semilogx()
    ax3.semilogy()
    ax3.set_xlim(19,210)
    ax3.set_xticks([20,60,200])
    ax3.set_xticklabels(['$20$','$60$','$200$'],fontsize=12)
    ax3.set_ylim(2.8e-10,3.3e-9)
    ax3.set_yticks([3e-10,1e-9,3e-9])
    ax3.set_yticklabels(['$10^{-9.5}$','$10^{-9}$','$10^{-8.5}$'],fontsize=12)
    ax3.set_ylabel('$\\rm Onest \\ mass  \\ loss  \\ rate  \\ [M_{\\odot} \\ yr^{-1}] $',fontsize=12)
    ax3.set_xlabel('$\\rm Cavity \\ expansion  \\ rate  \\ [AU \\ Myr^{-1}] $',fontsize=12)

    x_min = 0.9
    x_max  =0.95
    y_min = 0.4
    y_max  = 0.6
    rect = patches.Rectangle((x_min,y_min), x_max-x_min, y_max-y_min,linewidth=1,edgecolor='red',facecolor='none')
    ax3.add_patch(rect)
    cbar_ax = f.add_axes([0.91,0.11,0.01,0.77])
    cbar = f.colorbar(sc,cax=cbar_ax,orientation='vertical',ticks=[-6,-4,-2,0])
    cbar.ax.set_yticklabels(['$10^{-6}$','$10^{-4}$', '$10^{-2}$','$1$'],fontsize=12)
    cbar.ax.set_ylabel(' $ \\rm angular \\ momentum \\ deficit $',fontsize=12)
    if optSS == True:
        f.text(0.915,0.43,'--' ,ha = 'center', color='m',fontsize = 12)
        f.text(0.915,0.56,'--' ,ha = 'center', color='m',fontsize = 12)
        #f.text(0.915,0.45,'--' ,ha = 'center', color='m',fontsize = 12)
        #f.text(0.915,0.54,'--' ,ha = 'center', color='m',fontsize = 12)
        f.text(0.915,0.48,'-' ,ha = 'center', color='m',fontsize = 30)
        f.text(0.923,0.5,'solar system' ,va = 'center',rotation=90, color='m',fontsize =9)
        f.text(0.932,0.5,'analog' ,va = 'center',rotation=90, color='m',fontsize =9)
    f.savefig(savedir+filename+'.pdf',orientation='landscape', format='pdf',bbox_inches='tight', pad_inches=0.1)


def checksystem(N, namd,rmc,namdSS,rmcSS,S_max,S_min):
    N4 = 0
    N3 = 0
    N5=  0
    N6 = 0
    NSS = 0
    for i in range(len(N)):
        if N[i] == 4:  N4 = N4 +1
        if N[i] == 5:  N5 = N5 +1
        if N[i] == 6:  N6 = N6 +1
        if N[i] <= 3:  N3 = N3 +1
        if N[i] ==4 and namd[i]<S_max*namdSS and namd[i]>S_min*namdSS and rmc[i]<S_max*rmcSS and rmc[i]>S_min*rmcSS:
            NSS = NSS + 1
            #print (i)
    return  N3, N4, N5,N6, NSS



def diskparameter_color_new(semi,namd, rmc, Naim, mflux, vsr, tau0, taud, atext, namdSS, rmcSS, savedir, filename, nump, nvar,filenum0, wdir,pydir,fcase,ftype,opt_REBOUND,opt_FILE):
    plt.close('all')
    plt.clf()
    f,(ax1,ax2,ax3) = plt.subplots(1,3, num=33,figsize=(13,4))
    f.subplots_adjust(wspace=0.33)
    cm = plt.cm.get_cmap('coolwarm')
    optSS = True
    S_max = 3.0
    S_min = 1./S_max
    i_SS = 0
    f.text(0.52,0.9,atext ,ha = 'center',fontsize = 12)
    #mass,semi,ecc,inc,NP,TIMEP = data_MC(nump, nvar,filenum0, wdir,pydir,fcase,ftype,opt_REBOUND,opt_FILE)

    for i in range(len(Naim)):
    	if Naim[i] ==max(Naim):
        	sc = ax1.scatter([mflux[i]], [taud[i]], s=40,c=[np.log10(namd[i])],edgecolors='grey',linewidth=1.7,vmin=-5.,vmax=-0.0, marker='o',zorder=1,cmap=cm)
    	else:
        	sc = ax1.scatter([mflux[i]], [taud[i]], s=40,c=[np.log10(namd[i])],edgecolors=None,vmin=-5.,vmax=-0.0,marker='o',zorder=2,cmap=cm)
    	if Naim[i] ==4 and optSS == True:
        	if namd[i]< S_max*namdSS and  namd[i]>S_min*namdSS and rmc[i]< S_max*rmcSS and  rmc[i]>S_min*rmcSS and  semi[i][0] == sorted(semi[i])[0]  and  semi[i][1] == sorted(semi[i])[1] :
            		sc = ax1.scatter([mflux[i]], [taud[i]], s=40,c='k',vmin=-5.,vmax=-0., marker='o',zorder=3,cmap=cm)
 
   
    ax1.semilogx()
    ax1.semilogy()
    ax1.set_xlim(2.8e-10,3.3e-9)
    ax1.set_xticks([3e-10,1e-9,3e-9])
    ax1.set_xticklabels(['$10^{-9.5}$','$10^{-9}$','$10^{-8.5}$'],fontsize=12)
    ax1.set_ylim(0.95e+5,1.1e+6)
    ax1.set_yticks([1e+5,3.3e+5,1e+6])
    ax1.set_yticklabels(['$10^{5}$','$ 10^{5.5}$','$10^{6}$'],fontsize=12)
    ax1.set_ylabel('$\\rm Disk \\ dispersal  \\ timescale  \\ [ yr] $',fontsize=12)
    ax1.set_xlabel('$\\rm Onest \\ mass  \\ loss  \\ rate  \\ [M_{\\odot} \\ yr^{-1}] $',fontsize=12)

    for i in range(len(Naim)):
    	if Naim[i] ==max(Naim):
        	sc = ax2.scatter([taud[i]], [vsr[i]], s=40,c=[np.log10(namd[i])],edgecolors='grey',linewidth=1.7,vmin=-5.,vmax=-0.0, marker='o',zorder=1,cmap=cm)
    	else:
        	sc = ax2.scatter([taud[i]], [vsr[i]], s=40,c=[np.log10(namd[i])],edgecolors=None,vmin=-5.,vmax=-0.0,marker='o',zorder=2,cmap=cm)
    	if Naim[i] ==4 and optSS == True:
        	if namd[i]< S_max*namdSS and  namd[i]>S_min*namdSS and rmc[i]< S_max*rmcSS and  rmc[i]>S_min*rmcSS and  semi[i][0] == sorted(semi[i])[0]  and  semi[i][1] == sorted(semi[i])[1] :
                    sc = ax2.scatter([taud[i]], [vsr[i]], s=40,c='k',vmin=-5.,vmax=-0., marker='o',zorder=3,cmap=cm)





    ax2.semilogx()
    ax2.semilogy()
    ax2.set_ylim(19,210)
    ax2.set_yticks([20,60,200])
    ax2.set_yticklabels(['$20$','$60$','$200$'],fontsize=12)
    ax2.set_ylabel('$\\rm Cavity \\ expansion  \\ rate  \\ [AU \\ Myr^{-1}] $',fontsize=12)
    ax2.set_xlim(0.95e+5,1.1e+6)
    ax2.set_xticks([1e+5,3.3e+5,1e+6])
    ax2.set_xticklabels(['$10^{5}$','$ 10^{5.5}$','$10^{6}$'],fontsize=12)
    ax2.set_xlabel('$\\rm Disk \\ dispersal  \\ timescale  \\ [yr] $',fontsize=12)


    for i in range(len(Naim)):
        if Naim[i] ==max(Naim):
        	sc = ax3.scatter([vsr[i]], [mflux[i]], s=40,c=[np.log10(namd[i])],edgecolors='grey',linewidth=1.7,vmin=-5.,vmax=-0.0, marker='o',zorder=1,cmap=cm)
        else:
        	sc = ax3.scatter([vsr[i]],[mflux[i]], s=40,c=[np.log10(namd[i])],edgecolors=None,vmin=-5.,vmax=-0.0,marker='o',zorder=2,cmap=cm)
        if Naim[i] ==4 and optSS == True:
            if namd[i]< S_max*namdSS and  namd[i]>S_min*namdSS and rmc[i]< S_max*rmcSS and  rmc[i]>S_min*rmcSS and  semi[i][0] == sorted(semi[i])[0]  and  semi[i][1] == sorted(semi[i])[1]:
                sc = ax3.scatter([vsr[i]], [mflux[i]], s=40,c='k',vmin=-5.,vmax=-0., marker='o',zorder=3,cmap=cm)



    ax3.semilogx()
    ax3.semilogy()
    ax3.set_xlim(19,210)
    ax3.set_xticks([20,60,200])
    ax3.set_xticklabels(['$20$','$60$','$200$'],fontsize=12)
    ax3.set_ylim(2.8e-10,3.3e-9)
    ax3.set_yticks([3e-10,1e-9,3e-9])
    ax3.set_yticklabels(['$10^{-9.5}$','$10^{-9}$','$10^{-8.5}$'],fontsize=12)
    ax3.set_ylabel('$\\rm Onest \\ mass  \\ loss  \\ rate  \\ [M_{\\odot} \\ yr^{-1}] $',fontsize=12)
    ax3.set_xlabel('$\\rm Cavity \\ expansion  \\ rate  \\ [AU \\ Myr^{-1}] $',fontsize=12)

    x_min = 0.9
    x_max  =0.95
    y_min = 0.4
    y_max  = 0.6
    rect = patches.Rectangle((x_min,y_min), x_max-x_min, y_max-y_min,linewidth=1,edgecolor='red',facecolor='none')
    ax3.add_patch(rect)
    cbar_ax = f.add_axes([0.91,0.11,0.01,0.77])
    cbar = f.colorbar(sc,cax=cbar_ax,orientation='vertical',ticks=[-4,-2,0])
    cbar.ax.set_yticklabels(['$10^{-4}$', '$10^{-2}$','$1$'],fontsize=12)
    cbar.ax.set_ylabel(' $ \\rm angular \\ momentum \\ deficit $',fontsize=12)
    if optSS == True:
        f.text(0.915,0.37,'-' ,ha = 'center', color='k',fontsize = 30)
        f.text(0.915,0.51,'-' ,ha = 'center', color='k',fontsize = 30)
        f.text(0.923,0.44,'solar system' ,va = 'center',rotation=90, color='k',fontsize =9)
        f.text(0.932,0.45,'analogy' ,va = 'center',rotation=90, color='k',fontsize =9)
    f.savefig(savedir+filename+'.pdf',orientation='landscape', format='pdf',bbox_inches='tight', pad_inches=0.1)


