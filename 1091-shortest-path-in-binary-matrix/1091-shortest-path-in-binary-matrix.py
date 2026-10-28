import heapq
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        queue=[]
        n=len(grid)
        vis=[[float('inf') for _ in range(n)] for _ in range(n)]
        heapq.heappush(queue,[1,(0,0)])
        vis[0][0]=1

        while queue:
            dist,x=heapq.heappop(queue)
            i,j=x[0],x[1]
            if i+1 < n and grid[i+1][j] == 0 and vis[i+1][j] > dist+1:
                heapq.heappush(queue,[dist+1,(i+1,j)])
                vis[i+1][j]=dist+1
            if i-1 >= 0 and grid[i-1][j] == 0 and vis[i-1][j] > dist+1:
                heapq.heappush(queue,[dist+1,(i-1,j)])
                vis[i-1][j]=dist+1
            if j+1 < n and grid[i][j+1] == 0 and vis[i][j+1] > dist+1:
                heapq.heappush(queue,[dist+1,(i,j+1)])
                vis[i][j+1] = dist+1
            if j-1 >= 0 and grid[i][j-1] == 0 and vis[i][j-1] > dist+1:
                heapq.heappush(queue,[dist+1,(i,j-1)])
                vis[i][j-1] = dist+1
            if j+1 < n and i+1 < n and grid[i+1][j+1] == 0 and vis[i+1][j+1] > dist+1:
                heapq.heappush(queue,[dist+1,(i+1,j+1)])
                vis[i+1][j+1] = dist+1
            if j-1 >= 0 and i-1 >= 0 and grid[i-1][j-1] == 0 and vis[i-1][j-1] > dist+1:
                heapq.heappush(queue,[dist+1,(i-1,j-1)])
                vis[i-1][j-1] = dist+1
            if j+1 < n and i-1 >= 0 and grid[i-1][j+1] == 0 and vis[i-1][j+1] > dist+1:
                heapq.heappush(queue,[dist+1,(i-1,j+1)])
                vis[i-1][j+1] = dist+1
            if j-1 >= 0 and i+1 < n and grid[i+1][j-1] == 0 and vis[i+1][j-1] > dist+1:
                heapq.heappush(queue,[dist+1,(i+1,j-1)])
                vis[i+1][j-1] = dist+1
        if vis[n-1][n-1] == float('inf'):
            return -1
        return vis[n-1][n-1]