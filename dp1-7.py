# forループ...イテラブルの繰り返し処理（反復処理）
# forループに文字列を渡すと、1文字ずつ取り出して処理する
def print_char(name):
    """print character by 1character.
    """
    word = name
    for character in word:
        print(character)
name = 'Kuuga'
print_char(name)

# forループにリストを渡すと、要素を１つずつ取り出して処理する
def print_riders(heisei):
    """print character by 1youso.
    """
    word = heisei
    for character in word:
        print(character)
heisei = ['kuuga', 'agito', 'ryuki', '555', 'blade']
print_riders(heisei)

# タプルを渡しても一要素ずつ処理する
def print_riders2(heisei2):
    """print character by 1.
    """
    word = heisei2
    for character in word:
        print(character)
heisei2 = ('hibiki', 'den-o', 'kabuto', 'kiba', 'decade')
print_riders2(heisei2)

# 辞書型ではキーを１つずつ取り出して処理する
# バリューを表示してみたよ
def print_songs(songs):
    """print character by 1.
    """
    words = songs
    for character in words:
        print(songs[character])
songs = {'1': 'Be the one',
         '2': 'excite',
         '3': 'climax jump',
         '4': 'surprise drive',
         '5': 'cosmic mind'}
print_songs(songs)

# リストなどのミュータブルなイテラブルを更新できる
def update_riders(heisei):
    """print character by 1youso.
    """
    i = 0
    word = heisei
    for new in word:
        new = word[i]
        new = new.upper()
        word[i] = new
        i += 1
    print(word)
heisei = ['kuuga', 'agito', 'ryuki', '555', 'blade']
update_riders(heisei)
# インデックス値を自動的に用意してくれるenumerate関数を利用すると...
def update_riders2(heisei):
    """print character by 1youso.
    """
    word = heisei
    for i, new in enumerate(word):
        new = word[i]
        new = new.upper()
        word[i] = new
    print(word)
heisei = ['hibiki', 'den-o', 'kabuto', 'kiba', 'decade']
update_riders2(heisei)

# ループ処理でリストに突っ込めー(^^)もできる
def update_append(rider):
    """upper character by 1, and append to heisei_riders.
    """
    word = rider
    for show in word:
        show = show.upper()
        heisei_riders.append(show)
    print(heisei_riders)
heisei_riders = []
heisei = ['kuuga', 'agito', 'ryuki', '555', 'blade']
heisei2 = ['den-o', 'hibiki', 'kabuto', 'kiba', 'decade']
update_append(heisei)
update_append(heisei2)

# range関数は引数に指定した整数を順番に生成する
# range関数を繰り返し処理に放り込んでみる
def print_num():
    """print numbers from 1 to 10.
    """
    for i in range(1, 11):
        print(i)
print_num()

# whileループ...条件式がTrueを返す間はコードの実行を繰り返す
def count_down(num):
    """count down, and print words.
    """
    x = num
    while x > 0:
        print('{}'.format(x))
        x -= 1
    print('ハッピィ...バァースデイィィイッ！！')
num = 10
count_down(num)

# break文...ループ処理を終了させるための文
def loop_question():
    """'q'を入力するまで根掘り葉掘りする
    """
    qs = ['お名前は？', 'ご趣味は？', '何色がお好きですか？']
    n = 0
    while True:
        print('Type q to quit')
        a = input(qs[n])
        if a == 'q':
            break
        n = (n + 1) % 3
loop_question()

# continue文...実行中の反復処理を途中終了して、次の反復処理に入る
def use_continue():
    """３以外の数値を出力する
    """
    for i in range(1, 6):
        if i == 3:
            continue
        print(i)
use_continue()
# 上と全く同じ処理の別解
def use_continue2():
    """３以外の数値を出力する
    """
    i = 1
    while i <= 5:
        if i ==3:
            i += 1
            continue
        print(i)
        i += 1
use_continue2()

# ループ処理は入れ子にできる
# でも二段が限度ですね、普通。
def loop_in_loop():
    """ループの中にループをネストさせる
       数値の後に毎回abcが出力される
    """
    for i in range(1, 3):
        print(i)
        for char in ['a', 'b', 'c']:
          print(char)
loop_in_loop()

def add_result():
    """[list1] + [list2] => [result]
    """
    list1 = [1, 2, 3, 4]
    list2 = [10, 20, 30, 40]
    result = []
    for i in list1:
        for j in list2:
            result.append(i + j)
        print(result)
add_result()

def for_in_while():
    """type not 'n', print phrase.
    """
    while input('type \'n\' to quit') != 'n':
        for i in range(1, 4):
            print('(」・ω・)」うー!(/・ω・)/にゃー!\n' * i)
for_in_while()

# ここからチャレンジ問題

# １：リストの要素を出力する
def pick_from_list():
    """リストの要素を一個ずつ出力する
    """
    heisei = ['kuuga', 'agito', 'ryuki', '555', 'blade']
    for rider in heisei:
        print(rider)
pick_from_list()

# ２：２５から３５までの数値を出力する
def count_from25():
    """２５から３５までの数値を出力する
    """
    for i in range(25, 36):
        print(i)
count_from25()

# ３：リストの値をインデックス値と一緒に出力する
def print_index_and_value():
    """リストの値をインデックス値と一緒に出力する
    """
    heisei = ['kuuga', 'agito', 'ryuki', '555', 'blade']
    for i, rider in enumerate(heisei):
        rider = heisei[i]
        print(i)
        print(rider)
print_index_and_value()

# ４：無限ループする数字当てプログラムを作成する（終了方法あり）
def answer_num():
    """無限ループする数字当てプログラムを作成する（終了方法あり）
    """
    numbers = [2, 3, 5, 7, 11, 13, 17, 19]
    while True:
        answer = input('私の持っている数字は何でしょう？（qで終了）：')
        if answer == 'q':
            break
        try:
            answer = int(answer)
            if answer in numbers:
                print('正解です')
            else:
                print('落ち着いて〇〇を数えるんだ...')
        except ValueError:
            print('数字かqしか受付できないんだなぁ...')
answer_num()

# ５：リストの数値を全部掛け合わせて新しいリストに積を格納
def malti_result():
    """[list1] * [list2] => [result]
    """
    list1 = [1, 2, 3, 4]
    list2 = [10, 20, 30, 40]
    result = []
    for i in list1:
        for j in list2:
            result.append(i * j)
        print(result)
malti_result()