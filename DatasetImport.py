"""
DatasetImport module

This module loads the Rotten Tomatoes movies dataset from Kaggle using the kagglehub package.
It extracts only the movie title and the corresponding Rotten Tomatoes rating for further use.
"""

import kagglehub  # Import the kagglehub module to interact with Kaggle datasets
from kagglehub import KaggleDatasetAdapter

# Define the path to the CSV file inside the dataset.
file_path = "rotten_tomatoes_movies.csv"

# Load the dataset using the KaggleDatasetAdapter for Pandas.
# Here we specify to use only the 'movie_title' and 'tomatometer_rating' columns.
df = kagglehub.dataset_load(
    KaggleDatasetAdapter.PANDAS,
    "stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset",
    file_path,
    pandas_kwargs={"usecols": ["movie_title", "tomatometer_rating"]}
)
