# 4sum leetcode
# source :
# https://leetcode.com/problems/4sum-ii/discuss/93917/Easy-2-lines-O(N2)-Python

import collections


def fourSumCount(self, A, B, C, D):
    AB = collections.Counter(a + b for a in A for b in B)
    return sum(AB[-c - d] for c in C for d in D)
    # He must be a gnius


print("Fuck!!", end='')
