"""
This module have class BooksInferences for performing inference and visualization on book data.

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler


class BooksInference:
    """
    A class for performing inference and visualization on book data.

    Parameters:
    - data (pandas.DataFrame): The book data.

    Methods:
    - author_data():
        Calculate and return a DataFrame containing average ratings and book counts per author.

    - plot_scatter1():
        Plot a scatter plot to visualize the relationship between an author's book count and average rating.

    - plot_scatter2():
        Plot a scatter plot to visualize the relationship between an author's average rating and number of books.

    - predict1():
        Train a linear regression model to predict book ratings based on author, publication year, and evaluate the model.

    - predict2():
        Train a linear regression model to predict publication year based on author, book ratings, and evaluate the model.
    """
    
    def __init__(self, data):
        """
        Initialize the BooksInference object.

        Parameters:
        - data (pandas.DataFrame): The book data.
        """
        self.df = data
    
    def author_data(self):
        """
        Calculate and return a DataFrame containing average ratings and book counts per author.

        Returns:
        pandas.DataFrame: A DataFrame with 'Average Rating' and 'Book Count' columns per author.
        """
        # Step 1: Calculate Average Ratings
        average_ratings = self.df.groupby('Book-Author')['Book-Ratings'].mean()

        # Step 2: Count Number of Books per Author
        book_counts = self.df['Book-Author'].value_counts()

        # Combine the data into a new DataFrame
        author_data = pd.DataFrame({'Average Rating': average_ratings, 'Book Count': book_counts})
        return author_data

    def plot_scatter1(self):
        """
        Plot a scatter plot to visualize the relationship between an author's book count and average rating.

        Returns:
        None
        """
        
        author = self.author_data()
        # Step 3: Plot the Relationship
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='Book Count', y='Average Rating', data=author, alpha=0.5)
        plt.title('Relationship Between Author\'s Book Count and Average Rating')
        plt.xlabel('Number of Books')
        plt.ylabel('Average Rating')
        plt.grid(True)
        return plt.show()
        

    def ratings_and_year(self):
        """
        Plot a scatter plot showing the relationship between book ratings and year of publication.

        This method generates a scatter plot to visualize the relationship between
        book ratings and the year of publication.

        Returns:
        None
        """
        plt.figure(figsize=(12, 6))
        sns.scatterplot(x="Year-Of-Publication", y="Book-Ratings", data=self.df)
        plt.title("Relationship between Book Ratings and Year of Publication")
        plt.xlabel("Year of Publication")
        plt.ylabel("Book Ratings")
        plt.show()

        
    def corr_rating_year(self):
        cleaned_df = self.df[self.df['Book-Ratings'] != 0]

        # Scatter plot to visualize the correlation between 'Book-Ratings' and 'Year-Of-Publication'
        plt.figure(figsize=(12, 6))
        sns.scatterplot(x=cleaned_df['Year-Of-Publication'], y=cleaned_df['Book-Ratings'], data=self.df, alpha=0.5)
        plt.title('Correlation between Book Ratings and Year of Publication')
        plt.xlabel('Year of Publication')
        plt.ylabel('Book Ratings')
        plt.xlim(1800, max(cleaned_df['Year-Of-Publication']))
        return plt.show()
        
        
