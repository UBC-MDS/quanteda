import altair as alt

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
        alt.Chart
        
    """

    return missing_vals_plot