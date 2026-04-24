import numpy as np

def basic_stats(data):
    return {
        "mean": np.mean(data, axis=0),
        "median": np.median(data, axis=0),
        "std": np.std(data, axis=0)
    }

def normalize(data):
    return (data - np.min(data, axis=0)) / (np.max(data, axis=0) - np.min(data, axis=0))

def correlation(data):
    return np.corrcoef(data, rowvar=False)
