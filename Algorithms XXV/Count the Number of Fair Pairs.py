Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:

0 <= i < j < n, and
lower <= nums[i] + nums[j] <= upper
 

Example 1:

Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).
Example 2:

Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).
 

Constraints:

1 <= nums.length <= 105
nums.length == n
-109 <= nums[i] <= 109
-109 <= lower <= upper <= 109


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        from bisect import bisect_left, bisect_right

        nums.sort()
        n = len(nums)
        fair_pairs_count = 0
        
        # Step 2: For each element nums[i], find the valid range of nums[j]
        for i in range(n):
            # Find the smallest j such that nums[i] + nums[j] >= lower
            left = bisect_left(nums, lower - nums[i], i + 1)
            # Find the largest j such that nums[i] + nums[j] <= upper
            right = bisect_right(nums, upper - nums[i], i + 1) - 1
            
            # Add the count of valid pairs (i, j) where i < j
            fair_pairs_count += (right - left + 1)
        
        return fair_pairs_count