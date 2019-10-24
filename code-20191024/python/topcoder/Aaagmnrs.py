from collections import Counter
# from typing import List


class  Aaagmnrs:
    def  anagrams(self,words):
        ret_indexs = []
        d = dict() # dict<str,int>
        for i,word in enumerate(words):
            mark = self.mark_it(word.lower())
            if mark in d:
                if d[mark] >= 0:
                    ret_indexs.append(d[mark])
                    d[mark] = -1
            else:
                d[mark] = i
        for key in d:
            if d[key] >= 0:
                ret_indexs.append(d[key])
        ret_indexs.sort()
        ret = []
        for index in ret_indexs:
            ret.append(words[index])
        return ret

                
    
    def mark_it(self,word):
        def remove_space(word):
            return (c for c in word if c != ' ')
        c = Counter(remove_space(word))
        sorted_keys = sorted(c)
        ret = ''
        for key in sorted_keys:
            ret += key
            ret += str(c[key])
        return ret