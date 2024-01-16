import altair as alt
import pandas as pd

def plot_missing_vals(df):
    """
    Plot tick chart to display missing values for all numeric features in the dataset.

    This function is derived from UBC Master of Data Science course DSCI 531 Lecture 4 notes by Joel Ostblom 
    (https://pages.github.ubc.ca/MDS-2023-24/DSCI_531_viz-1_students/lectures/4-eda.html)

    Parameters
    ----------
    - df : DataFrame
        the dataset

    Returns
    -------
    self: object
        Altair chart object

    Examples
    --------
    plot_missing_vals(df)
        
    """

    if not isinstance(df, pd.DataFrame):
        raise ValueError("Data must be a pandas DataFrame")
    
    missing_vals_plot = alt.Chart(
        df.isna().reset_index().melt(
            id_vars='index'
        )
    ).mark_rect().encode(
        alt.X('index:O').axis(None),
        alt.Y('variable').title("Features"),
        alt.Color('value').title('Missing Values'),
        alt.Stroke('value')  
    ).properties(
        width=df.shape[0]
    )

    return missing_vals_plot