def get_players(name1, name2):
    name1=input("Player 1, enter your name: ")
    print("Hi ", name1)
    name2=input("Player 2, enter your name: ")
    print("Hi ", name2)

def input_word(name_player, word_list):
    word = input('Your turn, player '+name_player+' enter your word:')
    if not word in word_list:
        word_list.append(word)


def check_get_players(name1, name2):

    get_players(name1, name2)
    print('name of player 1', name1)
    print('name of player 2', name2)

if __name__=="__main__":
    name1 = ''
    name2 = ''
    wordlist1 = []
    wordlist2 = []
    check_get_players(name1, name2)
    input_word(name1, wordlist1)
    input_word(name2, wordlist2)
