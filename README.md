
# Higher Lower Game
Higher Lower Game is an interactive Python game that challenges you to guess which movie has a higher Rotten Tomatoes rating. The game uses a dataset of movies and their ratings loaded from Kaggle via the kagglehub package. In each round, two movies are randomly selected and displayed side by side. You must choose the movie you believe has the higher rating. The game continues, increasing your score with each correct guess, until you make an incorrect choice.

## Features

- **Data-Driven Gameplay:** Utilizes a Rotten Tomatoes movies dataset to provide real movie titles and ratings.

- **Interactive Matchups:** Each round presents two randomly chosen movies for you to compare.

- **Scoring System:** Earn points for every correct guess and track your score throughout the game.

- **Replay Option:** After each round, you can choose to play again for endless fun.

- **Clean User Interface:** Automatically clears the terminal between rounds to maintain a clutter-free experience.

## Installation

### Prerequisites

- **Python 3.x:** Ensure that Python 3 is installed on your system. You can download it from [Python's offical website](python.org).

- **`kagglehub` Package:** This package is required to load the dataset from Kaggle. Install it via pip:
```bash
pip install kagglehub
```
- **Internet Access:** The program downloads the dataset from Kaggle when first run, so an active internet connection is needed.

### How to Run

1. **Download the Code:** Clone the repository or save both `DatasetImport.py` and `HigherLowerGame.py` in the same directory on your computer.

2. **Open Terminal/Command Prompt:** Navigate to the directory containing the files.

3. **Run the program:** Execute the following command:

    ```bash
    python3 HigherLowerGame.py
    ```

4. **Follow the Prompts:**
   - The game will welcome you and display two movies.

   - Enter A if you believe Movie A has the higher rating, or B for Movie B.

   - After each round, you'll be asked if you'd like to play again. Enter y to restart or n to exit.


## Demo
![Higher Lower Game Demo](https://i.imgur.com/a3FvdKf.gif)
[Higher Lower Game Demo](https://i.imgur.com/a3FvdKf.gif)

## License

This project is open-source and available under the [MIT License](https://choosealicense.com/licenses/mit/).


## Authors

- Ivis Perdomo [@ivyper](https://www.github.com/ivyper)

