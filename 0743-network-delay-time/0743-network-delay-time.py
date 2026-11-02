import heapq
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        arr=[[]for _ in range(n+1)]
        for i , j , k1 in times:
            arr[i].append((j,k1))
        queue=[]
        heapq.heappush(queue,(0,k))
        dist=[float('inf')]*(n+1)
        dist[k]=0
        while queue:
            d,node=heapq.heappop(queue)
            if d>dist[node]:
                continue
            for i,weight in arr[node]:
                if dist[i] > dist[node] + weight:
                    dist[i] = dist[node] + weight
                    heapq.heappush(queue,(dist[i],i))
        
        maxTime=max(dist[1:])
        return maxTime if maxTime != float('inf') else -1