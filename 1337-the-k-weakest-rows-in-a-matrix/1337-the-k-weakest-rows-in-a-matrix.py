import heapq
class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        def cont(arr):
            c=0
            for i in arr:
                if i==1:
                    c+=1
                else:
                    break
            return c
        pq=[]
        i=0
        for j in mat:
            s=cont(j)
            heapq.heappush(pq,(s,i))
            i=i+1
        x=[]
        for i in range(k):
            x.append(heapq.heappop(pq)[1])
        return x