import altair as alt
import pandas as pd

def plot_missing_vals(data):
    """
    Plot binary heatmap chart ('True' where there is a missing value and 'False' where there is not)
    to display missing values for all numeric features in the dataset.

    This function is derived from UBC Master of Data Science course DSCI 531 Lecture 4 notes by Joel Ostblom 
    (https://pages.github.ubc.ca/MDS-2023-24/DSCI_531_viz-1_students/lectures/4-eda.html)

    Parameters
    ----------
    data : pandas.DataFrame
        The dataset.

    Returns
    -------
    altair.Chart
        Altair chart object.

    Examples
    --------
    >>> plot_missing_vals(data)
        
    """
    

    if not isinstance(data, pd.DataFrame):
        raise ValueError("Data must be a pandas DataFrame")
    
    missing_vals_plot = alt.Chart(
        data.isna().reset_index().melt(
            id_vars='index'
        )
    ).mark_rect().encode(
        alt.X('index:O').axis(None),
        alt.Y('variable').title("Features"),
        alt.Color('value').title('Missing Values'),
        alt.Stroke('value')  
    ).properties(
        width=data.shape[0]
    )

    return missing_vals_plot
