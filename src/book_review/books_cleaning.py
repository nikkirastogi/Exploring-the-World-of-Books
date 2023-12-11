import pandas as pd
import warnings

warnings.filterwarnings("ignore")


class cleaning:
    """ """

    def __init__(self):
        pass

    def merging(df, review):
        # Delete the last 3 columns
        cleaned_df = df.iloc[:, :-3]
        cleaned_df["Year-Of-Publication"] = pd.to_numeric(
            cleaned_df["Year-Of-Publication"], errors="coerce"
        )
        cleaned_df.dropna(subset=["Year-Of-Publication"], inplace=True)
        cleaned_df.insert(5, "Book-Ratings", review["Book-Rating"])
        cleaned_df["Book-Ratings"] = pd.to_numeric(
            cleaned_df["Book-Ratings"], errors="coerce"
        )
        return cleaned_df
