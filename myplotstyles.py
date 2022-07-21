

from cmath import log
from pytest import mark
import matplotlib.dates as mdates
import numpy as np

def plot_standard(datax,datay,xlimit,ylimit,xlabel,ylabel,title,\
    fignumber=0,type='o',color='deepskyblue',markersize=3, textonplot = False,textarray=[],\
    textposx=[],textposy=[],textsize=9, textcolor='black', textweight='normal',squareplot=True,\
    label='',labelloc='upper left', labelsize=8, xscale = 'linear', yscale= 'linear',linewidth=0,\
    cbar=False):

    # standardplot(datax,datay,style,xlim,ylim,xlabel,ylable,title)
    # optional - markersize etc. all what is optional in .plot

    #/////////////// loading modules////////////////
    from matplotlib.ticker import AutoMinorLocator
    import matplotlib.pyplot as plt
    from matplotlib.ticker import FormatStrFormatter
    import matplotlib as mplt
    # //////////////// set figure /////////////////
    fig=plt.figure(fignumber)

    # //////////////// plot data /////////////////

    # set the axes class
    if str(yscale) or str(xscale) == 'log':
        logarithmic = True
        ax = fig.add_subplot(1, 1, 1)
        ax.set_xscale(str(xscale)) # set linear or logarithmic
        ax.set_yscale(str(yscale)) # set linear or logarithmic

    else:
         ax = fig.add_axes([0.1,0.1,0.8,0.8])  #used to use this for linear plots
    
    # plot the data related to this axes
    if linewidth!=0:
        data = ax.plot(datax,datay,type,markersize=markersize, color=color, label=label, linewidth=linewidth)
    else:
         data = ax.plot(datax,datay,type,markersize=markersize, color=color, label=label)

    # range of axes depending on data
    ax.set_xlim(xlimit)
    ax.set_ylim(ylimit)
    
    #add Legend
    if (label!=''):
        ax.legend(prop={"size":labelsize},loc=labelloc, bbox_to_anchor=(1.0, 1.0))
    # /////////////////////////// axes style /////////////////////////////

    #make equal axes =  square plot
    if (squareplot==True):
        ax.set_aspect(1.0/ax.get_data_ratio(), adjustable='box')
    

    if logarithmic== True:
        #major ticks
        ax.tick_params(axis="y",which='major',direction="in", size=5)
        ax.tick_params(axis="x",which='major',direction="in", size=5)
        #minor ticks
        ax.tick_params(axis='x', which='minor',direction="in")
        ax.tick_params(axis='y', which='minor',direction="in")

    else:
        #major ticks
        ax.tick_params(axis="y",which='major',direction="in", size=5)
        ax.tick_params(axis="x",which='major',direction="in", size=5)
        #minor ticks
        ax.xaxis.set_minor_locator(AutoMinorLocator())
        ax.yaxis.set_minor_locator(AutoMinorLocator())
        ax.tick_params(which='minor', length=4, color='black',direction='in', size=3)
    

    # fonts
    font1 = {'family':'serif','fontname':'DejaVu Sans','color':'black','size':12}
    font2 = {'family':'serif','fontname':'DejaVu Sans','color':'black','size':10}  

    # labels and plot title
    ax.set_title(title,fontdict=font1)
    ax.set_xlabel(xlabel,fontdict=font2)
    ax.set_ylabel(ylabel,fontdict=font2)


    #///////////////  adding upper and right ticks /////////////////////

    if logarithmic==True:
        ''' we do not use set_minor_locator(AutoMinorLocator()) because it gives problems'''
        axx = ax.secondary_xaxis('top')
        axy = ax.secondary_yaxis('right')
        # major ticks
        axx.tick_params(axis="x",which='major',direction="in", size=5)
        axy.tick_params(axis="y",which='major',direction="in", size=5)
        #minor ticks
        axx.tick_params(axis="x",which='minor',direction="in", size=3)
        axy.tick_params(axis="y",which='minor',direction="in", size=3)
        # Turn off tick numbers
        axx.set_xticklabels([])
        axy.set_yticklabels([])

    else:
        axx = ax.secondary_xaxis('top')
        axy = ax.secondary_yaxis('right')
        # major ticks
        axx.tick_params(axis="x",which='major',direction="in", size=5)
        axy.tick_params(axis="y",which='major',direction="in", size=5)
        #minor ticks
        axx.xaxis.set_minor_locator(AutoMinorLocator())
        axy.yaxis.set_minor_locator(AutoMinorLocator())
        axx.tick_params(axis="x",which='minor',direction="in", size=3)
        axy.tick_params(axis="y",which='minor',direction="in", size=3)
        # Turn off tick numbers
        axx.set_xticklabels([])
        axy.set_yticklabels([])

    #plt.plot([0,200],[1,1],'--','black')


#///////////////// text on plot //////////////////
    if (textonplot==True):
        j=0
        for x,y in zip(textposx,textposy):
            textondata=textarray[j]
            plt.annotate(textondata,(x,y),textcoords='offset points',\
            xytext=(0,5),ha='center', fontsize=textsize,color=textcolor, weight=textweight)
            j +=1

#////////////////// add colorbar ////////////////

    if cbar == True:
        sm = plt.cm.ScalarMappable(cmap = plt.cm.rainbow, norm = mplt.colors.Normalize(vmin = 2, vmax = 8.2))
        cb=plt.colorbar(sm, fraction = 0.046, pad = 0.04, aspect=20)
        cb.set_label("T [keV]")
        cb.ax.tick_params(direction = "in", which = "major", labelsize = 10, size = 6, width = 1)
  
  
  
  
    

def oplot_standard(datax,datay,fignumber=0,type='o',color='',markersize=3, textonplot = False,textarray=[],\
    textposx=[],textposy=[],textsize=9, textcolor='black', textweight='normal', linewidth=0, label='', \
    labelloc='upper left', labelsize=8, cbar = True):

    
    #/////////////// loading modules////////////////
    import matplotlib.pyplot as plt
    import matplotlib as mplt
    # //////////////// set figure /////////////////
    if linewidth!=0:
        if color=='':
            plt.plot(datax,datay,type,markersize=markersize,linewidth=linewidth,label=label)
        else:
            plt.plot(datax,datay,type,color=color,markersize=markersize,linewidth=linewidth,label=label)
    else:
        if color=='':
            plt.plot(datax,datay,type,markersize=markersize,label=label)
        else:
            plt.plot(datax,datay,type,color=color,markersize=markersize,label=label)

    #add Legend
    if (label!=''):
        #plt.legend(prop={"size":labelsize}, loc=labelloc)
        plt.legend(prop={"size":labelsize},loc=labelloc, bbox_to_anchor=(1.0, 1.0))
    #///////////////// text on plot //////////////////
    if (textonplot==True):
        j=0
        for x,y in zip(textposx,textposy):
            textondata=textarray[j]
            plt.annotate(textondata,(x,y),textcoords='offset points',\
            xytext=(0,5),ha='center', fontsize=textsize, color=textcolor, weight=textweight)
            j +=1
  


def plot_linear_fit(datax,datay,xrange,position=[25,5.9],color='red'):
    
    import numpy as np
    import matplotlib.pyplot as plt
    import myfits as myf

    myf.linear(datax,datay,xrange)
    model=np.polyfit(datax, datay,1)

    slope=model[0]
    startb=model[1]

    freevariable = np.linspace(xrange[0],xrange[1],xrange[1]) # generate an array of 60 equally space points
    fit_eq = slope*freevariable + startb  #obtaining the y axis values for the fitting function

    plt.plot(freevariable,fit_eq, '-.',color=color,linewidth=0.4)
    plt.annotate('Linear Fit',(position[0],position[1]),textcoords='offset points',xytext=(0,0),ha='center',color='red')
    plt.annotate('y=a*x + b',(position[0],position[1]-0.5),textcoords='offset points',xytext=(0,0),ha='center',color='red')
    trunc_slope=round(slope,3)
    trunc_startb=round(startb,3)
    plt.annotate('a=',(position[0],position[1]-1.0),textcoords='offset points',xytext=(-15,0),ha='center',color='red')
    plt.annotate(trunc_slope,(position[0],position[1]-1.0),textcoords='offset points',xytext=(10,0),ha='center',color='red')
    plt.annotate('b=',(position[0],position[1]-1.5),textcoords='offset points',xytext=(-15,0),ha='center',color='red')
    plt.annotate(trunc_startb,(position[0],position[1]-1.5),textcoords='offset points',xytext=(10,0),ha='center',color='red')
