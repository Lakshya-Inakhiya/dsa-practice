import random
def pivot_index(nums , low , high):
    r = random.randint(low , high-1)
    nums[r] , nums[low] = nums[low] , nums[r]
    pivot = nums[low]
    i = low
    j = high - 1
    while i<j:
        while i <=high -1  and nums[i] <= pivot:
            i += 1
        while j>  low   and nums[j] > pivot:
            j -= 1
        if i <j:
            nums[i] , nums[j] = nums[j] , nums[i]
        
    nums[j] , nums[low] = nums[low] , nums[j]
    return j

def quickSort(nums , low , high):
    if high - low <= 1:
        return 
    j = pivot_index(nums , low , high)
    quickSort(nums , low , j)
    quickSort(nums , j+1, high)
    return nums

if __name__ == "__main__":
    nums = [random.randint(1, 100) for _ in range(random.randint(5, 10))]
    print(nums[:] ,"->",quickSort(nums , 0 , len(nums)))

