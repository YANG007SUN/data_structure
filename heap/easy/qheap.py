# https://www.hackerrank.com/challenges/qheap1/problem?isFullScreen=true

Q = int(input())
hp = []
for _ in range(Q):
    ls = list(map(int, input().split()))
    if ls[0]==1:
        if len(hp)==0:
            hp.append(ls[1])
            minv = hp[0]
        else:
            minv = min(ls[1], minv)
            hp.append(ls[1])
    elif ls[0]==2:
        hp.remove(ls[1])
        if ls[1] == minv and hp:
            minv = min(hp)
    else:
        print(minv)
        