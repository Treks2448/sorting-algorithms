from swap import swap

def quick_sort(A, p, r):
    if not p == r:
        q = partition(A, p, r);
        print(A)
        print(p , q, r)
        quick_sort(A, p, q)
        quick_sort(A, q+1, r)

def partition(A, p, r):
    q = p - 1
    for i in range(p, r+1):
        if A[i] <= A[r]:
            q += 1
            swap(A, i, q)
    return q

myArr = [5,4,2,7,9,1,8,3,6]
print(myArr)

quick_sort(myArr, 0, len(myArr)-1)
print(myArr)
