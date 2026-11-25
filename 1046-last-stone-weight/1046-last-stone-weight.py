class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        
        while len(stones) >1:
            x=max(stones)
            x=stones.pop(stones.index(x))
            y=max(stones)
            y=stones.pop(stones.index(y))
            z=abs(x-y)
            stones.append(z)
        return 0 if len(stones) == 0 else stones[0]
