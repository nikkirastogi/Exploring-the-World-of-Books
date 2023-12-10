"""
Importing the necessary libraries.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

import warnings

warnings.filterwarnings("ignore")


class EdaAnalysis:
    """
    This class contains all the functions needed for data reading,interpretation and cleaning.
    """


def __init__(self):
    """ """
    pass


def highest_publisher(df):
    # Top 10 publishers with the most books
    top_publishers = df["Publisher"].value_counts().head(10)
    plt.figure(figsize=(12, 6))
    top_publishers.plot(kind="bar", color="skyblue")
    plt.title("Top 10 Publishers with the Most Books")
    plt.xlabel("Publisher")
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha="right")
    plt.show()


def word_cloud(df):
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(
        " ".join(df["Book-Title"])
    )
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Word Cloud for Book Titles")
    plt.show()


def distribution(df):
    filtered_df = df[
        (df["Year-Of-Publication"] >= 1800) & (df["Year-Of-Publication"] <= 2050)
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


def highest_author(df):
    # Top 10 publishers with the most books
    top_publishers = df["Book-Author"].value_counts().head(10)
    plt.figure(figsize=(12, 6))
    top_publishers.plot(kind="bar", color="skyblue")
    plt.title("Top 10 Publishers with the Most Books")
    plt.xlabel("Publisher")
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha="right")
    plt.show()
