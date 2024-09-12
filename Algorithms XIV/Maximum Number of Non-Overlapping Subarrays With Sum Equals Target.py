Given an array nums and an integer target, return the maximum number of non-empty non-overlapping subarrays such that the sum of values in each subarray is equal to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 2
Output: 2
Explanation: There are 2 non-overlapping subarrays [1,1,1,1,1] with sum equals to target(2).
Example 2:

Input: nums = [-1,3,5,1,4,2,-9], target = 6
Output: 2
Explanation: There are 3 subarrays with sum equal to 6.
([5,1], [4,2], [3,5,1,4,2,-9]) but only the first 2 are non-overlapping.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
0 <= target <= 106






class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        prefix_sum = {0}
        curr_sum = 0
        count = 0
        for num in nums:
            curr_sum += num
            if curr_sum - target in prefix_sum:
                count += 1
                curr_sum = 0
                prefix_sum = {0}
            else:
                prefix_sum.add(curr_sum)
        return count
