import numpy as np
from scipy.special import comb

def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """
    # Write code here
    pmf = comb(n,k)*(p**k)*((1-p)**(n-k))
    print(pmf)
    cdf = 0
    for x in range(k+1):
        cdf+= comb(n,x)*(p**x)*((1-p)**(n-x))
    print(cdf)
    return (pmf,cdf)