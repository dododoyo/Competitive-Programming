# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ROWS,COLS = len(image),len(image[0])

        # reverse 
        for r in range(ROWS):
            left,right = 0,COLS-1
            while left < right:
                temp = image[r][left]
                image[r][left],image[r][right] = image[r][right],image[r][left]
                left += 1
                right -= 1
        print(image)
        # invert
        for r in range(ROWS):
            for c in range(COLS):
                if image[r][c] == 0:
                    image[r][c] = 1
                else:
                    image[r][c] = 0

        return image