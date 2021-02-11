
# ================================ 
# uses BFS (breadth first search)
# ================================



from collections import deque

# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY):
    visited= set()
    c = 0 # number of moves along one direction
    q = deque([[startX,startY,c]])
    moves = [[1,0],[-1,0],[0,1],[0,-1]]
    
    # actual logic
    while q:
        pathx, pathy, c = q.popleft()
        c+=1
        for xi,yi in moves:
            x,y = pathx, pathy 
            while True:
                x,y = x+xi, y+yi
                if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]=='.':
                    if x==goalX and y==goalY:
                        return c
                    elif (x,y) not in visited:
                        visited.add((x,y))
                        q.append([x,y,c])
                else:
                    break
    return -1     
                