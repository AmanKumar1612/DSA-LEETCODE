class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n=len(prices)-1
        arr=[]
        for i in range(n):
            m=0
            for j in range(i+1,n+1):
                if prices[j] <= prices[i]:
                    m=prices[j]
                    break
            arr.append(prices[i]-m)
        
        arr.append(prices[-1])
        return arr

        