# 複数のフォルダ名を引数として受け取りパスを組み立てる
import os
os.path.join('Users', 'bob', 'st.txt')

# ファイルを開いて書き込み、閉じる
# 指定のファイルがない場合、新規作成される
st = open('st.txt', 'w')
st.write('Hi from Python!')
st.close()
# 日本語で書き込むときは、エンコード指定もしてあげる必要あり
# writeだと前の記述があるときは上書きする形になる
st = open('st.txt', 'w', encoding='utf-8')
st.write('Pythonからコードを打ってテキストファイルに書き込む')
st.close()

# with文のブロック内でファイルのオープンをすると、実行後自動でファイルを閉じる
def use_with():
    """withを使ってファイルオープンすると実行後に自動でクローズする
    """
    with open('st.txt', 'w') as f:
        f.write('Hey--hey-hey... write from Python!!')
use_with()

# 'r'モードで作成したファイルを読み込む
def use_r_read():
    """上で書き込んだファイルを読み込む
    """
    with open('st.txt', 'r', encoding='utf-8') as f:
        print(f.read())
use_r_read()

# 読み込んだデータをリストに入れておく例
list9 = []
def append_txt():
    """append Data reading from txt to list9.
    """
    with open('st.txt', 'r', encoding='utf-8') as f:
        list9.append(f.read())
    print(list9)
append_txt()

# csvモジュールのwriterメソッドを用いてcsvデータを書き出す
import csv
def write_csv():
    """create 'st.csv'
    """
    with open('st.csv', 'w', newline='') as f:
        w = csv.writer(f, delimiter=',')
        w.writerow(['one', 'two', 'three'])
        w.writerow(['four', 'five', 'six'])
write_csv()

# csvモジュールのreaderメソッドを用いてcsvデータを読み込む
import csv
def read_csv():
    """read 'st.csv'
    """
    with open('st.csv', 'r') as f:
        r = csv.reader(f, delimiter=',')
        for row in r:
            print(','.join(row))
read_csv()


# ここからチャレンジ

# 入力された質問をファイルに書き出す
def cha_1():
    """入力された質問をファイルに書き出す
    """
    question = input('質問をどうぞ：')
    with open('st_8cha.txt', 'w') as f:
        f.write(question)
cha_1()

# リストの要素をcsvファイルに書き出す
import csv
def write_csv():
    """create 'st.csv'
    """
    with open('st.csv', 'w', newline='') as f:
        w = csv.writer(f, delimiter=',')
        w.writerow(['one', 'two', 'three']) 
        w.writerow(['four', 'five', 'six'])
movies = [['Top Gun', 'Risky Business', 'Minority Report'],['Titanic', 'The Revenant', 'Inception'], ['Training Day', 'Man on Fire', 'Flight']]
write_csv()