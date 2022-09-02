def mySqrt(x):
    l,r = 1,x
    while l <= r:
        mid =(l+r)//2
        if (mid*mid) > x:
            r = mid-1
        elif (mid*mid) < x:
            l = mid+1
        else:
            return mid
    return r   

if __name__ == '__main__':
    x = int(input())  
    print(mySqrt(x))      
