import numpy as np

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
        if value==100:
            result.append(x[n-1])
        elif value==0:
            result.append(x[0])
        elif n==1:
            result.append(x[0])
        else:
            index = value/100*(n-1)
            #print(value)
            print(index)
            lower = x[int(index)]
            #print(lower)
            upper = x[int(index)+1]
            #print(upper)
            weight = index - int(index)
            #print(weight)
            result.append(lower + (upper - lower)*weight)
    return np.array(result)
    #return np.array(x)
    