from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        queue=deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
        ans=0
        while queue:
            l=len(queue)
            for i in range(l):
                x,y=queue.popleft()
                if x-1 >= 0 and grid[x-1][y] == 1:
                    grid[x-1][y] = 2
                    queue.append((x-1,y))
                if x+1 < m and grid[x+1][y] == 1:
                    grid[x+1][y] = 2
                    queue.append((x+1,y))
                if y-1 >= 0 and grid[x][y-1] == 1:
                    grid[x][y-1] = 2
                    queue.append((x,y-1))
                if y+1 < n and grid[x][y+1] == 1:
                    grid[x][y+1] = 2
                    queue.append((x,y+1))
            if not queue:
                break
            ans+=1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return ans