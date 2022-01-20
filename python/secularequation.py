#!/usr/bin/env python
### calculate the eccentricity mode
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
from scipy.integrate import quad
from astrounit import *




f1 = lambda x,alpha: np.cos(x)/(1-2*alpha*np.cos(x)+alpha**2)**1.5/np.pi
f2 = lambda x,alpha: np.cos(2*x)/(1-2*alpha*np.cos(x)+alpha**2)**1.5/np.pi

def b1_l(alpha): 
    res = quad(f1,0,2*np.pi,args=(alpha,))
    return res[0] 

def b2_l(alpha): 
    res = quad(f2,0,2*np.pi,args=(alpha,))
    return res[0] 


def Axx(j,a,q):
    tmp = 0.0
    for i in range(0,len(a)):
        if j!= i:
            a_max = max(a[j],a[i])
            a_min = min(a[j],a[i])
            alpha = a_min/a_max
            b = b1_l(alpha)
            tmp = tmp + q[i]/(1+q[j])*alpha*b/a_max
    n_j = (G*Msun/(a[j]*AU)**3)**0.5*Year*180./np.pi # [degree/yr]
    res =  n_j*a[j]/4.0*tmp
    return  res 

def Axy(j,k,a,q):
    a_max = max(a[j],a[k])
    a_min = min(a[j],a[k])
    alpha = a_min/a_max
    b = b2_l(alpha)
    tmp =  q[k]/(1+q[j])*alpha*b/a_max
    n_j = (G*Msun/(a[j]*AU)**3)**0.5*Year*180./np.pi # [degree/yr]
    res =  -n_j*a[j]/4.0*tmp
    return  res 


def cal_eccmode(a,q,e,w):
    h = [e[0]*np.sin(w[0]),e[1]*np.sin(w[1])]
    k = [e[0]*np.cos(w[0]),e[1]*np.cos(w[1])]
    A= np.array([ [Axx(0,a,q), Axy(0,1,a,q)],[ Axy(1,0, a,q),Axx(1,a,q)]] )
    res1 = np.linalg.eig(A)[0]*3600 #arcsec/yr 
    E = np.linalg.eig(A)[1]
    S1sb = (h[0]*E[1,1]-h[1]*E[0,1])/(E[1,1]*E[0,0] -E[0,1]*E[1,0])
    S2sb  = (h[0] - E[0,0]*S1sb)/E[0,1]
    S1cb = (k[0]*E[1,1]-k[1]*E[0,1])/(E[1,1]*E[0,0] -E[0,1]*E[1,0])
    S2cb  = (k[0] - E[0,0]*S1cb)/E[0,1]
    S1 = (S1sb**2 + S1cb**2)**0.5
    S2 = (S2sb**2 + S2cb**2)**0.5
    res2 = [[E[0,0]*S1, E[0,1]*S2],[  E[1,0]*S1,E[1,1]*S2]]
    return res1, res2


