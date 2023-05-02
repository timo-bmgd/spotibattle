import json
import random


def get_random_artists():
    with open('artist_list.json', "r") as fp:
        data = json.load(fp)

        artist1_data = tuple(random.choice(list(data.items())))
        artist2_data = tuple(random.choice(list(data.items())))
        while artist1_data == artist2_data:
            # Avoid duplicate selections:
            artist2_data = tuple(random.choice(list(data.items())))

        artist1 = Artist(artist1_data[0], artist1_data[1], artist1_data[2])
        artist2 = Artist(artist2_data[0], artist2_data[1], artist2_data[2])
        return artist1, artist2



class Artist:
    def __init__(self, name, followers, popularity):
        self.name = name
        self.followers = followers
        self.popularity = popularity


class Game:
    artists = get_random_artists()
    score = 0

    def get_winner_artist(self):
        if self.artists[0].followers > self.artists[1].followers:
            return self.artists[0]
        else:
            return self.artists[1]

    def start_game(self):
        print("Which of the following artists has more followers?")
        print("1: " + self.one.name)
        print("2: " + self.two.name)

        answer = input()
        while answer != "1" and answer != "2":
            answer = input("Please write either \"1\" or \"2\"")
        selected = self.a1[(int(answer) - 1)]

        print(f"You selected {selected}")

        if selected == self.get_winner_artist():
            print("You won!")
            self.score += 1
            print("Your score is now " + str(self.score))
        else:
            print("Oh no! You lost!")
            self.score = 0
            print("Your score is now " + str(self.score))

        print("Here are the results:")
        print(f"1: {self.a1[0]} has {self.a1[1]} followers.")
        print(f"2: {self.a2[0]} has {self.a2[1]} followers.")


game = Game()
game.start_game()
