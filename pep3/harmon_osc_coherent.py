# harmon_osc_coherent.py - python script for animating the eigenfunctions of the harmonic oscillator
# by Andreas Gruebl, agruebl@kip.uni-heidelberg.de
#    and Bjoern Malte Schaefer, GSFP+/Heidelberg, bjoern.malte.schaefer@uni-heidelberg.de
# based on a script by Svenn-Arne Dragly, s@dragly.com

import numpy as np
from matplotlib.pylab import *
import time
import scipy.special as sp
import subprocess

ion()
plt.close()

# number of state(s). nmax=1 results in the ground state
nmax = 1

plot_xlim = 12
plot_ylim = 4

runtime = 10.0 # simulation duration

# x coordinates
x = np.linspace(-plot_xlim,plot_xlim,201)

# lambda (lbda): complex number that is required for the norm of a coherent state (single states are poisson-weighted)
# |lbda|^2 defines the mean quantum number of the state
lbda = 1*(1+1j)

# get Line2D objects from plot command for dynamic update -> animation of temporal development
rr, = plot(x,x,'b-',label='real part')
ii, = plot(x,x,'r-',label='imaginary part')
aa, = plot(x,x,'k-',label='absolute value',linewidth=2)

rr.axes.set_ylim(-plot_ylim,plot_ylim)
rr.axes.set_xlim(-plot_xlim,plot_xlim)

# comment out legend (following 3 lines), in case simulation runs too slow:
plt.xlabel('position $x$')
plt.ylabel('wave function $\psi(x,t)$')
plt.legend(loc='upper right')

# calculate eigenfunctions
def gauss_hermite(x,nosc):
        norm = 1.0 / np.sqrt(np.float64(2**nosc * math.factorial(nosc))) / np.pi ** 0.25
        result = sp.eval_hermite(nosc,x) * np.exp(-x**2 / 2.0) * norm
        return(result)

starttime = time.time()
t = 0
count = 0
# run over 'runtime' seconds real time
while(t < runtime):
        t = time.time() - starttime

        psi = np.zeros(x.shape) + 1j * np.zeros(x.shape)
        # calculate either superposition: set range(0, nmax)
        #                or single state: set range(nmax-1, nmax)
        for nosc in range(nmax-1, nmax):
                evo = np.exp(1j * (nosc+0.5) * t)
                # the norm for coherent states is initially set to 1 to show the result of a simple superposition
                coh_norm = 1
                # in order to construct a coherent state, use this definition of the norm:
                #coh_norm = lbda**nosc * np.exp(-(lbda**2)/2) / np.sqrt(np.float64(math.factorial(nosc)))
                psi += coh_norm * gauss_hermite(x,nosc) * evo 
        # update plot
        rr.set_ydata(psi.real)
        ii.set_ydata(psi.imag)
        aa.set_ydata(abs(psi))
        draw()
        # -- uncomment to have a movie saved:
        #savefig('./frames/frame'+str(count).zfill(5)+'.png')
        count += 1

print(count)

#plt.show()

# -- uncomment to have a movie saved:
# last one with legend...
#savefig('./frames/frame'+str(count).zfill(5)+'.png')

# -- uncomment to have a movie saved:
#subprocess.call(['ffmpeg', '-i', './frames/frame%5d.png', '../plots/temp_devel.avi'])
#subprocess.call(['ffmpeg', '-i', '../plots/temp_devel.avi', '-t', '8', '../plots/temp_devel.gif'])
