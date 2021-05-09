def bubble_sort(A):
    for i in range(len(A)):
        for j in range(len(A) - 1):
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp

myArr = [5,4,2,7,9,1,8,3,6]
print(myArr)

bubble_sort(myArr)
print(myArr)