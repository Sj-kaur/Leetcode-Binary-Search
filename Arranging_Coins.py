# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.
# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.

def arrangeCoins( n):
    lo ,hi = 1, n
    while lo <= hi:
        mid = (lo+hi)//2
        temp = mid*(mid+1)//2
        if temp == n:
            return mid
        elif temp < n:
            lo = mid+1
        else:
            hi = mid-1
    return hi

if __name__ == '__main__':
    x = int(input())  
    print(arrangeCoins(x))               
 