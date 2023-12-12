"""
This module defines the BooksEDA class for exploratory data analysis (EDA) on book data.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import warnings

warnings.filterwarnings("ignore")


class BooksEDA:
    """
    This class contains functions for exploratory data analysis (EDA) on book data.

    """

    def __init__(self, data):
        """
        Initialize the BooksEDA object.

        Parameters:
        - data (pandas.DataFrame): The book data.
        """
        self.df = data

    def highest_publisher(self):
        """
        Plot a bar chart of the top 10 publishers with the most books.

        This method generates a bar chart showing the distribution of books among
        the top 10 publishers based on the provided book data.

        Returns:
        None
        """
        top_publishers = self.df["Publisher"].value_counts().head(10)
        plt.figure(figsize=(12, 6))
        top_publishers.plot(kind="bar", color="skyblue")
        plt.title("Top 10 Publishers with the Most Books")
        plt.xlabel("Publisher")
        plt.ylabel("Count")
        plt.xticks(rotation=45, ha="right")
        plt.show()

    def df_word_cloud(self):
        """
        Generate and display a word cloud for book titles.

        This method creates a word cloud based on the book titles and displays it
        using the WordCloud library.

        Returns:
        None
        """
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(
            " ".join(self.df["Book-Title"])
        )
        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.title("Word Cloud for Book Titles")
        plt.show()

    def distribution(self):
        """
        Plot a histogram of the distribution of publication years.

        This method generates a histogram showing the distribution of publication
        years for books, filtering out unrealistic values.

        Returns:
        None
        """
        filtered_df = self.df[
            (self.df["Year-Of-Publication"] >= 1800) & (self.df["Year-Of-Publication"] <= 2050)
        ]
        plt.figure(figsize=(12, 6))
        plt.hist(
            filtered_df["Year-Of-Publication"].dropna(),
            bins=range(1800, 2051, 10),
            edgecolor="black",
        )
        plt.title("Distribution of Publication Years")
        plt.xlabel("Publication Year")
        plt.ylabel("Count")
        plt.grid(axis="y", linestyle="--", alpha=0.7)
        plt.show()

    def highest_author(self):
        """
        Plot a bar chart of the top 10 authors with the most books.

        This method generates a bar chart showing the distribution of books among
        the top 10 authors based on the provided book data.

        Returns:
        None
        """
        top_authors = self.df["Book-Author"].value_counts().head(10)
        plt.figure(figsize=(12, 6))
        top_authors.plot(kind="bar", color="skyblue")
        plt.title("Top 10 Authors with Most Books")
        plt.xlabel("Author")
        plt.ylabel("Count")
        plt.xticks(rotation=45, ha="right")
        plt.show()

    def highest_ratings(self):
        """
        Plot a histogram of the distribution of book ratings.

        This method generates a histogram showing the distribution of book ratings.

        Returns:
        None
        """
        plt.figure(figsize=(10, 6))
        sns.histplot(self.df["Book-Ratings"], bins=20, kde=True)
        plt.title("Distribution of Book Ratings")
        plt.xlabel("Book Ratings")
        plt.ylabel("Frequency")
        plt.show()

    
    def ratings_per_book(self):
        """
        Plot a count plot showing the distribution of ratings per book.

        This method generates a count plot to visualize the distribution of ratings
        per book.

        Returns:
        None
        """
        plt.figure(figsize=(12, 6))
        sns.countplot(x="Book-Ratings", data=self.df)
        plt.title("Count of Ratings per Book")
        plt.xlabel("Rating")
        plt.ylabel("Count")
        plt.show()
