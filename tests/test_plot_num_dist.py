import pytest
import altair as alt
import pandas as pd
from quanteda.plot_num_dist import plot_num_dist


def test_plot_type(input_daily_returns_df):
    """Check if object returned is the right type"""
    test_plot = plot_num_dist(input_daily_returns_df)
    assert isinstance(test_plot, alt.RepeatChart), "The chart created is not an altair repeated chart"

def test_plot_col_num(input_daily_returns_df):
    """Check that the plots make a grid with 3 columns"""
    test_plot = plot_num_dist(input_daily_returns_df)
    assert test_plot.columns == 3, "The chart has the wrong number of columns"

def test_mark_type(input_daily_returns_df):
    """Check that the chart is made up of bar charts"""
    test_plot = plot_num_dist(input_daily_returns_df)
    assert test_plot.to_dict()['spec']['mark']['type'] == 'bar', "The marks on the chart are not bars"

def test_feature_type(input_daily_returns_df):
    """Check that the variables on the X axis are numerical"""
    test_plot = plot_num_dist(input_daily_returns_df)
    assert test_plot.to_dict()['spec']['encoding']['x']['type'] == 'quantitative', "The variables being plotted are not numeric"

def test_plot_aggregate(input_daily_returns_df):
    """Check that the y axis represents a count"""
    test_plot = plot_num_dist(input_daily_returns_df)
    assert test_plot.to_dict()['spec']['encoding']['y']['aggregate'] == 'count', "The y-axis does not represent a count"

def test_subplot_num(input_daily_returns_df):
    """Check that the number of subplots match number of numeric features"""
    test_plot = plot_num_dist(input_daily_returns_df)
    assert len(test_plot.to_dict()['repeat']) == 9, "The number of subplots is not 3"

def test_plot_dims(input_daily_returns_df):
    """Check that the size of the plot is as expected"""
    test_plot = plot_num_dist(input_daily_returns_df)
    assert test_plot.to_dict()['spec']['height'] == 125, "The height of the plot is not 125"
    assert test_plot.to_dict()['spec']['width'] == 125, "The width of the plot is not 125"

def test_for_dataframe():
    """Checking if the input is a dataframe or not."""
    with pytest.raises(AssertionError, match="dataset must be a pandas DataFrame"):
        plot_num_dist(123)

def test_for_numeric_dataframe():
    """Checking if the dataframe has numeric columns."""
    with pytest.raises(AssertionError, match="dataset has no numeric features"):
        plot_num_dist(pd.DataFrame({'col1': ['a', 'b'], 'col2': ['a', 'b']}))

