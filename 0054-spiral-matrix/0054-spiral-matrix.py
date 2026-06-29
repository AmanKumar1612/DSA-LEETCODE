class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        l=[]
        vis=[[False]*n for _ in range(m)]
        i,j=0,0
        while not vis[i][j]:
            l.append(matrix[i][j])
            vis[i][j]=True
            while j+1 < n and not vis[i][j+1]: #right
                j=j+1
                l.append(matrix[i][j])
                vis[i][j]=True
            while i+1 < m and not vis[i+1][j]: #down
                i=i+1
                l.append(matrix[i][j])
                vis[i][j]=True
            while j-1>=0 and not vis[i][j-1]: #left
                j=j-1
                l.append(matrix[i][j])
                vis[i][j]=True
            while i-1 >=0 and not vis[i-1][j]: #up
                i=i-1
                l.append(matrix[i][j])
                vis[i][j]=True
            if j+1 < n:
                j=j+1
        return l