import numpy as np
import pandas as pd

def generate_financial_metrics(random_returns_df, annual_risk_free=0.00):
    """
    Calculate financial metrics based on a DataFrame of random returns on time series.

    Parameters
    ----------
    random_returns_df : pd.DataFrame
        DataFrame containing random return values with a datetime index.

    annual_risk_free : float, default 0.00.
        Annualized risk-free rate as a decimal (e.g., 0.02 for 2%).
        
    Returns
    -------
    DataFrame
        A DataFrame containing financial metrics including count (number of returns), 
        total return, annualized return, annualized volatility, and Sharpe ratio.

    Examples
    --------
    >>> random_returns_df = generate_return_series(expected_annual_return, 
                                                   annual_volatility, 
                                                   freq='H', 
                                                   n_rows=5, 
                                                   num_series=3, 
                                                   dist="normal")
    >>> generate_financial_metrics(random_returns_df, annual_risk_free=0.02)
              count  total_return  annual_return  annual_volatility  sharpe_ratio
    series_1	5	  0.000229	   0.400912	      0.256443	         1.485364
    series_2	5	  0.010870	   19.043645	  0.166200	         114.462216
    series_3	5	  -0.000990	   -1.734509	  0.253074	         -6.932784
    """

    if random_returns_df.empty:
        raise ValueError("Random returns DataFrame is empty.")
    
    if not isinstance(random_returns_df.index, pd.DatetimeIndex):
        raise ValueError("Index must be a pd.DatetimeIndex.")  

    if random_returns_df.isnull().values.any():
        raise ValueError("Random returns DataFrame contains missing values.")

    if not isinstance(annual_risk_free, (int, float)):
        raise ValueError("Annual risk-free rate must be numeric.")

    freq = pd.infer_freq(random_returns_df.index)
    
    if freq == 'D':
        periods_per_year = 365
    elif freq == 'H':
        periods_per_year = 365 * 24
    elif freq == 'min':
        periods_per_year = 365 * 24 * 60
    else:
        raise ValueError("Invalid frequency. Frequency should be either 'D' for daily, 'H' for hourly, or 'min' for minutely.") 
    
    metrics_df = pd.DataFrame({
        'count': random_returns_df.count(),
        'total_return': random_returns_df.sum(),
        'annual_return': random_returns_df.mean() * periods_per_year,
        'annual_volatility': random_returns_df.std() * np.sqrt(periods_per_year),
    })
    metrics_df['sharpe_ratio'] = (metrics_df['annual_return'] - annual_risk_free) / metrics_df['annual_volatility']
    
    return metrics_df