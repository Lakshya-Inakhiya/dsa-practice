'''Problem Statement '''
#You are given an n ×m matrix and an integer k. For every column whose index is a
#multiple of k (1-based indexing), reverse the order of its elements (top to bottom).
from MatrixCreator import PrintMatrix,MatrixRowWise
def ReverseColumn(): #O(n*n)
    matrix = MatrixRowWise()
    row = len(matrix)
    col = len(matrix[0])
    k = int(input())
    for j in range(k - 1, col, k):
        for i in range(row // 2):
            matrix[i][j], matrix[row - i - 1][j] = matrix[row - i - 1][j], matrix[i][j]

    return matrix
                

if __name__=="__main__":
    PrintMatrix(ReverseColumn())