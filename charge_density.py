import numpy as np
import pylab as pl
import matplotlib.pyplot as mpl
import pandas as pd
import glob
import sys
import os
filenames = glob.glob('C:/cygwin64/home\siu851591172/mos2_defect\*.dat')
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['mathtext.fontset'] = 'dejavuserif'
for f in filenames:
    
    save_name = os.path.split(f)[-1]
    save_name = save_name.split('.')[0].split('_')
    delim = ' '
    save_delim = '_'
    final_save = save_delim.join(save_name)
    title = delim.join(save_name).title()
    if 'H3' in title:
        y_max = 10.5
    else:
        y_max = 10
    print(y_max)
    df = pd.read_csv(f,header=None,sep='\s+')
    charge_den = df.iloc[:,1]
    position = df.iloc[:,0]
    position = position/1.88973
    plot = mpl.plot(charge_den,position,c='r',linewidth=2)
    mpl.tight_layout(pad=4.5)
    mpl.ticklabel_format(style='sci',axis='x',scilimits=(0,0),useMathText=True)
    #mpl.title(label=title,fontsize='xx-large')
    left_lim = -1*max(charge_den)
    right_lim = max(charge_den)
    mpl.xlim(left_lim,right_lim)
    mpl.ylim(3.5,y_max)
    mpl.grid(b=True,dashes=(5,1),alpha=0.7)
    mpl.tick_params(axis='both',labelsize='large',direction='in',grid_linewidth=0.5)
    mpl.xticks([left_lim, left_lim/2,0,right_lim/2,right_lim])
    mpl.xlabel(r'$\rho$ (e/$\AA$)',fontsize='xx-large',fontname='serif')
    mpl.ylabel(r'Z ($\AA$)',fontsize='xx-large')
    mpl.axvline(0,linewidth=.5,color='black',dashes=(7,3))
    mpl.savefig(final_save,optimize=True)
    mpl.show()
    mpl.clf()
