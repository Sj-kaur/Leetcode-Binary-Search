# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

def searchInsert(nums,target):
        
    start , end = 0, len(nums)-1
    
    while start<=end:
        
        mid = (start+end)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return start
                
if __name__ == '__main__':
    n = int(input())
    nums = list(map(int,input().split()))
    target = int(input())
    print(searchInsert(nums,target))
