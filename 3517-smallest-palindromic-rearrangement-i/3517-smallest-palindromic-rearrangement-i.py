from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        s="".join(sorted(s))
        arr=dict(Counter(s))
        s1=''
        common=''
        for i,j in arr.items():
            if j%2!=0:
                common=i 
            s1+=i*(j//2)
            
        return s1+common+s1[::-1]
