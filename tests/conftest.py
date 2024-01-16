import pytest
import numpy as np
from quanteda.generate_return_series import generate_return_series
from quanteda.plot_num_dist import plot_num_dist

@pytest.fixture
def input_minute_returns_df():
    """
    Fixture for generating a DataFrame with minute-frequency returns for testing.
    """
    df = generate_return_series(
        expected_annual_return=0.05,
        annual_volatility=0.2,
        n_rows=1440,
        freq='min',
        num_series=3,
        dist='normal',
        random_state=524,
        start_date='2024-01-01'
    )
    return df

@pytest.fixture
def input_daily_returns_df():
    """
    Fixture for generating a DataFrame with daily returns for testing.
    """
    df = generate_return_series(
        expected_annual_return=0.05,
        annual_volatility=0.2,
        n_rows=365,
        freq='D',
        num_series=9,
        dist='normal',
        random_state=524,
        start_date='2024-01-01'
    )
    return df

@pytest.fixture
def input_daily_returns_with_nan_df(input_daily_returns_df):
    """
    Fixture for generating a DataFrame with daily returns and missing values for testing.
    """
    df = input_daily_returns_df.copy()
    df.loc["2024-02-01":"2024-12-30", "series_1"] = np.nan
    df.loc["2024-02-01":"2024-03-01", "series_2"] = np.nan
    df.loc["2024-09-01":"2024-10-01", "series_8"] = np.nan
    df.loc[:, 'series_3'] = np.nan
    df.loc["2024-01-08"] = np.nan
    return df

@pytest.fixture
def num_dist_plot(input_daily_returns_df):
    """
    Fixture for generating a test Chart for plot_num_dist
    """
    return plot_num_dist(input_daily_returns_df)