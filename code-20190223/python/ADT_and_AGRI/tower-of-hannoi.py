def hannoi(n, src, des, tem):

    if n >= 1:
        hannoi(n - 1, src, tem, des)
        print("move %d -> %d" % (src, des))
        hannoi(n - 1, tem, des, src)


hannoi(3, 1, 3, 2)
