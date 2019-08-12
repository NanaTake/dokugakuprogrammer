# 文字列操作

# 文字列に対してインデックスを指定すると対応する1文字を取り出せる
author = '京極夏彦'
print(author[0])
print(author[2])
# マイナスをインデックスにつけると、右側から順番に対応する文字を取り出せる
print(author[-1])
print(author[-3])
# 文字列はその一部だけを別の文字に入れ替えられない
# 変更したかったら、新しく文字列を定義し直す必要あり
# 文字列は連結できる
chain = 'こぶた' + 'たぬき' + 'きつね' + 'ねこ'
print(chain)
# 文字列に整数を掛け算すると、回数分繰り返しの文字列が返ってくる
phrase = 'Wow--' + 'wow-' * 2 + ' Take your Amazonz!!'
print(phrase)
# 大文字・小文字への一括変換はできる
print(phrase.upper())
print(phrase.lower())
# 頭だけ大文字にすることも可能
print(phrase.capitalize())

# format（書式化）メソッドを使えば、すでにある文字列に後から文字を挿入できる
hello = 'Hello, {}. It is {} today.'
name = 'Mr Ishinomori'
weather = 'sunny'
print(hello.format(name, weather))
# formatの引数にinputを渡すこともできる
def introduction():
    """create self introduction.
    """
    self_introduction = '{}は{}{}。{}。'
    first_person = input('一人称：')
    name = input('名前：')
    ending = input('語尾：')
    message = input('一言：')
    answer = self_introduction.format(first_person, name, ending, message)
    print(answer)
introduction()

# split（分割）メソッドでは、渡した文字列の位置で元の文字列が分割される
dove = 'ぽっぽっぽー、はとぽっぽー'
answer = dove.split('、')
print(answer)

# join（結合）メソッドを使うと、初めに指定した文字列を引数の文字列の間に挟んで結合する
# 文字列を引数にすると、1文字ずつの間に頭の文字列を挟んでいく
first = 'abc'
answer = '+'.join(first)
print(answer)
# リストを引数にすると、要素の間に初めに指定した文字列を挟んで繋げていく
words = ['天が呼ぶ', '地が呼ぶ', '人が呼ぶ', '俺の名は...']
result = '!'.join(words)
print(result)

# strip（空白除去）メソッドで、前後の空白を駆逐可能
# ただし、文字の間の空白は駆逐範囲外
manyblanks = '   Nya   nya   nya   '
manyblanks = manyblanks.strip()
print (manyblanks)
print(manyblanks + manyblanks)

# replace（置換）メソッドで、第一引数の文字列を第二引数の文字列に置換する
hayato = 'ならば...お見せしようッ！！'
hayato2 = hayato.replace('.', '、')
print(hayato2)

# index（文字検索）メソッドで、引数の文字の最初のインデックス値を得る
# 検索結果がない場合の例外処理もセットで書くのがベターだと思うよ
def index_words(input_word, check_word):
    """use index
    
    Arguments:
        input_word {[string]} -- [word for index]
    """
    try:
        print(input_word.index(check_word))
    except:
        print('Not found...')

input_word = 'kamen-rider'
check_word = 'n'
index_words(input_word, check_word)

# in（包含）メソッドを使うと、前の文字列が後の文字列に含まれるか判定できる
# bool型で返ってくる
result = 'kuuga' in 'kuuga, agito, ryuki'
print(result)
# 大文字は別物判定？　→やっぱり別物ですね。
result = 'Kuuga' in 'kuuga, agito, ryuki'
print(result)

# Pythonにおいて、エスケープ文字は\
# ""の中で""を使いたかったら、各"の前に\をつければよろし
print('ご用のある方は、\'ピーッ\'という発信音の後に')
# ""と''を併用すればエスケープ文字いらんけどね。
print('だれだ、だれだ、だれだ〜ッ！？"にゃー"...何だ、ネコか...')

# \nを入れたところで改行されます
print('だれだッ！？\n"にゃー"\n...何だ、ネコか...')

# スライス...開始位置から終了位置の手前までを取り出す
heisei = ['kuuga', 'agito', 'ryuki', '555', 'blade']
print(heisei[0:3])
phrase = 'Wow--' + 'wow-' * 2 + ' Take your Amazonz!!'
print(phrase[:14]) #最初から
print(phrase[14:]) #最後まで


# ここからチャレンジ問題

# １："CAMUS"を1文字ずつ出力する
print("CAMUS"[0])
print("CAMUS"[1])
print("CAMUS"[2])
print("CAMUS"[3])
print("CAMUS"[4])
# forで反復処理した方がスマートかしらん
def brandy_call():
    brandy = "CAMUS"
    for char in brandy:
        print(char)
brandy_call()

# ２：入力させた２つの文字列を挿入した文字列を作る
def yesterday():
    """yesterday, what and whom do you write to ?
    """
    yesterday = '私は昨日{}を書いて{}に送った。'
    what = input('何を書いた？：')
    who = input('誰に送った？：')
    answer = yesterday.format(what, who)
    print(answer)
yesterday()

# ３：先頭の1文字を大文字にする
phrase = 'wow--' + 'wow-' * 2 + ' Take your Amazonz!!'
print(phrase.lower())
print(phrase.capitalize())
# 1文字目だけ取り出して大文字にしてから残りと繋ぎ直す
front = phrase[:1].upper()
answer = front + phrase[1:]
print(answer)

# ４：空白で区切ったリストにする
dove = 'どこで？　誰が？　いつ？'
answer = dove.split('　')
print(answer)

# ５：リストの言葉を連結して正常な記述の英文にする
fox_jump = ['The', 'fox', 'jump', 'over', 'the', 'fence', '.']
result = ' '.join(fox_jump)
print(result)