class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while True:
            if val in nums:
                nums.pop(nums.index(val))
                
            else:
                return len(nums)
            