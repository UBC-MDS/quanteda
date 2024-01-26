import numpy as np
import pandas as pd

def generate_financial_metrics(random_returns_df, annual_risk_free=0.00):
    """
    Calculate financial metrics based on a DataFrame of random returns on time series.

    Parameters
    ----------
    random_returns_df : pandas.DataFrame
        DataFrame containing returns of stocks on time series.

    annual_risk_free : float, default 0.00.
        Annualized risk-free rate as a decimal (e.g., 0.02 for 2%).
        
    Returns
    -------
    pandas.DataFrame
        A DataFrame containing financial metrics including count (number of returns), 
        total return, annualized return, annualized volatility, and Sharpe ratio for each
        stock return series

    Examples
    --------
    >>> random_returns_df = pd.DataFrame([
    {'index': '2024-01-01 00:00:00', 'stock_1': -0.002286, 'stock_2': 0.002545, 'stock_3': 0.002997},
    {'index': '2024-01-01 01:00:00', 'stock_1': 0.003045, 'stock_2': 0.002913, 'stock_3': -0.000855},
    {'index': '2024-01-01 02:00:00', 'stock_1': -0.001142, 'stock_2': 0.000635, 'stock_3': -0.002592},
    {'index': '2024-01-01 03:00:00', 'stock_1': 0.000971, 'stock_2': -0.000168, 'stock_3': 0.000074},
    {'index': '2024-01-01 04:00:00', 'stock_1': -0.000392, 'stock_2': 0.002252, 'stock_3': -0.000342}
    ])
                                                   
    >>> generate_financial_metrics(random_returns_df, annual_risk_free=0.02)
            	count	total_return	annual_return	annual_volatility	sharpe_ratio
    stock_1 	5	    0.000196	    0.343184	    0.192332	        1.680339
    stock_2 	5	    0.008177	    14.325234	    0.124650	        114.763058
    stock_3 	5	    -0.000718	    -1.258381	    0.189806	        -6.735214
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
