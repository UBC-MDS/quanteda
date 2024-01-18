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

    n_rows : int, default 365 
        Number of days, hours, or minutes (rows) to generate.

    freq : {'D', 'H', 'min'}, default 'D'
        Frequency of returns ('D' for daily, 'H' for hourly, 'min' for minute).

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
    pandas.DataFrame
        A DataFrame with columns as independent return time series.

    Examples
    --------
    >>> generate_return_series(0.05, 0.2, n_rows=3, freq='D', num_series=3, dist='normal', random_state=123, start_date='2024-01-01')
                series_1  series_2  series_3
    2024-01-01 -0.012345  0.016767  0.022222
    2024-01-02  0.043215  0.019105 -0.005555
    2024-01-03 -0.001011  0.003333 -0.011111
    """
    np.random.seed(random_state)
    if annual_volatility < 0:
        raise ValueError("annual_volatility < 0.")

    if freq == 'D':
        periods_per_year = 365
    elif freq == 'H':
        periods_per_year = 365 * 24
    elif freq == 'min':
        periods_per_year = 365 * 24 * 60
    else:
        raise ValueError("Invalid frequency. Use 'D' for day, 'H' for hour, 'min' for minute.") 

    num_periods = int(periods_per_year) * num_series

    if dist == 'normal':
        returns = np.random.normal(
            expected_annual_return / periods_per_year,
            annual_volatility / np.sqrt(periods_per_year),
            (n_rows, num_series)
        )
    elif dist == 'lognormal':
        mu = np.log(1 + expected_annual_return) - 0.5 * (annual_volatility ** 2) / periods_per_year
        sigma = annual_volatility / np.sqrt(periods_per_year)
        returns = np.random.lognormal(mu, sigma, (n_rows, num_series))
    else:
        raise ValueError("Invalid distribution. Use 'normal' or 'lognormal'.")

    datetime_range = pd.date_range(start=start_date, periods=n_rows, freq=freq)
    
    return pd.DataFrame(returns, index=datetime_range, columns=[f'series_{i+1}' for i in range(num_series)])
