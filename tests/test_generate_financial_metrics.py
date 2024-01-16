import pytest
import pandas as pd
import numpy as np
from quanteda.generate_return_series import generate_return_series
from quanteda.generate_financial_metrics import generate_financial_metrics

idx_h=pd.date_range("2018-01-01", periods=5, freq="H")
idx_w=pd.date_range("2018-01-01", periods=5, freq="W")

input_df = pd.DataFrame(pd.Series(range(len(idx_h)), index=idx_h))
mising_values_df = pd.DataFrame([np.nan, np.nan, 1, 2, 3], index=idx_h)
incorrect_freq_df = pd.DataFrame(pd.Series(range(len(idx_w)), index=idx_w))
zero_vol_df = df = pd.DataFrame(([0, 0, 0, 0, 0]), index=idx_h)
test_cal_df = pd.DataFrame(([0.5, 0.2, -0.3, 0, 0]), index=idx_h)

def test_empty_dataframe():
    """Checking if an input dataframe is empty or not."""
    with pytest.raises(ValueError, match="Random returns DataFrame is empty."):
        generate_financial_metrics(pd.DataFrame())
        
def test_index_type():
    """Checking if the dataframe index is pd.DatatimeIndex"""
    with pytest.raises(ValueError, match="Index must be a pd.DatetimeIndex."):
        generate_financial_metrics(pd.DataFrame({'returns': [0.01, 0.02]}))

def test_missing_values():
    """Checking if the input dataframe has missing values"""
    with pytest.raises(ValueError, match="Random returns DataFrame contains missing values."):
        generate_financial_metrics(mising_values_df)

def test_risk_free_rate_type():
    """Checking if the input annual_risk_free is numeric"""
    with pytest.raises(ValueError, match="Annual risk-free rate must be numeric."):
        generate_financial_metrics(input_df, annual_risk_free='not numeric')

def test_invalid_frequency():
    """Checking if the input dataframe index frequency is either daily, hourly or minutely"""
    with pytest.raises(ValueError, match="Invalid frequency. Frequency should be either 'D' for daily, 'H' for hourly, or 'min' for minutely."):
        generate_financial_metrics(incorrect_freq_df)

def test_single_return():
    """Checking if the output dataframe has an expected length"""
    result_df = generate_financial_metrics(input_df, annual_risk_free=0.01)
    assert len(result_df) == 1  # Expecting one row in the result DataFrame

def test_zero_volatility():
    """Checking if the output volatility is calcuated correctly"""
    result_df = generate_financial_metrics(zero_vol_df, annual_risk_free=0.01)
    assert result_df['annual_volatility'].all() == 0.0  # Expecting zero annual volatility

def test_calculations():
    """Checking if the output metrics are expected"""
    result_df = generate_financial_metrics(test_cal_df, annual_risk_free=0.01).round(1)
    assert result_df['count'][0] == 5
    assert result_df['total_return'][0] == 0.4
    assert result_df['annual_return'][0] == 700.8
    assert result_df['annual_volatility'][0] == 27.6
    assert result_df['sharpe_ratio'][0] == 25.4
    
    

