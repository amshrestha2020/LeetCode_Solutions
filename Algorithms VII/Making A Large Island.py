You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

 

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.





class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def move(x, y):
            for dx, dy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= dx < n and 0 <= dy < n:
                    yield dx, dy

        def dfs(x, y, index):
            res = 1
            grid[x][y] = index
            for i, j in move(x, y):
                if grid[i][j] == 1:
                    res += dfs(i, j, index)
            return res

        def neighbors(x, y):
            res = set()
            for i, j in move(x, y):
                if grid[i][j] > 1:
                    res.add(grid[i][j])
            return res

        index = 2
        area = {}
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 1:
                    area[index] = dfs(x, y, index)
                    index += 1

        res = max(area.values() or [0])
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 0:
                    res = max(res, 1 + sum(area[i] for i in neighbors(x, y)))
        return res

