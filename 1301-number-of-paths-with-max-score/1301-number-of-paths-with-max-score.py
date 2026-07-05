class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7
        
        dp_sum = [[-1] * n for _ in range(n)]
        dp_cnt = [[0] * n for _ in range(n)]
        
        dp_sum[0][0] = 0
        dp_cnt[0][0] = 1
        
        for r in range(n):
            for c in range(n):
                if board[r][c] == 'X' or (r == 0 and c == 0):
                    continue
                
                max_score = -1
                paths = 0
                
                directions = [(r - 1, c), (r, c - 1), (r - 1, c - 1)]
                
                for nr, nc in directions:
                    if 0 <= nr < n and 0 <= nc < n and dp_sum[nr][nc] != -1:
                        if dp_sum[nr][nc] > max_score:
                            max_score = dp_sum[nr][nc]
                            paths = dp_cnt[nr][nc]
                        elif dp_sum[nr][nc] == max_score:
                            paths = (paths + dp_cnt[nr][nc]) % MOD
                
                if max_score != -1:
                    curr_val = 0
                    if board[r][c] != 'S':
                        curr_val = int(board[r][c])
                    
                    dp_sum[r][c] = max_score + curr_val
                    dp_cnt[r][c] = paths
        
        if dp_sum[n-1][n-1] == -1:
            return [0, 0]
            
        return [dp_sum[n-1][n-1], dp_cnt[n-1][n-1]]