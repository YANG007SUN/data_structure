# https://www.hackerrank.com/challenges/tree-postorder-traversal/problem?isFullScreen=true

def postOrder(root):
    #Write your code here
    if root is not None:
        postOrder(root.left)
        postOrder(root.right)
        print(root.info,end=' ')

