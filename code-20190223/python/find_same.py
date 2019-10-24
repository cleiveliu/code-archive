# find_same.py
# solution for this:https://www.youtube.com/watch?v=10WnvBk9sZc

# let me tell you what is shit code
# like this,below
# maybe I will rewrite it somedays :P


def find_same(s1: str, s2: str) -> str:
    assert(isinstance(s1, str) and isinstance(s2, str))
    s1, s2 = remove_un_ovelap(s1, s2)
    path = []
    helper(s1, s2, "", path)
    print(f"path -> {path}")
    print(f"path[0] -> {path[0]}")
    res = ""
    for c in path:
        if len(c) > len(res):
            res = c
    print(f"the answer -> {res}")
    return res


def helper(s1, s2, tem, path=[]):
    if not s1 or not s2:
        path.append(tem)
        return
    for i in range(len(s1)):
        flag, after_s2 = find_single_char(s1[i], s2)
        if flag is True:
            helper(s1[i + 1:], after_s2, tem + s1[i], path)
        else:
            helper(s1[i + 1:], after_s2, tem, path)


def find_single_char(c: str, s: str):
    for i in range(len(s)):
        if c == s[i]:
            return True, s[i + 1:]
    return False, s


def remove_un_ovelap(s1, s2):
    def my_filter(s1, s2):
        return ''.join(filter(lambda x: x in s2, s1))
    new_s1 = my_filter(s1, s2)
    new_s2 = my_filter(s2, s1)
    return new_s1, new_s2
