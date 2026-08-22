class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=0
        p=1
        x=n
        while x >0:
            rem=x%10
            s+=rem
            p*=rem
            x=x//10
        s=s+p
        return n%s==0