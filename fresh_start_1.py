def get_players():
    namelist=[]
    name1=input("Player 1, enter your name: ")
    print("Hi ", name1)
    namelist.append(name1)
    name2=input("Player 2, enter your name: ")
    print("Hi ", name2)
    namelist.append(name2)
    return namelist

def input_word(name_player, word_list):
    word = input('Your turn, player '+name_player+' enter your word:')
    if word=='':
        print('Finish game!')
        return False
    if not word in word_list:
        word_list.append(word)
    else:
        print('This word has been used!')

    return True


def check_get_players():
    namelist = get_players()
    print('name of player 1', namelist[0])
    print('name of player 2', namelist[1])

if __name__=="__main__":
    wordlist1 = []
    wordlist2 = []
    game_on = True
    namelist = []
    namelist = check_get_players()

    #input_word(namelist[0], wordlist1, game_on)
    #input_word(namelist[1], wordlist2, game_on)

