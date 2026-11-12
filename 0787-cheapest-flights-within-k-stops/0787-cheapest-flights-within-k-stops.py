from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        arr=[[] for _ in range(n)]
        for s,d,w in flights:
            arr[s].append((d,w))
        
        dist=[float('inf')] * n
        dist[src] = 0
        queue=deque()
        queue.append((src,-1,0))
        
        while queue:
            x,step,cost=queue.popleft()
            if step >= k:
                continue
            for v,w in arr[x]:
                if cost + w < dist[v] :
                    dist[v] = cost+w
                    queue.append((v,step+1,dist[v]))
        return -1 if dist[dst] == float('inf') else dist[dst]