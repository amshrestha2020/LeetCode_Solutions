A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

 

Example 1:


Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:

while this one is not:

In total, there is only one magic square inside the given grid.
Example 2:

Input: grid = [[8]]
Output: 0
 

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 10
0 <= grid[i][j] <= 15




class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagicSquare(grid, row, col):
            nums = set()
            for i in range(3):
                for j in range(3):
                    num = grid[row + i][col + j]
                    if num < 1 or num > 9 or num in nums:
                        return False
                    nums.add(num)

            if (grid[row][col] + grid[row][col + 1] + grid[row][col + 2] != 15 or
                grid[row + 1][col] + grid[row + 1][col + 1] + grid[row + 1][col + 2] != 15 or
                grid[row + 2][col] + grid[row + 2][col + 1] + grid[row + 2][col + 2] != 15 or
                grid[row][col] + grid[row + 1][col] + grid[row + 2][col] != 15 or
                grid[row][col + 1] + grid[row + 1][col + 1] + grid[row + 2][col + 1] != 15 or
                grid[row][col + 2] + grid[row + 1][col + 2] + grid[row + 2][col + 2] != 15 or
                grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2] != 15 or
                grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col] != 15):
                return False

            return True
        
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        
        for i in range(rows - 2):
            for j in range(cols - 2):
                if isMagicSquare(grid, i, j):
                    count += 1
        
        return count



