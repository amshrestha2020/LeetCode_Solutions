Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1
 

Constraints:

rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.







class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0
        
        for i in range(rows):
            for j in range(cols):
                # Update the height of the histogram for each row
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            # Calculate the largest rectangle area for the current row
            max_area = max(max_area, self.largestRectangleArea(heights))
        
        return max_area
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)
        
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                top_index = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                area = heights[top_index] * width
                max_area = max(max_area, area)
            
            stack.append(i)
        
        return max_area
