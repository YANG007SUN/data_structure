# https://www.hackerrank.com/challenges/game-of-two-stacks/problem

# =========================================================
# First take as many elements from a
# Then take elements from b while removing element from a
# return the maxnum of elements from a and b
# =========================================================

def twoStacks(x, a, b):

    mxnum =i=j=total=0
    # take as many elements from a
    while i<len(a) and total+a[i]<=x:
        total+=a[i]
        i+=1
        mxnum+=1
    # take element from b
    while j<len(b) and i>=0:
        total+=b[j]
        j+=1
        # check of total is greater than x
        while total>x and i>0:
            i-=1
            total-=a[i]
        # update maxnum
        if total<=x and mxnum<i+j:
            mxnum=j+i
            
    return mxnum