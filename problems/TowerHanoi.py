'''
Problem Statement
Given n disks and three pegs — a source peg, a helper peg, and a destination peg—
print the sequence of moves required to transfer all the disks from the source peg to the
destination peg following the rules of the Tower of Hanoi.
Each move should be represented in the format:
Move disk X from peg A to peg B
The rules are:
1. Only one disk can be moved at a time.
2. A larger disk can never be placed on top of a smaller disk.
3. All disks must be moved from the source peg to the destination peg using the helper
peg.
'''
def TowerHanoi(n:int , a:str="A", b:str="B" ,c:str="C"  ):#O(2^n) 
    # peg A = source , peg B = helper , peg C = destination

    if n==1:
        print(f"Move disk 1 from peg {a} to peg {c}") 
        return
    TowerHanoi(n-1 , a , c , b )
    print(f"Move disk {n} from peg {a} to peg {c}")
    TowerHanoi(n-1 , b , a , c)



if __name__ =="__main__":
    TowerHanoi(3)