import qmcpy  #we import the environment at the start to use it
import numpy as np  #basic numerical routines in Python
import time  #timing routines
import warnings  #to suppress warnings when needed
import torch  #only needed for PyTorch Sobol' backend
from torch.quasirandom import SobolEngine
from matplotlib import pyplot  #plotting

def plot_successive_points(distrib,ld_name,first_n=64,n_cols=1,pt_clr='bgkcmy',xlim=[0,1],ylim=[0,1],coord1 = 0,coord2 = 1,file_name = 'pic'):
    fig,ax = pyplot.subplots(nrows=1,ncols=n_cols,figsize=(50*n_cols,50))
    if n_cols==1:
        ax = [ax]
    last_n = first_n*(2**n_cols)
    points = distrib.gen_samples(n=last_n)
    for i in range(n_cols):
        n = first_n
        nstart = 0
        for j in range(i+1):
            n = first_n*(2**j)
            ax[i].scatter(points[nstart:n,coord1],points[nstart:n,coord2],color=pt_clr[j],s = 1)
            nstart = n
        ax[i].set_title('n = %d'%n)
        ax[i].set_xlim(xlim); ax[i].set_xticks(xlim); ax[i].set_xlabel('$x_{i,%d}$'%(coord1+1))
        ax[i].set_ylim(ylim); ax[i].set_yticks(ylim); ax[i].set_ylabel('$x_{i,%d}$'%(coord2+1))
        ax[i].set_aspect((xlim[1]-xlim[0])/(ylim[1]-ylim[0]))
    fig.suptitle('%s Points'%ld_name)
    pyplot.savefig('{}.png'.format(file_name))

def generate_halton(row,columns,n):
    halton = qmcpy.Halton(columns)
    points = halton.gen_samples(row)
    print(f'\nLD Halton Points with shape {points.shape}\n'+str(points))
    plot_successive_points(halton,'Halton',first_n=n, file_name =str(row)+'_'+str(columns)+'_'+str(n))

generate_halton(1,2,1000)
generate_halton(1,3,1000)
generate_halton(1,4,1000)
generate_halton(1,30,1000)
generate_halton(29,30,1000)
generate_halton(10,11,1000)
generate_halton(1,2,100000)
generate_halton(1,3,100000)
generate_halton(1,4,100000)
generate_halton(1,30,100000)
generate_halton(29,30,100000)
generate_halton(10,11,100000)


