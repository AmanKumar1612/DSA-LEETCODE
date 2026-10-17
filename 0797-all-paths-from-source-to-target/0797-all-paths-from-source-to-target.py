class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        res=[]
        d=len(graph)-1
        def dfs(no,path):
            if no == d:
                res.append(list(path))
                return
            for i in graph[no]:
                path.append(i)
                dfs(i,path)
                path.pop()
        dfs(0,[0])
        return res
