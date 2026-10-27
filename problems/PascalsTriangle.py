def PascalsTriangle(n:int ):#O(n*n)
    if n <= 0:
        return []
    if n == 1:
        return [1]
    ans = [ 0 for i in range(n)]
    prev =PascalsTriangle(n-1)
    ans = [1] + [prev[i] + prev[i - 1] for i in range(1, n - 1)] + [1]
    return ans
    
def PrintPascal(n:int):#O(n*n)
    if n <= 0:
        return 
    lst = [1]
    for row in range(1 ,n +1):
        print(" "*(n - row ), end="")
        print(" ".join(f"{x}" for x in lst))
        if row != n:
            lst = [1] + [lst[i] + lst[i - 1] for i in range(1, len(lst))] + [1]

if __name__ == "__main__":
        PrintPascal(3)

