# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Follow up: Do not use any built-in library function such as sqrt.

 

# Example 1:

# Input: num = 16
# Output: true

def isPerfectSquare( num):
        
    lo = 1
    hi = num
    
    while lo <= hi:
        mid = (lo+hi)//2
        
        if (mid*mid) == num:
            return True
        elif mid*mid > num:
            hi = mid-1
        else:
            lo = mid+1
    return False

if __name__ == '__main__':
    x = int(input())  
    print(isPerfectSquare(x))      