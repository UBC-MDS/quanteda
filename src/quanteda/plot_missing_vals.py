import altair as alt
import pandas as pd

def plot_missing_vals():
    """
    Plot tick chart to display missing values for all numeric features in the dataset.

    Parameters
    ----------
    - df : DataFrame
        the dataset

    Returns
    -------
    object
        Altair chart object

    Examples
    --------
    plot_missing_vals(df)
        
    """

    return missing_vals_plot