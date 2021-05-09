from math import inf, floor
from swap import swap

def merge_sort(A, p, r):
    def merge(A, p, q, r):
        lhs = A[p:q+1]
        rhs = A[q+1:r+1]
        lhs.append(inf)
        rhs.append(inf)
        i = 0
        j = 0
        for k in range(p, r+1):
            if lhs[i] <= rhs[j]:
                A[k] = lhs[i]
                i += 1
            else:
                A[k] = rhs[j]
                j += 1

    # if abs(p - r) == 2:
    #     if A[p] > A[r]:
    #         swap(A, p, r)

    if p == r:
        return
    else:
        q = floor((r+p)/2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

myArr = [5,4,2,7,9,1,8,3,6]
print(myArr)

merge_sort(myArr, 0, len(myArr) - 1)
print(myArr)
