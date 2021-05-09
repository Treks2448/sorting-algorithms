def insertion_sort(A):
    for i in range(1, len(A)):
        j = i
        temp = A[i]
        while j > 0 and temp < A[j-1]:
            A[j] = A[j-1] 
            j -= 1
        A[j] = temp

myArr = [5,4,2,7,9,1,8,3,6]
print(myArr)

insertion_sort(myArr)
print(myArr)