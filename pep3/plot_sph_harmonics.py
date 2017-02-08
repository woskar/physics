# plot_sph_harmonics.py - python script for plotting spherical harmonics
# by Andreas Gruebl, agruebl@kip.uni-heidelberg.de

import numpy as np
import matplotlib.pyplot as plt

# there's a function to calculate spherical harmonics:
from scipy.special import sph_harm 

# required for colored 3D plots:
from mpl_toolkits.mplot3d import Axes3D 
from matplotlib import cm


theta_1d = np.linspace(0,   np.pi,  91) # 2-degree steps
phi_1d   = np.linspace(0, 2*np.pi, 181)

# generate coordinate system for 3D polar plot
theta_2d, phi_2d = np.meshgrid(theta_1d, phi_1d)
xyz_2d = np.array([np.sin(theta_2d) * np.sin(phi_2d),
                  np.sin(theta_2d) * np.cos(phi_2d),
                  np.cos(theta_2d)]) 


# real-value of Y will be coded as color. Define the color range here:
colormap = cm.ScalarMappable( cmap=plt.get_cmap("cool"))
colormap.set_clim(-.45, .45)
colormap.set_array(xyz_2d)
limit = .1

def show_Y_lm(l, m):
    print("Y_%i_%i" % (l,m)) # show what we're plotting
    plt.figure()
    # we want a 3D figure:
    ax = plt.gca(projection = "3d")
    
    # label everything
    ax.set_title("$Y^{%i}_{%i}$" % (m,l))
    ax.set_xlabel("$|Y^{%i}_{%i}|_x^2$" % (m,l))
    ax.set_ylabel("$|Y^{%i}_{%i}|_y^2$" % (m,l))
    ax.set_zlabel("$|Y^{%i}_{%i}|_z^2$" % (m,l))
    
    # value of sph. harm. function (will be color-coded in the plot)
    Y_lm = sph_harm(m,l, phi_2d, theta_2d)
    
    # the squared absolute value will be used as distance from origin
    r = (np.abs(Y_lm)**2)*xyz_2d
    surf = ax.plot_surface(r[0], r[1], r[2],
                    facecolors=colormap.to_rgba(Y_lm.real),
                    rstride=4, cstride=2, linewidth=.25, shade=False)
    # make the edges visible...:
    surf.set_edgecolors('black')
    
    # make it nice...
    ax.set_xlim(-np.amax(r), np.amax(r))
    ax.set_ylim(-np.amax(r), np.amax(r))
    ax.set_zlim(-np.amax(r), np.amax(r))
    plt.colorbar(colormap)
    

# Plot everything with the following values for l and m:
l = 1
m = 1

plt.close()
show_Y_lm(l,m)

plt.savefig('y_l'+str(l)+'_m'+str(m)+'_3d.png')

plt.show()