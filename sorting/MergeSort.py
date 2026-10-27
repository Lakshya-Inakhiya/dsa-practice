import random

def merge(left , right):#O(N)
    i , j = 0 , 0
    l = len(left)
    r = len(right)
    ans = []
    while i < l and j < r:
        if left[i]>= right[j]:
            ans.append(right[j])
            j += 1

        else:
            ans.append(left[i])
            i += 1

    ans.extend(left[i:])
    ans.extend(right[j:])

    return ans

def mergeSort(nums):#O(NlogN)
    n = len(nums)
    if n <= 1:
        return nums
    mid = n// 2

    l = nums[:mid]
    r = nums[mid:]
    left = mergeSort(l)
    right = mergeSort(r)

    return merge(left , right)

#better merge

def bmerge(nums , low , mid , high ,):
    temp =[]
    left = low
    right = mid + 1
    while left <=mid and right <=high:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            right += 1

    while left <= mid:
        temp.append(nums[left])
        left += 1

    while right <= high:
        temp.append(nums[right])
        right += 1

    for i in range(low , high+1):
        nums[i] = temp[i - low]


def bmergeSort(nums , low , high):
    if low >= high:
        return
    mid = low + (high - low)//2
    bmergeSort(nums , low , mid)
    bmergeSort(nums , mid +1 , high)
    bmerge(nums , low , mid , high)
    return nums

if __name__ == "__main__":
    nums = [random.randint(1, 100) for _ in range(random.randint(5, 10))]
    print(nums[:] ,"->",bmergeSort(nums , 0 , len(nums)-1))
