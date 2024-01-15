import pandas as pd
import altair as alt

def plot_num_dist(data, group = None):
    """
    Creates a chart of histograms for all numeric features in a data set.

    Parameters
    ----------
    data : Data
        An object containing the dataset of interest
    group : string
        The name of a column in a dataset that a user wants to group their
        data by.

    Returns
    -------
    self: Altair chart object
        Returns an altair chart object

    Examples
    --------
    >>> plot_num_dist(dataset)

    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError('dataset must be a DataFrame') 
    
    numeric_features = data.select_dtypes(include=np.number).columns.tolist()

    plot = alt.Chart(data).mark_bar().encode(
        alt.X(alt.repeat()).type('quantitative').bin(maxbins=20),
        alt.Y('count()', stack=None).title('Frequency of Occurrence'),
        alt.Color(target).title(target).scale(scheme='viridis')
    ).properties(
        width = 125,
        height = 125
    ).repeat(
        numeric_features,
        columns = 3
    )
    return


