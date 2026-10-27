'''Problem Statement'''
#You are given an n×n matrix. Treat the matrix as consisting of layers (outer ring, next
#inner ring, etc.). Rotate each layer by one position in the clockwise direction.
from MatrixCreator import PrintMatrix,MatrixRowWise
def MatrixLayerRotation(matrix):#O(n*n)
    row = len(matrix)
    layers = row//2
    for L in range(layers):
        top , left= L , L
        bottom , right = row - L -1 , row - L -1 
        ring =[]
        #for top of layer
        for c in range(left , right):
            ring.append(matrix[top][c])
        #for right of layer
        for r in range(top , bottom):
            ring.append(matrix[r][right])
        #for bottom of layer
        for c in range(right , left , -1 ):
            ring.append(matrix[bottom][c])
        #for left of layer
        for r in range(bottom , top ,-1):
            ring.append(matrix[r][left])
        ring = ring[-1:]+ring[:-1]
        # printing back the matrix
        i=-1
        #for top of layer
        for c in range(left , right):
            i+=1
            matrix[top][c] = ring[i]
            
        #for right of layer
        for r in range(top , bottom):
            i+=1 
            matrix[r][right] = ring[i]
        #for bottom of layer
        for c in range(right , left , -1 ):
            i+=1
            matrix[bottom][c] = ring[i]
             
        #for left of layer
        for r in range(bottom , top ,-1):
            i+=1
            matrix[r][left] = ring[i]
            

    return matrix

if __name__ == "__main__" :
    matrix = MatrixRowWise()
    print("")
    PrintMatrix(MatrixLayerRotation(matrix))
    print("")