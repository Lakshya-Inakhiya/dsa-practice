'''
Problem Statement
A rook is placed at the bottom-left corner of an n*m chessboard. The rook can only
move either one step to the right or one step up at a time. Determine the number of
distinct ways the rook can reach the top-right corner.
4
Hint
To reach the destination, the rook must make exactly (n-1) upward moves and (m-1)
rightward moves, in any order. The total number of unique paths is determined by the
possible combinations of these moves.
'''
from functools import lru_cache
@lru_cache(None)
def RookMove(n:int ,m:int):#O(n·m)
    if n==1 or m==1:
        return 1
    return RookMove(n-1 , m) + RookMove(n,m-1)

if __name__=="__main__":
    print(RookMove(3,3))