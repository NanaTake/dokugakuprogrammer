# 文字列を変換するメソッド例
"Hello".upper()
"hello".replace("o", "@")

# リストは要素を指定順番通りに格納するコンテナ
# 番号を指定してあげると中身の値を取り出せる

fruit = list()
fruit

fruit = []
fruit

fruit = ['apple', 'orange', 'pear']
fruit.append('banana')
fruit
fruit[0]
fruit[2] = 'melon'
fruit

fruit = ['apple', 'orange', 'pear']
basket = fruit.pop()
basket
fruit

fruits = ['apple', 'orange', 'pear']
basket = ['banana', 'melon', 'strawberry']
fruits_basket = fruits + basket
print(fruits_basket)

'orange' in fruits
'orange' in basket
'orange' in fruits_basket
'orange' not in fruits
'orange' not in basket
'orange' not in fruits_basket

len(fruits)
len(fruits_basket)

def guess_color():
    colors = ['blue', 'white', 'silver']
    guess = input("Guess my favorite color!(please input):")
    if guess in colors:
        print('Right!')
    else:
        print('Wrong...try again,please.')
guess_color()

# タプルは任意の順番でオブジェクトを保管できるコンテナ
# 一度作成すると後からの変更は一切できない
my_tuple = tuple()
my_tuple1 = ()
my_tuple2 = ('M.Jackson', 1958, 'thriller')
my_tuple3 = ('nya',)
print(my_tuple2)
print(my_tuple2[0])
1958 in my_tuple2
1958 not in my_tuple3

# 辞書型コンテナはキーとバリューのセットでの複数保管が出来るタイプ
# 順番はごっちゃになる時がある
# キーは後から変更できないので注意（バリューは変更可能）

my_dict = dict()
my_dict = {}

fruits = {'apple': 'red',
          'banana': 'yellow'}
print(fruits)

# キーバリューペアの追加、削除は可能
facts = {}
facts['code'] = 'interesting'
facts['Bill'] = 'Gates'
facts['today'] = '2019-07-25'
print(facts)
print(facts['Bill'])

books = {'Dracula': 'Stoker',
         '1984': 'Orwell',
         'Trial': 'Kafka'}
del books['Trial']
print(books)

# inでキーの検索、確認ができる
bill = {'Bill Gates': 'Microsoft'}
'Bill Gates' in bill
'Bill' in bill
print(bill['Bill'])

def check_songs():
    """
    check input(number) in songs{}.
    """
    songs = {'1': 'Be the one',
            '2': 'excite',
            '3': 'climax jump',
            '4': 'surprise drive',
            '5': 'cosmic mind'}
    n = input('数字を入力してください:')
    if n in songs:
        song = songs[n]
        print(song)
    else:
        print('見つかりません。')
check_songs()

# コンテナの中にコンテナ入れられるってよ。

# リストinリスト
lists = []
silver = ['zoffy', 'ultraman', 'Ace']
red = ['seven', 'taro', 'leo']
blue = ['aguru', 'hikari', 'bull?']
lists.append(silver)
lists.append(red)
lists.append(blue)
print(lists)
print(lists[0])
# inしたリストの中身も増やせる
lists[0].append('80')
print(lists)

# リストの中にタプル
cantries = []
asia = ('Japan', 'China')
europe = ('France', 'Germany')
cantries.append(asia)
cantries.append(europe)
print(cantries)

# タプルの中にリスト
sweets = ['cake', 'doughnat']
drinks = ['tea', 'coffee']
foods = (sweets, drinks)
print(foods)
# タプル内のリストは変更できるみたいですにゃん
foods[0].append('cookie')
print(foods)
# あくまでタプルの名前、要素（リスト名）と順番が変更不可って事かな
foods = (drinks, sweets)
print(foods)
# 変更可能な要素をもたせたらタプルさんは変更不可でなくなるらしい
# 最初は鉄壁感出してるのに、１度無理矢理突っ込まれたらガバガバになるのか

# 辞書をリストにin、そしてリストをタプルにinして最終的にガバガバタプルが残る
release_year = {'kuuga': '2000',
                'agito': '2001'}
heisei_rider = [release_year]
print(heisei_rider)
gaba = (heisei_rider,)
print(gaba)

# コンテナ組み合わせの良い例
new_york = {
    '座標': (40.7128, 74.0059),
    'セレブ': [
        'ウッディ・アレン',
        'ジェイ・Z',
        'ケヴィン・ベーコン'
        ],
    '事実': {
        '国': 'アメリカ',
        '州': 'ニューヨーク'
    }
}

# チャレンジ問題

# 好きなミュージシャンのリストを作る...そんなものはない。
musicians = ['子門正人', '水木一郎', '田中昌幸']

# 行った事のある場所と座標をタプルに格納し、リストに放り込む
lo1 = ('tojinbo', 36.1405, 136.0741)
lo2 = ('shirahama', 33.6781, 135.3481)
lo3 = ('tokyo_skytree', 35.7100, 139.8107)
locations = [lo1, lo2, lo3]
print(locations)

# 辞書型コンテナに格納したプロフィールを取り出せる関数を作る
def check_dic():
    """check input in keys,
       if true, print value.
    """
    me = {'height': 157,
        'age': 30,
        'color': 'pale_blue',
        'weight': '60kgを切りたい',
        'author': '京極夏彦',
        'musician': '推し作品の主題歌歌ってくれる人',
        'novel': '京極堂シリーズ',
        'drama': '仮面ライダーシリーズ'}
    keyword = input('知りたいプロフィールを英単語入力する')
    if keyword in me:
        print(me[keyword])
    else:
        print ('me:「そんなの俺が知るか！！」')
check_dic()

# ミュージシャンをキー、値に曲名のリストを持たせた辞書型コンテナを作成する
musicians = {'子門真人': ['仮面ライダーの歌', 'ライダーアクション'],
             '水木一郎': ['セタップ！仮面ライダーX', '仮面ライダーストロンガーの歌'],
             '田中昌幸': ['仮面ライダークウガ！！'],
             '相川七瀬': ['BLADE BRAVE']}
print(musicians)
print(musicians['水木一郎'])
print(musicians['水木一郎'][0])

# Pythonのsetとは何ぞや？
# セットは要素の重複がないコンテナで、要素の順序もない。
# set関数にリストを渡して生成する。
languages = ['Python', 'Ruby', 'PHP', '#C', 'Python']
set_languages = set(languages)
print(set_languages)
# 追加：add / 削除： remove
set_languages.add('Java')
print(set_languages)
set_languages.remove('#C')
print(set_languages)
# 集合の作成に特化したコンテナ型である。 ここから集合のターン
A = {1, 2, 3}
B = {3, 4, 5}
# 和集合 => ２つのset型の要素を全てもつ集合
C = A | B
print(C)
D = A.union(B)
print(D)
# 積集合 => ２つのset型で重複する要素を持つ集合
E = A & B
print(E)
F = A.intersection(B)
print(F)
# 差集合 => AからAとBの積集合を削除した要素のみを持つ集合
G = A - B
print(G)
H = A.difference(B)
print(H)
# 排他的論理和集合 => ２つのset型の和集合から積集合を差し引いた集合
I = A ^ B
print(I)
J = A.symmetric_difference(B)
print(J)