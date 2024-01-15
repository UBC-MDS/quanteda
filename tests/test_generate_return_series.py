import pytest
import pandas as pd
from quanteda.generate_return_series import generate_return_series

def test_negative_annual_volatility():
    # 1.1. test ValueError("ValueError: annual_volatility < 0")
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
    # 1.2. test ValueError("Invalid frequency. Use 'D' for daily, 'H' for hourly, 'min' for minutely.")
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
    assert str(error.value) == "Invalid frequency. Use 'D' for daily, 'H' for hourly, 'min' for minutely."

def test_invalid_dist():
    # 1.3. test ValueError("Invalid distribution. Use 'normal' or 'lognormal'.")
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
    # 2.1. shape == (n_rows, num_series)
    # 2.2. test object is data.frame
    n_rows = 365
    num_series = 10

    output = generate_return_series(
        expected_annual_return=0.05,
        annual_volatility=0.2,
        n_rows=n_rows,
        freq='D',
        num_series=num_series,
        dist='lognormal',
        random_state=524,
        start_date='2024-01-01'
    )

    assert isinstance(output, pd.DataFrame), f"Output should be a pd.DataFrame (current type: {type(output)})."
    assert output.shape == (n_rows, num_series), f"Shape does not match, {(n_rows, num_series)} is expected (current shape: {output.shape})."

def test_freq():
    # 2.3. test the frequency == freq as expected
    pass
