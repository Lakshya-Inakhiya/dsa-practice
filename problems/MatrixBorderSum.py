def MatrixBorderSum(matrix):
    # Guard For Empty Matrix.
    if not matrix or not matrix[0]:
        return 0

    row = len(matrix)
    col = len(matrix[0])

    # Handle Single Row Or Single Column Without Double Counting.
    if row == 1:
        return sum(matrix[0])
    if col == 1:
        return sum(matrix[r][0] for r in range(row))

    top , left = 0 , 0
    right , bottom = col - 1 , row - 1

    bsum = 0
    # For Top (Exclude Top-Right Corner).
    for c in range(left, right):
        bsum += matrix[top][c]
    # For Right (Include Top-Right, Exclude Bottom-Right).
    for r in range(top, bottom):
        bsum += matrix[r][right]
    # For Bottom (Include Bottom-Right, Exclude Bottom-Left).
    for c in range(right, left, -1):
        bsum += matrix[bottom][c]
    # For Left (Include Bottom-Left, Exclude Top-Left).
    for r in range(bottom, top, -1):
        bsum += matrix[r][left]

    return bsum


if __name__=="__main__":
    from MatrixCreator import MatrixRowWise
    matrix=MatrixRowWise()
    print("")
    print("BorderSum:",MatrixBorderSum(matrix))