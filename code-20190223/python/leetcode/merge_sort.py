def mergeSortedList(a, b):
    """
    :a:list
    :b:list
    :rtpe:list
    """
    res = []
    while a and b:
        if a[0] < b[0]:
            res.append(a.pop(0))
        else:
            res.append(b.pop(0))
    if a:
        res += a
    if b:
        res += b
    return res


def mergeSort(alist):
    """
    :alist:list
    :rtype:list
    """
    if len(alist) <= 1:
        return alist
    mid = len(alist) // 2
    left = alist[:mid]
    right = alist[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return mergeSortedList(left, right)


if __name__ == "__main__":
    a = list(range(3)) + list(range(6, 9)) + list(range(3, 6))
    print("before:", a)
    print("after :", mergeSort(a))
"""
def mergeSort(self,lst):
        if len(lst)== 1:
            return lst
        mid=len(lst)//2
        left=lst[:mid]
        right=lst[mid:]

        return self.mergeSortedList(self.mergeSort(left),self.mergeSort(right))

def mergeSortedList(self,lst1,lst2):
    if not lst1 or not lst2:
        return lst1 or lst2
    res=[]
    i,j=0,0
    while i< len(lst1) and j< len(lst2):
        if lst1[i]< lst2[j]:
            res.append(lst1[i])
            i+=1
        else:
            res.append(lst2[j])
            j+=1
    if i< len(lst1)-1:
        while i< len(lst1):
            res.append(lst1[i])
            i+=1
    if j< len(lst2)-1:
        while j< len(lst2):
            res.append(lst2[j])
            j+=1
    return res

"""
