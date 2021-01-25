# https://www.hackerrank.com/challenges/tree-top-view/problem?isFullScreen=true

# ====================================================================================================
# The goal is empty out q
# Initialize root as 0, go left -1, go right +1, then only print unique value after +-1
# root.info -> data
# root.left -> left node (not left data, we still need to call root.left.info to find out left data)
# every time pop out node, we check left and right node
# ====================================================================================================


def topView(root):
    #Write your code here
    q = []
    d = {}
    root.level = 0
    q.append(root)
    while len(q)!=0:
        root = q.pop(0)
        if root.level not in d:
            d[root.level] = root.info
        if root.left is not None:    
            root.left.level = root.level -1
            q.append(root.left)
        if root.right is not None:
            root.right.level = root.level+1
            q.append(root.right)
    res =  dict(sorted(d.items(), key = lambda x: x[0]))
    print(*res.values())