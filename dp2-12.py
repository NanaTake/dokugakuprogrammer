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