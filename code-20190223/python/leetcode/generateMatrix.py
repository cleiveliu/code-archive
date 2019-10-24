def generateMatrix(self, n):
    A = [[0] * n for _ in range(n)]
    i, j, di, dj = 0, 0, 0, 1
    for k in xrange(n * n):
        A[i][j] = k + 1
        if A[(i + di) % n][(j + dj) % n]:
            di, dj = dj, -di
        i += di
        j += dj
    return A


def generateMatrix(self, n):
    """
    :type n: int
    :rtype: List[List[int]]
    """

    matrix = [[0] * n for _ in range(n)]
    l, r, u, d = 0, n - 1, 0, n - 1
    num = 1

    while l < r and u < d:
        for i in range(l, r):
            matrix[l][i] = num
            num += 1

        for j in range(u, d):
            matrix[j][d] = num
            num += 1

        for z in range(r, l, -1):
            matrix[r][z] = num
            num += 1

        for h in range(d, u, -1):
            matrix[h][u] = num
            num += 1

        l += 1
        r -= 1
        u += 1
        d -= 1

    if l == r or u == d:
        matrix[l][r] = num

    return matrix
