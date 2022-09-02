# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

def search(nums, target):
    nums.sort()
    lo , hi = 0 , len(nums)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid+1
        else:
            hi = mid-1
    return -1

if __name__ == '__main__':
    nums = list(map(int,input().split()))
    target = int(input())
    print(search(nums,target))
      