#!/usr/bin/env python
# This was written by Levi Lentz for the Kolpak Group at MIT
# This is distributed under the MIT license


import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
import sys
import pylab

mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['mathtext.fontset'] = 'dejavuserif'


#This function extracts the high symmetry points from the output of bandx.out
def Symmetries(fstring): 
  f = open(fstring,'r')
  x = np.zeros(0)
  for i in f:
    if "high-symmetry" in i:
      x = np.append(x,float(i.split()[-1]))
  f.close()
  return x
# This function takes in the datafile, the fermi energy, the symmetry file, a subplot, and the label
# It then extracts the band data, and plots the bands, the fermi energy in red, and the high symmetry points
def bndplot(datafile,fermi,symmetryfile,subplot,label,name):
  z = np.loadtxt(datafile) #This loads the bandx.dat.gnu file
  x = np.unique(z[:,0]) #This is all the unique x-points
  bands = []
  bndl = len(z[z[:,0]==x[1]]) #This gives the number of bands in the calculation
  Fermi = float(fermi)
  for i in range(0,bndl):
    bands.append(np.zeros([len(x),2])) #This is where we store the bands
  for i in range(0,len(x)):
    sel = z[z[:,0] == x[i]]  #Here is the energies for a given x
    test = []
    for j in range(0,bndl): #This separates it out into a single band
      bands[j][i][0] = x[i]
      bands[j][i][1] = np.multiply(sel[j][1],1) - Fermi
  axes = [min(x),max(x), -2.5,  2.5]
  for i in bands: #Here we plots the bands
    subplot.plot(i[:,0],i[:,1],color="black")
  temp = Symmetries(symmetryfile)
  for j in temp: #This is the high symmetry lines
    x1 = [j,j]
    x2 = [axes[2],axes[3]]
    fig = subplot.plot(x1,x2,'--',lw=0.55,color='black',alpha=0.75)
  subplot.plot([min(x),max(x)],[0,0],color='red',)
  subplot.xticks(Symmetries(symmetryfile),[r'$\Gamma$','K','M',r'$\Gamma$'])
  plt.tick_params
  subplot.ylim([axes[2],axes[3]])
  subplot.xlim([axes[0],axes[1]])
  #subplot.text((axes[1]-axes[0])/2.0,axes[3]+0.2,label,va='center',ha='center',fontsize=18)
  plt.tick_params(axis="both", direction="in", right=True, labelsize=16)
  plt.ylabel("eV - $\epsilon$", fontsize=22)
  #plt.savefig(name)

dstring = "C:\PythonProjects\Research_Projects\Plot\mos2.band.gnu"
astring = "C:\PythonProjects\Research_Projects\Plot/bands.out"
name = "Bilayer_two_unit_Mos2_3"
title = "Two by Two Unit cell Bilayer MoS2"
bndplot(dstring,2.9029,astring,pylab,title,name)
plt.show()
