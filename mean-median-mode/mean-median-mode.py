import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x = np.array(x)
    centralTendency =()
    mean = np.mean(x)
    median = np.median(x)
    counts = Counter(x)
    mode_value, frequency = counts.most_common(1)[0]
    print(mode_value)
    print(frequency)
    centralTendency+=(mean,median,mode_value)
    return centralTendency