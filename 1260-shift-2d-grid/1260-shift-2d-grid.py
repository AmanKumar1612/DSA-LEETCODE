class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        x=len(grid)
        for i in range(k):
            y=grid[-1].pop()
            grid[0].insert(0,y)
            for j in range(x-1):
                a=grid[j].pop()
                grid[j+1].insert(0,a)
        return grid