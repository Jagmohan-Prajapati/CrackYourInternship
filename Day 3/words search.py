"""Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])

        for row in range(n):
            for col in range(m):
                if self.depthFirstSearch(row, col, word, board):
                    return True
        return False

    def depthFirstSearch(
        self, row: int, col: int, word: str, grid: List[List[str]]
    ) -> bool:
        if len(word) == 0:
            return True
        if (
            row < 0
            or row >= len(grid)
            or col < 0
            or col >= len(grid[0])
            or grid[row][col] != word[0]
        ):
            return False

        result = False
        grid[row][col] = "*"

        offsets = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for rowOffset, colOffset in offsets:
            result = self.depthFirstSearch(
                row + rowOffset, col + colOffset, word[1:], grid
            )
            if result:
                break

        grid[row][col] = word[0]
        return result