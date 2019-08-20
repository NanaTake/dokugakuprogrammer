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