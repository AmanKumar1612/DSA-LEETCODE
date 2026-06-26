class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        shift = n + 1
        bit = [0] * (2 * n + 2)
        
        def update(idx, val):
            while idx < len(bit):
                bit[idx] += val
                idx += idx & (-idx)
                
        def query(idx):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s
            
        update(0 + shift, 1)
        
        prefix_sum = 0
        total_subarrays = 0
        
        for num in nums:
            if num == target:
                prefix_sum += 1
            else:
                prefix_sum -= 1
                
            total_subarrays += query(prefix_sum + shift - 1)
            update(prefix_sum + shift, 1)
            
        return total_subarrays