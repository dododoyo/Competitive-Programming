class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image;
        
        def dfs(r,c,old_color):
            if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]) or image[r][c] != old_color:
                return
            image[r][c] = color;
            
            dfs(r+1, c, old_color);
            dfs(r-1, c, old_color);
            dfs(r, c+1, old_color);
            dfs(r, c-1, old_color);

        dfs(sr, sc, image[sr][sc]);
        return image;