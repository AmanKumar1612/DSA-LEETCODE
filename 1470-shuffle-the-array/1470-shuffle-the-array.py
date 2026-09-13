class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        x=1
        for i in range(n):
            a=nums.pop(i+n)
            nums.insert(x,a)
            x=x+2
        return nums