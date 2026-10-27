def RecSum(nums:list[int] , i:int=0):#O(n)
    k= len(nums)
    if i>=k:
        return 0
    return nums[i] + RecSum(nums, i+1)

if __name__ =="__main__":
    print(RecSum([1 , 2 , 3 , 4 , 5 ,6]))
