# https://www.hackerrank.com/challenges/tree-preorder-traversal/problem


def preOrder(root):
    #Write your code here
    if root is not None:
        print(root.info,end=' ')
        preOrder(root.left)
        preOrder(root.right)