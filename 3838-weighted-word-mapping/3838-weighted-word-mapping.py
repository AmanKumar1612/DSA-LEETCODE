class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        x=0
        st=''
        alpha='zyxwvutsrqponmlkjihgfedcba'
        alp=alpha[::-1]
        for i in words:
            s=0
            for j in i:
                ind=alp.index(j)
                no=weights[ind]
                s=s+no
            s=s%26
            st+=alpha[s]
        return st