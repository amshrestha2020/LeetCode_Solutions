You are given a 2D array of axis-aligned rectangles. Each rectangle[i] = [xi1, yi1, xi2, yi2] denotes the ith rectangle where (xi1, yi1) are the coordinates of the bottom-left corner, and (xi2, yi2) are the coordinates of the top-right corner.

Calculate the total area covered by all rectangles in the plane. Any area covered by two or more rectangles should only be counted once.

Return the total area. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:


Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: A total area of 6 is covered by all three rectangles, as illustrated in the picture.
From (1,1) to (2,2), the green and red rectangles overlap.
From (1,0) to (2,3), all three rectangles overlap.
Example 2:

Input: rectangles = [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 1018 modulo (109 + 7), which is 49.
 

Constraints:

1 <= rectangles.length <= 200
rectanges[i].length == 4
0 <= xi1, yi1, xi2, yi2 <= 109
xi1 <= xi2
yi1 <= yi2





class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # Collect all unique x and y coordinates
        x_coords = sorted(set(x for x1, _, x2, _ in rectangles for x in [x1, x2]))
        y_coords = sorted(set(y for _, y1, _, y2 in rectangles for y in [y1, y2]))

        # Create a grid to represent the coverage of rectangles
        grid = [[0] * len(y_coords) for _ in range(len(x_coords))]

        # Mark the coverage of each rectangle in the grid
        for x1, y1, x2, y2 in rectangles:
            x1_idx = x_coords.index(x1)
            y1_idx = y_coords.index(y1)
            x2_idx = x_coords.index(x2)
            y2_idx = y_coords.index(y2)
            for i in range(x1_idx, x2_idx):
                for j in range(y1_idx, y2_idx):
                    grid[i][j] = 1

        # Calculate the total area covered by rectangles
        total_area = 0
        for i in range(len(x_coords) - 1):
            for j in range(len(y_coords) - 1):
                if grid[i][j] == 1:
                    total_area += (x_coords[i + 1] - x_coords[i]) * (y_coords[j + 1] - y_coords[j])
                    total_area %= MOD

        return total_area

