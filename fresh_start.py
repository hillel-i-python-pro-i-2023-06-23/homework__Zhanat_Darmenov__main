from fresh_start_1 import *


def game_cycle():
    game_on = True
    player1 = True

    # Get player Names:
    namelist = []
    namelist = get_players()

    wordlist1 = []
    wordlist2 = []

    while(game_on):
        # Add Player word to List:
        if player1:
            # Add first player word to List
            game_on = input_word(namelist[0], wordlist1)
            player1 = False
            if game_on == False:
                print('Your looser ',namelist[0])
                print('Your WIN', namelist[1])
        else:
            # Add second player word to List
            game_on = input_word(namelist[1], wordlist2)
            player1 = True
            if game_on == False:
                print('Your looser ',namelist[1])
                print('Your WIN', namelist[0])










if __name__ == "__main__":
    game_cycle()