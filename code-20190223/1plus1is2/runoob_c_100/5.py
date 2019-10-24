"""
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
"""
# 1 max(x,y,z)


def main():
    try:
        x, y, z = map(int, input("请输入3个整数:\n").strip().split())
    except BaseException:
        print("invaled input!!")
        return main()
    if x > y:
        x, y = y, x
    if x > z:
        x, z = z, x
    if y > z:
        y, z = z, y
    print(f'从小到大顺序为:{x} {y} {z}')


if __name__ == "__main__":
    main()
