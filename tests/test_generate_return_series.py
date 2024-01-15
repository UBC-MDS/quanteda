from quanteda.generate_return_series import generate_return_series

# 1. test input error
## 1.1. test ValueError("ValueError: annual_volatility < 0")
## 1.2. test ValueError("Invalid frequency. Use 'D' for daily, 'H' for hourly, 'min' for minutely.")
## 1.3. test ValueError("Invalid distribution. Use 'normal' or 'lognormal'.")

# 2. test output
# 2.1. shape == (n_rows, num_series)
# 2.2. test object is data.frame
# 2.3. test the frequency == freq as expected
