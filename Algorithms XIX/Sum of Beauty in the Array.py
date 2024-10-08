You are given a 0-indexed integer array nums. For each index i (1 <= i <= nums.length - 2) the beauty of nums[i] equals:

2, if nums[j] < nums[i] < nums[k], for all 0 <= j < i and for all i < k <= nums.length - 1.
1, if nums[i - 1] < nums[i] < nums[i + 1], and the previous condition is not satisfied.
0, if none of the previous conditions holds.
Return the sum of beauty of all nums[i] where 1 <= i <= nums.length - 2.

 

Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation: For each index i in the range 1 <= i <= 1:
- The beauty of nums[1] equals 2.
Example 2:

Input: nums = [2,4,6,4]
Output: 1
Explanation: For each index i in the range 1 <= i <= 2:
- The beauty of nums[1] equals 1.
- The beauty of nums[2] equals 0.
Example 3:

Input: nums = [3,2,1]
Output: 0
Explanation: For each index i in the range 1 <= i <= 1:
- The beauty of nums[1] equals 0.
 

Constraints:

3 <= nums.length <= 105
1 <= nums[i] <= 105



class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        from typing import List

        n = len(nums)
        left_max = [0] * n
        right_min = [0] * n
        
        # Fill left_max array
        left_max[0] = nums[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], nums[i])
        
        # Fill right_min array
        right_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            right_min[i] = min(right_min[i + 1], nums[i])
        
        beauty_sum = 0
        
        # Calculate the beauty
        for i in range(1, n - 1):
            if left_max[i - 1] < nums[i] < right_min[i + 1]:
                beauty_sum += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                beauty_sum += 1
        
        return beauty_sum        