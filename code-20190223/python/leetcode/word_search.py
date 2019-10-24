# source:
# https://leetcode.com/problems/word-search/discuss/27791/99.77-Python-Solution-with-Precheck


class Solution(object):


def exist(self, board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    def preCheck():
        preDict = {}

        for i in word:
            if i in preDict:
                preDict[i] += 1
            else:
                preDict[i] = 1

        for i in board:
            for j in i:
                if j in preDict and preDict[j] > 0:
                    preDict[j] -= 1
        for i in preDict.values():
            if i > 0:
                return False
        return True

    def helper(wordIdx, x, y):
        if board[x][y] != word[wordIdx]:
            return False
        elif wordIdx == l - 1:
            return True
        else:
            wordIdx += 1
            tempChar = board[x][y]
            board[x][y] = None
            for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                xNext = x + d[0]
                yNext = y + d[1]
                if -1 < xNext < m and -1 < yNext < n and board[xNext][yNext]:
                    if helper(wordIdx, xNext, yNext):
                        return True
            board[x][y] = tempChar
            return False

    if not board:
        return False
    if not word:
        return True

    if not preCheck():
        return False

    m = len(board)
    n = len(board[0])
    l = len(word)
    for i in xrange(m):
        for j in xrange(n):
            if helper(0, i, j):
                return True

    return False
