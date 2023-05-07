import json
import random
from datetime import datetime
random.seed(datetime.now().timestamp())

def get_random_artists():
    with open('artists_cleaned.json', "r") as fp:
        data = json.load(fp)

        artist1_data = random.choice(data)
        artist2_data = random.choice(data)

        while artist1_data == artist2_data:
             #Avoid duplicate selections:
            artist2_data = random.choice(data)

        artist1 = Artist(artist1_data["name"], artist1_data["followers"], artist1_data["popularity"])
        artist2 = Artist(artist2_data["name"], artist2_data["followers"], artist2_data["popularity"])
        return artist1, artist2



class Artist:
    def __init__(self, name, followers, popularity):
        self.name = name
        self.followers = followers
        self.popularity = popularity


class Game:

    def __init__(self):
        self.artists = get_random_artists()
        self.score = 0

    def get_winner_artist(self):
        if self.artists[0].followers > self.artists[1].followers:
            return self.artists[0]
        else:
            return self.artists[1]

    def start_game(self):
        print("Which of the following artists has more followers?")
        print("1: " + self.artists[0].name)
        print("2: " + self.artists[1].name)

        answer = input()
        while answer != "1" and answer != "2":
            answer = input("Please write either \"1\" or \"2\"")
        selected = self.artists[(int(answer)-1)]

        print(f"You selected {selected.name}")

        if selected == self.get_winner_artist():
            print("You won!")
            self.score += 1
            print("Your score is now " + str(self.score))
        else:
            print("Oh no! You lost!")
            print("Your score is now " + str(self.score))

        print("Here are the results:")
        print(f"1: {self.artists[0].name} has {self.artists[0].followers} followers.")
        print(f"2: {self.artists[1].name} has {self.artists[1].followers} followers.")
        print("_____________________________________________________")
        if selected == self.get_winner_artist():
            game = Game()
            game.score = self.score
            game.start_game()

def run():
    game = Game()
    game.start_game()


