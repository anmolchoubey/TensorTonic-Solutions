import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    np.array(p)
    sum_check = np.sum(p)
    print(sum_check)
    if(sum_check!=1 or len(p)!=len(x)):
        raise ValueError("ValueError")
        return 
    else:
        expected = 0
        for index in range(len(x)):
            expected+= x[index]*p[index]
        return expected
