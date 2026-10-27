def PrintMatrix(matrix, width=2):#O(n*n)
    fmt =f"{{:0{width}d}}" #fmt = format
    for row in matrix:
        s = " ".join(fmt.format(x) for x in row)
        print(s)

def MatrixRowWise():#O(n*n)
    r = int(input("Enter Number of Rows: "))
    print("Enter Numbers for each Row Below: ")
    matrix =[]
    for _ in range(r):
        matrix.append(list(map(int , input("").split())))
    return matrix

def MatrixFromFlat():#O(n*n)
    nums = list(map(int , input("Enter Numbers: ").split()))
    r = int(input("Enter Number of Rows: "))
    c = int(input("Enter Number of columns: "))
    matrix = [nums[i*c : (i+1)*c ] for i in range(r)]
    return matrix

'''
if we want square matrix only , in first func ,
add column input and at each row iteration check length
for second check wether r = c  
'''
if __name__ == "__main__":
    PrintMatrix(MatrixRowWise())
    print('************************')
    PrintMatrix(MatrixFromFlat())
    print('************************')



