There are some prizes on the X-axis. You are given an integer array prizePositions that is sorted in non-decreasing order, where prizePositions[i] is the position of the ith prize. There could be different prizes at the same position on the line. You are also given an integer k.

You are allowed to select two segments with integer endpoints. The length of each segment must be k. You will collect all prizes whose position falls within at least one of the two selected segments (including the endpoints of the segments). The two selected segments may intersect.

For example if k = 2, you can choose segments [1, 3] and [2, 4], and you will win any prize i that satisfies 1 <= prizePositions[i] <= 3 or 2 <= prizePositions[i] <= 4.
Return the maximum number of prizes you can win if you choose the two segments optimally.

 

Example 1:

Input: prizePositions = [1,1,2,2,3,3,5], k = 2
Output: 7
Explanation: In this example, you can win all 7 prizes by selecting two segments [1, 3] and [3, 5].
Example 2:

Input: prizePositions = [1,2,3,4], k = 0
Output: 2
Explanation: For this example, one choice for the segments is [3, 3] and [4, 4], and you will be able to get 2 prizes. 
 

Constraints:

1 <= prizePositions.length <= 105
1 <= prizePositions[i] <= 109
0 <= k <= 109 
prizePositions is sorted in non-decreasing order.




class Solution:

    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        from typing import List

        n = len(prizePositions)
        b = [(0, 0)] * n
        s = [(0, 0)] * n
        
        for i in range(n):
            target = prizePositions[i] + k
            idx = max(0, self.upper_bound(prizePositions, target) - 1)
            b[i] = (i, idx)
        
        mx = 0
        curr = (0, 0)
        for i in range(n - 1, -1, -1):
            if b[i][1] - b[i][0] + 1 > mx:
                mx = b[i][1] - b[i][0] + 1
                curr = (b[i][0], b[i][1])
            s[i] = curr
        
        res = 0  # Initialize result to 0
        for i in range(n):
            j = b[i][1]
            res = max(res, b[i][1] - b[i][0] + 1 + s[j][1] - s[j][0] + 1 - (s[j][0] == b[i][1]))
        
        return res

    def upper_bound(self, a: List[int], target: int) -> int:
        """Find the first index in a where the element is greater than target."""
        left, right = 0, len(a)
        while left < right:
            mid = (left + right) // 2
            if a[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left