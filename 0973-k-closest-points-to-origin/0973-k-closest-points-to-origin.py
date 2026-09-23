import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        h=[]
        for i,j in points:
            d=i*i+j*j
            heapq.heappush(h,(d,[i,j]))
        x=[]
        for i in range(k):
            x.append(heapq.heappop(h)[1])
        return x