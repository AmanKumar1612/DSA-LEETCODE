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
        i=n
        while True:
            if prod(i) % t==0:
                return i
            i=i+1