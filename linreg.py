import numpy as np

def lin_regr_func(x,y):
    n = len(x)
    # denominator
    d = (n*(x**2).sum()-x.sum()**2)
    # intercept
    a = (y.sum()*(x**2).sum()-x.sum()*(x*y).sum())/d
    # slope
    b = (n*(x*y).sum()-x.sum()*y.sum())/d
    
    y_pred = x*b+a
    yyi = (y-y_pred)**2
    xxi = (x.mean()-x)**2
    
    #standard error for a
    sa = np.sqrt(yyi.sum()/(n-2)*(1/n+(x.mean())**2/xxi.sum()))
    
    
    #standard error for b
    sb = np.sqrt(yyi.sum()/(n-2))/np.sqrt(xxi.sum())
    
    # correlation coefficient
    corr_coeff = (n*(x*y).sum() - x.sum()*y.sum())/(np.sqrt(n*(x**2).sum()-x.sum()**2)*np.sqrt((n*(y**2).sum()-y.sum()**2)))
    
    return a,b,corr_coeff,sa,sb

