You are given an m x n binary grid, where each 1 represents a brick and 0 represents an empty space. A brick is stable if:

It is directly connected to the top of the grid, or
At least one other brick in its four adjacent cells is stable.
You are also given an array hits, which is a sequence of erasures we want to apply. Each time we want to erase the brick at the location hits[i] = (rowi, coli). The brick on that location (if it exists) will disappear. Some other bricks may no longer be stable because of that erasure and will fall. Once a brick falls, it is immediately erased from the grid (i.e., it does not land on other stable bricks).

Return an array result, where each result[i] is the number of bricks that will fall after the ith erasure is applied.

Note that an erasure may refer to a location with no brick, and if it does, no bricks drop.

 

Example 1:

Input: grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
Output: [2]
Explanation: Starting with the grid:
[[1,0,0,0],
 [1,1,1,0]]
We erase the underlined brick at (1,0), resulting in the grid:
[[1,0,0,0],
 [0,1,1,0]]
The two underlined bricks are no longer stable as they are no longer connected to the top nor adjacent to another stable brick, so they will fall. The resulting grid is:
[[1,0,0,0],
 [0,0,0,0]]
Hence the result is [2].
Example 2:

Input: grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]
Output: [0,0]
Explanation: Starting with the grid:
[[1,0,0,0],
 [1,1,0,0]]
We erase the underlined brick at (1,1), resulting in the grid:
[[1,0,0,0],
 [1,0,0,0]]
All remaining bricks are still stable, so no bricks fall. The grid remains the same:
[[1,0,0,0],
 [1,0,0,0]]
Next, we erase the underlined brick at (1,0), resulting in the grid:
[[1,0,0,0],
 [0,0,0,0]]
Once again, all remaining bricks are still stable, so no bricks fall.
Hence the result is [0,0].
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
grid[i][j] is 0 or 1.
1 <= hits.length <= 4 * 104
hits[i].length == 2
0 <= xi <= m - 1
0 <= yi <= n - 1
All (xi, yi) are unique.






from typing import List

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        
        def index(r, c):
            return r * cols + c
        
        def in_bounds(r, c):
            return 0 <= r < rows and 0 <= c < cols

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Step 1: Apply the hits (temporarily erase the bricks)
        for r, c in hits:
            if grid[r][c] == 1:
                grid[r][c] = 2  # Mark the brick as to be removed

        # Step 2: Mark all stable bricks
        def dfs(r, c):
            stack = [(r, c)]
            while stack:
                x, y = stack.pop()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if in_bounds(nx, ny) and grid[nx][ny] == 1:
                        grid[nx][ny] = 3
                        stack.append((nx, ny))
        
        for c in range(cols):
            if grid[0][c] == 1:
                grid[0][c] = 3
                dfs(0, c)
        
        # Step 3: Reverse the hits and count the falling bricks
        result = []
        for r, c in reversed(hits):
            if grid[r][c] == 2:
                grid[r][c] = 1
                if self.is_connected_to_top(r, c, grid):
                    newly_connected = self.dfs_count(r, c, grid)
                    result.append(newly_connected - 1)
                else:
                    result.append(0)
            else:
                result.append(0)
        
        return result[::-1]
    
    def is_connected_to_top(self, r, c, grid):
        if r == 0:
            return True
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 3:
                return True
        return False

    def dfs_count(self, r, c, grid):
        stack = [(r, c)]
        count = 0
        while stack:
            x, y = stack.pop()
            count += 1
            grid[x][y] = 3
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                    grid[nx][ny] = 3
                    stack.append((nx, ny))
        return count
