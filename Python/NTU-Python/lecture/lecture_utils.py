import numpy as np

def samples_example(start, end, samples):
    step = (end-start)/samples
    x = np.arange(start, end, step)
    y = np.square(x)-2*x-3



    return (x.tolist(),y.tolist())

def sample_rate_example(start, end, fs):
    step = 1/fs
    x = np.arange(start, end, step)
    y = np.square(x)-2*x-3



    return (x.tolist(),y.tolist())

def sin_example(start, end, f):
    fs = 1000000
    step = 1/fs
    x = np.arange(start, end, step)
    y = np.sin(2*np.pi*f*x)

    return (x.tolist(),y.tolist())
