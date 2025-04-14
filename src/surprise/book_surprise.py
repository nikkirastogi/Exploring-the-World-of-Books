import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from surprise import Dataset, Reader
from surprise.model_selection import train_test_split
from surprise import SVD

class BooksSurprise:
    """
    A class for incorporating Surprise library to analyze book ratings data.
    
    Parameters:
    - data (pandas.DataFrame): The book ratings dataset.
    """

    def __init__(self, data):
        """
        Initialize the BooksSurprise object.

        Parameters:
        - data (pandas.DataFrame): The book ratings dataset.
        """
        self.df = data

    def df_surprise(self):
        """
        Process and analyze book ratings data using the Surprise library.

        This method performs data preprocessing, visualization, and applies the Surprise library
        to build and train a collaborative filtering recommendation model.

        Returns:
        None
        """
        # Create a label encoder
        label_encoder = LabelEncoder()
        obj = self.df[self.df['Book-Ratings'] != 0]

        # Encode book titles and authors
        obj['Year-Of-Publication'] = label_encoder.fit_transform(obj['ISBN'])
        obj['Book-Author'] = label_encoder.fit_transform(obj['Book-Author'])

        # Visualize the distribution of ratings
        plt.hist(obj['Book-Ratings'], bins=10, edgecolor='black')
        plt.title('Distribution of Book Ratings')
        plt.xlabel('Rating')
        plt.ylabel('Frequency')
        plt.show()

        # Scale ratings to a range between 1 and 10 (or any desired range)
        scaler = MinMaxScaler(feature_range=(1, 10))
        obj['Book-Ratings'] = scaler.fit_transform(obj['Book-Ratings'].values.reshape(-1, 1))

        # Load your dataset into Surprise
        reader = Reader(rating_scale=(1, 10))
        data = Dataset.load_from_df(obj[['Year-Of-Publication', 'Book-Ratings', 'Book-Author']], reader)

        # Split the data into train and test sets
        trainset, testset = train_test_split(data, test_size=0.2)

        # Choose the SVD algorithm
        algo = SVD()

        # Train the algorithm on the trainset
        return algo.fit(trainset)
