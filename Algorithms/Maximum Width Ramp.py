A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

 

Example 1:

Input: nums = [6,0,8,2,1,5]
Output: 4
Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
Example 2:

Input: nums = [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.
 

Constraints:

2 <= nums.length <= 5 * 104
0 <= nums[i] <= 5 * 104





class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        max_width = 0

        # Traverse the array from left to right and maintain a stack of indices with decreasing values
        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        # Traverse the array from right to left
        for j in range(len(nums) - 1, -1, -1):
            # While the stack is not empty and the current element is greater than or equal to the top element of the stack
            while stack and nums[j] >= nums[stack[-1]]:
                # Update the maximum width
                max_width = max(max_width, j - stack[-1])
                # Pop the top element from the stack
                stack.pop()

        return max_width
