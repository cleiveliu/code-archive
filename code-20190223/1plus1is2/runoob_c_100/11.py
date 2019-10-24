"""
题目：古典问题（兔子生崽）：有一对兔子，从出生后第3个月起每个月都生一对兔子，
小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？（输出前40个月即可）
"""


def print_fib_nums(n):

    if n == 1:
        print([1])
        return [1]
    elif n == 2:
        print([1, 1])
        return [1, 1]
    else:
        res = [1, 1]
        for i in range(2, n):
            res.append(res[i - 2] + res[i - 1])
        print(res)
        return res


print_fib_nums(40)
