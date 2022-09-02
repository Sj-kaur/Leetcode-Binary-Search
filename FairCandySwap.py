# Alice and Bob have a different total number of candies. You are given two integer arrays aliceSizes and bobSizes where aliceSizes[i] is the number of candies of the ith box of candy that Alice has and bobSizes[j] is the number of candies of the jth box of candy that Bob has.

# Since they are friends, they would like to exchange one candy box each so that after the exchange, they both have the same total amount of candy. The total amount of candy a person has is the sum of the number of candies in each box they have.

# Return an integer array answer where answer[0] is the number of candies in the box that Alice must exchange, and answer[1] is the number of candies in the box that Bob must exchange. If there are multiple answers, you may return any one of them. It is guaranteed that at least one answer exists.

 

# Example 1:

# Input: aliceSizes = [1,1], bobSizes = [2,2]
# Output: [1,2]

def fairCandySwap(aliceSizes, bobSizes):
        
        
    def binary_search(arr, target):
        l, r = 0, len(arr)-1

        while l <= r:
            mid = l + (r-l)//2

            if arr[mid] == target:
                return mid
            elif target > arr[mid]:
                l = mid+1
            else:
                r = mid-1
        return -1

    aliceSizes.sort()
    bobSizes.sort()
    x = sum(aliceSizes)
    y = sum(bobSizes)
    final_sum = int((x+y)//2)
    
    for a in aliceSizes:
        if binary_search(bobSizes, final_sum+a-x) != -1:
            return [a, final_sum+a-x]

if __name__ == '__main__':
    nums1 = list(map(int,input().split()))
    nums2 = list(map(int,input().split()))
    print(fairCandySwap(nums1,nums2))