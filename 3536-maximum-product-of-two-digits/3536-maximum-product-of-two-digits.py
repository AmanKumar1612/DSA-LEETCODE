class Solution:
    def maxProduct(self, n: int) -> int:
        l=[]
        x=n
        while x>0:
            rem=x%10
            l.append(rem)
            x=x//10
        l.sort()
        a=l[-1]
        b=l[-2]
        return a*b