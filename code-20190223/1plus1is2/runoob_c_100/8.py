"""
题目：输出9*9口诀。
"""


def main():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f'{j}*{i}={j*i}', end='  ')
        print('\n')


main()
