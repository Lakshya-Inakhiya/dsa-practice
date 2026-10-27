import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '2.Sorting-2')))
import QuickSort  # type: ignore

# Optimal Solution
def lar_ele(arr):#O(n)
    m = arr[0]
    n = len(arr)
    for i in range(1,n):
        if m< arr[i]:
            m = arr[i]

    return m

# Brute 
def le(arr):#O(sorting)
    QuickSort.quickSort(arr , 0 , len(arr))
    return arr[-1]

if __name__ == "__main__":
    nums = [random.randint(1, 100) for _ in range(random.randint(5, 10))]
    print(nums ,lar_ele(nums))
