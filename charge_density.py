import numpy as np
import pylab as pl
import matplotlib.pyplot as mpl
import pandas as pd

df = pd.read_csv('avg.dat',header=None,sep='\s+')
charge_den = df.iloc[:,1]
position = df.iloc[:,0]
position = position/1.88973
plot = mpl.plot(charge_den,position,c='r',linewidth=2)
mpl.ticklabel_format(style='sci',axis='both',scilimits=(0,0),useMathText=True)
mpl.xlim(-0.000125,0.000125)
mpl.ylim(0,25)
mpl.grid(b=True,dashes=(5,1),alpha=0.7)
mpl.tick_params(axis='both',labelsize='large',direction='in',grid_linewidth=0.5)
#pl.xlabel(r'$\rho$(C/$\AA^3$)',fontsize='x-large',fontname='Comic Sans MS')
pl.xlabel(r'$\rho$(C/$\AA^3$)',fontsize='x-large')
pl.ylabel(r'Z($\AA$)',fontsize='x-large')
pl.axvline(0,linewidth=.5,color='black',dashes=(7,3))
pl.savefig("Methanol_OH_MoS2_Monolayer_ChargeDen")
