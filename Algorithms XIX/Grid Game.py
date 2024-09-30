You are given a 0-indexed 2D array grid of size 2 x n, where grid[r][c] represents the number of points at position (r, c) on the matrix. Two robots are playing a game on this matrix.

Both robots initially start at (0, 0) and want to reach (1, n-1). Each robot may only move to the right ((r, c) to (r, c + 1)) or down ((r, c) to (r + 1, c)).

At the start of the game, the first robot moves from (0, 0) to (1, n-1), collecting all the points from the cells on its path. For all cells (r, c) traversed on the path, grid[r][c] is set to 0. Then, the second robot moves from (0, 0) to (1, n-1), collecting the points on its path. Note that their paths may intersect with one another.

The first robot wants to minimize the number of points collected by the second robot. In contrast, the second robot wants to maximize the number of points it collects. If both robots play optimally, return the number of points collected by the second robot.

 

Example 1:


Input: grid = [[2,5,4],[1,5,1]]
Output: 4
Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
The cells visited by the first robot are set to 0.
The second robot will collect 0 + 0 + 4 + 0 = 4 points.
Example 2:


Input: grid = [[3,3,1],[8,5,2]]
Output: 4
Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
The cells visited by the first robot are set to 0.
The second robot will collect 0 + 3 + 1 + 0 = 4 points.
Example 3:


Input: grid = [[1,3,1,15],[1,3,3,1]]
Output: 7
Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
The cells visited by the first robot are set to 0.
The second robot will collect 0 + 1 + 3 + 3 + 0 = 7 points.
 

Constraints:

grid.length == 2
n == grid[r].length
1 <= n <= 5 * 104
1 <= grid[r][c] <= 105




class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        from typing import List


        n = len(grid[0])
        
        # Calculate the prefix sums for row 0 (top row) and row 1 (bottom row)
        prefix_top = [0] * n
        prefix_bottom = [0] * n
        
        # Fill prefix sums for the top row
        prefix_top[0] = grid[0][0]
        for i in range(1, n):
            prefix_top[i] = prefix_top[i - 1] + grid[0][i]
        
        # Fill prefix sums for the bottom row
        prefix_bottom[0] = grid[1][0]
        for i in range(1, n):
            prefix_bottom[i] = prefix_bottom[i - 1] + grid[1][i]
        
        # The goal is to minimize the maximum points the second robot can get
        min_second_robot_points = float('inf')
        
        # Try every possible column to switch from the top to bottom row
        for c in range(n):
            # When the first robot switches at column c:
            # Robot 1 leaves the upper grid[0][c] and moves down to grid[1][c]
            # Robot 2 can either:
            # a) Move from the top left and go straight to bottom at the first row and move right (0 to c)
            # b) Move straight in the second row
            top_left_points = prefix_top[n - 1] - prefix_top[c] if c < n - 1 else 0
            bottom_right_points = prefix_bottom[c - 1] if c > 0 else 0
            
            # The second robot will take the max of these two routes
            second_robot_points = max(top_left_points, bottom_right_points)
            
            # Minimize the maximum points second robot can get
            min_second_robot_points = min(min_second_robot_points, second_robot_points)
        
        return min_second_robot_points