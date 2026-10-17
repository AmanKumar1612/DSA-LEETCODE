class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def check(i,j):
            vis[i][j]=True
            if i-1 >= 0 and (not vis[i-1][j] and grid[i-1][j] == "1") :
                check(i-1,j)
            if i+1 < m and not vis[i+1][j] and grid[i+1][j] == "1":
                check(i+1,j)
            if j-1>=0 and not vis[i][j-1] and grid[i][j-1] == "1":
                check(i,j-1)
            if j+1 < n and not vis[i][j+1] and grid[i][j+1] == "1":
                check(i,j+1)
        m=len(grid)
        n=len(grid[0])
        vis=[[False for _ in range(n)]for j in range(m)]
        c=0
        for i in range(m):
            for j in range(n):
                if not vis[i][j] and grid[i][j] =="1":
                    check(i,j)
                    c+=1
        return c

