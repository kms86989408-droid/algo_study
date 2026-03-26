# https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image [sr][sc]

        if original == color :
            return image
        
        rows = len(image)
        cols = len(image[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if image[r][c] != original:
                return
            
            image[r][c] = color

            dfs(r+1 , c) # 아래
            dfs(r - 1, c) # 위
            dfs(r, c + 1) # 오른쪽
            dfs(r, c-1) # 왼쪽

        dfs(sr, sc)
        return image