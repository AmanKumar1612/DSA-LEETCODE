class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        x=arr.copy()
        x.sort()
        c=0
        l={}
        for i in x:
            if i not in l:
                l[i]=c+1
                c=c+1
        a=[]
        for i in arr:
            a.append(l[i])
        return a
        