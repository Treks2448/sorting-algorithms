from swap import swap

def quick_sort(A, p, r):
    def partition(A, p, r):
        q = p - 1
        for i in range(p, r):
            if A[i] <= A[r]:
                q += 1
                swap(A, i, q)
        q += 1
        swap(A, r, q)
        return q
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q  -1)
        quick_sort(A, q, r)

myArr = [5,4,2,7,9,1,8,3,6]
print(myArr)

quick_sort(myArr, 0, len(myArr)-1)
print(myArr)
