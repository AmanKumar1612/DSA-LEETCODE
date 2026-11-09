class Solution:
    def tribonacci(self, n: int) -> int:
        s={0:0,1:1,2:1}
        def find(n):
            if n in s:
                return s[n]
            s[n] = find(n-1) + find(n-2)+find(n-3)
            return s[n]
        if n <3 :
            return s[n]
        return find(n)
        