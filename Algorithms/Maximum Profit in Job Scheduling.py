We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

 

Example 1:



Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
Example 2:



Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.
Example 3:



Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6
 

Constraints:

1 <= startTime.length == endTime.length == profit.length <= 5 * 104
1 <= startTime[i] < endTime[i] <= 109
1 <= profit[i] <= 104




from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, zip(endTime, profit)), key=lambda v: v[1][0])
        dp = [(0, 0)]

        for job in jobs:
            currentProfit = dp[-1][1] + job[1][1]
            if job[0] >= dp[-1][0]:
                dp.append((job[1][0], currentProfit))
            else:
                l, r = 0, len(dp) - 1
                while l < r:
                    m = (l + r) // 2
                    if dp[m][0] <= job[0]:
                        l = m + 1
                    else:
                        r = m
                lastProfit = dp[l-1][1] + job[1][1]
                if lastProfit > dp[-1][1]:
                    dp.append((job[1][0], lastProfit))

        return dp[-1][1]

