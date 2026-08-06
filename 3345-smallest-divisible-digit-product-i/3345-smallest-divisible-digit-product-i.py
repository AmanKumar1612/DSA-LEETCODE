class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        if n==1:
            return t
        def prod(n):
            p=1
            while n>0:
                p*=n%10
                n=n//10
            return p
        for i in range(n,(n*10)+1):
            if prod(i) % t==0:
                return i