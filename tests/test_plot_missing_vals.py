import pytest
import pandas as pd
from quanteda.plot_missing_vals import plot_missing_vals
import altair as alt

def test_output_type(input_daily_returns_with_nan_df):
    """Test to confirm the output object is an altair chart"""
    test_plot = plot_missing_vals(input_daily_returns_with_nan_df)
    assert type(test_plot) == alt.Chart, "The function did not output an altair chart."

def test_mark_type(input_daily_returns_with_nan_df):
    """Test to confirm the output is a rect chart"""
    test_plot = plot_missing_vals(input_daily_returns_with_nan_df)
    assert test_plot.to_dict()['mark']['type'] == 'rect', "The function did not output the correct type of chart."

def test_plot_encoding(input_daily_returns_with_nan_df):
    """Test to confirm the coloring in the plot is associated with the value"""
    test_plot = plot_missing_vals(input_daily_returns_with_nan_df)
    assert test_plot.to_dict()['encoding']['color']['field'] == 'value', "The plot's color is not associated with whether a value is missing."

def test_plot_legend_title(input_daily_returns_with_nan_df):
    """Test to confirm the legend title"""
    test_plot = plot_missing_vals(input_daily_returns_with_nan_df)
    assert test_plot.to_dict()['encoding']['color']['title'] == 'Missing Values', "The plot title is incorrect."

def test_y_axis_title(input_daily_returns_with_nan_df):
    """Test to confirm the y-axis title"""
    test_plot = plot_missing_vals(input_daily_returns_with_nan_df)
    assert test_plot.to_dict()['encoding']['y']['title'] == 'Features', "The y-axis title is incorrect."

