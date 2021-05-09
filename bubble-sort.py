from swap import swap

def bubble_sort(A):
    for i in range(len(A)):
        for j in range(len(A) - i - 1):
            if A[j] > A[j+1]:
                swap(A, j, j+1)

myArr = [5,4,2,7,9,1,8,3,6]
print(myArr)

bubble_sort(myArr)
print(myArr)