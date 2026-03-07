import numpy as np
import math

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    n = len(x)
    print(n)
    x=np.sort(x)
    print(x)
    result = []
    for value in q:
        # if value==100:
        #     result.append(x[n-1])
        # elif value==0:
        #     result.append(x[0])
        # elif n==1:
        #     result.append(x[0])
        # else:
        index = value/100*(n-1)
            #print(value)
        print(index)
        lower = math.floor(index)
            #print(lower)
        upper =math.ceil(index)

        if lower==upper:
            result.append(x[lower])
            continue
            #print(upper)
        weight = index-lower
        lower_val = x[lower]
        upper_val = x[upper]
            #print(weight)
        result.append(lower_val + (upper_val - lower_val)*weight)
    return np.array(result)
    #return np.array(x)
    