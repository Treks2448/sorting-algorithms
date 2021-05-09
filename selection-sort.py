from swap import swap

def selection_sort(A):
    for i in range(len(A)):
        j_min = i
        for j in range(i + 1, len(A)):
            if (A[j] < A[j_min]):
                j_min = j
        swap(A, i, j_min)

myArr = [5,4,2,7,9,1,8,3,6]
print(myArr)

selection_sort(myArr)
print(myArr)
