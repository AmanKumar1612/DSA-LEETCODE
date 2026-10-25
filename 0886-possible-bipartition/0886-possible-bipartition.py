from collections import deque
class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        
        arr=[[]for _ in range(n+1)]
        for i,j in dislikes:
            arr[i].append(j)
            arr[j].append(i)
        color=[0]*(n+1)
        queue=deque()
        for i in range(n):
            if color[i] == 0:
                queue.append(i)
                color[i]=1
                while queue:
                    x=queue.popleft()
                    
                    for j in arr[x]:
                        if color[j] == 0:
                            if color[x]==1:
                                color[j]=2
                            else:
                                color[j]=1
                            queue.append(j)
                        elif color[j] == color[x]:
                            return False
                        
        return True