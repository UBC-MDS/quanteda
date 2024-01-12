import pandas as pd
import numpy as np

def generate_return_series(
    expected_annual_return, 
    annual_volatility, 
    n_rows=365, 
    freq='D', 
    num_series=1, 
    dist='normal', 
    random_state=524,
    start_date='2024-01-01'):
    """
    Generate a DataFrame with independent time series of returns.

    Parameters
    ----------
    expected_annual_return : float
        Expected annualized return as a decimal (e.g., 0.05 for 5%).

    annual_volatility : float
        Annualized volatility as a decimal (e.g., 0.2 for 20%).

    n_rows=365, 
        Number of days, hours, or minutes to generate.

    freq : {'D', 'H', 'min'}, default 'D'
        Frequency of returns ('D' for daily, 'H' for hourly, 'min' for minutely).

    num_series : int, default 1
        Number of independent time series (columns) to generate.

    dist : {'normal', 'lognormal'}, default 'normal'
        Type of return distribution. Only support Normal and Log-normal distribution.

    random_state : int, default 524
        Seed for numpy random number generation.

    start_date : str, default '2024-01-01'
        Start date for the series in the format 'YYYY-MM-DD'. 

    Returns
    -------
    DataFrame
        A DataFrame with columns as independent return time series.

    Examples
    --------
    >>> generate_return_series(0.05, 0.2, length=3, freq='D', num_series=3, dist='normal', random_state=123, start_date='2024-01-01')
                series_1  series_2  series_3
    2024-01-01 -0.012345  0.016767  0.022222
    2024-01-02  0.043215  0.019105 -0.005555
    2024-01-03 -0.001011  0.003333 -0.011111
    """