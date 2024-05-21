Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.

A boomerang is a set of three points that are all distinct and not in a straight line.

 

Example 1:

Input: points = [[1,1],[2,3],[3,2]]
Output: true
Example 2:

Input: points = [[1,1],[2,2],[3,3]]
Output: false
 

Constraints:

points.length == 3
points[i].length == 2
0 <= xi, yi <= 100





class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x0, y0 = points[0]
        x1, y1 = points[1]
        x2, y2 = points[2]
        
        # Check if the points are distinct
        if points[0] == points[1] or points[1] == points[2] or points[0] == points[2]:
            return False
        
        # Calculate the slopes
        if x1 - x0 != 0 and x2 - x1 != 0:
            slope1 = (y1 - y0) / (x1 - x0)
            slope2 = (y2 - y1) / (x2 - x1)
            return slope1 != slope2
        else:
            # If the denominator is zero, then the points are vertically aligned
            return x1 - x0 != x2 - x1
