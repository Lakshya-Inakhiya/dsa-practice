def ColSum(m):#O(n*n)
    row = len(m)
    col = len(m[0])
    sums = []
    for c in range(col):
        csum = 0
        for r in range(row):
            csum += m[r][c]
        sums.append(csum)
    print(f"Column sum: {sums}")

def minInCol(m): #O(n*n)
    row = len(m)
    col = len(m[0])
    mins =[]
    p = 1
    for c in range(col):
        cmin = m[0][c]
        for r in range(1 ,row):
            if cmin > m[r][c]:
                cmin = m[r][c]
        p *= cmin
        mins.append(cmin)
    print(f"Column min: {mins} and Product: {p}")


if __name__ == "__main__":
    from MatrixCreator import  MatrixRowWise 
    m = MatrixRowWise()
    print("")
    print(ColSum(m))
    print("")
    print(minInCol(m))
    print("")

