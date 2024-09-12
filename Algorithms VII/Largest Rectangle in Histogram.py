Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104




class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        
        # Append a sentinel value 0 at the end to handle the case where the stack is not empty at the end of traversal
        heights.append(0)
        
        for i in range(len(heights)):
            # While the current bar's height is less than the height of the bar at the top of the stack, calculate the area
            while stack and heights[i] < heights[stack[-1]]:
                # Pop the index of the top bar from the stack
                top_index = stack.pop()
                # Calculate the width of the rectangle by considering the index difference
                width = i if not stack else i - stack[-1] - 1
                # Calculate the area of the rectangle
                area = heights[top_index] * width
                # Update the maximum area
                max_area = max(max_area, area)
            
            # Append the current index to the stack
            stack.append(i)
        
        return max_area
