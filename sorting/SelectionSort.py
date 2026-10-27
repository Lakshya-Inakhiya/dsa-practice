import random
def selectionSort(nums):#O(N^2)
    n = len(nums)
    for i in range(n-1):
        min_ = i
        for j in range(i+1 , n):
            if nums[min_] > nums[j]:
                min_ = j

        nums[min_] , nums[i] = nums[i] , nums[min_]

    return nums

if __name__ == "__main__":
    nums = [random.randint(1, 100) for _ in range(random.randint(5, 10))]
    print(nums[:] ,"->",selectionSort(nums))