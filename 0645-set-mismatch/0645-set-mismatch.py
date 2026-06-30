class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l=[0]*(len(nums)+1)
        for i in nums:
            l[i-1]+=1
        r=0
        d=0
        for i in l:
            if i>1:
                r=l.index(i) +1
            if i==0:
                d=l.index(i)+1
        return [r,d]