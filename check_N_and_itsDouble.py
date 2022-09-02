# Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

# More formally check if there exists two indices i and j such that :

# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]
 

# Example 1:

# Input: arr = [10,2,5,3]
# Output: true
# Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.

def checkIfExist( arr):
        
    def binarySearch(arr,target):
        lo , hi = 0 , len(arr)-1
        while lo <= hi:
            mid = (lo+hi)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                lo = mid+1
            else:
                hi = mid-1
        return -1
        
        
    arr.sort()
    for i in range(len(arr)):
        index = binarySearch(arr,arr[i]*2)
        
        if index != -1 and index != i:
            return True
    return False

if __name__ == '__main__':
    nums = list(map(int,input().split()))
    print(checkIfExist(nums))               
    