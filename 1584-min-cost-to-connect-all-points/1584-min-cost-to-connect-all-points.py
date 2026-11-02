import heapq
class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n=len(points)
        arr=[[]for _ in range(n)]

        for i,x in enumerate(points):
            a,b=x[0],x[1]
            for j,y in enumerate(points):
                c,d=y[0],y[1]
                if i==j:
                    continue
                dist=abs(a-c) + abs(b-d)
                arr[i].append((j,dist))
        mst=set()
        queue=[(0,0)]
        ans=0
        while queue:
            dist,node=heapq.heappop(queue)
            if node not in mst:
                ans+=dist
                mst.add(node)
                for i,d in arr[node]:
                    heapq.heappush(queue,(d,i))
        return ans