"""
Importing the necessary libraries.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import warnings

warnings.filterwarnings("ignore")


class BooksEDA:
    """
    This class contains all the functions needed for data reading,interpretation and cleaning.
    """

    def __init__(data):
        """ """
        self.df = data

    def highest_publisher(self):
        # Top 10 publishers with the most books
        top_publishers = self.df["Publisher"].value_counts().head(10)
        plt.figure(figsize=(12, 6))
        top_publishers.plot(kind="bar", color="skyblue")
        plt.title("Top 10 Publishers with the Most Books")
        plt.xlabel("Publisher")
        plt.ylabel("Count")
        plt.xticks(rotation=45, ha="right")
        plt.show()

    def word_cloud(self):
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(
            " ".join(self.df["Book-Title"])
        )
        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.title("Word Cloud for Book Titles")
        plt.show()

    def distribution(self):
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
        # Top 10 publishers with the most books
        top_publishers = self.df["Book-Author"].value_counts().head(10)
        plt.figure(figsize=(12, 6))
        top_publishers.plot(kind="bar", color="skyblue")
        plt.title("Top 10 Authors with Most Books")
        plt.xlabel("Author")
        plt.ylabel("Count")
        plt.xticks(rotation=45, ha="right")
        plt.show()

    def highest_ratings(self):
        # Distribution of Book Ratings
        plt.figure(figsize=(10, 6))
        sns.histplot(self.df["Book-Ratings"], bins=20, kde=True)
        plt.title("Distribution of Book Ratings")
        plt.xlabel("Book Ratings")
        plt.ylabel("Frequency")
        plt.show()

    def ratings_and_year(self):
        # Relationship between Book Ratings and Year of Publication
        plt.figure(figsize=(12, 6))
        sns.scatterplot(x="Year-Of-Publication", y="Book-Ratings", data=self.df)
        plt.title("Relationship between Book Ratings and Year of Publication")
        plt.xlabel("Year of Publication")
        plt.ylabel("Book Ratings")
        plt.show()

    def ratings_per_book(self):
        # Count of ratings per book
        plt.figure(figsize=(12, 6))
        sns.countplot(x="Book-Ratings", data=self.df)
        plt.title("Count of Ratings per Book")
        plt.xlabel("Rating")
        plt.ylabel("Count")
        plt.show()

    def location_and_ratings(self):
        # Visualize the top 10 locations with the most ratings
        top_locations = self.df["Location"].value_counts().nlargest(10)
        plt.figure(figsize=(12, 6))
        sns.barplot(x=top_locations.values, y=top_locations.index, palette="viridis")
        plt.title("Top 10 Locations with Most Ratings")
        plt.xlabel("Number of Ratings")
        plt.ylabel("Location")
        plt.show()
