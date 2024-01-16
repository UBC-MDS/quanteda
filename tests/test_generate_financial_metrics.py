import pytest
import pandas as pd
import numpy as np
from quanteda.generate_return_series import generate_return_series
from quanteda.generate_financial_metrics import generate_financial_metrics

idx=pd.date_range("2018-01-01", periods=5, freq="H")
input_df = pd.DataFrame(pd.Series(range(len(idx)), index=idx))


def test_empty_dataframe():
    """
    Checking if an input dataframe is empty or not.
    """
    with pytest.raises(ValueError, match="Random returns DataFrame is empty."):
        generate_financial_metrics(pd.DataFrame())
        
def test_index_type():
    """
    Checking if the dataframe index is pd.DatatimeIndex
    """
    with pytest.raises(ValueError, match="Index must be a pd.DatetimeIndex."):
        generate_financial_metrics(pd.DataFrame({'returns': [0.01, 0.02]}))

def test_missing_values():
    """
    Checking if the input dataframe has missing values
    """
    with pytest.raises(ValueError, match="Random returns DataFrame contains missing values."):
        generate_financial_metrics(pd.DataFrame([np.nan, np.nan, 1, 2, 3], index=idx))

def test_risk_free_rate_type():
    """
    Checking if the input annual_risk_free is numeric
    """
    with pytest.raises(ValueError, match="Annual risk-free rate must be numeric."):
        df = pd.DataFrame(pd.Series(range(len(idx)), index=idx))
        generate_financial_metrics(pd.DataFrame(df), annual_risk_free='not numeric')

def test_invalid_frequency():
    """
    Checking if the input dataframe index frequency is either daily, hourly or minutely
    """
    with pytest.raises(ValueError, match="Invalid frequency. Frequency should be either 'D' for daily, 'H' for hourly, or 'min' for minutely."):
        idx=pd.date_range("2018-01-01", periods=5, freq="W")
        df = pd.DataFrame(pd.Series(range(len(idx)), index=idx))
        generate_financial_metrics(pd.DataFrame(df))

def test_single_return():
    """
    Checking if the output dataframe has an expected length
    """
    df = pd.DataFrame(pd.Series(range(len(idx)), index=idx))
    result_df = generate_financial_metrics(pd.DataFrame(df), annual_risk_free=0.01)
    assert len(result_df) == 1  # Expecting one row in the result DataFrame

def test_zero_volatility():
    """
    Checking if the output volatility is calcuated correctly
    """
    df = pd.DataFrame(([0, 0, 0, 0, 0]), index=idx)
    result_df = generate_financial_metrics(pd.DataFrame(df), annual_risk_free=0.01)
    assert result_df['annual_volatility'].all() == 0.0  # Expecting zero annual volatility

def test_calculations():
    """
    Checking if the output metrics are expected
    """
    df = pd.DataFrame(([0.5, 0.2, -0.3, 0, 0]), index=idx)
    result_df = generate_financial_metrics(pd.DataFrame(df), annual_risk_free=0.01).round(1)
    assert result_df['count'][0] == 5
    assert result_df['total_return'][0] == 0.4
    assert result_df['annual_return'][0] == 700.8
    assert result_df['annual_volatility'][0] == 27.6
    assert result_df['sharpe_ratio'][0] == 25.4
    
    

