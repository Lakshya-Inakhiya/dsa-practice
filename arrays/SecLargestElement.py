import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '2.Sorting-2')))
import QuickSort  # type: ignore

# Brute
def s_l_e(arr):#O(NlogN + N)
    n = len(arr)
    QuickSort.quickSort(arr , 0 , n)

    for i in range(n-2 , -1 , -1 ):
        if arr[i] != arr[n-1]:
            return arr[i]

# Better

def sle(arr):#O(2N)
    n = len(arr)
    l = arr[0]
    for i in range(1,n):
        if l < arr[i]:
            l = arr[i]

    sl = -1
    for i in range(n):
        if  sl < arr[i] and l != arr[i] :
            sl = arr[i]

    return sl , l

# Optimal

def sec_lar_ele(arr):#O(N)
    if not arr:
        return None    
    l = arr[0]
    float("-inf")
    n = len(arr)
    for i in range(1 , n):
        if l < arr[i]:
            sl = l
            l = arr[i]
        elif arr[i] != l and sl < arr[i]:
            sl = arr[i]
    return sl if sl != float("-inf") else -1

def sec_small_ele(arr):
    if not arr:
        return None
    s = arr[0]
    ss = float("inf")
    n = len(arr)
    for i in range(1 , n):
        if s > arr[i]:
            ss = s
            s = arr[i]
        elif arr[i] != s and ss > arr[i]:
            ss = arr[i]
    return ss


if __name__ == "__main__":
    nums = [random.randint(1, 100) for _ in range(random.randint(5, 10))]
    print(nums , sec_lar_ele(nums) , sec_small_ele(nums))

