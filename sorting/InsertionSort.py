import random
def insertionSort(nums):#O(N^2)
    n = len(nums)

    for i in range(1,n):
        k = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > k:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = k

    return nums

if __name__ == "__main__":        
    nums = [random.randint(1, 100) for _ in range(random.randint(5, 10))]
    print(nums[:] ,"->",insertionSort(nums))