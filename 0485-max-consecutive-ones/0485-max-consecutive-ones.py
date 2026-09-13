class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_con=0
        c=0
        for i in nums:
            if i==0:
                max_con=max(c,max_con)
                c=0
            else:
                c=c+1
        max_con=max(c,max_con)
        return max_con
        