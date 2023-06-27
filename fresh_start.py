from fresh_start_1 import *


def game_cycle():
    game_on = True
    player1 = True

    # Get player Names:
    name1 = ''
    name2 = ''
    get_players(name1, name2)

    wordlist1 = []
    wordlist2 = []

    while(game_on):
        # Add Player word to List:
        if player1:
            # Add first player word to List
            input_word(name1, wordlist1, game_on)
            player1 = False
        else:
            # Add second player word to List
            input_word(name2, wordlist2, game_on)
            player1 = True










if __name__ == "__main__":
    game_cycle()