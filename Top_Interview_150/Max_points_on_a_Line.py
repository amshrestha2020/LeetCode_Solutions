Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

 

Example 1:


Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Example 2:


Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
 

Constraints:

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.





class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def max_points_on_a_line_containing_point_i(i):
            def slope_coprime(x1, y1, x2, y2):
                delta_x, delta_y = x1 - x2, y1 - y2
                if delta_x == 0:  # vertical line
                    return (0, 0)
                elif delta_y == 0:  # horizontal line
                    return (float('inf'), float('inf'))
                elif delta_x < 0:
                    delta_x, delta_y = - delta_x, - delta_y
                gcd = math.gcd(delta_x, delta_y)
                slope = (delta_x / gcd, delta_y / gcd)
                return slope

            def add_line(i, j, count, duplicates):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2 and y1 == y2:  
                    duplicates += 1
                elif y1 == y2:  # horizontal line
                    nonlocal horizontal_lines
                    horizontal_lines += 1
                    count = max(horizontal_lines, count)
                else:
                    slope = slope_coprime(x1, y1, x2, y2)
                    lines[slope] = lines.get(slope, 1) + 1
                    count = max(lines[slope], count)
                return count, duplicates

            lines, horizontal_lines = {}, 1
            count = 1  # At least one point in the line
            duplicates = 0
            for j in range(i + 1, n):  # Compute the max number of points
                count, duplicates = add_line(i, j, count, duplicates)
            return count + duplicates

        n = len(points)
        if n <= 2:
            return n

        max_count = 1
        for i in range(n - 1):
            max_count = max(max_points_on_a_line_containing_point_i(i), max_count)
        return max_count
