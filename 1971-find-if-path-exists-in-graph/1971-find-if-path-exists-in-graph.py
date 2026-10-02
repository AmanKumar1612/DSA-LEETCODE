class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        def bfs(arr):
            vis=[False for _ in range(n)]
            queue=[source]
            vis[source]=True
            while queue:
                x=queue.pop(0)
                if x == destination:
                    return True
                for i in arr[x]:
                    if not vis[i]:
                        queue.append(i)
                        vis[i]=True
            return False
        arr=[[] for _ in range(n)]
        for i,j in edges:
            arr[i].append(j)
            arr[j].append(i)
        return bfs(arr)