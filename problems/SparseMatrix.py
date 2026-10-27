'''
Problem Statement
Implement two tasks:
1. Convert a given n*m matrix into its sparse representation, storing only nonzero
entries as triples (row, column, value).
2. Given two matrices in sparse representation, compute their product and output the
result in sparse format.

Input
• A dense matrix of size n*m.
• Two sparse matrices to be multiplied, given as lists of triples.
Output
• Sparse representation of the input dense matrix.
• Sparse representation of the product of the two input sparse matrices.
'''

def SparseMatrix(matrix):#O(n*n)
    # BuildTriples(Row, Col, Value) For Nonzero Entries.
    sparseform = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            val = matrix[row][col]
            if val:
                sparseform.append((row, col, val))
    return sparseform


def PrintSparse(matrix, name):#O(n)
    sparseform = SparseMatrix(matrix)
    print(f"{name}: " + " ".join(str(tup) for tup in sparseform))

def SparseMatrixMul(matrixA, matrixB):#O(n*n*n)
    # Dense×Dense Then Print As Sparse.
    n, k1 = len(matrixA), len(matrixA[0]) if matrixA else 0
    k2, m = len(matrixB), len(matrixB[0]) if matrixB else 0
    if k1 != k2:
        raise ValueError("Shape mismatch: A is n*k, B must be k*m")

    BT = []
    for j in range(m):
        row = []
        for i in range(k2):
            row.append(matrixB[i][j])
        BT.append(row)

    C = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            s = 0
            for t in range(k1):
                s += matrixA[i][t] * BT[j][t]
            C[i][j] = s
    return C  
        
if __name__=="__main__":    
    from MatrixCreator import MatrixFromFlat
    matrixes =[]
    for i in range(1,3):
        print(f"Input the Details of Matrix {i}")
        matrix = MatrixFromFlat()
        matrixes.append(matrix)
        print("")
    PrintSparse(matrixes[0] ,"A")
    PrintSparse(matrixes[1] ,"B")
    print("")
    PrintSparse(SparseMatrixMul(matrixes[0] ,matrixes[1]),"C")
