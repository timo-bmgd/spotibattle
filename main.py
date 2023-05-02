import get_api_data
import get_artist_data
import game
import sys

argument = sys.argv[1]
command = argument

if(command=="game"):
    game.run()
elif(command=="update"):
    get_api_data.create_unclean_json_file()
    get_artist_data.update()
    print("Update successful")
else:
    print("Your command "+command+" was not found.")
    print("Use either 'game' to play the game or 'update' to update the JSON file.")