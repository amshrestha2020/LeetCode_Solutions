Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

 

Example 1:

Input: nums = [1,2,1,2,6,7,5,1], k = 2
Output: [0,3,5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
Example 2:

Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
Output: [0,2,4]
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] < 216
1 <= k <= floor(nums.length / 3)




class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # Calculate the sum of every subarray of length k
        sums = [0] * (len(nums) - k + 1)
        sums[0] = sum(nums[:k])
        for i in range(1, len(sums)):
            sums[i] = sums[i-1] - nums[i-1] + nums[i+k-1]
        
        # Initialize the arrays to keep track of the maximum sum subarray on the left and right
        left = [0] * len(sums)
        right = [0] * len(sums)
        best = 0
        
        # Calculate the maximum sum subarray on the left of each position
        for i in range(len(sums)):
            if sums[i] > sums[best]:
                best = i
            left[i] = best
        
        # Calculate the maximum sum subarray on the right of each position
        best = len(sums) - 1
        for i in range(len(sums) - 1, -1, -1):
            if sums[i] >= sums[best]:
                best = i
            right[i] = best
        
        # Find the maximum sum of three non-overlapping subarrays
        ans = None
        for j in range(k, len(sums) - k):
            i, l = left[j - k], right[j + k]
            if ans is None or (sums[i] + sums[j] + sums[l] > sums[ans[0]] + sums[ans[1]] + sums[ans[2]]):
                ans = i, j, l
        
        return ans
