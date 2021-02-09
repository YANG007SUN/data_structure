
# https://www.hackerrank.com/challenges/queue-using-two-stacks/problem

N = int(input())
Q = []
for _ in range(N):
    q = list(map(int, input().split()))
    if q[0]==1:
        Q.append(q[1])
    elif q[0]==2:
        Q.pop(0)
    else:
        print(Q[0])
    