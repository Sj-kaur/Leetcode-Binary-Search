# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

def intersection(nums1, nums2):
        
    nums1.sort()
    nums2.sort()
    
    l , r = 0 , 0
    result = []
    while l < len(nums1) and r < len(nums2):
        if nums1[l] < nums2[r]:
            l += 1
        elif nums1[l] > nums2[r]:
            r += 1
        else:
            result.append(nums1[l])
            l += 1
            r += 1
    return list(set(result))

if __name__ == '__main__':
    nums1 = list(map(int,input().split()))
    nums2 = list(map(int,input().split()))
    print(intersection(nums1,nums2))