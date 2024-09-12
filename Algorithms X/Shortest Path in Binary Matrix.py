Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1






from queue import PriorityQueue

delRow = [-1, -1, 0, +1, +1, +1, 0, -1]
delCol = [0, +1, +1, +1, 0, -1, -1, -1]

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][0] != 0:
            return -1
        dist = [[float('inf')]*n for _ in range(m)]
        dist[0][0] = 1
        pq = PriorityQueue()
        pq.put((1, (0, 0)))
        while not pq.empty():
            dis, (row, col) = pq.get()
            if row == m - 1 and col == n - 1:
                return dis
            for i in range(8):
                nrow, ncol = row + delRow[i], col + delCol[i]
                if 0 <= nrow < m and 0 <= ncol < n and grid[nrow][ncol] == 0 and dist[nrow][ncol] > dis + 1:
                    dist[nrow][ncol] = dis + 1
                    pq.put((dis + 1, (nrow, ncol)))
        return -1
