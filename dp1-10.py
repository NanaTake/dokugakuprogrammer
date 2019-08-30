# listsの中身の単語をランダムに選出し、ハングマンゲームを開始する

import random

def hangman(word):
    """guess word until print hangman.
    Arguments:
        word {[string]} -- [answer player should guess.]
    """
    wrong = 0
    stages = ["",
              "_____     ",
              "|    |    ",
              "|    |    ",
              "|    O    ",
              "|   /|\\   ",
              "|   / \\   ",
              "|_________"
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンげーむ、はっじまっるよー")
    limit = len(stages) - 1
    while wrong < limit:
        print("\n")
        char = input("1文字を予想してね")
        if char in rletters:
            char_ind = rletters.index(char)
            board[char_ind] = char
            rletters[char_ind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print(" ".join(board))
            print("君の勝ちー、おめでとー")
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("君の負けー、ざんねんでした！\n答えは{}だよー".format(word))

lists = ['kuuga', 'agito', 'ryuki', '555', 'blade', 'den-o', 'hibiki', 'kabuto', 'kiba', 'decade']
num = random.randint(0,len(lists))
hangman(lists[num])