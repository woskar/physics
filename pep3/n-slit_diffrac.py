# n-slit_diffrac.py - diffraction with sampling of particle positions
# by Bjoern Malte Schaefer, GSFP+/Heidelberg, bjoern.malte.schaefer@uni-heidelberg.de
#    Andreas Gruebl, KIP Heidelberg, agruebl@kip.uni-heidelberg.de

import numpy as np
import pylab as plt

rep = 1000
nslit = 4

# constants that can be used for computation including slit geometry:
# -> these are needed, in case you simulate for the diffraction angle
# -> use reasonable values :-)
# slit spacing/pitch
g = 1e-6
# wave length
l = 1e-8

plt.close()


# define intensity as a function of phi
def intensity(phi):
        # THE FOLLOWING RESULT IS NONSENSE!
        # put the calculation of the intensity here!!!
        result = (0.1 * phi)**2
        return(result)


# plot calculated diffraction pattern
x = np.linspace(-np.pi,+np.pi,100)
y = intensity(x)
# norm intensity:
norm = np.trapz(y,x)
plt.plot(x,y/norm,'g--',linewidth=3)

# random experiment
data = np.zeros(rep)
i = 0
for i in range(0,rep):
        sample = 0
        while(sample == 0):
                pos = np.random.uniform(-np.pi,+np.pi,1)
                target = intensity(pos)
                trial = np.random.uniform(0.0,1.0,1)
                if trial <= target:
                        data[i] = pos
                        i = i + 1
                        sample = 1
                else:
                        sample = 0

# plot samples
plt.hist(data,x,normed = True)

# add axis labelling
plt.xlabel(r'phase difference $\varphi$')
plt.ylabel(r'intensity $I(\varphi)$')
plt.xlim([-4,+4])

# plot pattern (into separate box)
aux = np.random.uniform(0,1,rep)

a = plt.axes([0.2, 0.6, .2, .2])
plt.plot(data,aux,'k,')
plt.setp(a, xlim=(-4,+4),xticks=[-4,-2,0,2,4],yticks=[])

plt.show()
