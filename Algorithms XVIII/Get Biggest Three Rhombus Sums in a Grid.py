You are given an m x n integer matrix grid​​​.

A rhombus sum is the sum of the elements that form the border of a regular rhombus shape in grid​​​. The rhombus must have the shape of a square rotated 45 degrees with each of the corners centered in a grid cell. Below is an image of four valid rhombus shapes with the corresponding colored cells that should be included in each rhombus sum:


Note that the rhombus can have an area of 0, which is depicted by the purple rhombus in the bottom right corner.

Return the biggest three distinct rhombus sums in the grid in descending order. If there are less than three distinct values, return all of them.

 

Example 1:


Input: grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
Output: [228,216,211]
Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 20 + 3 + 200 + 5 = 228
- Red: 200 + 2 + 10 + 4 = 216
- Green: 5 + 200 + 4 + 2 = 211
Example 2:


Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
Output: [20,9,8]
Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 4 + 2 + 6 + 8 = 20
- Red: 9 (area 0 rhombus in the bottom right corner)
- Green: 8 (area 0 rhombus in the bottom middle)
Example 3:

Input: grid = [[7,7,7]]
Output: [7]
Explanation: All three possible rhombus sums are the same, so return [7].
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
1 <= grid[i][j] <= 105




class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        m = len(grid[0])
        ans = [0, 0, 0]

        # Iterate through each cell in the grid
        for r in range(n):
            for c in range(m):
                # Iterate through possible diamond shapes around the current cell
                for d in range(40):
                    top = r - d
                    left = c - d
                    right = c + d
                    bottom = r + d

                    # Check if the diamond shape is within the grid boundaries
                    if top < 0 or left < 0 or right >= m or bottom >= n:
                        break

                    cnt = grid[r][c] if d == 0 else 0
                    _c = c

                    # Traverse top side of the diamond
                    while top != r:
                        cnt += grid[top][_c]
                        top += 1
                        _c += 1

                    # Traverse right side of the diamond
                    _r = r
                    while right != c:
                        cnt += grid[_r][right]
                        _r += 1
                        right -= 1

                    # Traverse bottom side of the diamond
                    _c = c
                    while bottom != r:
                        cnt += grid[bottom][_c]
                        bottom -= 1
                        _c -= 1

                    # Traverse left side of the diamond
                    _r = r
                    while left != c:
                        cnt += grid[_r][left]
                        left += 1
                        _r -= 1

                    # Update the top three maximum values
                    one, two, three = ans
                    if cnt > one:
                        ans = [cnt, one, two]
                    elif one > cnt > two:
                        ans = [one, cnt, two]
                    elif two > cnt > three:
                        ans = [one, two, cnt]

        # Filter out any zeros from the result and return the top three values
        return [i for i in ans if i != 0]