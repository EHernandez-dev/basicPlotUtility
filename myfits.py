def linear(datax,datay,xrange=[0,3]):
    
    import numpy as np
    model=np.polyfit(datax, datay,1)

    slope=model[0]
    startb=model[1]

    freevariable = np.linspace(xrange[0],xrange[1],xrange[1]) # generate an array of 60 equally space points
    fit_eq = slope*freevariable + startb  #obtaining the y axis values for the fitting function

