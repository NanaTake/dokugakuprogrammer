def cubed_num(num):
    try:
        num = int(num)
        answer = num ** 3
        print(answer)
    except ValueError:
        print('ValueError...input number, please.')