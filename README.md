# quanteda
![CI/CD](https://github.com/UBC-MDS/quanteda/actions/workflows/ci-cd.yml/badge.svg) 
[![codecov](https://codecov.io/gh/UBC-MDS/quanteda/branch/main/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/quanteda) 
[![Documentation Status](https://readthedocs.org/projects/quanteda/badge/?version=latest)](https://quanteda.readthedocs.io/en/latest/?badge=latest) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 
[![Python 3.9.0](https://img.shields.io/badge/python-3.9.0-blue.svg)](https://www.python.org/downloads/release/python-390/) 
![release](https://img.shields.io/github/release-date/UBC-MDS/quanteda) ![version](https://img.shields.io/github/v/release/UBC-MDS/quanteda)
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)

Perform exploratory data analysis (EDA) on quantitative data.

## Function Description

This package aims to be the starting point for any analysis of quantitative financial data by supplying functions that create charts and metrics to simplify  exploratory data analysis and give the user a jump-start on their project. This package simplifies the creation of charts that look at the distribution of numeric features and missing information in the data set; two critical steps in any financial analysis. The package also includes a function that will generate a random time series. Financial variables like stock prices and interest rates vary over time, so this ability to generate a time series quickly is extremely useful. Finally, this package also includes a function that will automatically calculate several useful financial metrics so that more time can be spent on more complicated analysis.

The functions in this package include:

- `plot_missing_vals`: Plot tick chart to display missing values for all numeric features in the dataset.
- `plot_num_dist`: Creates a chart of histograms for all numeric features in a data set.
- `generate_return_series`: Generates a DataFrame with independent time series of returns.
- `generate_financial_metrics`: Calculates financial metrics based on a DataFrame of random returns on time series. These metrics are [`total return`](https://www.investopedia.com/terms/t/totalreturn.asp), [`annual return`](https://www.investopedia.com/terms/a/annual-return.asp), [`annual volatilities`](https://www.investopedia.com/terms/v/volatility.asp) and [`sharpe ratio`](https://www.investopedia.com/terms/s/sharperatio.asp)

## Contributors

- Doris (Yun Yi) Cai 
- Jake Barnabe 
- John Shiu 
- Merete Lutz

## Installation

### For User

To install the package, run the following command from the terminal
```bash
pip install quanteda
```

### For Developers

1. Clone this repository.

```bash
 git clone git@github.com:UBC-MDS/quanteda.git
 cd quanteda/
``` 

2. Install the virtual environment.

```bash
 conda env create -f environment.yml
```

3. Activate the installed environment:

```bash
 conda activate quanteda
```    

4. Install the package.

```bash
 poetry install
```
## Usage

### Using this package
To use this package, import and call the functions in Python. Below is an example:

```python
from quanteda.plot_missing_vals import plot_missing_vals
from quanteda.plot_num_dist import plot_num_dist
from quanteda.generate_financial_metrics import generate_financial_metrics
from quanteda.generate_return_series import generate_return_series
```

Call function `plot_missing_vals` to visualize the presence of missing values.
<img width="647" alt="image" src="https://github.com/UBC-MDS/quanteda/assets/100008826/a39d5d99-a303-4066-9d42-f23113ce5531">

Call function `plot_num_dist` to plot the distribution of the return series.
<img width="637" alt="image" src="https://github.com/UBC-MDS/quanteda/assets/100008826/c2d42ec8-9ec9-4af6-9597-7fb813a3965c">

Call function `generate_financial_metrics` to calculate the financial metrics of the return series.
<img width="648" alt="image" src="https://github.com/UBC-MDS/quanteda/assets/100008826/9354795c-d94b-4fd2-ab9b-2a9f5c28ea7e">

Call function `generate_return_series` to simulate time series return given an expected return, volatility and return distribution of a stock.

<img width="576" alt="image" src="https://github.com/UBC-MDS/quanteda/assets/100008826/73331894-1354-4aa3-a6f4-c8c41e309e6b">

### Run unit tests

Execute the following in the project root directory to run the unit tests of the package,

```bash
 poetry run pytest
```

or, to run with the code covergage reporting,

```bash
 poetry run pytest --cov=quanteda
```

## Documentation

The official documentation is hosted on Read the Docs: https://quanteda.readthedocs.io/en/latest/

## quanteda in the Python Ecosystem
Our package fills a gap in the python ecosystem by being marketed specifically to financial data. Python users commonly create EDA charts using popular packages like [matplotlib](https://pypi.org/project/matplotlib/), [altair](https://pypi.org/project/altair/), and [seaborn](https://pypi.org/project/seaborn/), and conduct their financial analysis using packages like [pandas](https://pypi.org/project/pandas/), [numpy](https://pypi.org/project/numpy/), and [scipy](https://pypi.org/project/SciPy/). These libraries are extensive, but have been generalized to be as useful as possible to as many differen fields as possible. It takes time to learn the syntax and code of these packages that work for financial data. This can be time consuming during EDA, when the goal is to quickly get a rough idea of what the data set you are using looks like. Our package will simplify these actions into a few functions that will save time on tedious EDA so that more time can be spent on analysis and testing.

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`quanteda` was created by Doris (Yun Yi) Cai, Jake Barnabe, John Shiu, Merete Lutz. It is licensed under the terms of the MIT license.

## Credits

`quanteda` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
