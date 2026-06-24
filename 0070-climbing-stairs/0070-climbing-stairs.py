class Solution:
    def climbStairs(self, n: int) -> int:
        l=[1,1]
        for i in range(1,n):
            l.append(l[i]+l[i-1])
        return l[-1]