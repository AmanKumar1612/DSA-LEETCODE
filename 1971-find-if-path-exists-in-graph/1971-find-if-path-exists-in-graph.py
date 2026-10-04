class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        def bfs(x,end,vis,arr):
            if x==end:
                return True
            vis[x]=True
            for i in arr[x]:
                if not vis[i]:
                    if bfs(i,end,vis,arr):
                        return True
            return False
        vis=[False]*n
        arr=[[] for _ in range(n)]
        for i , j in edges:
            arr[i].append(j)
            arr[j].append(i)
        return bfs(source,destination,vis,arr)