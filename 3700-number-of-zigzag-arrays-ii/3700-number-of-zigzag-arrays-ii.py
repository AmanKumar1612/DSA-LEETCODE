class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        M = r - l + 1
        
        if n == 1:
            return M
            
        dim = 2 * M
        T = [[0] * dim for _ in range(dim)]
        
        for y in range(M):
            for x in range(y + 1, M):
                T[y][M + x] = 1
                
        for y in range(M):
            for x in range(y):
                T[M + y][x] = 1
                
        def multiply(A, B):
            C = [[0] * dim for _ in range(dim)]
            for i in range(dim):
                for k in range(dim):
                    if not A[i][k]:
                        continue
                    for j in range(dim):
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
            return C

        def power(matrix, p):
            res = [[1 if i == j else 0 for j in range(dim)] for i in range(dim)]
            base = matrix
            while p > 0:
                if p & 1:
                    res = multiply(res, base)
                base = multiply(base, base)
                p >>= 1
            return res

        T_pow = power(T, n - 1)
        V = [1] * dim
        
        ans = 0
        for i in range(dim):
            row_sum = 0
            for j in range(dim):
                row_sum = (row_sum + T_pow[i][j] * V[j]) % MOD
            ans = (ans + row_sum) % MOD
            
        return ans