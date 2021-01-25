# https://www.hackerrank.com/challenges/tree-level-order-traversal/problem?isFullScreen=true

def levelOrder(root):
    #Write your code here
    q = []
    d = {}
    root.level = 0
    q.append(root)
    while len(q)!=0:
        root = q.pop(0)
        if root.info not in d:
            d[root.info] = root.level
        if root.left is not None:
            root.left.level = root.level -1
            q.append(root.left)
        if root.right is not None:
            root.right.level = root.level -1
            q.append(root.right)
    res = dict(sorted(d.items(), key = lambda x:x[1], reverse =True))
    print(*res.keys())   