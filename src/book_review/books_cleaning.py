import pandas as pd
import warnings

warnings.filterwarnings("ignore")


class BooksCleaning:
    """ """

    def __init__(self, data, rating_df):
        self.df = data
        self.rating_df = rating_df

    def select_attributes(self):
        self.df = self.df.iloc[:, :-3]
        return self.df

    def merge_dfs(self):  
        self.df["Year-Of-Publication"] = pd.to_numeric(
        self.df["Year-Of-Publication"], errors="coerce")
        self.df.dropna(subset=["Year-Of-Publication"], inplace=True)
        self.df.insert(5, "Book-Ratings", self.rating_df["Book-Rating"])
        self.df["Book-Ratings"] = pd.to_numeric(
            self.df["Book-Ratings"], errors="coerce"
            )
        return self.df
