import pandas as pd

def generate_financial_metrics(random_returns_df, annual_risk_free=0.00):
    """
    Calculate financial metrics based on a DataFrame of random returns on time series.

    Parameters
    ----------
    random_returns_df : pd.DataFrame
        DataFrame containing random return values with a datetime index.

    annual_risk_free : float, default 0.00
        Annualized risk-free rate as a decimal (e.g., 0.02 for 2%).
        
    Returns
    -------
    pd.DataFrame
        DataFrame containing financial metrics including count (number of returns), 
        average return, total return, volatility, and Sharpe ratio.

    Examples
    --------
    >>> random_returns_df = generate_return_series(expected_annual_return, 
                                                   annual_volatility, 
                                                   freq='H', 
                                                   length=5, 
                                                   num_series=3, 
                                                   dist="normal")
    >>> result = generate_financial_metrics(random_returns_df, annual_risk_free_rate)
              count  avg_return  total_return       vol  sharpe_ratio
    series_1      5    0.000046      0.000229  0.002740     0.015870
    series_2      5    0.002174      0.010870  0.001776     1.222954
    series_3      5   -0.000198     -0.000990  0.002704    -0.074072
    """