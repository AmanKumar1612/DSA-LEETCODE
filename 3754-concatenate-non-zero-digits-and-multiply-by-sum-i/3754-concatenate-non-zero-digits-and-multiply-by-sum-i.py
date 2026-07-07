class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s=0
        p=0
        i=0
        while n>0:
            x=n%10
            if x !=0:
                s=x*(10**i)+s
                p=p+x
                i=i+1
            n=n//10
        return p*s
        