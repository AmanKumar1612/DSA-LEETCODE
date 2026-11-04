class Solution:
    def validStrings(self, n: int) -> List[str]:
        l=[]
        m=2**n
        for i in range(m):
            x=f"{i:0{n}b}"
            
            flag=0
            for i in range(n-1):
                if x[i] == '0' and x[i] == x[i+1]:
                    flag=1
                    break
            if flag==0:
                l.append(x)
        return l