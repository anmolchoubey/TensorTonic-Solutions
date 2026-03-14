import numpy as np
import math
def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    n = len(x)
    sum = 0
    np.array(x)
    print(x)
    meanX = np.mean(x)
    print(meanX)
    for value in x:
        sum += (value-meanX)**2
    var = sum/(n-1)
    std = math.sqrt(var)
    
    return (var,std)