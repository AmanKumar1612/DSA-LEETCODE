class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        def change(a,b):
            x=image[a][b]
            if image[a][b] != color:
                image[a][b] = color
            if a-1 >=0 and image[a-1][b] == x:
                change(a-1,b)
            if a+1 < m and image[a+1][b] == x:
                change(a+1,b)
            if b-1 >=0 and image[a][b-1] == x:
                change(a,b-1)
            if b+1 < n and image[a][b+1] == x:
                change(a,b+1)
        m=len(image)
        n=len(image[0])
        if image[sr][sc] == color:
            return image
        change(sr,sc)
        return image