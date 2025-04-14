"""
This module defines the BooksCleaning class for cleaning and processing book data.
"""
import pandas as pd
import warnings

warnings.filterwarnings("ignore")


class BooksCleaning:
    """A class for cleaning and processing book data."""

    def __init__(self, data, rating_df):
        """
        Initialize the BooksCleaning object.

        Parameters:
        - data (pandas.DataFrame): The main book data.
        - rating_df (pandas.DataFrame): The dataframe containing book ratings.
        """
        self.df = data
        self.rating_df = rating_df

    def select_attributes(self):
        """
        Select relevant attributes from the book data.

        Returns:
        pandas.DataFrame: The updated dataframe with selected attributes.
        """
        self.df = self.df.iloc[:, :-3]
        return self.df

    def merge_dfs(self):
        """
        Merge the book data and ratings dataframe.

        This method cleans and merges the dataframes by converting the
        'Year-Of-Publication' and 'Book-Ratings' columns to numeric types,
        and handling missing values.

        Returns:
        pandas.DataFrame: The merged and cleaned dataframe.
        """
        self.df["Year-Of-Publication"] = pd.to_numeric(
            self.df["Year-Of-Publication"], errors="coerce")
        self.df.dropna(subset=["Year-Of-Publication"], inplace=True)
        self.df.insert(5, "Book-Ratings", self.rating_df["Book-Rating"])
        self.df["Book-Ratings"] = pd.to_numeric(
            self.df["Book-Ratings"], errors="coerce"
        )
        return self.df
