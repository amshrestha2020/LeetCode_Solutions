You are given a 2D integer array stockPrices where stockPrices[i] = [dayi, pricei] indicates the price of the stock on day dayi is pricei. A line chart is created from the array by plotting the points on an XY plane with the X-axis representing the day and the Y-axis representing the price and connecting adjacent points. One such example is shown below:


Return the minimum number of lines needed to represent the line chart.

 

Example 1:


Input: stockPrices = [[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]
Output: 3
Explanation:
The diagram above represents the input, with the X-axis representing the day and Y-axis representing the price.
The following 3 lines can be drawn to represent the line chart:
- Line 1 (in red) from (1,7) to (4,4) passing through (1,7), (2,6), (3,5), and (4,4).
- Line 2 (in blue) from (4,4) to (5,4).
- Line 3 (in green) from (5,4) to (8,1) passing through (5,4), (6,3), (7,2), and (8,1).
It can be shown that it is not possible to represent the line chart using less than 3 lines.
Example 2:


Input: stockPrices = [[3,4],[1,2],[7,8],[2,3]]
Output: 1
Explanation:
As shown in the diagram above, the line chart can be represented with a single line.
 

Constraints:

1 <= stockPrices.length <= 105
stockPrices[i].length == 2
1 <= dayi, pricei <= 109
All dayi are distinct.





class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        from typing import List


        stockPrices.sort()  # Sort by the first element (day)
        
        # Step 2: Handle special cases
        if len(stockPrices) < 2:
            return 0  # No lines needed for less than 2 points

        lines_count = 0
        prev_slope = None
        
        # Step 3: Calculate slopes and count lines
        for i in range(1, len(stockPrices) - 1):
            # Calculate the current slope between points i-1 and i, and i and i+1
            day1, price1 = stockPrices[i - 1]
            day2, price2 = stockPrices[i]
            day3, price3 = stockPrices[i + 1]
            
            # Calculate the slopes
            # Using tuple to avoid floating-point precision issues
            slope1 = (price2 - price1, day2 - day1)  # slope between points i-1 and i
            slope2 = (price3 - price2, day3 - day2)  # slope between points i and i+1
            
            # Normalize the slopes to check for collinearity
            # The slopes are compared by cross-multiplication to avoid division:
            # If slope1 == slope2, then (price2 - price1) * (day3 - day2) == (price3 - price2) * (day2 - day1)
            if slope1[0] * slope2[1] != slope2[0] * slope1[1]:  # Check if slopes are different
                lines_count += 1
        
        return lines_count + 1 