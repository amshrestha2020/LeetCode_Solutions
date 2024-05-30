Given a 2D grid of 0s and 1s, return the number of elements in the largest square subgrid that has all 1s on its border, or 0 if such a subgrid doesn't exist in the grid.

 

Example 1:

Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 9
Example 2:

Input: grid = [[1,1,0,0]]
Output: 1
 

Constraints:

1 <= grid.length <= 100
1 <= grid[0].length <= 100
grid[i][j] is 0 or 1






class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        left = [[0]*n for _ in range(m)]
        top = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    left[i][j] = 1 if j == 0 else left[i][j-1] + 1
                    top[i][j] = 1 if i == 0 else top[i-1][j] + 1
        max_side = 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                side = min(left[i][j], top[i][j])
                while side > max_side:
                    if left[i-side+1][j] >= side and top[i][j-side+1] >= side:
                        max_side = side
                    side -= 1
        return max_side * max_side
