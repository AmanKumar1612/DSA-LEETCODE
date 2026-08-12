class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        x=[]
        y=[]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    x.append(i)
                    y.append(j)
        for i in range(m):
            for j in range(n):
                if i in x or j in y:
                    matrix[i][j]=0
        
