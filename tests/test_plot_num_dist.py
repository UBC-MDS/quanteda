import pytest
import pandas as pd
import altair as alt
import numpy as np

from quanteda.plot_num_dist import plot_num_dist

def test_object_type():
    assert isinstance(plot_num_dist(data), alt.RepeatChart), "The chart created is not an altair repeated chart"


