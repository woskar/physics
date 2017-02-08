#PEP3 Blatt 4 Aufgabe 2: Wellenfunktion
#Plot einer Wahrscheinlichkeitsdichte

%matplotlib notebook
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.constants import *
import math
math.pi
matplotlib.rc('text', usetex=True)
matplotlib.rc('font', size=14.0)
matplotlib.rcParams['text.latex.preamble'] = [r'\usepackage{siunitx}']

c=10

f = np.linspace(-100,100,10000)
n_f = [(c/pi)**0.5*(1/((x**2)+c**2)**0.5) for x in f ]
plt.plot(n_f, label=r'$\psi(x)=\psi_{0}\times \ \frac{1}{\sqrt{x^{2}+\sigma^{2}}}$')
#plt.ylabel(r'Vsink $v \, [\mathrm{m/s}]$')


# Titel
plt.title('Aufgabe 4.2: Wellenfunktion')

# Achsenbeschriftungen
plt.xlabel(r'x')# $\phi \, [\mathrm{m}]$')
plt.ylabel(r'Wahrscheinlichkeit') # $d \, [\mathrm{cm}]$')

# Legende
plt.legend(loc='best')
