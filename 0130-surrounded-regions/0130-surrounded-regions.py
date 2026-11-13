class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def check(i,j):
            if i==0 or j==0 or i == m-1 or j == n-1:
                return False
            if i >0 and board[i-1][j] =='O' and not vis[i-1][j]:
                vis[i-1][j]=True
                if not check(i-1,j):
                    return False
            if i <m and board[i+1][j] =='O'and not vis[i+1][j]:
                vis[i+1][j]=True
                if not check(i+1,j):
                    return False
            if j >0 and board[i][j-1] =='O'and not vis[i][j-1]:
                vis[i][j-1]=True
                if not check(i,j-1):
                    return False
            if j <n and board[i][j+1] =='O'and not vis[i][j+1]:
                vis[i][j+1]=True
                if not check(i,j+1):
                    return False
            return True
        m=len(board)
        n=len(board[0])
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    vis=[[False]*n for _ in range(m)]
                    vis[i][j]=True
                    
                    if check(i,j):
                        for r in range(m):
                            for c in range(n):
                                if vis[r][c]:
                                    board[r][c] = 'X'