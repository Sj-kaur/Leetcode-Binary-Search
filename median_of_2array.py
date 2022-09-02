# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.




def findMedianSortedArrays( nums1, nums2):
    arr = (nums1 + nums2)
    arr.sort()
    lo,hi = 0 , len(arr)-1
    while lo <= hi:
        mid = (lo+hi)//2
        
        if len(arr)%2 == 0 :
            return (arr[mid]+arr[mid+1])/2
        else :
            return arr[mid]


if __name__ == '__main__':
    nums1 = list(map(int,input().split()))
    nums2 = list(map(int,input().split()))
    print(findMedianSortedArrays(nums1,nums2))