# Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.

# Note that the letters wrap around.

# For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
 

# Example 1:

# Input: letters = ["c","f","j"], target = "a"
# Output: "c"

def nextGreatestLetter(letters, target):
        
    if target >= letters[-1] or target < letters[0]:
        return letters[0]
    
    lo , hi = 0 , len(letters)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if letters[mid] <= target:
            lo = mid+1
        elif letters[mid] > target:
            hi = mid-1
            
    return letters[lo]

if __name__ == '__main__':
    nums = list(input().split())
    target = input()
    print(nextGreatestLetter(nums,target))

