import numpy as np
from scipy.stats import binom
def checknonzero(val,p):
    if val==0:
        return 1-p
    else:
        return p
def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    np.array(x)
    np.array(p)
    Mean = p
    var = p*(1-p)
    pmf = []
    for val in x:
        if val ==0:
            pmf.append(1-p)
        else:
            pmf.append(p)
    return (np.array(pmf),Mean,var)
    pass