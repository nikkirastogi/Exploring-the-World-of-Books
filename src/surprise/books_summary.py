"""
BooksSummary Module

This module defines the BooksSummary class, which contains functions for data reading, interpretation, and basic summary statistics.

"""

import pandas as pd
import warnings

warnings.filterwarnings("ignore")


class BooksSummary:
    """
    This class contains functions for data reading, interpretation, and basic summary statistics.
    """

    def __init__(self, data):
        """
        Initialize the BooksSummary object.

        Parameters:
        - data (pandas.DataFrame): The dataset to be analyzed.
        """
        self.df = data

    def df_details(self):
        """
        Display the first few rows of the dataset to provide an initial overview.

        Returns:
        pandas.DataFrame: A preview of the dataset.
        """
        return self.df.head()

    def df_attributes(self):
        """
        Get the names of the attributes (columns) in the dataset.

        Returns:
        Index: The attribute names.
        """
        return self.df.columns

    def df_info(self):
        """
        Display information about the dataset, including the count of non-null values and data types.

        Returns:
        None
        """
        return self.df.info()

    def df_null_values(self):
        """
        Get the count of non-null values for each attribute in the dataset.

        Returns:
        pandas.Series: Count of non-null values for each attribute.
        """
        return pd.isnull(self.df).sum()

    def df_shape(self):
        """
        Get the dimensions (number of rows and columns) of the dataset.

        Returns:
        tuple: The number of rows and columns in the dataset.
        """
        return self.df.shape

    def df_describe(self):
        """
        Display basic statistical summary of the dataset.

        Returns:
        pandas.DataFrame: Statistical summary of the dataset.
        """
        return self.df.describe()
