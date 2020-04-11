# オブジェクト指向での主要概念

# カプセル化...複数の変数とメソッドをまとめ、外から見えないようにする
class Data:
    """__init__    数値をlist型のコンテナnumsに格納している
       change_data 指定された順の数値を変更する
    """
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]
    
    def change_data(self, index, n):
        self.nums[index] = n

data_one = Data()
print(data_one.nums)
data_one.change_data(0, 100)
print(data_one.nums)
