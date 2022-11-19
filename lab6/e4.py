'''
Using list comprehension, create a matrix of random integers between 0 and 10 of size 5x5. The matrix should be a list of lists of integers. Effectively, it is a list of rows, where each row is a list of numbers.
Print the matrix (just using normal loops).
Using list comprehension, create a vector (list) of maximum elements in each row.
Using list comprehension, create a vector (list) of maximum elements in each column.
Using list comprehension, create a vector (list) with the elements on the main diagonal of M.
'''
import random

m = [[random.randint(0,10) for _ in range(5)] for _ in range(5)]
row = 0
while row<len(m):
    print(f"{row} row:{m[row]}")
    row+=1

maxR = [max(row) for row in m]
print(f"maximum elements of each row:{maxR}")
print([max([m[i][j] for i in range(5)]) for j in range(5)])
#maxC = [max([m[i][j] for i in range(5) for j in range(5)])]