import pandas as pd
import numpy as np

def calculate_psi():
    expected = pd.read_csv("data/expected_home_loan.csv")
    actual = pd.read_csv("data/actual_home_loan.csv")

    expected_perc = np.histogram(expected['score'], bins=10)[0] / len(expected)
    actual_perc = np.histogram(actual['score'], bins=10)[0] / len(actual)

    psi = np.sum((actual_perc - expected_perc) * np.log((actual_perc + 1e-6) / (expected_perc + 1e-6)))

    return float(psi)
