# You are given a 0-indexed integer array nums and a target element target.

# A target index is an index i such that nums[i] == target.

# Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

 

# Example 1:

# Input: nums = [1,2,5,2,3], target = 2
# Output: [1,2]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The indices where nums[i] == 2 are 1 and 2.




def targetIndices(nums, target):
    nums.sort()

    lo ,hi = 0 ,len(nums)-1
    start , end =-1, -1
    while lo <= hi:
        mid = (lo+hi)//2
        if nums[mid] == target:
            start = mid
            hi = mid -1
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    
    lo , hi = start , len(nums)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if nums[mid] == target:
            end= mid
            lo = mid+1
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    if start==end==-1:
        return []
    else:
        res = list(range(start,end+1))
        return res

if __name__ == '__main__':
    nums = list(map(int,input().split()))
    target = int(input())
    print(targetIndices(nums,target))
