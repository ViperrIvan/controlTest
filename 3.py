from random import randint
N = randint(10, 100)
matrix = [[randint(1, 100) for i in range(N)] for j in range(N)]
promezList = []
def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp
for i in range(N):
    for j in range(N):
        promezList.append(matrix[j][i])
    insertion_sort(promezList)
    for c in range(N):
        matrix[c][i], promezList[c] = promezList[c], matrix[c][i]
for elem in matrix:
    print(elem)
