def BinaryPyramid(num:int = 5):#O(n*n)
    print()
    for i in range(num):
        ch = "0" if (i % 2 == 0) else "1"  # PickCharByParityOnce.
        print(ch * (i + 1))

def ReverseBinaryPyramid(num:int = 5):#O(n*n)
    print()
    for i in range(num - 1 , - 1 , -1):
        ch = "0" if (i % 2 == 0) else "1"  # PickCharByParityOnce.
        print(ch * (i + 1))

def RightTriangle(num:int = 5):#O(n*n)
    print()
    for row in range(1 , num+ 1):
        for col in range(1 ,row + 1):
            print(col , end = "")
        print()

def ReverseRightTriangle(num:int = 5):#O(n*n)
    print()
    print("Type 1")
    for row in range(num , 0 , - 1):
        for col in range(1 ,row + 1):
            print(col , end = "")
        print()
    print()
    print("Type 2")
    for row in range(num):
        for col in range(num - row , 0 , -1):
            print(col , end = "")
        print()

def Star(num:int = 5):#O(n*n)
    print()
    for row in range(1 , num + 1):
        print(" "*(num - row) , end ="")#space
        print("*"*(2*(row) - 1))

def ReverseStar(num: int = 5):#O(n*n)
    print()
    for row in range(num , 0 , -1):
        print(" "*(num - row) , end ="")#space
        print("*"*(2*(row) - 1))

def DiamondStar(num: int = 5):#O(n*n)
    print()
    for row in range(1 , num+1):
        print(" "*(num - row), end = "")
        print("*"*(2*row - 1))
    for row in range(num - 1 , 0 , -1):
        print(" "*(num - row) , end ="")#space
        print("*"*(2*(row) - 1))

if __name__ == "__main__":  
    BinaryPyramid()
    ReverseBinaryPyramid()
    RightTriangle()
    ReverseRightTriangle()
    Star()
    ReverseStar()
    DiamondStar()