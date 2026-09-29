class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        x=[]
        for i in d:
            x.append(d[i])
        while x:
            a=x.pop()
            if a in x:
                return False
        return True