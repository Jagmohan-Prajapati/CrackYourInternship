"""You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.

 

Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

Output: [[2,2,2],[2,2,0],[2,0,1]]

Explanation:



From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.

Note the bottom corner is not colored 2, because it is not horizontally or vertically connected to the starting pixel.

Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0

Output: [[0,0,0],[0,0,0]]

Explanation:

The starting pixel is already colored with 0, which is the same as the target color. Therefore, no changes are made to the image.

 

Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 216
0 <= sr < m
0 <= sc < n"""



class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        # If the source cell already has the same value as `color`, return the 
        # original image
        if image[sr][sc] == color:
            return image

        # Storing the original value of the starting cell
        old_color = image[sr][sc]
        # Replacing the value of the starting cell with the specified color
        image[sr][sc] = color

        # Calling the dfs function to replace the values of all connected cells
        self.dfs(image, sr, sc, old_color, color)

        # Return the modified image
        return image

    def dfs(
        self,
        grid: List[List[int]],
        row: int,
        col: int,
        old_target: int,
        new_target: int,
    ):
        # Defining the four cells adjacent to the starting cell
        adjacent_cells = [
            [0, 1],  # move right
            [1, 0],  # move down
            [-1, 0],  # move up
            [0, -1],  # move left
        ]

        # Get the dimensions of the grid
        grid_length = len(grid)
        total_cells = len(grid[0])

        # For each cell in the list of adjacent cells
        for cell_value in adjacent_cells:
            r = row + cell_value[0]
            c = col + cell_value[1]

            # If the adjacent cell is within the bounds of the grid
            # and has the same value as the starting cell
            if (
                0 <= r < grid_length
                and 0 <= c < total_cells
                and grid[r][c] == old_target
            ):
                # Replace the value of the adjacent cell with the specified 
                # target
                grid[r][c] = new_target
                # Recursively call the dfs function on the adjacent cell
                self.dfs(grid, r, c, old_target, new_target)