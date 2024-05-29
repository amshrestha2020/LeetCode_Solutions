In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
 

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.





class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            if not (0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 0):
                return 0
            # save the value of the cell because we need to backtrack later
            gold = grid[x][y]
            # mark the cell as visited
            grid[x][y] = 0
            # explore the four directions
            max_gold = 0
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                max_gold = max(max_gold, dfs(x + dx, y + dy))
            # backtrack
            grid[x][y] = gold
            # return the maximum gold collected from this cell
            return max_gold + gold

        max_gold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    max_gold = max(max_gold, dfs(i, j))
        return max_gold

