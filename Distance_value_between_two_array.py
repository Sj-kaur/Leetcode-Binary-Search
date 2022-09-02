def findTheDistanceValue(arr1, arr2, d):
        
    arr2.sort()
    count = 0
    for x in arr1:
        lo , hi = 0,len(arr2)
        while lo < hi:
            mid  = (lo+hi)//2
            if abs(arr2[mid]-x) <= d:
                count -= 1
                break
            elif arr2[mid] > x:
                hi = mid
            else:
                lo = mid + 1
        count += 1
        
    return count

if __name__ == '__main__':
    nums1 = list(map(int,input().split()))
    nums2 = list(map(int,input().split()))
    target = int(input())
    print(findTheDistanceValue(nums1,nums2))

