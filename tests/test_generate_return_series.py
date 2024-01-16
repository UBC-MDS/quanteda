import pytest
import pandas as pd
from quanteda.generate_return_series import generate_return_series

test_n_rows = 365
test_num_series = 10

test_df = generate_return_series(
    expected_annual_return=0.05,
    annual_volatility=0.2,
    n_rows=test_n_rows,
    freq='D',
    num_series=test_num_series,
    dist='lognormal',
    random_state=524,
    start_date='2024-01-01'
)

def test_negative_annual_volatility():
    """
    Test case for ValueError when `annual_volatility` is negative.
    """
    with pytest.raises(ValueError) as error:
        generate_return_series(
            expected_annual_return=0.05,
            annual_volatility=-0.2,
            n_rows=3,
            freq='D',
            num_series=3,
            dist='normal',
            random_state=524,
            start_date='2024-01-01'
        )
    assert str(error.value) == "annual_volatility < 0."

def test_invalid_freq():
    """
    Test case for ValueError when an invalid `freq` is provided.
    """
    with pytest.raises(ValueError) as error:
        generate_return_series(
            expected_annual_return=0.05,
            annual_volatility=0.2,
            n_rows=3,
            freq='ABC',
            num_series=3,
            dist='normal',
            random_state=524,
            start_date='2024-01-01'
        )
    assert str(error.value) == "Invalid frequency. Use 'D' for day, 'H' for hour, 'min' for minute."

def test_invalid_dist():
    """
    Test case for ValueError when an invalid `dist` is provided.
    """
    with pytest.raises(ValueError) as error:
        generate_return_series(
            expected_annual_return=0.05,
            annual_volatility=0.2,
            n_rows=3,
            freq='D',
            num_series=3,
            dist='t',
            random_state=524,
            start_date='2024-01-01'
        )
    assert str(error.value) == "Invalid distribution. Use 'normal' or 'lognormal'."

def test_output_dataframe():
    """
    Test case for generating a pd.DataFrame as output with correct shape.
    """
    assert isinstance(test_df, pd.DataFrame), f"Output should be a pd.DataFrame (current type: {type(output)})."
    assert test_df.shape == (test_n_rows, test_num_series), f"Shape does not match, {(n_rows, num_series)} is expected (current shape: {output.shape})."

