# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

# Return the kth positive integer that is missing from this array.

 

# Example 1:

# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

def findKthPositive( arr, k):
    arr.sort()
    lo , hi = 0, len(arr)
    
    while lo < hi:
        mid = (lo+hi)//2
        
        if arr[mid] - mid - 1 < k:
            lo = mid+1
        else:
            hi = mid
    return hi + k

if __name__ == '__main__':
    nums = list(map(int,input().split()))
    target = int(input())
    print(findKthPositive(nums,target))
    
      