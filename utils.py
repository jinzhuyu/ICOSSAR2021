# -*- coding: utf-8 -*-
# set default plot parameters
def set_default_plot_param(plt):
	# %matplotlib inline
	# from matplotlib import pyplot as plt
    
    plt.style.use('classic')
    
    plt.rcParams["font.family"] = "Helvetica"
    plt.rcParams['font.weight']= 'normal'
    plt.rcParams['figure.figsize'] = [6, 6*3/4]
   
    plt.rcParams['figure.facecolor'] = 'white'
    plt.rcParams['axes.facecolor'] = 'white'
    plt.rcParams['axes.axisbelow'] = True

    plt.rc('axes', titlesize=16, labelsize=15, linewidth=0.9)    # fontsize of the axes title, the x and y labels
    
    plt.rc('lines', linewidth=1.8, markersize=6, markeredgecolor='none')
    
    plt.rc('xtick', labelsize=13)
    plt.rc('ytick', labelsize=13)

    plt.rcParams['axes.formatter.useoffset'] = False # turn off offset
    # To turn off scientific notation, use: ax.ticklabel_format(style='plain') or
    # plt.ticklabel_format(style='plain')

    
    plt.rcParams['legend.fontsize'] = 13
    plt.rcParams["legend.fancybox"] = True
    plt.rcParams["legend.loc"] = "best"
    plt.rcParams["legend.framealpha"] = 0.5

    
    plt.rcParams['savefig.bbox'] = 'tight'
    plt.rcParams['savefig.dpi'] = 800
    
#    plt.rc('text', usetex=False)
