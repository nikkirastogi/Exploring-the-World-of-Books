"""
Importing the necessary libraries.
"""
import pandas as pd
import warnings

warnings.filterwarnings("ignore")


class data:
    """
    This class contains all the functions needed for data reading,interpretation and cleaning.
    """


def __init__(self):
    """ """
    pass


def cleaning(df, review, user):
    # Delete the last 3 columns
    df = df.iloc[:, :-3]
    cleaned_df = df.dropna(subset=["Year-Of-Publication"])
    cleaned_df["Year-Of-Publication"] = pd.to_numeric(
        cleaned_df["Year-Of-Publication"], errors="coerce"
    )
    cleaned_df.insert(5, "Book-Ratings", review["Book-Rating"])
    cleaned_df.insert(6, "Location", user["Location"])
    return cleaned_df


# cleaned_df = cleaning()


def details(df):
    """
    Function used to show some of the initial content of the dataset to get an idea on how the data looks like.
    """
    return df.head()


def attributes(df):
    """
    Function used to show the attributes of dataset.
    """
    return df.columns


def info(df):
    """
    This function shows the details of the attributes such as count of non-null values and data type.
    """
    info = df.info()
    return info


def null_values(df):
    """
    Function showing the count of non-null values of each attributes.
    """
    null_values = pd.isnull(df).sum()
    return null_values


def shape(df):
    """
    Function showing the dimension of the dataset.
    """
    shape = df.shape
    return shape


def describe(df):
    """
    Function used to see the statistical summary of data
    """
    describe = df.describe()
    return describe


def data_type(df):
    """
    Function used to see datatypes of attributes
    """
    data_types = df.dtypes
    return data_types
