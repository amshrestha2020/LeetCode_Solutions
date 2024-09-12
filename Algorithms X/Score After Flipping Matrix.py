You are given an m x n binary matrix grid.

A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including zero moves).

 

Example 1:


Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
Example 2:

Input: grid = [[0]]
Output: 1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
grid[i][j] is either 0 or 1.






class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # Flip all rows that have a 0 in the first column
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = 1 - grid[i][j]
        # Flip all columns where the number of 0's is greater than the number of 1's
        for j in range(1, n):
            zero_count = sum(grid[i][j] == 0 for i in range(m))
            if zero_count > m / 2:
                for i in range(m):
                    grid[i][j] = 1 - grid[i][j]
        # Calculate the score
        score = 0
        for i in range(m):
            for j in range(n):
                score += grid[i][j] << (n - 1 - j)
        return score
