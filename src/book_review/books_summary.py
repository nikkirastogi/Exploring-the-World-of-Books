"""
Importing the necessary libraries.

"""

import pandas as pd
import warnings

warnings.filterwarnings("ignore")


class BooksSummary:
    """
    This class contains all the functions needed for data reading,interpretation and cleaning.
    """

    def __init__(self, data):
        """ """
        self.df = data

    def df_details(self):
        """
        Function used to show some of the initial content of the dataset to get an idea on how the data looks like.
        """
        return self.df.head()

    def df_attributes(self):
        """
        Function used to show the attributes of dataset.
        """
        return self.df.columns

    def df_info(self):
        """
        This function shows the details of the attributes such as count of non-null values and data type.
        """
        return self.df.info()

    def df_null_values(self):
        """
        Function showing the count of non-null values of each attributes.
        """
        return pd.isnull(self.df).sum()

    def df_shape(self):
        """
        Function showing the dimension of the dataset.
        """
        return self.df.shape

    def df_describe(self):
        """
        Function used to see the statistical summary of data
        """
        return self.df.describe()