from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]
        arr=[ [] for _ in range(n)]
        indegree=[0]*n
        for i , j in edges:
            arr[i].append(j)
            arr[j].append(i)
            indegree[i]+=1
            indegree[j]+=1
        queue=deque()
        print(arr,indegree)

        for i , j in enumerate(indegree):
            if j == 1:
                queue.append(i)
        while queue:
            ans=[]
            l=len(queue)
            for i in range(l):
                x=queue.popleft()
                ans.append(x)
                for i in arr[x]:
                    indegree[i]-=1
                    if indegree[i] == 1:
                        
                        queue.append(i)
            
        return ans