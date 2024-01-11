import pandas as pd
import numpy as np

def generate_return_series(expected_annual_return, annual_volatility, freq, num_series=1, start_date='2023-01-01', dist='normal', length=365):
    """
    Generate a DataFrame with independent series of returns.

    Parameters:
    - expected_annual_return: Expected annual return as a decimal (e.g., 0.05 for 5%).
    - annual_volatility: Annual volatility as a decimal (e.g., 0.2 for 20%).
    - freq: Frequency of returns ('D' for daily, 'H' for hourly, 'T' for minutely).
    - num_series: Number of independent series to generate. Default is 1.
    - start_date: Start date for the series. Default is '2022-01-01'.
    - dist: Distribution type ('normal' or 'lognormal'). Default is 'normal'.
    - length: Number of days, hours, or minutes to generate. Default is 252.

    Returns:
    - DataFrame with columns as independent return series.
    """