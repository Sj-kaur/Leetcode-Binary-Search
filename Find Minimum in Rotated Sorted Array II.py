class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo,hi = 0 , len(nums)-1
        while lo < hi:

            while lo<hi and nums[lo] == nums[lo+1]:
                lo += 1
            while lo<hi and nums[hi] == nums[hi-1]:
                hi -= 1

            mid = (lo+hi)//2
            if nums[mid] > nums[hi]:
                lo = mid+1
            else:
                hi = mid
        return nums[lo]
        
