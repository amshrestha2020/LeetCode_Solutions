You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.

A uni-value grid is a grid where all the elements of it are equal.

Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.

 

Example 1:


Input: grid = [[2,4],[6,8]], x = 2
Output: 4
Explanation: We can make every element equal to 4 by doing the following: 
- Add x to 2 once.
- Subtract x from 6 once.
- Subtract x from 8 twice.
A total of 4 operations were used.
Example 2:


Input: grid = [[1,5],[2,3]], x = 1
Output: 5
Explanation: We can make every element equal to 3.
Example 3:


Input: grid = [[1,2],[3,4]], x = 2
Output: -1
Explanation: It is impossible to make every element equal.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 105
1 <= m * n <= 105
1 <= x, grid[i][j] <= 104



class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flat_grid = [cell for row in grid for cell in row]
        
        # Check if all elements have the same remainder when divided by x
        remainder = flat_grid[0] % x
        for value in flat_grid:
            if value % x != remainder:
                return -1  # Impossible to make all elements equal

        # Sort the grid and find the median
        flat_grid.sort()
        median = flat_grid[len(flat_grid) // 2]
        
        # Count operations to make all elements equal to the median
        operations = 0
        for value in flat_grid:
            operations += abs(value - median) // x
        
        return operations        