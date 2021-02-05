# https://www.hackerrank.com/challenges/balanced-brackets/problem

def isBalanced(s):
    o = ['(','[','{']
    d = {'}':'{',')':'(',']':'['}
    stack = []
    if s[0] not in o:return 'NO'
    for i in s:
        if i in o:
            stack.append(i)
        else:
            if len(stack)==0: return 'NO'
            m = stack.pop()
            if m!=d[i]:return 'NO'
        
    if len(stack)!=0:return 'NO'
    return 'YES'