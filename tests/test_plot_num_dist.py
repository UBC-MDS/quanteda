import pytest
import altair as alt
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
