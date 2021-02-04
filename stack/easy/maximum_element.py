
N = int(input())
stack = []
for _ in range(N):
    q = list(map(int, input().split()))
    if q[0]==1:
        if stack:
            stack.append(max(stack[-1], q[1]))
        else:
            stack.append(q[1])
    elif q[0]==2:
        stack.pop()
    else:
        print(stack[-1])        

