class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        smallest=nums[0]
        biggest=nums[-1]
        gcd=1
        for i in range(2,smallest+1):
            if smallest%i==0 and biggest%i==0:
                gcd=i
        return gcd