"""
题目：输入某年某月某日，判断这一天是这一年的第几天？
"""


def main():
    try:
        year, month, day = map(
            int, input("请输入年月日，格式为:\n Year Month Day:\n").strip().split())
    except BaseException:
        print("invalid input,Try again!!")
        return main()
    month_days = {
        1: 0,
        2: 31,
        3: 59,
        4: 90,
        5: 120,
        6: 151,
        7: 181,
        8: 212,
        9: 243,
        10: 273,
        11: 304,
        12: 334
    }


if __name__ == "__main__":
    main()
