# An array arr a mountain if the following properties hold:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

# You must solve it in O(log(arr.length)) time complexity.

 

# Example 1:

# Input: arr = [0,1,0]
# Output: 1
def peakIndexInMountainArray(arr):

    lo , hi = 0 , len(arr)-1
    while lo < hi:
        mid = (lo+hi)//2
        if arr[mid] >= arr[mid-1] and arr[mid] >= arr[mid+1]:
            return mid
        elif arr[mid] < arr[mid+1]:
            lo = mid
        else:
            hi = mid

if __name__ == '__main__':
    nums = list(map(int,input().split()))
    print(peakIndexInMountainArray(nums))               
    
    