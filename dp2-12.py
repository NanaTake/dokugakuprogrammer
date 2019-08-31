# 手続き型プログラミング...データはグローバル変数で扱い、関数でデータ操作
# 分かりやすいが、グローバル関数が変更される事でエラーが起きる可能性がある
showa = []
heisei = []

def collect_songs():
    """曲名をshowaまたはheiseiリストに保存していく
    """
    song = '曲名を入力してください：'
    ask = 'showaかheiseiのどちらのリストに保存しますか？（qで終了）：'

    while True:
        genre = input(ask)
        if genre == 'q':
            break
        
        if genre == 'showa':
            sho = input(song)
            showa.append(sho)
        elif genre == 'heisei':
            hei = input(song)
            heisei.append(hei)
        else:
            print('不正な値です。やり直し！')
        
        print('showa songs: ', showa)
        print('heisei songs: ', heisei)

collect_songs()


# 関数型プログラミング...グローバルステートを用いず、引数を渡して処理する
# グローバルステート原因のエラーを排除できるが、扱いづらくなってしまいがち
def increment(int_a):
    return int_a + 1

increment(3)

# オブジェクト指向...複数クラスで相互作用するオブジェクト集合を定義する
# コードの再利用と保守がしやすいコードになるが、計画と設計が重要になる
class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mold = 0
        print('Created!')
    
    def rot(self, days, temp):
        """腐る性質の付加
        Arguments:
            days {[days]} -- [経過日数]
            temp {[temp]} -- [摂氏温度]
        """
        self.mold = days * temp

or1 = Orange(10, 'dark orange')
print(or1)
print(or1.weight)
print(or1.color)
# インスタンスの持つ値は変更できる
or1.weight = 100
or1.color = 'light orange'
print(or1.weight)
print(or1.color)
# インスタンスは複数作成できる、同名のインスタンスを作成すると後のが生き残る
or1 = Orange(4, 'light orange')
or2 = Orange(8, 'dark orange')
or3 = Orange(14, 'yellow')
# 腐敗の性質の追加をするとこんな感じ
or4 = Orange(200, 'orange')
print(or4.mold)
or4.rot(10, 37)
print(or4.mold)


# 長方形を表すクラス
class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l
    
    def area(self):
        return self.width * self.len

    def change_size(self, w, l):
        self.width = w
        self.len = l

rec1 = Rectangle(10, 20)
print(rec1.area())
rec1.change_size(20, 40)
print(rec1.area())


# ここからチャレンジ

# １：４つの属性をインスタンス変数にもつAppleクラスを定義する
class Apple:
    def __init__(self, wei, col, swe, pri):
        self.weight = wei
        self.color = col
        self.sweet = swe
        self.price = pri
        print('Created!')

app1 = Apple(200, 'red', 10, 100)
print(app1.weight)

# ２：円を表すCircleクラスを定義する
import math
class Circle:
    def __init__(self, rad):
        self.radius = rad
        print('Created!')
    
    def area(self):
        return self.radius ** 2 * math.pi

    def change_size(self, rad):
        self.radius = rad
        print('Changed!')

cir1 = Circle(10)
print(cir1.area())
cir1.change_size(3)
print(cir1.area())

# ３：三角形を表すTriangleクラスを定義する
class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h
        print('Created!')
    
    def area(self):
        return self.base * self.height / 2

    def change_size(self, b, h):
        self.base = b
        self.height = h
        print('Changed!')

tri1 = Triangle(10, 10)
print(tri1.area())
tri1.change_size(20, 15)
print(tri1.area())

# ４：六角形を表すHexagonクラスを定義する
class Hexagon:
    def __init__(self, l):
        self.length = l
        print('Created!')
    
    def area(self):
        return self.length * 6

    def change_size(self, l):
        self.length = l
        print('Changed!')

hex1 = Hexagon(10)
print(hex1.area())
hex1.change_size(15)
print(hex1.area())