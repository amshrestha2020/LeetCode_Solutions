You are given a 0-indexed integer array nums. In one step, remove all elements nums[i] where nums[i - 1] > nums[i] for all 0 < i < nums.length.

Return the number of steps performed until nums becomes a non-decreasing array.

 

Example 1:

Input: nums = [5,3,4,4,7,3,6,11,8,5,11]
Output: 3
Explanation: The following are the steps performed:
- Step 1: [5,3,4,4,7,3,6,11,8,5,11] becomes [5,4,4,7,6,11,11]
- Step 2: [5,4,4,7,6,11,11] becomes [5,4,7,11,11]
- Step 3: [5,4,7,11,11] becomes [5,7,11,11]
[5,7,11,11] is a non-decreasing array. Therefore, we return 3.
Example 2:

Input: nums = [4,5,7,7,13]
Output: 0
Explanation: nums is already a non-decreasing array. Therefore, we return 0.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109




class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = []  # Stack to keep track of indices
        dp = [0] * len(nums)  # dp array to store the steps for each index
        max_steps = 0  # To keep track of the maximum steps

        # Traverse the array from the last element to the first
        for i in range(len(nums) - 1, -1, -1):
            # While the stack is not empty and the current number is greater than the number at the index at the top of the stack
            while stack and nums[i] > nums[stack[-1]]:
                # Update dp[i] with the maximum of current steps or the steps of the popped index
                dp[i] = max(dp[i] + 1, dp[stack.pop()])
                # Update the maximum steps encountered
                max_steps = max(max_steps, dp[i])

            # Push the current index onto the stack
            stack.append(i)

        return max_steps        