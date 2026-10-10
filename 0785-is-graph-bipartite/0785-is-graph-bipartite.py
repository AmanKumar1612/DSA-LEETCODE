class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        def bfs(arr,n,vis,queue):
            n=len(arr)
            color=[-1 for _ in range(n)]
            flag=0
            while queue:
                y=queue[0]
                while queue:
                    x=queue.pop(0)
                    if color[x]==-1:
                        color[x]=flag
                        vis[x]=True
                    for i in arr[x]:
                        if color[i] == color[x] and color[x] != -1:
                            return False
                for i in arr[y]:
                    if color[i] == -1:
                        queue.append(i)
                flag=1-flag
            print(color)
            return True
        n=len(graph)
        vis=[False for i in range(n)]
        for i in range(n):
            if not vis[i]:
                if not bfs(graph,n,vis,[i]):
                    return False
        return True