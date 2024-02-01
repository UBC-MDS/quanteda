import pandas as pd
import altair as alt
import numpy as np

def plot_num_dist(data):
    """
    Creates a chart of histograms for all numeric features in a data set.

    Parameters
    ----------
    data : pandas.DataFrame
        An object containing the dataset of interest

    Returns
    -------
    altair.Chart
        Altair chart object

    Examples
    --------
    >>> plot_num_dist(dataset)

    """
    if not isinstance(data, pd.DataFrame):
        raise AssertionError('dataset must be a pandas DataFrame')
    
    # Get list of numeric features
    numeric_features = data.select_dtypes(include=np.number).columns.to_list()

    if len(numeric_features) == 0:
        raise AssertionError('dataset has no numeric features')

    # Create plot
    plot = alt.Chart(data).mark_bar().encode(
        alt.X(alt.repeat()).type('quantitative').bin(maxbins=20),
        alt.Y('count()', stack=None).title('Frequency of Occurrence')
    ).properties(
        width = 125,
        height = 125
    ).repeat(
        numeric_features,
        columns = 3
    )
    return plot


