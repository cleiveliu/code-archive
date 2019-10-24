class Solution:
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if not A:
            return None
        A = sorted(A)
        if K == 0:
            return A[-1] - A[0]
        if len(A) == 1:
            return 0
        dis = A[-1] - A[0]

        if dis >= 3 * K:
            return dis - 2 * K
        elif dis >= 2 * K:
            maxn = A[-1] - K
            minn = A[0] + K
            for i in A:
                if i + K > maxn and i - K < minn:
                    if i + K - maxn >= minn - (i - K):
                        minn = i - K
                    else:
                        maxn = i + K
            return maxn - minn
        elif dis > K:
            maxn1 = A[-1] + K
            minn1 = A[0] + K
            for i in A:
                if i + K > maxn1 and i - K < minn1:
                    if i + K - maxn1 >= minn1 - (i - K):
                        minn1 = i - K
                    else:
                        maxn1 = i + K
            maxn = max(A[0] + K, A[-1] - K)
            minn = min(A[0] + K, A[-1] - K)
            for i in A:
                if i + K > maxn and i - K < minn:
                    if i + K - maxn >= minn - (i - K):
                        minn = i - K
                    else:
                        maxn = i + K
            return min(maxn - minn, maxn1 - minn1)
        else:
            return dis
