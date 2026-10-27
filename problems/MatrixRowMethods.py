def RowSum(m): #O(n*n)
    row = len(m)
    col = len(m[0])
    sums = []
    for r in range(row):
        rsum = 0
        for c in range(col):
            rsum += m[r][c]
        sums.append(rsum)
    print(f"Row sum: {sums}")

def MinInRow(m):#O(n*n)
    row = len(m)
    col = len(m[0])
    mins =[]
    p = 1
    for r in range(row):
        rsum = m[r][0]
        for c in range(1 ,col):
            if rsum > m[r][c]:
                rsum = m[r][c]
        p *= rsum
        mins.append(rsum)
    print(f"Row min: {mins} and Product: {p}")

if __name__ == "__main__":
    from MatrixCreator import MatrixRowWise
    m = MatrixRowWise()
    print("")
    print(RowSum(m ))
    print("")
    print(MinInRow(m))
    print("")
