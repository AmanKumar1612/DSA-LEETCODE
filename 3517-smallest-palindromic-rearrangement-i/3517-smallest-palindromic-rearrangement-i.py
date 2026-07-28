from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        s="".join(sorted(s))
        arr=dict(Counter(s))
        s1=''
        s2=''
        common=''
        for i,j in arr.items():
            if j%2==0:
                s1+=i*(j//2)
                s2=i*(j//2)+s2
            else:
                common=i
                s1+=i*(j//2)
                s2=i*(j//2)+s2
        return s1+common+s2
