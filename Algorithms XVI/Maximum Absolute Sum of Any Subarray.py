You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:

If x is a negative integer, then abs(x) = -x.
If x is a non-negative integer, then abs(x) = x.
 

Example 1:

Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.
Example 2:

Input: nums = [2,-5,1,-4,3,-2]
Output: 8
Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104




class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        from typing import List

        max_sum = float('-inf')
        min_sum = float('inf')
        current_max = 0
        current_min = 0
        
        for num in nums:
            # Update max_sum using Kadane's Algorithm
            current_max = max(num, current_max + num)
            max_sum = max(max_sum, current_max)
            
            # Update min_sum using a modified Kadane's Algorithm
            current_min = min(num, current_min + num)
            min_sum = min(min_sum, current_min)
        
        # The maximum absolute sum is the maximum of the absolute values of max_sum and min_sum
        return max(abs(max_sum), abs(min_sum))        