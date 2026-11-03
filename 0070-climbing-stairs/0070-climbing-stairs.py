class Solution:
    def climbStairs(self, n: int) -> int:
        def find(n,arr):
        
            if n in arr:
                return arr[n]
            arr[n] = find(n-1,arr) + find(n-2,arr)
            return arr[n]
        arr={ 1:1 , 2:2 }
        find(n,arr)
        return arr[n]