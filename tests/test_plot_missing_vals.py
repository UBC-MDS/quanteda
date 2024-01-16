import pytest
import pandas as pd
from quanteda.plot_missing_vals import plot_missing_vals
import altair as alt

def test_plot_type ():
    test_plot = plot_missing_vals(input_daily_returns_with_nan_df)
    assert type(test_plot) == altair.Chart

def test_mark_type():
    test_plot = plot_missing_vals(input_daily_returns_with_nan_df)
    assert test_plot.to_dict()['mark']['type'] == 'rect'

def test_plot_encoding():
    test_plot = plot_missing_vals(input_daily_returns_with_nan_df)
    assert test_plot.to_dict()['encoding']['color']['field'] == 'value'

def test_plot_legend_title():
    test_plot = plot_missing_vals(input_daily_returns_with_nan_df)
    assert test_plot.to_dict()['encoding']['color']['title'] == 'NaN'



