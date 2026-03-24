import numpy as np
import pandas as pd

def calculate_psi(expected, actual, buckets=10):
    breakpoints = np.linspace(0, 1, buckets+1)
    expected_perc = np.histogram(expected, breakpoints)[0] / len(expected)
    actual_perc = np.histogram(actual, breakpoints)[0] / len(actual)

    psi = np.sum((expected_perc - actual_perc) * np.log((expected_perc+1e-6)/(actual_perc+1e-6)))
    return psi

def calculate_csi(train, prod, column, buckets=10):
    breakpoints = np.percentile(train[column], np.arange(0, 101, 100/buckets))

    train_bins = pd.cut(train[column], breakpoints, include_lowest=True)
    prod_bins = pd.cut(prod[column], breakpoints, include_lowest=True)

    train_dist = train_bins.value_counts(normalize=True)
    prod_dist = prod_bins.value_counts(normalize=True)

    csi = np.sum((train_dist - prod_dist) * np.log((train_dist+1e-6)/(prod_dist+1e-6)))
    return csi
