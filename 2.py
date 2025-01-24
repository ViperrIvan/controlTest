from random import randint
N = randint(10, 100)
matrix = [[randint(1, 100) for i in range(N)] for j in range(N)]
for i in range(N-1):
    if i==N:
        matrix[i], matrix[0] = matrix[0], matrix[i]
    else:
        matrix[i], matrix[i+1] = matrix[i+1], matrix[i]
print(matrix)
