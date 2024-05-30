You are given several boxes with different colors represented by different positive numbers.

You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes with the same color (i.e., composed of k boxes, k >= 1), remove them and get k * k points.

Return the maximum points you can get.

 

Example 1:

Input: boxes = [1,3,2,2,2,3,4,3,1]
Output: 23
Explanation:
[1, 3, 2, 2, 2, 3, 4, 3, 1] 
----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
----> [1, 3, 3, 3, 1] (1*1=1 points) 
----> [1, 1] (3*3=9 points) 
----> [] (2*2=4 points)
Example 2:

Input: boxes = [1,1,1]
Output: 9
Example 3:

Input: boxes = [1]
Output: 1
 

Constraints:

1 <= boxes.length <= 100
1 <= boxes[i] <= 100




class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        dp = [[[0] * (n+1) for _ in range(n)] for _ in range(n)]
        
        # Initialize DP table for single boxes
        for i in range(n):
            for k in range(n):
                dp[i][i][k] = (k + 1) ** 2
        
        # Bottom-up DP
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                for k in range(n):
                    points = (k + 1) ** 2 + dp[i + 1][j][0]
                    for m in range(i + 1, j + 1):
                        if boxes[i] == boxes[m]:
                            points = max(points, dp[i + 1][m - 1][0] + dp[m][j][k + 1])
                    dp[i][j][k] = points
        
        return dp[0][n - 1][0]

