def findPeakElement(nums):
        
        
    lo ,hi = 0,len(nums)-1
    while lo < hi:
        mid = (lo+hi)//2
        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            return mid
        elif nums[mid] < nums[mid+1]:
            lo = mid+1
        else:
            hi = mid-1
    if nums[lo] >= nums[hi]:
        return lo
    else:
        return hi

if __name__ == '__main__':
    nums = list(map(int,input().split()))
    print(findPeakElement(nums))               
    
    
