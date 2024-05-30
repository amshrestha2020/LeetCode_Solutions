You are given an m x n integer matrix grid, and three integers row, col, and color. Each value in the grid represents the color of the grid square at that location.

Two squares are called adjacent if they are next to each other in any of the 4 directions.

Two squares belong to the same connected component if they have the same color and they are adjacent.

The border of a connected component is all the squares in the connected component that are either adjacent to (at least) a square not in the component, or on the boundary of the grid (the first or last row or column).

You should color the border of the connected component that contains the square grid[row][col] with color.

Return the final grid.

 

Example 1:

Input: grid = [[1,1],[1,2]], row = 0, col = 0, color = 3
Output: [[3,3],[3,2]]
Example 2:

Input: grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3
Output: [[1,3,3],[2,3,3]]
Example 3:

Input: grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2
Output: [[2,2,2],[2,1,2],[2,2,2]]
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
1 <= grid[i][j], color <= 1000
0 <= row < m
0 <= col < n






class Solution:
    def __init__(self):
        self.col = 0
        self.initialCol = 0
        self.ans = []

    def helper(self, arr, r, c):
        n = len(arr)
        m = len(arr[0])
        if r < 0 or c < 0 or r >= n or c >= m or arr[r][c] != self.initialCol:
            return

        arr[r][c] = -self.col  # to distinguish between colors
        self.helper(arr, r, c + 1)
        self.helper(arr, r, c - 1)
        self.helper(arr, r + 1, c)
        self.helper(arr, r - 1, c)

        # Backtracking

        # checking if it was boundary color or not

        if not (r == 0 or c == 0 or r == n - 1 or c == m - 1 or arr[r + 1][c] != -self.col or arr[r - 1][c] != -self.col or arr[r][c - 1] != -self.col or arr[r][c + 1] != -self.col):
            self.ans.append((r, c))  # internal color

    def colorBorder(self, arr, r, c, color):
        self.col = color
        self.initialCol = arr[r][c]

        if self.col == self.initialCol:
            return arr
        self.helper(arr, r, c)
        for p in self.ans:
            i, j = p
            arr[i][j] = self.initialCol  # retaining the color of internal node

        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] < 0:
                    arr[i][j] = self.col  # boundary color

        return arr
