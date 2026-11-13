import heapq
class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        m=len(heights)
        n=len(heights[0])
        vis=[[float('inf')]*n for _ in range(m)]
        vis[0][0]=0
        pq=[(0,0,0)] #[diff_curr,row,column]
        direction=[(-1,0),(1,0),(0,-1),(0,1)]
        while pq:
            d,r,c=heapq.heappop(pq)
            if r==m-1 and c==n-1:
                return d
            if d>vis[r][c] :
                continue
            for dr,dc in direction:
                nr,nc=r+dr,c+dc
                if 0<= nr < m and 0<= nc < n:
                    diff=abs(heights[r][c]-heights[nr][nc])
                    n_diff=max(d,diff)
                    if n_diff < vis[nr][nc]:
                        vis[nr][nc]=n_diff
                        heapq.heappush(pq,(n_diff,nr,nc))
        return 0