import pytest
import altair as alt


from quanteda.plot_num_dist import plot_num_dist

test_data = input_minute_returns_df
test_plot = plot_num_dist(test_data)

def test_plot_type():
    assert isinstance(test_plot, alt.RepeatChart), "The chart created is not an altair repeated chart"

def test_plot_col_num():
    assert test_plot.columns == 3, "The chart has the wrong number of columns"

def test_mark_type():
    assert test_plot.to_dict()['spec']['mark']['type'] == 'bar', "The marks on the chart are not bars"

def test_feature_type():
    assert test_plot.to_dict()['spec']['encoding']['x']['type'] == 'quantitative', "The variables being plotted are not numeric"

def test_plot_aggregate():
    assert test_plot.to_dict()['spec']['encoding']['y']['aggregate'] == 'count', "The y-axis does not represent a count"
