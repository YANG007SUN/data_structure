def path(root, k):
    if not root:
        return []
    if root.info == k:
        return [root]
    res = path(root.left, k)
    if res:
        return [root] + res
    res = path(root.right, k)
    if res:
        return [root] + res
    return []
    
def lca(root, v1, v2):
  #Enter your code here
    l1 = path(root, v1)
    l2 = path(root, v2)
    res= None
    for i,v in zip(l1,l2):
        if i==v:
            res = i
        else:
            break
    return res