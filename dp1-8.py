# mathという組み込みモジュールを使ってみる
# pow(x, y) => x ** y
import math
math.pow(2, 3)

# randomモジュールのrandint関数は、渡した引数の間で乱数を返す
import random
random.randint(0, 20)

# statisticsモジュールは整数のリストから平均値、中央値、最頻値を算出できる
nums = [1, 4, 24, 4, 13, 36, 2, 5]
import statistics
statistics.mean(nums)
statistics.median(nums)
statistics.mode(nums)

# keywordモジュールは、引数がPythonのキーワードかをチェックできる
import keyword
keyword.iskeyword('for')
keyword.iskeyword('football')


# ここからチャレンジ

# statisticsモジュールで別の関数を使ってみる
nums = [1, 4, 24, 4, 13, 36, 2, 5, 7]
import statistics
statistics.median_grouped(nums)