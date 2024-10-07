You are given a 2D integer array grid of size m x n, where each cell contains a positive integer.

A cornered path is defined as a set of adjacent cells with at most one turn. More specifically, the path should exclusively move either horizontally or vertically up to the turn (if there is one), without returning to a previously visited cell. After the turn, the path will then move exclusively in the alternate direction: move vertically if it moved horizontally, and vice versa, also without returning to a previously visited cell.

The product of a path is defined as the product of all the values in the path.

Return the maximum number of trailing zeros in the product of a cornered path found in grid.

Note:

Horizontal movement means moving in either the left or right direction.
Vertical movement means moving in either the up or down direction.
 

Example 1:


Input: grid = [[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]]
Output: 3
Explanation: The grid on the left shows a valid cornered path.
It has a product of 15 * 20 * 6 * 1 * 10 = 18000 which has 3 trailing zeros.
It can be shown that this is the maximum trailing zeros in the product of a cornered path.

The grid in the middle is not a cornered path as it has more than one turn.
The grid on the right is not a cornered path as it requires a return to a previously visited cell.
Example 2:


Input: grid = [[4,3,2],[7,6,1],[8,8,8]]
Output: 0
Explanation: The grid is shown in the figure above.
There are no cornered paths in the grid that result in a product with a trailing zero.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 105
1 <= m * n <= 105
1 <= grid[i][j] <= 1000






class Solution:
    def util(self, val):
        x = 0
        while val > 0 and val % 5 == 0:
            val //= 5
            x += 1
            
        y = 0
        while val > 0 and val % 2 == 0:
            val //= 2
            y += 1
            
        return (x, y)

    def calculate_util(self, grid):
        n = len(grid)
        m = len(grid[0])
        matrix = [[self.util(grid[i][j]) for j in range(m)] for i in range(n)]
        
        # Right to left
        matrix1 = [[(0, 0)] * m for _ in range(n)]
        for i in range(n):
            for j in range(m - 1, -1, -1):
                if j == m - 1:
                    matrix1[i][j] = matrix[i][j]
                else:
                    matrix1[i][j] = (matrix[i][j][0] + matrix1[i][j + 1][0],
                                     matrix[i][j][1] + matrix1[i][j + 1][1])

        # Left to right
        matrix2 = [[(0, 0)] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if j == 0:
                    matrix2[i][j] = matrix[i][j]
                else:
                    matrix2[i][j] = (matrix[i][j][0] + matrix2[i][j - 1][0],
                                     matrix[i][j][1] + matrix2[i][j - 1][1])

        res = 0

        # Calculating by traversing from up to down
        for j in range(m):
            sum_pair = (0, 0)
            for i in range(n):
                sum_pair = (sum_pair[0] + matrix[i][j][0], sum_pair[1] + matrix[i][j][1])
                res = max(res, min(sum_pair))

                if j > 0:
                    p1 = matrix2[i][j - 1]
                    res = max(res, min(sum_pair[0] + p1[0], sum_pair[1] + p1[1]))

                if j < m - 1:
                    p1 = matrix1[i][j + 1]
                    res = max(res, min(sum_pair[0] + p1[0], sum_pair[1] + p1[1]))

        return res

    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        # Transpose the grid
        grid2 = [[grid[i][j] for i in range(n)] for j in range(m)]
        
        res = max(self.calculate_util(grid), self.calculate_util(grid2))
        
        # Reverse the grid
        grid3 = [grid[n - i - 1] for i in range(n)]
        
        return max(res, self.calculate_util(grid3))        