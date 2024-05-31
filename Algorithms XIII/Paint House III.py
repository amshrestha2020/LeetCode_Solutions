There is a row of m houses in a small city, each house must be painted with one of the n colors (labeled from 1 to n), some houses that have been painted last summer should not be painted again.

A neighborhood is a maximal group of continuous houses that are painted with the same color.

For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods [{1}, {2,2}, {3,3}, {2}, {1,1}].
Given an array houses, an m x n matrix cost and an integer target where:

houses[i]: is the color of the house i, and 0 if the house is not painted yet.
cost[i][j]: is the cost of paint the house i with the color j + 1.
Return the minimum cost of painting all the remaining houses in such a way that there are exactly target neighborhoods. If it is not possible, return -1.

 

Example 1:

Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 9
Explanation: Paint houses of this way [1,2,2,1,1]
This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.
Example 2:

Input: houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 11
Explanation: Some houses are already painted, Paint the houses of this way [2,2,1,2,2]
This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}]. 
Cost of paint the first and last house (10 + 1) = 11.
Example 3:

Input: houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
Output: -1
Explanation: Houses are already painted with a total of 4 neighborhoods [{3},{1},{2},{3}] different of target = 3.
 

Constraints:

m == houses.length == cost.length
n == cost[i].length
1 <= m <= 100
1 <= n <= 20
1 <= target <= m
0 <= houses[i] <= n
1 <= cost[i][j] <= 104







class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # Use a large number to represent infinity
        inf = float('inf')
        # Initialize the dp array with infinity
        dp = [[[inf] * n for _ in range(target + 1)] for _ in range(m)]
        
        # Base case for the first house
        if houses[0] == 0:  # Not painted
            for k in range(n):
                dp[0][1][k] = cost[0][k]
        else:  # Already painted
            dp[0][1][houses[0] - 1] = 0
        
        # Fill the dp array
        for i in range(1, m):
            for j in range(1, target + 1):
                for k in range(n):
                    if houses[i] == 0 or houses[i] == k + 1:
                        cost_to_paint = cost[i][k] if houses[i] == 0 else 0
                        for prev_k in range(n):
                            if prev_k == k:
                                dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][prev_k] + cost_to_paint)
                            else:
                                dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j - 1][prev_k] + cost_to_paint)
        
        # Get the minimum cost for painting all houses with exactly target neighborhoods
        min_cost = min(dp[m - 1][target])
        
        return -1 if min_cost == inf else min_cost
