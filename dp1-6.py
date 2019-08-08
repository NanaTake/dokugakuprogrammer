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

# index（文字検索）メソッドで、引数の文字のインデックス値を得る
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