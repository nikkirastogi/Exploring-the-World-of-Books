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
        #plt.scatter(author_data['Book Count'], author_data['Average Rating'], alpha=0.5)
        plt.title('Relationship Between Author\'s Book Count and Average Rating')
        plt.xlabel('Number of Books')
        plt.ylabel('Average Rating')
        plt.grid(True)
        return plt.show()
        
    def plot_scatter2(self):
        """
        Plot a scatter plot to visualize the relationship between an author's average rating and number of books.

        Returns:
        None
        """
        
        # Step 1: Calculate Author-wise Average Ratings
        average_ratings = self.df.groupby('Book-Author')['Book-Ratings'].mean()

        # Step 2: Count the Number of Books per Author
        book_counts = self.df['Book-Author'].value_counts()

        # Step 3: Plot the Relationship
        plt.figure(figsize=(12, 6))
        #sns.scatterplot(x='Book Count', y='Average Rating', data=author_data, alpha=0.5)
        plt.scatter(book_counts, average_ratings, alpha=0.5)
        plt.title('Relationship between Author\'s Average Rating and Number of Books')
        plt.xlabel('Number of Books')
        plt.ylabel('Average Rating')
        return plt.show()

    def predict1(self):
        """
        Train a linear regression model to predict book ratings based on author, publication year, and evaluate the model.

        Returns:
        None
        """
        
        # Assume 'Book-Author' and 'Year-Of-Publication' are features for prediction
        X = self.df[['Book-Author', 'Year-Of-Publication']]
        y = self.df['Book-Ratings']

        # Convert categorical features to numerical using one-hot encoding
        X = pd.get_dummies(X, columns=['Book-Author'], drop_first=True)

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Standardize the features
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        # Train a Linear Regression model
        model = LinearRegression()
        model.fit(X_train_scaled, y_train)

        # Make predictions on the test set
        predictions = model.predict(X_test_scaled)

        # Evaluate the model
        mse = mean_squared_error(y_test, predictions)
        print(f'Mean Squared Error: {mse}')
        
        
    def predict2(self):
        """
        Train a linear regression model to predict publication year based on author, book ratings, and evaluate the model.

        Returns:
        None
        """
        
        # Assume 'Book-Author' and 'Year-Of-Publication' are features for prediction
        X = self.df[['Book-Author', 'Book-Ratings']]
        y = self.df['Year-Of-Publication']

        # Convert categorical features to numerical using one-hot encoding
        X = pd.get_dummies(X, columns=['Book-Author'], drop_first=True)

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Standardize the features
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        # Train a Linear Regression model
        model = LinearRegression()
        model.fit(X_train_scaled, y_train)

        # Make predictions on the test set
        predictions = model.predict(X_test_scaled)

        # Evaluate the model
        mse = mean_squared_error(y_test, predictions)
        print(f'Mean Squared Error: {mse}')
        
        
