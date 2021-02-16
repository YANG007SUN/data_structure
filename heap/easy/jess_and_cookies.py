# https://www.hackerrank.com/challenges/jesse-and-cookies/problem

from heapq import heapify, heappush, heappop

#
# Complete the cookies function below.
#
def cookies(k, A):
    #
    # Write your code here.
    #
    heapify(A)
    i =0
    counter= 0
    while True:
        x = heappop(A)
        if x>=k:
            return counter
        if A:
            y = heappop(A)
            s = x+y*2
            heappush(A, s)
            counter+=1
        else:
            return -1