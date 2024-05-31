Given the array houses where houses[i] is the location of the ith house along a street and an integer k, allocate k mailboxes in the street.

Return the minimum total distance between each house and its nearest mailbox.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:


Input: houses = [1,4,8,10,20], k = 3
Output: 5
Explanation: Allocate mailboxes in position 3, 9 and 20.
Minimum total distance from each houses to nearest mailboxes is |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5 
Example 2:


Input: houses = [2,3,5,12,18], k = 2
Output: 9
Explanation: Allocate mailboxes in position 3 and 14.
Minimum total distance from each houses to nearest mailboxes is |2-3| + |3-3| + |5-3| + |12-14| + |18-14| = 9.
 

Constraints:

1 <= k <= houses.length <= 100
1 <= houses[i] <= 104
All the integers of houses are unique.




class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        m = len(houses)
        
        # cost[i][j] is the cost of placing one mailbox for houses[i:j+1]
        cost = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(i, m):
                mid = (i + j) // 2
                for t in range(i, j + 1):
                    cost[i][j] += abs(houses[t] - houses[mid])
        
        # dp[i][j] is the minimum distance to place j mailboxes among first i+1 houses
        dp = [[float('inf')] * (k + 1) for _ in range(m)]
        
        # Base case: One mailbox
        for i in range(m):
            dp[i][1] = cost[0][i]
        
        for j in range(2, k + 1):
            for i in range(m):
                for t in range(i):
                    dp[i][j] = min(dp[i][j], dp[t][j - 1] + cost[t + 1][i])
        
        return dp[m - 1][k]
