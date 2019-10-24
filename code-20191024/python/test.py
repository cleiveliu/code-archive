from typing import List

class Solution:
    def minAvailableDuration(self, s1: List[List[int]], s2: List[List[int]], d: int) -> List[int]:
        def h(a1,a2,d):
            start1,end1 = a1
            start2,end2 = a2
            start = max(start1, start2)
            end = min(end1,end2)
            if end >= start and end-start>d:
                return start,start+d
            else:
                return None
        s1.sort()
        s2.sort()
        i,j = 0,0
        while i < len(s1) and j < len(s2):
            ret = h(s1[i],s2[j],d)
            print(ret)
            print(ret[1]-ret[0])
            if ret != None:
                return list(ret)
            
            if s1[i][1] >= s2[j][1]:
                j += 1
            else:
                i += 1
        return []

a = Solution()
a1 = [[216397070,363167701],[98730764,158208909],[441003187,466254040],[558239978,678368334],[683942980,717766451]]
a2 = [[50490609,222653186],[512711631,670791418],[730229023,802410205],[812553104,891266775],[230032010,399152578]]
d = 456085

a.minAvailableDuration(a1,a2,d)