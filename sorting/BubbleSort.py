import random
# BruteForce
def bubbleSort(nums):#O(N^2)
    n = len(nums)

    for i in range( n- 1 , 0 , -1):
        for j in range(i):
            if nums[j]> nums[j+1]:
                nums[j] , nums[j+1] = nums[j+1] , nums[j]

    return nums

# Optimal Solution
def bubbleSort_o(nums):#O(N^2)
    n = len(nums)
    for i in range( n- 1 , 0 , -1):
        check = True
        for j in range(i):
            if nums[j]> nums[j+1]:
                nums[j] , nums[j+1] = nums[j+1] , nums[j]
                check = False

        if check:
            break
        
    return nums
if __name__ == "__main__":
    nums = [random.randint(1, 100) for _ in range(random.randint(5, 10))]
    print(nums[:] ,"->",bubbleSort_o(nums))