# SpotiBattle 🎵🎤

SpotiBattle is a fun and engaging command-line game built in Python 🐍. It quizzes the player about the popularity and number of followers of different artists on Spotify 🌟. The game fetches artist data using the Spotify API and updates the game data with the most recent information 📈.

<img src="https://user-images.githubusercontent.com/78025568/235758741-7bce3c08-822e-4339-a315-1404572a0b56.png" alt="SPOTIBATTLE" width="300" height="300">


## Getting Started 🚀

1. Clone this repository 📂
2. Install the required Python packages using `pip install python-dotenv` 📦
3. Run the game using `python main.py game` 🎮
4. To update the artist data, run `python main.py update` 🔄

## How to Play 🕹️

The game presents two artists, and the player has to guess which artist has more followers on Spotify. If the player's guess is correct, their score increases, and a new round starts with different artists. The game continues until the player makes an incorrect guess.

## Game Flow 🌊

1. The game fetches the top artists from Spotify using the `get_api_data.py` file.
2. The artist data is cleaned and saved as a JSON file using the `get_artist_data.py` file.
3. The game randomly selects two artists from the cleaned JSON file using the `game.py` file.
4. The player is asked to guess which artist has more followers.
5. If the player guesses correctly, their score increases, and the game continues with new artists. If they guess incorrectly, the game ends and shows their final score.

## Future Improvements 🔮

We are planning to add more features to SpotiBattle, such as playing with artists from a selected playlist and providing a graphical user interface (GUI) for a more immersive and enjoyable experience. Stay tuned for updates! 🎉
