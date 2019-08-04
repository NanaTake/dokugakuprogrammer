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