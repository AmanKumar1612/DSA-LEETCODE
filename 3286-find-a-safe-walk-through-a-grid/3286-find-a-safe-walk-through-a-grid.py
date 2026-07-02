from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        # min_cost[i][j] stores the minimum health lost to reach cell (i, j)
        min_cost = [[float('inf')] * n for _ in range(m)]
        
        # Base case: starting cell cost
        min_cost[0][0] = grid[0][0]
        
        # Deque for 0-1 BFS: stores (row, col)
        queue = deque([(0, 0)])
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            r, c = queue.popleft()
            
            # If we reach the destination, check if remaining health is positive
            if r == m - 1 and c == n - 1:
                return health - min_cost[r][c] >= 1
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    new_cost = min_cost[r][c] + grid[nr][nc]
                    
                    # If we found a path with less health loss
                    if new_cost < min_cost[nr][nc]:
                        min_cost[nr][nc] = new_cost
                        # 0-1 BFS logic: push to front if weight is 0, back if 1
                        if grid[nr][nc] == 0:
                            queue.appendleft((nr, nc))
                        else:
                            queue.append((nr, nc))
                            
        return health - min_cost[m-1][n-1] >= 1