def findDuplicate(nums):
    nums.sort()
    lo,hi = 0, len(nums)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if nums.count(nums[mid]) > 1:
            return nums[mid]
        else:
            if hi-mid > nums[hi]-nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
                
if __name__ == '__main__':
    nums = list(map(int,input().split()))
    print(findDuplicate(nums))      
