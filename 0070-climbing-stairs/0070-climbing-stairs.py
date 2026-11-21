class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        a1=1
        a2=2
        for i in range(3,n+1):
            x=a1+a2
            a1=a2
            a2=x
        return a2