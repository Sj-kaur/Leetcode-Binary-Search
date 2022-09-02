# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

# Example 1:

# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

def missingNumber( nums):
    start , end = 0 , len(nums)-1
    res = -1
    nums.sort()
    while start <= end:
        mid = (start+end)//2
        if nums[mid] == mid:
            start = mid+1
        elif nums[mid] > mid:
            res = mid
            end = mid -1
    if res == -1:
        return len(nums)
    else:
        return res

if __name__ == '__main__':
    nums = list(map(int,input().split()))
    print(missingNumber(nums))
