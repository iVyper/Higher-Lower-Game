"""
HigherLowerGame module

This module implements a game where the player guesses which movie has a higher Rotten Tomatoes rating.
It randomly selects two movies from the dataset, compares their ratings, and prompts the player to guess.
The game continues until the player makes an incorrect guess.
"""

import DatasetImport  # Import the dataset loaded in the DatasetImport module
import os  # For clearing the terminal screen


def clear_screen():
    """
    Clears the terminal screen.

    Uses 'cls' for Windows and 'clear' for Unix-based systems.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def select_random_movie():
    """
    Selects a random movie from the dataset.

    Returns:
        list: A list containing the movie title and its Rotten Tomatoes rating.
    """
    movie = []
    # Pick one random record from the dataset DataFrame
    record = DatasetImport.df.sample(n=1).iloc[0]
    movie.append(record["movie_title"])  # Add the movie title
    movie.append(record["tomatometer_rating"])  # Add the movie rating
    return movie


def generate_matchup():
    """
    Generates a matchup between two randomly selected movies and compares their ratings.

    It prints the matchup and returns which movie has the higher rating.

    Returns:
        str: 'A' if Movie A has a higher rating, 'B' if Movie B is higher,
             or 'Tie' if both ratings are equal.
    """
    movie_A = select_random_movie()
    movie_B = select_random_movie()

    # Compare the ratings to determine the higher-rated movie
    if movie_A[1] > movie_B[1]:
        higher_rating = "A"
    elif movie_A[1] < movie_B[1]:
        higher_rating = "B"
    else:
        higher_rating = "Tie"

    # Display the two movies for the player
    print(f"Movie A: {movie_A[0]}\nvs.\nMovie B: {movie_B[0]}")
    return higher_rating


def game_logic():
    """
    Runs the main game loop.

    It generates matchups, prompts the player to guess which movie has the higher rating,
    updates the score if correct, and ends the game when the guess is wrong.
    """
    game = True
    user_score = 0

    while game:
        higher_rating = generate_matchup()  # Create a matchup and get the winning movie identifier
        user_choice = input(
            "Who has the higher Rotten Tomatoes rating?\nType 'A' for Movie A, 'B' for Movie B: ").upper()

        # Check for a tie in ratings
        if higher_rating == "Tie":
            print(f"The ratings for both movies are the same!\nYour score is: {user_score}")
        # Correct guess increases the score
        elif user_choice == higher_rating:
            user_score += 1
            print(f"You are correct!\nYour score is: {user_score}")
        # Wrong guess ends the game
        else:
            print(f"That is wrong, sorry.\nGame Over, your final score was: {user_score}")
            game = False


def main():
    """
    Main entry point for the Higher-Lower Game.

    Displays a welcome message, runs the game logic, and handles replay prompts.
    Clears the screen between games to maintain a clean interface.
    """
    print("Welcome to the Higher-Lower Game!")

    game_end_status = False

    while not game_end_status:
        game_logic()
        try:
            # Ask the player if they want to play another round
            restart = input("Would you like to play again? Type 'y' for yes, 'n' for no: ").lower()
            if restart == "n":
                game_end_status = True
            elif restart != "y":
                # Handle any invalid input by raising an exception
                raise ValueError('Empty or Invalid Input. Please try again.')
        except ValueError as e:
            print(e)
        clear_screen()

    print("Thank you for playing!")


# Start the game when this script is executed directly.
main()
