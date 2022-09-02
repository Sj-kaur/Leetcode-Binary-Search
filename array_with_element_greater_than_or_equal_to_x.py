# You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

# Notice that x does not have to be an element in nums.

# Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

 

# Example 1:

# Input: nums = [3,5]
# Output: 2
# Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.

def specialArray(nums):
    nums.sort()
    lo , hi = 0, len(nums)-1
    
    while lo <= hi:
        mid = (lo+hi)//2
        x = len(nums) - mid
        
        if nums[mid] >= x:
            if mid==0 or nums[mid-1] < x:
                return x
            else:
                hi = mid-1
        else:
            lo = mid+1
    return -1

if __name__ == '__main__':
    nums = list(map(int,input().split()))
    print(specialArray(nums))      