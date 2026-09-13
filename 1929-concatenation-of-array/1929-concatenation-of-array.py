class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        x=nums[::]
        for i in x:
            nums.append(i)
        return nums