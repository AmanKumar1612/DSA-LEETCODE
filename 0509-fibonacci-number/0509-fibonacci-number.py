class Solution:
    def fib(self, n: int) -> int:
        arr={0:0,1:1}
        def fibo(n):
            if n in arr:
                return arr[n]
            arr[n] = fibo(n-1) + fibo(n-2)
            return arr[n]
        return fibo(n)