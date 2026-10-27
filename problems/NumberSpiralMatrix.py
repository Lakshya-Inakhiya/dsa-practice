from MatrixCreator import PrintMatrix
def NumberSpiralMatrix(n: int):#O(n*n)
    spiral = [[0 for _ in range(n)] for _ in range(n)]
    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
    cr, cc, d = 0, 0, 0
    nr, nc = cr + dirs[d][0], cc + dirs[d][1]

    for i in range(1, n*n + 1):
        # write current cell
        spiral[cr][cc] = i

        # compute next candidate and turn if needed
        if not (0 <= nr < n and 0 <= nc < n) or spiral[nr][nc] != 0:
            d = (d + 1) % 4
            nr, nc = cr + dirs[d][0], cc + dirs[d][1]

        # advance
        cr, cc = nr, nc
        nr, nc = cr + dirs[d][0], cc + dirs[d][1]

    PrintMatrix(spiral)

def SpiralThroughLayer(n:int):#O(n*n)
    i=1
    spiral =[[ 0 for _ in range(n)] for _ in range(n)]
    layer = (n+1)//2
    for l in range(layer):
        top , left = l , l
        right , bottom = n-l-1 ,n-l-1

        # single-center case (odd n, last layer)
        if top == bottom and left == right:
            spiral[top][left] = i; i += 1
            break
        # for top
        for c in range(left , right):
            spiral[top][c]= i
            i+=1
        # for right
        for r in range(top , bottom):
            spiral[r][right]= i
            i+=1
        #for bottom
        for c in range( right , left ,-1):
            spiral[bottom][c]= i
            i+=1

        #for left
        for r in range(bottom , top , -1):
            spiral[r][left]=i
            i+=1
    PrintMatrix(spiral)


def SpiralThroughLayerWithDiffClock(n:int):#O(n*n)
    i=1
    spiral =[[ 0 for _ in range(n)] for _ in range(n)]
    layer = (n+1)//2
    for l in range(layer):
        top , left = l , l
        right , bottom = n-l-1 ,n-l-1

        # single-center case (odd n, last layer)
        if top == bottom and left == right:
            spiral[top][left] = i; i += 1
            break
        if not l%2:
            # for top
            for c in range(left , right):
                spiral[top][c]= i
                i+=1
            # for right
            for r in range(top , bottom):
                spiral[r][right]= i
                i+=1
            #for bottom
            for c in range( right , left ,-1):
                spiral[bottom][c]= i
                i+=1
            #for left
            for r in range(bottom , top , -1):
                spiral[r][left]=i
                i+=1
        else:
            #for left       
            for r in range(top , bottom):
                spiral[r][left]=i
                i+=1
            #for bottom
            for c in range(left , right):
                spiral[bottom][c]= i
                i+=1
            # for right
            for r in range(bottom , top , -1):
                spiral[r][right]= i
                i+=1
            # for top
            for c in range( right , left ,-1):
                spiral[top][c]= i
                i+=1
            
    PrintMatrix(spiral)

if __name__=="__main__":
    print("")
    NumberSpiralMatrix(4)
    print("")
    SpiralThroughLayer(5)
    print("")
    SpiralThroughLayerWithDiffClock(5)
